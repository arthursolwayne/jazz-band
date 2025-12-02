
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
    (36, 0.0, 0.375),
    (38, 0.375, 0.375),
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    
    (36, 1.5, 0.375),
    (38, 1.875, 0.375),
    (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (53, 1.5, 0.375),  # Fm7 root
    (52, 1.875, 0.375),  # Eb
    (50, 2.25, 0.375),   # D
    (51, 2.625, 0.375),  # Eb

    (53, 2.8125, 0.375), # F
    (52, 3.1875, 0.375), # Eb
    (50, 3.5625, 0.375), # D
    (51, 3.9375, 0.375), # Eb

    (53, 4.3125, 0.375), # F
    (52, 4.6875, 0.375), # Eb
    (50, 5.0625, 0.375), # D
    (51, 5.4375, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (59, 1.875, 0.375),  # Bb
    (60, 1.875, 0.375),  # B
    (62, 1.875, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (57, 1.875, 0.375),  # Ab

    # Bar 3
    (59, 3.1875, 0.375), # Bb
    (60, 3.1875, 0.375), # B
    (62, 3.1875, 0.375), # D
    (64, 3.1875, 0.375), # F
    (57, 3.1875, 0.375), # Ab

    # Bar 4
    (59, 4.6875, 0.375), # Bb
    (60, 4.6875, 0.375), # B
    (62, 4.6875, 0.375), # D
    (64, 4.6875, 0.375), # F
    (57, 4.6875, 0.375)  # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Tenor melody - one short motif, make it sing
sax_notes = [
    (65, 1.5, 0.375),  # G (Fm7)
    (67, 1.875, 0.375), # A (Ab7)
    (65, 2.25, 0.375),  # G (Fm7)
    (68, 2.625, 0.375), # Bb

    (65, 2.8125, 0.375), # G
    (67, 3.1875, 0.375), # A
    (65, 3.5625, 0.375), # G
    (69, 3.9375, 0.375), # B

    (65, 4.3125, 0.375), # G
    (67, 4.6875, 0.375), # A
    (65, 5.0625, 0.375), # G
    (71, 5.4375, 0.375)  # D (half step resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
