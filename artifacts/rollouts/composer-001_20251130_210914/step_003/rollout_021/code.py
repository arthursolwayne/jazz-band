
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375),
    (66, 4.5, 0.375), (67, 4.875, 0.375), (64, 5.25, 0.375), (66, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (79, 1.5, 0.1875), (76, 1.5, 0.1875), (74, 1.5, 0.1875), (71, 1.5, 0.1875),  # D7
    (79, 2.25, 0.1875), (76, 2.25, 0.1875), (74, 2.25, 0.1875), (71, 2.25, 0.1875),  # D7
    # Bar 3
    (82, 3.0, 0.1875), (79, 3.0, 0.1875), (77, 3.0, 0.1875), (74, 3.0, 0.1875),  # G7
    (82, 3.75, 0.1875), (79, 3.75, 0.1875), (77, 3.75, 0.1875), (74, 3.75, 0.1875),  # G7
    # Bar 4
    (80, 4.5, 0.1875), (77, 4.5, 0.1875), (75, 4.5, 0.1875), (72, 4.5, 0.1875),  # Bm7
    (80, 5.25, 0.1875), (77, 5.25, 0.1875), (75, 5.25, 0.1875), (72, 5.25, 0.1875)   # Bm7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax - motif in D, short and singable
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F#
    (67, 2.25, 0.375),  # A
    (62, 2.625, 0.375),  # D
    (65, 3.0, 0.375),  # F#
    (67, 3.375, 0.375),  # A
    (62, 3.75, 0.375),  # D
    (65, 4.125, 0.375),  # F#
    (67, 4.5, 0.375),  # A
    (62, 4.875, 0.375),  # D
    (65, 5.25, 0.375),  # F#
    (67, 5.625, 0.375)   # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums continue through bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
