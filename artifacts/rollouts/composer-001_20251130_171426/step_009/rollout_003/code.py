
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
    # Bar starts at 0.0s
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, cutoff=0.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 59),  # D
    (1.875, 60), # Eb
    (2.25, 62),  # F
    (2.625, 63), # Gb
    (3.0, 64),   # G
    (3.375, 65), # Ab
    (3.75, 67),  # A
    (4.125, 69), # Bb
    (4.5, 70),   # B
    (4.875, 71), # C
    (5.25, 72),  # C#
    (5.625, 74), # D
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.75, 62), (1.75, 67), (1.75, 72), (1.75, 74),  # D7
    # Bar 3 (3.0 - 4.5s)
    (3.25, 64), (3.25, 69), (3.25, 74), (3.25, 76),  # F7
    # Bar 4 (4.5 - 6.0s)
    (4.75, 67), (4.75, 72), (4.75, 77), (4.75, 79),  # A7
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5, cutoff=0.125)
    drums.notes.append(kick)
    drums.notes.append(snare)
    drums.notes.append(hihat)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5 - 3.0s)
# Motif: D (62) -> F (65) -> D (62) -> Eb (64)
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 62), (1.5, 64),  # Start the motif
    (2.75, 62), (2.75, 65), (2.75, 62), (2.75, 64),  # Repeat the motif
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
