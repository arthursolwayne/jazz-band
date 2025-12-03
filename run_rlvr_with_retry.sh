#!/bin/bash
# Retry script - keeps running until success or Ctrl+C

CMD="uv run python -m rlvr --resume composer-001_20251201_201755 --steps 100 --rollouts 32"
LOGFILE="rlvr_retry.log"
ATTEMPT=1

echo "=== Logging to $LOGFILE ===" | tee -a "$LOGFILE"

while true; do
    echo "=== Attempt #$ATTEMPT starting at $(date) ===" | tee -a "$LOGFILE"
    $CMD 2>&1 | tee -a "$LOGFILE"
    EXIT_CODE=${PIPESTATUS[0]}

    if [ $EXIT_CODE -eq 0 ]; then
        echo "=== Completed successfully after $ATTEMPT attempt(s) at $(date) ===" | tee -a "$LOGFILE"
        break
    else
        echo "=== Attempt #$ATTEMPT failed with exit code $EXIT_CODE at $(date). Retrying in 5s... ===" | tee -a "$LOGFILE"
        ATTEMPT=$((ATTEMPT + 1))
        sleep 5
    fi
done
