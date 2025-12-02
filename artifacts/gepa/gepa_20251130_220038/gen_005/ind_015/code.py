
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875), (42, 2.8125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
# D minor scale: D, Eb, F, G, Ab, Bb, C
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (60, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), (63, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
# D7: D, F#, A, C
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.375), (67, 1.875, 0.375), (74, 1.875, 0.375), (76, 1.875, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (62, 3.375, 0.375), (67, 3.375, 0.375), (74, 3.375, 0.375), (76, 3.375, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.875, 0.375), (67, 4.875, 0.375), (74, 4.875, 0.375), (76, 4.875, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), G (67), D (62) - staggered entrance
sax_notes = [
    (62, 1.5, 0.125), (65, 1.625, 0.125), (67, 1.75, 0.125),
    (62, 3.0, 0.125), (65, 3.125, 0.125), (67, 3.25, 0.125),
    (62, 4.5, 0.125), (65, 4.625, 0.125), (67, 4.75, 0.125)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_intro.mid")
