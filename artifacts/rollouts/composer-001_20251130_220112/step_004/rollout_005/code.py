
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
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (36, 1.5, 0.375), (38, 1.875, 0.375)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5s)
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (61, 2.625, 0.375),
    # Bar 3 (3.0s)
    (63, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (61, 4.125, 0.375),
    # Bar 4 (4.5s)
    (60, 4.5, 0.375), (62, 4.875, 0.375), (63, 5.25, 0.375), (64, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on 2 and 4
    (69, 2.25, 0.375), (67, 2.25, 0.375), (65, 2.25, 0.375), (64, 2.25, 0.375),
    (69, 2.625, 0.375), (67, 2.625, 0.375), (65, 2.625, 0.375), (64, 2.625, 0.375),
    # Bar 3
    (69, 3.75, 0.375), (67, 3.75, 0.375), (65, 3.75, 0.375), (64, 3.75, 0.375),
    (69, 4.125, 0.375), (67, 4.125, 0.375), (65, 4.125, 0.375), (64, 4.125, 0.375),
    # Bar 4
    (69, 5.25, 0.375), (67, 5.25, 0.375), (65, 5.25, 0.375), (64, 5.25, 0.375),
    (69, 5.625, 0.375), (67, 5.625, 0.375), (65, 5.625, 0.375), (64, 5.625, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, motif that starts and ends with D (62), with a chromatic twist
sax_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (62, 3.75, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
