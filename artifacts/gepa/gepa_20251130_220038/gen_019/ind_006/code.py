
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)        # Tenor sax
bass = pretty_midi.Instrument(program=33)       # Double bass
piano = pretty_midi.Instrument(program=0)       # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum definitions
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar = 1.5 seconds (160 BPM)
BAR_DURATION = 1.5
TIME_PER_BEAT = 0.375  # 160 BPM = 60 / 160 = 0.375 seconds per beat
BEAT_DURATION = 0.375

# --- Bar 1: Only Drums (0.0 - 1.5s) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = beat * BEAT_DURATION
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + BEAT_DURATION))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + BEAT_DURATION))
    # Hi-hat on every eighth
    for eighth in [0, 0.5]:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + eighth, end=time + eighth + 0.125))

# --- Bars 2-4: Full Quartet (1.5 - 6.0s) ---

# Start time for bar 2
start_time = 1.5

# --- Drums: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth ---
for bar in [2, 3, 4]:
    for beat in [0, 1, 2, 3]:
        time = start_time + (bar - 2) * BAR_DURATION + beat * BEAT_DURATION
        if beat % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + BEAT_DURATION))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + BEAT_DURATION))
        # Hi-hat on every eighth
        for eighth in [0, 0.5]:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=time + eighth, end=time + eighth + 0.125))

# --- Bass line: Walking line, chromatic approaches, no repeated notes ---
# D major scale: D E F# G A B C# D
# Bass line in D major with chromatic approaches

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=start_time, end=start_time + BEAT_DURATION),    # D
    pretty_midi.Note(velocity=90, pitch=64, start=start_time + BEAT_DURATION, end=start_time + 2 * BEAT_DURATION),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=start_time + 2 * BEAT_DURATION, end=start_time + 3 * BEAT_DURATION),  # F# (chromatic up)
    pretty_midi.Note(velocity=90, pitch=67, start=start_time + 3 * BEAT_DURATION, end=start_time + 4 * BEAT_DURATION),  # G

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=start_time + 4 * BEAT_DURATION, end=start_time + 5 * BEAT_DURATION),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=start_time + 5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=start_time + 6 * BEAT_DURATION, end=start_time + 7 * BEAT_DURATION),  # C# (chromatic up)
    pretty_midi.Note(velocity=90, pitch=67, start=start_time + 7 * BEAT_DURATION, end=start_time + 8 * BEAT_DURATION),  # G

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=start_time + 8 * BEAT_DURATION, end=start_time + 9 * BEAT_DURATION),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=start_time + 9 * BEAT_DURATION, end=start_time + 10 * BEAT_DURATION),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=start_time + 10 * BEAT_DURATION, end=start_time + 11 * BEAT_DURATION),  # F# (chromatic down)
    pretty_midi.Note(velocity=90, pitch=62, start=start_time + 11 * BEAT_DURATION, end=start_time + 12 * BEAT_DURATION),  # D
]

bass.notes.extend(bass_notes)

# --- Piano: 7th chords on 2 and 4, comp with emotional weight (D7, G7, C#7, Bm7) ---
# Bar 2: D7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=start_time + 1 * BEAT_DURATION, end=start_time + 2 * BEAT_DURATION))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start_time + 1 * BEAT_DURATION, end=start_time + 2 * BEAT_DURATION))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=start_time + 1 * BEAT_DURATION, end=start_time + 2 * BEAT_DURATION))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=start_time + 1 * BEAT_DURATION, end=start_time + 2 * BEAT_DURATION))  # B

# Bar 3: G7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=start_time + 5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=start_time + 5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=start_time + 5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=start_time + 5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION))  # F#

# Bar 4: C#7
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=start_time + 9 * BEAT_DURATION, end=start_time + 10 * BEAT_DURATION))  # C#
piano.notes.append(pretty_midi.Note(velocity=90, pitch=75, start=start_time + 9 * BEAT_DURATION, end=start_time + 10 * BEAT_DURATION))  # E
piano.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=start_time + 9 * BEAT_DURATION, end=start_time + 10 * BEAT_DURATION))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=79, start=start_time + 9 * BEAT_DURATION, end=start_time + 10 * BEAT_DURATION))  # B

# --- Sax: Melody — short motif, sing, leave it hanging, return and finish ---
# Play a short motif starting on beat 1 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=start_time, end=start_time + 0.5 * BEAT_DURATION),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 0.5 * BEAT_DURATION, end=start_time + BEAT_DURATION),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=start_time + 1.5 * BEAT_DURATION, end=start_time + 2 * BEAT_DURATION),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 2.5 * BEAT_DURATION, end=start_time + 3 * BEAT_DURATION),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=start_time + 3.5 * BEAT_DURATION, end=start_time + 4 * BEAT_DURATION),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 4.5 * BEAT_DURATION, end=start_time + 5 * BEAT_DURATION),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=start_time + 5.5 * BEAT_DURATION, end=start_time + 6 * BEAT_DURATION),  # A
]

sax.notes.extend(sax_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
