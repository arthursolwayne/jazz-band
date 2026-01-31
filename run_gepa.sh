#!/bin/bash
# Robust GEPA runner with retry logic and circuit breaker

CMD="uv run python -m gepa --generations 100 --population 32"
LOGFILE="logs/gepa_$(date +%Y%m%d_%H%M%S).log"
RESUME_ID=""

# Circuit breaker: max 10 retries in 5 min window
MAX_RETRIES=10
WINDOW_SECONDS=300
RETRY_DELAY=10

# Create logs dir
mkdir -p logs

# Track retry timestamps
declare -a RETRY_TIMES=()

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOGFILE"
}

check_circuit_breaker() {
    local now=$(date +%s)
    local cutoff=$((now - WINDOW_SECONDS))

    # Filter to only recent retries
    local recent=()
    for t in "${RETRY_TIMES[@]}"; do
        if [ "$t" -ge "$cutoff" ]; then
            recent+=("$t")
        fi
    done
    RETRY_TIMES=("${recent[@]}")

    if [ ${#RETRY_TIMES[@]} -ge $MAX_RETRIES ]; then
        return 1  # Circuit breaker tripped
    fi
    return 0
}

log "=== GEPA Runner Started ==="
log "Command: $CMD"
log "Logging to: $LOGFILE"
log "Circuit breaker: $MAX_RETRIES retries in ${WINDOW_SECONDS}s window"

ATTEMPT=0
while true; do
    ATTEMPT=$((ATTEMPT + 1))

    # Build command with resume if we have one
    if [ -n "$RESUME_ID" ]; then
        RUN_CMD="$CMD --resume $RESUME_ID"
    else
        RUN_CMD="$CMD"
    fi

    log "=== Attempt #$ATTEMPT ==="
    log "Running: $RUN_CMD"

    # Run and capture output
    $RUN_CMD 2>&1 | tee -a "$LOGFILE"
    EXIT_CODE=${PIPESTATUS[0]}

    if [ $EXIT_CODE -eq 0 ]; then
        log "=== Completed successfully after $ATTEMPT attempt(s) ==="
        break
    fi

    log "=== Failed with exit code $EXIT_CODE ==="

    # Extract run_id from log for resume (look for "GEPA Evolution Run: gepa_XXXXXX")
    RESUME_ID=$(grep -oP 'GEPA Evolution Run: \K[a-z0-9_]+' "$LOGFILE" | tail -1)
    if [ -n "$RESUME_ID" ]; then
        log "Will resume from: $RESUME_ID"
    fi

    # Check circuit breaker
    RETRY_TIMES+=("$(date +%s)")
    if ! check_circuit_breaker; then
        log "=== CIRCUIT BREAKER TRIPPED ==="
        log "$MAX_RETRIES failures in $WINDOW_SECONDS seconds. Giving up."
        exit 1
    fi

    log "Retrying in ${RETRY_DELAY}s... (${#RETRY_TIMES[@]}/$MAX_RETRIES in window)"
    sleep $RETRY_DELAY
done

log "=== Session Complete ==="
