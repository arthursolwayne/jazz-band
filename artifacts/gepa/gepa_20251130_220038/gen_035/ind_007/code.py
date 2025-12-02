
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1&
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2&
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3&
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),     # D
    (63, 1.875, 0.375),   # Eb
    (64, 2.25, 0.375),    # E
    (65, 2.625, 0.375),   # F
    (67, 3.0, 0.375),     # G
    (68, 3.375, 0.375),   # Ab
    (69, 3.75, 0.375),    # A
    (70, 4.125, 0.375),   # Bb
    (72, 4.5, 0.375),     # B
    (73, 4.875, 0.375),   # C
    (74, 5.25, 0.375),    # C#
    (76, 5.625, 0.375),   # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375),   # G7 on 2
    (67, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (71, 2.25, 0.1875),
    (72, 2.25, 0.1875),
    (67, 3.375, 0.375),   # G7 on 4
    (67, 3.75, 0.1875),
    (69, 3.75, 0.1875),
    (71, 3.75, 0.1875),
    (72, 3.75, 0.1875),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (36, start, 0.375),     # Kick on 1
        (42, start, 0.1875),    # Hihat on 1&
        (38, start + 0.375, 0.375),   # Snare on 2
        (42, start + 0.375, 0.1875),  # Hihat on 2&
        (36, start + 0.75, 0.375),    # Kick on 3
        (42, start + 0.75, 0.1875),   # Hihat on 3&
        (38, start + 1.125, 0.375),   # Snare on 4
        (42, start + 1.125, 0.1875)   # Hihat on 4&
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Sax: Melody - one short motif, make it sing
sax_notes = [
    (67, 1.5, 0.5),       # G
    (69, 2.0, 0.5),       # A
    (71, 2.5, 0.5),       # B
    (67, 3.0, 0.5),       # G
    (69, 3.5, 0.5),       # A
    (71, 4.0, 0.5),       # B
    (72, 4.5, 0.5),       # C
    (71, 5.0, 0.5),       # B
    (72, 5.5, 0.5),       # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
