
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes = [time_signature]

# Define key signature (D major)
key_signature = pretty_midi.KeySignature(key_number=2, time=0)  # D major
midi.key_signature_changes = [key_signature]

# Define the tempo (160 BPM)
midi.set_tempo(160)

# Define the 4-bar intro (6 seconds at 160 BPM = 4 bars)
# Each bar = 1.5 seconds, beat = 0.375 seconds
# We'll create 4 bars of music

# Instrument 1: Drums (Little Ray)
drum_program = pretty_midi.Instrument(program=56)  # Drums
midi.instruments.append(drum_program)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Each bar is 1.5 seconds, so 6 beats per bar at 160 BPM (each beat = 0.375s)
# 4 bars = 24 beats, each 0.375s

# Define the time positions for each beat
for bar in range(4):
    bar_start = bar * 1.5
    # Beat 1
    drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375))
    # Beat 2
    drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    # Beat 3
    drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Beat 4
    drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every 8th
    for i in range(2):
        drum_program.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# Instrument 2: Bass (Marcus)
bass_program = pretty_midi.Instrument(program=33)  # Double Bass
midi.instruments.append(bass_program)

# Walking bass line in D major with chromatic tension
# D major scale: D, E, F#, G, A, B, C#
# Chromatic tension: inserts accidentals between scale degrees
# We'll use a chromatic line from D to C#

bass_notes = [
    # Bar 1
    (0.0, 62),  # D3
    (0.375, 64),  # E3
    (0.75, 63),  # Eb3 (chromatic)
    (1.125, 65),  # F#3

    # Bar 2
    (1.5, 67),  # G3
    (1.875, 69),  # A3
    (2.25, 70),  # Bb3 (chromatic)
    (2.625, 71),  # B3

    # Bar 3
    (3.0, 72),  # C#3
    (3.375, 69),  # A3
    (3.75, 71),  # B3
    (4.125, 67),  # G3

    # Bar 4
    (4.5, 65),  # F#3
    (4.875, 63),  # Eb3
    (5.25, 64),  # E3
    (5.625, 62),  # D3
]

for start, pitch in bass_notes:
    bass_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Instrument 3: Piano (Diane)
piano_program = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
midi.instruments.append(piano_program)

# Piano comping: 7th chords on 2 and 4
# D major 7th: D, F#, A, C#
# G7: G, B, D, F
# A7: A, C#, E, G
# B7: B, D#, F#, A

chords = [
    # Bar 1 (no chord on beat 1)
    (0.375, [62, 67, 69, 74]),  # D7
    (0.75, [62, 67, 69, 74]),  # D7
    (1.125, [62, 67, 69, 74]),  # D7
    (1.5, [62, 67, 69, 74]),  # D7

    # Bar 2
    (1.875, [67, 72, 69, 71]),  # G7
    (2.25, [67, 72, 69, 71]),  # G7
    (2.625, [67, 72, 69, 71]),  # G7
    (3.0, [67, 72, 69, 71]),  # G7

    # Bar 3
    (3.375, [69, 74, 72, 71]),  # A7
    (3.75, [69, 74, 72, 71]),  # A7
    (4.125, [69, 74, 72, 71]),  # A7
    (4.5, [69, 74, 72, 71]),  # A7

    # Bar 4
    (4.875, [71, 76, 74, 72]),  # B7
    (5.25, [71, 76, 74, 72]),  # B7
    (5.625, [71, 76, 74, 72]),  # B7
    (6.0, [71, 76, 74, 72]),  # B7
]

for start, pitches in chords:
    for pitch in pitches:
        piano_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Instrument 4: Tenor Sax (Dante)
sax_program = pretty_midi.Instrument(program=62)  # Tenor Saxophone
midi.instruments.append(sax_program)

# Saxophone motif: start on D (62), move to F# (67), then G (67), then D (62), then F# (67), then G (67)
# Use quarter note on 1, eighth note on 2, eighth note on 3, then repeat the motif again on 4
# Each note is 0.375s

sax_notes = [
    (0.0, 62),  # D3
    (0.375, 67),  # F#3
    (0.75, 67),  # G3
    (1.125, 62),  # D3
    (1.5, 67),  # F#3
    (1.875, 67),  # G3
    (2.25, 62),  # D3
    (2.625, 67),  # F#3
    (3.0, 67),  # G3
    (3.375, 62),  # D3
    (3.75, 67),  # F#3
    (4.125, 67),  # G3
    (4.5, 62),  # D3
    (4.875, 67),  # F#3
    (5.25, 67),  # G3
    (5.625, 62),  # D3
]

for start, pitch in sax_notes:
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Save the MIDI file
midi.write("cellar_intro.mid")
