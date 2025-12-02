
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.1875, 0.1875),  # Hihat on 1&
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.9375, 0.1875),  # Hihat on 3&
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),   # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),   # E
    (65, 2.625, 0.375),  # F
    (67, 2.875, 0.375),  # G
    (69, 3.25, 0.375),   # A
    (67, 3.625, 0.375),  # G
    (65, 4.0, 0.375),    # F
    (64, 4.375, 0.375),  # E
    (62, 4.75, 0.375),   # D
    (60, 5.125, 0.375),  # C
    (62, 5.5, 0.375)     # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (62, 1.5, 0.1875),   # D
    (67, 1.5, 0.1875),   # A
    (64, 1.5, 0.1875),   # E
    (69, 1.5, 0.1875),   # B
    (67, 1.875, 0.1875),  # A
    (69, 1.875, 0.1875),  # B
    (71, 1.875, 0.1875),  # C#
    (62, 1.875, 0.1875),  # D
    # Bar 3: D7
    (62, 2.25, 0.1875),
    (67, 2.25, 0.1875),
    (64, 2.25, 0.1875),
    (69, 2.25, 0.1875),
    (67, 2.625, 0.1875),
    (69, 2.625, 0.1875),
    (71, 2.625, 0.1875),
    (62, 2.625, 0.1875),
    # Bar 4: D7
    (62, 3.0, 0.1875),
    (67, 3.0, 0.1875),
    (64, 3.0, 0.1875),
    (69, 3.0, 0.1875),
    (67, 3.375, 0.1875),
    (69, 3.375, 0.1875),
    (71, 3.375, 0.1875),
    (62, 3.375, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = 1.5 + (bar - 2) * 1.5
    # Kick 1
    drums.notes.append(pretty_midi.Note(100, 36, start, start + 0.375))
    # Hihat 1&
    drums.notes.append(pretty_midi.Note(100, 42, start + 0.1875, start + 0.1875))
    # Snare 2
    drums.notes.append(pretty_midi.Note(100, 38, start + 0.75, start + 0.375))
    # Hihat 2&
    drums.notes.append(pretty_midi.Note(100, 42, start + 0.9375, start + 0.1875))
    # Kick 3
    drums.notes.append(pretty_midi.Note(100, 36, start + 1.125, start + 0.375))
    # Hihat 3&
    drums.notes.append(pretty_midi.Note(100, 42, start + 1.3125, start + 0.1875))
    # Snare 4
    drums.notes.append(pretty_midi.Note(100, 38, start + 1.5, start + 0.375))
    # Hihat 4&
    drums.notes.append(pretty_midi.Note(100, 42, start + 1.6875, start + 0.1875))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - F# - B - D (D7 arpeggio)
sax_notes = [
    (62, 1.5, 0.1875),   # D
    (67, 1.875, 0.1875),  # F#
    (69, 2.25, 0.1875),   # B
    (62, 2.625, 0.1875),  # D
    (67, 3.0, 0.1875),    # F#
    (69, 3.375, 0.1875),  # B
    (62, 3.75, 0.1875)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
