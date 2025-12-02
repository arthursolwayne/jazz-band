
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 & 2
    (42, 0.375, 0.1875), # Hihat on 2
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.1875),  # Hihat on 2 & 3
    (42, 1.125, 0.1875), # Hihat on 3
    (36, 1.5, 0.375),    # Kick on 3
    (42, 1.5, 0.1875),   # Hihat on 3 & 4
    (42, 1.875, 0.1875), # Hihat on 4
    (38, 2.25, 0.375),   # Snare on 4
    (42, 2.25, 0.1875),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    (44, 1.5, 0.375),  # Fm7
    (45, 1.875, 0.375), # Gb
    (42, 2.25, 0.375),  # Eb
    (41, 2.625, 0.375), # D
    (45, 2.625, 0.375), # Gb
    (44, 3.0, 0.375),   # F
    (42, 3.375, 0.375), # Eb
    (41, 3.75, 0.375),  # D
    (40, 4.125, 0.375), # C
    (42, 4.5, 0.375),   # Eb
    (44, 4.875, 0.375), # F
    (45, 5.25, 0.375),  # Gb
    (42, 5.625, 0.375), # Eb
    (41, 6.0, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (44, 1.5, 0.1875),  # F7
    (46, 1.5, 0.1875),
    (49, 1.5, 0.1875),
    (51, 1.5, 0.1875),
    # Bar 3
    (44, 1.5, 0.1875),  # F7
    (46, 1.5, 0.1875),
    (49, 1.5, 0.1875),
    (51, 1.5, 0.1875),
    # Bar 4
    (44, 1.5, 0.1875),  # F7
    (46, 1.5, 0.1875),
    (49, 1.5, 0.1875),
    (51, 1.5, 0.1875),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (44, 1.5, 0.375),  # F (start)
    (46, 2.25, 0.375),  # Gb (return)
    (44, 3.0, 0.375),  # F (finish)
    (49, 3.75, 0.375),  # Bb
    (46, 4.5, 0.375),  # Gb
    (44, 5.25, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Full bar
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1 & 2
    (42, 1.875, 0.1875), # Hihat on 2
    (38, 2.25, 0.375),   # Snare on 2
    (42, 2.25, 0.1875),  # Hihat on 2 & 3
    (42, 2.625, 0.1875), # Hihat on 3
    (36, 3.0, 0.375),    # Kick on 3
    (42, 3.0, 0.1875),   # Hihat on 3 & 4
    (42, 3.375, 0.1875), # Hihat on 4
    (38, 3.75, 0.375),   # Snare on 4
    (42, 3.75, 0.1875),  # Hihat on 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1 & 2
    (42, 4.875, 0.1875), # Hihat on 2
    (38, 5.25, 0.375),   # Snare on 2
    (42, 5.25, 0.1875),  # Hihat on 2 & 3
    (42, 5.625, 0.1875), # Hihat on 3
    (36, 6.0, 0.375),    # Kick on 3
    (42, 6.0, 0.1875),   # Hihat on 3 & 4
    (42, 6.375, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_piece.mid")
