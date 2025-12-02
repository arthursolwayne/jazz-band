
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875),
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375),
    (65, 4.5, 0.375), (67, 4.875, 0.375), (65, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    (58, 1.875, 0.375), (62, 1.875, 0.375), (60, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 3: Gm7 (Bb, D, F, G)
    (57, 3.375, 0.375), (62, 3.375, 0.375), (59, 3.375, 0.375), (60, 3.375, 0.375),
    # Bar 4: Cm7 (Eb, G, Bb, C)
    (61, 4.875, 0.375), (67, 4.875, 0.375), (60, 4.875, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 2.625, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.875, 0.375), (38, 5.25, 0.375), (42, 4.875, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D, Eb, F, G, A, Bb, C, D
sax_notes = [
    (62, 1.5, 0.375),       # D
    (60, 1.875, 0.375),     # Bb
    (62, 2.25, 0.375),      # D
    (64, 2.625, 0.375),     # F
    (62, 3.0, 0.375),       # D
    (60, 3.375, 0.375),     # Bb
    (62, 3.75, 0.375),      # D
    (64, 4.125, 0.375),     # F
    (67, 4.5, 0.375),       # A
    (64, 4.875, 0.375),     # F
    (62, 5.25, 0.375),      # D
    (60, 5.625, 0.375)      # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
