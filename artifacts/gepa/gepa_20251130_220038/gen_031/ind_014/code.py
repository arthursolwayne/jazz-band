
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + i*0.125, end=bar*1.5 + i*0.125 + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 40, 100),  # F
    (1.875, 41, 100), # Gb
    (2.25, 39, 100),  # E
    (2.625, 40, 100), # F
    (2.875, 41, 100), # Gb
    (3.25, 42, 100),  # Ab
    (3.625, 43, 100), # Bb
    (4.0, 42, 100),   # Ab
    (4.375, 43, 100), # Bb
    (4.75, 44, 100),  # B
    (5.125, 45, 100), # C
    (5.5, 44, 100),   # B
    (5.875, 45, 100), # C
]
for start, pitch, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 45, 100),  # C7 (F7)
    (1.875, 45, 100), # C7
    (2.25, 45, 100),  # C7
    (2.625, 45, 100), # C7
    (3.0, 47, 100),   # D7
    (3.375, 47, 100), # D7
    (3.75, 47, 100),  # D7
    (4.125, 47, 100), # D7
    (4.5, 46, 100),   # Bb7
    (4.875, 46, 100), # Bb7
    (5.25, 46, 100),  # Bb7
    (5.625, 46, 100), # Bb7
]
for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2]:
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1))
    for i in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + i*0.125, end=bar*1.5 + i*0.125 + 0.05))

# Sax: Motif in F
# Start with F (45), then Bb (46), then D (47), then F (45)
# Leave it hanging at the end
sax_notes = [
    (1.5, 45, 110),  # F
    (1.625, 46, 110), # Bb
    (1.75, 47, 110),  # D
    (1.875, 45, 110), # F
    (2.25, 45, 110),  # F
    (2.625, 44, 110), # B
    (2.875, 43, 110), # A
    (3.0, 42, 110),   # Ab
    (3.25, 45, 110),  # F
    (3.5, 47, 110),   # D
    (3.75, 45, 110),  # F
]
for start, pitch, vel in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
