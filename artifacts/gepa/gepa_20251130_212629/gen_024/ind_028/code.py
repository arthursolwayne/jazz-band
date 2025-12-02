
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875),
    (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875),
    (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375)   # Kick on 3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (62, 1.5, 0.375),  # D
    (60, 1.875, 0.375), # Bb
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375), # F
    (65, 3.0, 0.375),   # F#
    (64, 3.375, 0.375), # F
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # Bb
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # F
    (65, 5.25, 0.375),  # F#
    (67, 5.625, 0.375)  # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),  # D7: D, F#, A, C
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    (60, 1.5, 0.375),
    (62, 2.25, 0.375), # D7 again on 3
    (64, 2.25, 0.375),
    (67, 2.25, 0.375),
    (60, 2.25, 0.375),
    (62, 3.0, 0.375),  # D7 on 4
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    (60, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D, F, A, C
sax_notes = [
    (62, 1.5, 0.25),   # D
    (60, 1.75, 0.25),  # F
    (67, 2.0, 0.25),   # A
    (60, 2.25, 0.25),  # F
    (62, 2.5, 0.25),   # D
    (67, 2.75, 0.25),  # A
    (65, 3.0, 0.25),   # F#
    (62, 3.25, 0.25),  # D
    (67, 3.5, 0.25),   # A
    (65, 3.75, 0.25),  # F#
    (62, 4.0, 0.25),   # D
    (67, 4.25, 0.25),  # A
    (65, 4.5, 0.25),   # F#
    (62, 4.75, 0.25)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1 & 2
    (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875),
    (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875),
    (42, 2.4375, 0.1875),
    (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    (36, 3.0, 0.375),  # Kick on 3
    (38, 3.375, 0.375), # Snare on 4
    (42, 3.0, 0.1875), # Hihat on 3 & 4
    (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875),
    (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875),
    (42, 3.9375, 0.1875),
    (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1 & 2
    (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875),
    (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875),
    (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    (36, 6.0, 0.375)   # Kick on 3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
