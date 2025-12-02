
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),    # D (1)
    (61, 1.875, 0.375),  # C (2)
    (63, 2.25, 0.375),   # Eb (3)
    (62, 2.625, 0.375),  # D (4)
    (60, 3.0, 0.375),    # C (1)
    (61, 3.375, 0.375),  # Db (2)
    (63, 3.75, 0.375),   # Eb (3)
    (62, 4.125, 0.375),  # D (4)
    (62, 4.5, 0.375),    # D (1)
    (61, 4.875, 0.375),  # C (2)
    (63, 5.25, 0.375),   # Eb (3)
    (62, 5.625, 0.375)   # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.1875),  # D7: D
    (67, 1.875, 0.1875),  # D7: A
    (64, 1.875, 0.1875),  # D7: F
    (69, 1.875, 0.1875),  # D7: C
    # Bar 3
    (62, 3.375, 0.1875),  # D7: D
    (67, 3.375, 0.1875),  # D7: A
    (64, 3.375, 0.1875),  # D7: F
    (69, 3.375, 0.1875),  # D7: C
    # Bar 4
    (62, 4.875, 0.1875),  # D7: D
    (67, 4.875, 0.1875),  # D7: A
    (64, 4.875, 0.1875),  # D7: F
    (69, 4.875, 0.1875)   # D7: C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat every eighth
    for i in range(0, 8):
        hihat_start = start + (i * 0.1875)
        hihat_end = hihat_start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end))

# Sax: Motif in Dm, short and singable
sax_notes = [
    (62, 1.5, 0.375),    # D (1)
    (64, 1.875, 0.375),  # F (2)
    (62, 2.25, 0.375),   # D (3)
    (60, 2.625, 0.375),  # C (4)
    (62, 3.0, 0.375),    # D (1)
    (64, 3.375, 0.375),  # F (2)
    (62, 3.75, 0.375),   # D (3)
    (60, 4.125, 0.375),  # C (4)
    (62, 4.5, 0.375),    # D (1)
    (64, 4.875, 0.375),  # F (2)
    (62, 5.25, 0.375),   # D (3)
    (60, 5.625, 0.375)   # C (4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
