
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: D minor
# Scale degrees: D, Eb, F, G, Ab, Bb, C
# We'll use D minor for all instruments

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
bass_instrument = pretty_midi.Instrument(program=33)  # Double Bass
piano_instrument = pretty_midi.Instrument(program=0)   # Acoustic Piano
drum_instrument = pretty_midi.Instrument(program=118) # Drums

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# BPM: 160
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Constants
bar_duration = 1.5  # 6 seconds for 4 bars, so 1.5 seconds per bar
beat_duration = bar_duration / 4  # 0.375s per beat

# -----------------------------
# Bar 1: Drums only
# -----------------------------
# Kick on 1 and 3
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=beat_duration))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2*beat_duration, end=3*beat_duration))

# Snare on 2 and 4
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1*beat_duration, end=2*beat_duration))
drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3*beat_duration, end=4*beat_duration))

# Hi-hat on every eighth note
for i in range(0, 4):
    for j in range(0, 2):
        drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * beat_duration + j * beat_duration / 2, end=i * beat_duration + j * beat_duration / 2 + beat_duration / 2))

# -----------------------------
# Bar 2: All instruments in
# -----------------------------
# Bass line: Dm7 walking line with chromatic approaches
# Dm7: D, F, Ab, C
# Walking line: D, Eb, F, G, Ab, Bb, C, B

bass_notes = [
    (0.0, 2),  # D
    (0.375, 3),  # Eb
    (0.75, 5),  # F
    (1.125, 7),  # G
    (1.5, 8),  # Ab
    (1.875, 10),  # Bb
    (2.25, 11),  # B
    (2.625, 10),  # Bb
    (3.0, 8),  # Ab
]

for start, pitch in bass_notes:
    bass_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: Dm7 chords on beats 2 and 4 (1.5 and 3.0)
# Dm7: D, F, Ab, C
# Chord voicings: D7sus4 (D, G, C, F) on beat 2, and Dm7 (D, F, Ab, C) on beat 4

# Beat 2
piano_notes = [62, 67, 60, 64]  # D, G, C, F (D7sus4)
for note in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.875))

# Beat 4
piano_notes = [62, 64, 67, 60]  # D, F, G, C (D7sus4)
for note in piano_notes:
    piano_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.375))

# Saxophone motif: D, Eb, C, rest
# D (62), Eb (63), C (60), rest
# Notes on beat 1, 2, and 3
sax_notes = [
    (0.0, 62),  # D
    (0.375, 63),  # Eb
    (0.75, 60),  # C
    (1.125, 62),  # D
    (1.5, 63),  # Eb
    (1.875, 60),  # C
    (2.25, 62),  # D
    (2.625, 63),  # Eb
    (3.0, 60),  # C
    (3.375, 0),  # Rest
]

for start, pitch in sax_notes:
    if pitch != 0:
        sax_instrument.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# Add instruments to the PrettyMIDI object
pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

# Save the MIDI file
pm.write("jazz_intro_dmin.mid")
