
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
    (42, 1.0, 0.1875), (42, 1.25, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in D, chromatic approach to 7th chord
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (65, 2.625, 0.375),
    (67, 3.0, 0.375), (69, 3.375, 0.375), (68, 3.75, 0.375), (70, 4.125, 0.375),
    (72, 4.5, 0.375), (74, 4.875, 0.375), (73, 5.25, 0.375), (75, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (72, 1.875, 0.375), (74, 1.875, 0.375), (76, 1.875, 0.375), (79, 1.875, 0.375),
    (72, 2.625, 0.375), (74, 2.625, 0.375), (76, 2.625, 0.375), (79, 2.625, 0.375),
    # Bar 3
    (72, 3.375, 0.375), (74, 3.375, 0.375), (76, 3.375, 0.375), (79, 3.375, 0.375),
    (72, 4.125, 0.375), (74, 4.125, 0.375), (76, 4.125, 0.375), (79, 4.125, 0.375),
    # Bar 4
    (72, 4.875, 0.375), (74, 4.875, 0.375), (76, 4.875, 0.375), (79, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone - short motif, 4 notes, space between
sax_notes = [
    (62, 1.5, 0.375),
    (65, 2.25, 0.375),
    (67, 3.0, 0.375),
    (69, 4.5, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums - continue for bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (42, 2.5, 0.1875), (42, 2.75, 0.1875), (42, 3.0, 0.1875),
    (36, 3.375, 0.375), (38, 3.75, 0.375), (42, 3.375, 0.1875),
    (36, 4.125, 0.375), (38, 4.5, 0.375), (42, 4.125, 0.1875),
    (42, 4.375, 0.1875), (42, 4.625, 0.1875), (42, 4.875, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
