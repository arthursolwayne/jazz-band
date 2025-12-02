
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (20, 1.5, 0.375), (21, 1.875, 0.375),
    (22, 2.25, 0.375), (23, 2.625, 0.375),
    (21, 2.875, 0.375), (20, 3.25, 0.375),
    (19, 3.625, 0.375), (18, 4.0, 0.375),
    (19, 4.375, 0.375), (20, 4.75, 0.375),
    (21, 5.125, 0.375), (22, 5.5, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.125), (67, 1.5, 0.125), (69, 1.5, 0.125), (71, 1.5, 0.125),  # F7
    (64, 2.25, 0.125), (67, 2.25, 0.125), (69, 2.25, 0.125), (71, 2.25, 0.125),  # F7
    # Bar 3
    (64, 3.0, 0.125), (67, 3.0, 0.125), (69, 3.0, 0.125), (71, 3.0, 0.125),  # F7
    (64, 3.75, 0.125), (67, 3.75, 0.125), (69, 3.75, 0.125), (71, 3.75, 0.125),  # F7
    # Bar 4
    (64, 4.5, 0.125), (67, 4.5, 0.125), (69, 4.5, 0.125), (71, 4.5, 0.125),  # F7
    (64, 5.25, 0.125), (67, 5.25, 0.125), (69, 5.25, 0.125), (71, 5.25, 0.125)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (64, 1.5, 0.25),  # F
    (66, 1.75, 0.25),  # G
    (64, 2.0, 0.25),  # F
    (62, 2.25, 0.25),  # E
    (64, 2.75, 0.25),  # F
    (66, 3.0, 0.25),  # G
    (69, 3.25, 0.25),  # A
    (67, 3.5, 0.25),  # G
    (64, 4.0, 0.25),  # F
    (62, 4.25, 0.25),  # E
    (64, 4.75, 0.25),  # F
    (66, 5.0, 0.25),  # G
    (69, 5.25, 0.25)   # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
