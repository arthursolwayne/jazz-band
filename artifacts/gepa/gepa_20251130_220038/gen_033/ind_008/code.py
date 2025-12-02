
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
for bar in range(1):
    start = bar * 1.5
    # Kick on beat 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on beat 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),  # D
    (1.875, 63),  # Eb
    (2.25, 64),  # E
    (2.625, 65),  # F
    (3.0, 67),  # G
    (3.375, 69),  # A
    (3.75, 67),  # G
    (4.125, 65),  # F
    (4.5, 64),  # E
    (4.875, 63),  # Eb
    (5.25, 62),  # D
    (5.625, 61),  # C
    (6.0, 62),  # D
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 64), (1.875, 67), (1.875, 71), (1.875, 72),  # D7 on beat 2
    (3.0, 64), (3.0, 67), (3.0, 71), (3.0, 72),  # D7 on beat 4
    (4.5, 64), (4.5, 67), (4.5, 71), (4.5, 72)   # D7 on beat 2 of bar 3
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, sing it, leave it hanging, come back and finish it
# D (62), F (65), Bb (66), D (62) - motif
# Start at bar 2 (1.5s), play first two notes, leave it hanging, come back at bar 3

note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125)
sax.notes.append(note)

# Add the final note of the motif at the end
note = pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0)
sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
