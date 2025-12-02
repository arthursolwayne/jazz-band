
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
]

for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64), (1.875, 65), (2.25, 63), (2.625, 62),
    # Bar 3 (3.0 - 4.5s)
    (3.0, 60), (3.375, 61), (3.75, 59), (4.125, 58),
    # Bar 4 (4.5 - 6.0s)
    (4.5, 62), (4.875, 63), (5.25, 61), (5.625, 60),
]

for start, note in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano comping: 7th chords on 2 and 4, aggressive but supportive
# Dm7 = D, F, A, C
# Bar 2 (1.5 - 3.0s)
# 2nd beat: Dm7, 4th beat: Dm7
piano_notes = [
    # Bar 2
    (1.875, 62), (1.875, 65), (1.875, 67), (1.875, 69),
    (2.625, 62), (2.625, 65), (2.625, 67), (2.625, 69),
    # Bar 3
    (3.375, 62), (3.375, 65), (3.375, 67), (3.375, 69),
    (4.125, 62), (4.125, 65), (4.125, 67), (4.125, 69),
    # Bar 4
    (4.875, 62), (4.875, 65), (4.875, 67), (4.875, 69),
    (5.625, 62), (5.625, 65), (5.625, 67), (5.625, 69),
]

for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125)
    piano.notes.append(note)

# Saxophone motif: simple, emotionally charged, leaves it hanging
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G (half note on D, 8th on F, 8th on Eb, 8th on G)
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 64), (2.25, 67),
    (2.5, 62), (2.75, 65), (3.0, 64), (3.25, 67),
    (3.5, 62), (3.75, 65), (4.0, 64), (4.25, 67),
    (4.5, 62), (4.75, 65), (5.0, 64), (5.25, 67),
]

for start, note in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
