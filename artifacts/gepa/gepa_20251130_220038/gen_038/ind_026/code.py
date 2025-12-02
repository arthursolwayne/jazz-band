
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375),
    
    (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875), (42, 3.0, 0.1875),
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic, no repeated notes
bass_notes = [
    (53, 1.5, 0.375), (54, 1.875, 0.375), (52, 2.25, 0.375), (50, 2.625, 0.375),
    (51, 2.625, 0.375), (52, 2.625, 0.375), (53, 2.625, 0.375), (54, 2.625, 0.375),
    (55, 2.625, 0.375), (56, 2.625, 0.375), (55, 2.625, 0.375), (54, 2.625, 0.375),
    (53, 2.625, 0.375), (52, 2.625, 0.375), (51, 2.625, 0.375), (50, 2.625, 0.375),
    (51, 3.0, 0.375), (52, 3.375, 0.375), (54, 3.75, 0.375), (55, 4.125, 0.375),
    (56, 4.5, 0.375), (55, 4.875, 0.375), (54, 5.25, 0.375), (53, 5.625, 0.375),
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (67, 1.875, 0.375), (64, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3
    (62, 3.375, 0.375), (67, 3.375, 0.375), (64, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 4
    (62, 4.875, 0.375), (67, 4.875, 0.375), (64, 4.875, 0.375), (69, 4.875, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody - one motif, make it sing
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375), (65, 2.625, 0.375),
    (62, 3.0, 0.375), (65, 3.375, 0.375), (67, 3.75, 0.375), (69, 4.125, 0.375),
    (67, 4.5, 0.375), (65, 4.875, 0.375), (62, 5.25, 0.375), (64, 5.625, 0.375),
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
