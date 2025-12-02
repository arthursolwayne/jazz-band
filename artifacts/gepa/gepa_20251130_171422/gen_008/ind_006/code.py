
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Note durations: 1/4 = 0.375s, 1/8 = 0.1875s, etc.

# Time in seconds per bar: 1.5s
# Time per beat: 0.375s

# --- Bar 1: Drums only (build tension) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),   # Snare on 2
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.1875),   # Hihat on 1
    pretty_midi.Note(velocity=70, pitch=42, start=0.1875, end=0.375), # Hihat on &
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.5625), # Hihat on 2
    pretty_midi.Note(velocity=70, pitch=42, start=0.5625, end=0.75),  # Hihat on &
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125),   # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),    # Snare on 4
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=0.9375),  # Hihat on 3
    pretty_midi.Note(velocity=70, pitch=42, start=0.9375, end=1.125), # Hihat on &
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.3125), # Hihat on 4
    pretty_midi.Note(velocity=70, pitch=42, start=1.3125, end=1.5),   # Hihat on &
]

for note in drum_notes:
    drums.notes.append(note)

# --- Bar 2: Everyone in, sax starts motif (Fm key) ---

# Time starts at 1.5s
time = 1.5

# Bass line: walking line with chromatic approaches
# Fm7: F, Ab, Bb, Db
# Walking bass line: F -> Gb -> G -> Ab -> Bb -> B -> C -> Db -> Eb -> F

# Notes in Fm scale: F, Gb, G, Ab, Bb, B, C, Db, Eb
# Using quarter notes for walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),   # G (F->G)
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Gb (G->Gb)
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # G (Gb->G)
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),   # Ab (G->Ab)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords on 2 and 4, comp with emotion
# 7th chords in Fm: F7, Bb7, Eb7, Ab7
# Time is 1.5s (start of bar 2) -> 2.25s (beat 2), 3.0s (beat 4)

# F7 (F, A, C, Eb) on beat 1 (but Diane doesn't play on 1, only on 2 and 4)
# Bb7 (Bb, D, F, Ab) on beat 2 (2.25s)
# Eb7 (Eb, G, Bb, Db) on beat 4 (3.0s)

# Bb7 (chord on beat 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # Ab

    # Eb7 (chord on beat 4)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),   # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # Db
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: One short motif, make it sing — start it, leave it hanging, finish it
# Fm key: F, Gb, G, Ab, Bb, B, C, Db, Eb
# Motif: F -> Gb -> Bb -> F (a simple but haunting phrase)
# Notes in quarters, but leave it hanging on Bb

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb
    # Leave it hanging — don’t resolve on the first bar
    # Return to F in bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75)  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("Fm_intro.mid")
