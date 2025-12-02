
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
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# D minor key: D, Eb, F, G, A, Bb, C
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (61, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3
    (63, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (62, 4.5, 0.375), (61, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# C7: C, E, G, Bb
piano_notes = [
    # Bar 2: D7 on 2 and 4
    (62, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (64, 1.875, 0.375),
    (62, 2.625, 0.375), (67, 2.625, 0.375), (69, 2.625, 0.375), (64, 2.625, 0.375),
    # Bar 3: G7 on 2 and 4
    (67, 3.375, 0.375), (71, 3.375, 0.375), (69, 3.375, 0.375), (66, 3.375, 0.375),
    (67, 4.125, 0.375), (71, 4.125, 0.375), (69, 4.125, 0.375), (66, 4.125, 0.375),
    # Bar 4: C7 on 2 and 4
    (64, 4.875, 0.375), (69, 4.875, 0.375), (71, 4.875, 0.375), (67, 4.875, 0.375),
    (64, 5.625, 0.375), (69, 5.625, 0.375), (71, 5.625, 0.375), (67, 5.625, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D minor motif: D, Eb, F, D
sax_notes = [
    (62, 1.5, 0.375), (61, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),  # Melody
    (62, 3.0, 0.375), (61, 3.375, 0.375), (60, 3.75, 0.375), (62, 4.125, 0.375),  # Repeat
    (62, 4.5, 0.375), (61, 4.875, 0.375), (60, 5.25, 0.375), (62, 5.625, 0.375)   # Repeat
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Fill the bar
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875), (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875), (42, 2.0625, 0.1875), (36, 2.25, 0.375), (38, 2.625, 0.375),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875), (42, 2.8125, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875), (36, 3.75, 0.375), (38, 4.125, 0.375),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
