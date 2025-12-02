
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
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2 & 3
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 & 4
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),    # D (root)
    (63, 1.875, 0.375),  # Eb (b9)
    (60, 2.25, 0.375),   # C (5)
    (62, 2.625, 0.375),  # D (root)
    (64, 3.0, 0.375),    # E (3)
    (63, 3.375, 0.375),  # Eb (b9)
    (60, 3.75, 0.375),   # C (5)
    (62, 4.125, 0.375),  # D (root)
    (65, 4.5, 0.375),    # F (7)
    (63, 4.875, 0.375),  # Eb (b9)
    (60, 5.25, 0.375),   # C (5)
    (62, 5.625, 0.375)   # D (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),    # D7 (D, F#, A, C)
    (67, 1.5, 0.375),
    (69, 1.5, 0.375),
    (60, 1.5, 0.375),
    (62, 1.875, 0.375),  # D7 (comp on 2)
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (60, 1.875, 0.375),
    # Bar 3
    (62, 2.25, 0.375),   # D7
    (67, 2.25, 0.375),
    (69, 2.25, 0.375),
    (60, 2.25, 0.375),
    (62, 2.625, 0.375),  # D7 (comp on 4)
    (67, 2.625, 0.375),
    (69, 2.625, 0.375),
    (60, 2.625, 0.375),
    # Bar 4
    (62, 3.0, 0.375),    # D7
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    (60, 3.0, 0.375),
    (62, 3.375, 0.375),  # D7 (comp on 2)
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (60, 3.375, 0.375),
    (62, 3.75, 0.375),   # D7
    (67, 3.75, 0.375),
    (69, 3.75, 0.375),
    (60, 3.75, 0.375),
    (62, 4.125, 0.375),  # D7 (comp on 4)
    (67, 4.125, 0.375),
    (69, 4.125, 0.375),
    (60, 4.125, 0.375),
    (62, 4.5, 0.375),    # D7
    (67, 4.5, 0.375),
    (69, 4.5, 0.375),
    (60, 4.5, 0.375),
    (62, 4.875, 0.375),  # D7 (comp on 4)
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    (60, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),    # D (start motif)
    (65, 1.875, 0.375),  # F (hold)
    (62, 2.25, 0.375),   # D (resolve)
    (60, 2.625, 0.375),  # C (leave hanging)
    (62, 3.0, 0.375),    # D (return)
    (65, 3.375, 0.375),  # F (hold)
    (62, 3.75, 0.375),   # D (resolve)
    (60, 4.125, 0.375),  # C (end)
    (62, 4.5, 0.375),    # D (callback)
    (65, 4.875, 0.375)   # F (end)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.1875),   # Hihat on 1 & 2
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2 & 3
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.1875),  # Hihat on 3 & 4
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.1875),
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.1875),   # Hihat on 1 & 2
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2 & 3
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.1875),  # Hihat on 3 & 4
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.1875),
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.1875),   # Hihat on 1 & 2
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2 & 3
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3 & 4
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne.mid')
