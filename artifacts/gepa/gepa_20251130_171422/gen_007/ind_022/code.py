
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
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375),
    (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375),
    (38, 2.25, 0.375),
    # Hi-hat on every eighth
    (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s)
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (62, 2.625, 0.375), # D
    # Bar 3 (3.0s - 4.5s)
    (60, 3.0, 0.375),  # C
    (61, 3.375, 0.375), # C#
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # C
    # Bar 4 (4.5s - 6.0s)
    (64, 4.5, 0.375),  # E
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = []
# Bar 2 (1.5s - 3.0s)
piano_notes.extend([
    (64, 1.875, 0.375),  # D7 (D, F#, A, C)
    (69, 1.875, 0.375),
    (67, 1.875, 0.375),
    (62, 1.875, 0.375)
])
# Bar 3 (3.0s - 4.5s)
piano_notes.extend([
    (64, 3.375, 0.375),  # D7
    (69, 3.375, 0.375),
    (67, 3.375, 0.375),
    (62, 3.375, 0.375)
])
# Bar 4 (4.5s - 6.0s)
piano_notes.extend([
    (64, 5.25, 0.375),  # D7
    (69, 5.25, 0.375),
    (67, 5.25, 0.375),
    (62, 5.25, 0.375)
])
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante) - one short motif, make it sing
sax_notes = [
    # Bar 2 (1.5s - 3.0s)
    (62, 1.5, 0.375),  # D
    (66, 1.875, 0.375),  # G
    (67, 2.25, 0.375),  # G#
    (66, 2.625, 0.375),  # G
    # Bar 3 (3.0s - 4.5s)
    (62, 3.0, 0.375),  # D
    (65, 3.375, 0.375),  # F#
    (67, 3.75, 0.375),  # G#
    (66, 4.125, 0.375),  # G
    # Bar 4 (4.5s - 6.0s)
    (62, 4.5, 0.375),  # D
    (65, 4.875, 0.375),  # F#
    (67, 5.25, 0.375),  # G#
    (66, 5.625, 0.375)  # G
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Drums continue (bars 2-4)
drum_notes_2 = [
    # Kick on 1 and 3
    (36, 1.5, 0.375),
    (36, 2.625, 0.375),
    (36, 3.75, 0.375),
    (36, 4.875, 0.375),
    # Snare on 2 and 4
    (38, 1.875, 0.375),
    (38, 3.0, 0.375),
    (38, 4.125, 0.375),
    (38, 5.25, 0.375),
    # Hi-hat on every eighth
    (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875)
]
for note in drum_notes_2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_moment.mid')
