
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

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (60, 1.875, 0.375), (61, 2.25, 0.375), (63, 2.625, 0.375),
    # Bar 3
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (59, 4.125, 0.375),
    # Bar 4
    (60, 4.5, 0.375), (62, 4.875, 0.375), (63, 5.25, 0.375), (64, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.1875), (64, 1.875, 0.1875), (67, 1.875, 0.1875),
    (60, 2.25, 0.1875), (64, 2.25, 0.1875), (67, 2.25, 0.1875),
    (60, 2.625, 0.1875), (64, 2.625, 0.1875), (67, 2.625, 0.1875),
    # Bar 3
    (60, 3.375, 0.1875), (64, 3.375, 0.1875), (67, 3.375, 0.1875),
    (60, 3.75, 0.1875), (64, 3.75, 0.1875), (67, 3.75, 0.1875),
    (60, 4.125, 0.1875), (64, 4.125, 0.1875), (67, 4.125, 0.1875),
    # Bar 4
    (60, 4.875, 0.1875), (64, 4.875, 0.1875), (67, 4.875, 0.1875),
    (60, 5.25, 0.1875), (64, 5.25, 0.1875), (67, 5.25, 0.1875),
    (60, 5.625, 0.1875), (64, 5.625, 0.1875), (67, 5.625, 0.1875)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_notes = [
    (60, 1.5, 0.375), (62, 1.875, 0.375), (64, 2.25, 0.375),  # First phrase
]

# Bar 3: Silence, let it breathe
# No notes here

# Bar 4: Return, finish the motif
sax_notes.extend([
    (62, 4.5, 0.375), (64, 4.875, 0.375), (65, 5.25, 0.375), (64, 5.625, 0.375)
])

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_moment.mid")
