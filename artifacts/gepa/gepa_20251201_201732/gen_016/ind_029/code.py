
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor (F, Gb, Ab, Bb, B, C, D)
# MIDI notes for F minor scale (C4 = 60): F (65), Gb (66), Ab (67), Bb (68), B (69), C (72), D (74)
# We'll use C4 as the base for all instruments (mid note), adjust accordingly

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
drums = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Define time signature: 4/4
pm.time_signature_changes.append(pretty_midi.TimeSignature(4, 4, 0))

# Define bar length in seconds (160 BPM = 6/160 = 0.375s per beat => 1.5s per bar)
bar_length = 1.5

# Define the time for each bar: 0s, 1.5s, 3s, 4.5s
bar_times = [0, 1.5, 3.0, 4.5]

# -----------------------------
# DRUMS: Little Ray
# Bar 1: Kick on 1 & 3, Snare on 2 & 4, Hi-hats on every eighth
# Bar 2-4: Keep the energy, but let the melody take over

# Bar 1 (0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=21, start=0.375, end=0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=21, start=1.125, end=1.5))  # Snare on 4

# Hi-hats on every 8th
for i in range(0, 6):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2 (1.5s) onward: Continue energy but keep it subtle
for bar in range(2, 5):
    start = bar_times[bar]
    # Kick on 1 & 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=35, start=start + 0.75, end=start + 1.125))
    # Snare on 2 & 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=21, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=21, start=start + 1.125, end=start + 1.5))
    # Hi-hats on every 8th
    for i in range(0, 6):
        start_eighth = start + i * 0.375
        end_eighth = start_eighth + 0.125
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_eighth, end=end_eighth))

# -----------------------------
# BASS: Marcus (walking line, chromatic steps)
# Fm = F, Ab, Bb, C, D, Eb, F
# Bass notes (in D2-G2 range, ~62-67 MIDI)
# Walking line with chromatic steps

# Bar 1 (0s): F (65) -> E (64) -> F (65) -> Gb (66)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0, end=0.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.375, end=0.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=1.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.125, end=1.5))

# Bar 2 (1.5s): Ab (67) -> G (67) -> Ab (67) -> Bb (68)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0))

# Bar 3 (3.0s): Bb (68) -> A (69) -> Bb (68) -> C (72)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5))

# Bar 4 (4.5s): D (74) -> C (72) -> D (74) -> Eb (70)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0))

# -----------------------------
# PIANO: Diane — open voicings, one chord per bar

# Fm7: F, Ab, C, Eb
# Fm7: F (65), Ab (67), C (72), Eb (69)
# Dorian: F, Gb, Ab, Bb, B, C, D
# Bar 1: Fm7
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0, end=1.5))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=0, end=1.5))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=0, end=1.5))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=0, end=1.5))  # C

# Bar 2: Bbmaj7: Bb (68), D (74), F (65), A (79)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0))

# Bar 3: Am7 (Dorian): A (69), C (72), E (76), G (71)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5))

# Bar 4: D7: D (74), F (65), A (79), C (72)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0))

# -----------------------------
# SAX: You — a short, motif

# Start with a simple motive: F (65), Ab (67), Bb (68), F (65)
# Play on beat 1 of bar 1: F
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=0, end=0.375))
# Ab on beat 2: 0.375s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=0.375, end=0.75))
# Bb on beat 3: 0.75s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=0.75, end=1.125))
# F on beat 4: 1.125s
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=1.125, end=1.5))

# Return to complete the motif on beat 2 of bar 3 (3.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=3.75, end=4.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5))

# Save the MIDI file
pm.write('Dante Intro - Fm.mid')

print("MIDI file saved as 'Dante Intro - Fm.mid'")
