
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
for i in range(0, 4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))  # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.5))  # Snare
    for j in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + j * 0.125, end=time + j * 0.125 + 0.0625))  # Hi-hat

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approach
bass_notes = [
    (1.5, 59),  # D
    (1.875, 60),  # Eb
    (2.25, 58),  # C
    (2.625, 59),  # D
    (2.875, 60),  # Eb
    (3.25, 58),  # C
    (3.625, 59),  # D
    (4.0, 60),  # Eb
    (4.375, 58),  # C
    (4.75, 59),  # D
    (5.125, 60),  # Eb
    (5.5, 58),  # C
    (5.875, 59),  # D
    (6.25, 60)  # Eb
]
for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25))

# Piano: comp on 2 and 4, 7th chords
piano_notes = [
    (1.875, 62),  # F (Dm7)
    (1.875, 67),  # Bb
    (1.875, 69),  # D
    (1.875, 71),  # F
    (2.625, 62),  # F
    (2.625, 67),  # Bb
    (2.625, 69),  # D
    (2.625, 71),  # F
    (3.25, 64),  # G (Dm7)
    (3.25, 67),  # Bb
    (3.25, 69),  # D
    (3.25, 71),  # F
    (4.0, 64),  # G
    (4.0, 67),  # Bb
    (4.0, 69),  # D
    (4.0, 71),  # F
    (4.75, 62),  # F
    (4.75, 67),  # Bb
    (4.75, 69),  # D
    (4.75, 71),  # F
    (5.5, 62),  # F
    (5.5, 67),  # Bb
    (5.5, 69),  # D
    (5.5, 71)  # F
]
for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25))

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 62),  # D
    (1.625, 65),  # F
    (1.75, 62),  # D
    (1.875, 65),  # F
    (2.25, 62),  # D
    (2.375, 65),  # F
    (2.5, 62),  # D
    (2.625, 65),  # F
    (3.0, 62),  # D
    (3.125, 65),  # F
    (3.25, 62),  # D
    (3.375, 65),  # F
    (3.5, 62),  # D
    (3.625, 65),  # F
    (3.75, 62),  # D
    (3.875, 65),  # F
    (4.25, 62),  # D
    (4.375, 65),  # F
    (4.5, 62),  # D
    (4.625, 65),  # F
    (5.0, 62),  # D
    (5.125, 65),  # F
    (5.25, 62),  # D
    (5.375, 65),  # F
    (5.5, 62),  # D
    (5.625, 65),  # F
    (5.75, 62),  # D
    (5.875, 65),  # F
    (6.0, 62),  # D
    (6.125, 65)  # F
]
for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Drums: continue with kick, snare, hihat
for i in range(4, 12):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))  # Kick
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.5))  # Snare
    for j in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + j * 0.125, end=time + j * 0.125 + 0.0625))  # Hi-hat

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
