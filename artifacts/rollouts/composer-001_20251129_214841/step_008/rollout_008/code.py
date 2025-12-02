
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums in Bar 1
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.75),   # Hihat on 2
    (36, 0.75, 1.125),   # Kick on 3
    (42, 1.125, 1.5),    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),    # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),   # D
    (63, 2.625, 0.375),  # D#
    (64, 3.0, 0.375),    # E
    (65, 3.375, 0.375),  # F
    (66, 3.75, 0.375),   # F#
    (67, 4.125, 0.375),  # G
    (68, 4.5, 0.375),    # G#
    (69, 4.875, 0.375),  # A
    (70, 5.25, 0.375),   # A#
    (71, 5.625, 0.375),  # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 1.875, 0.375),  # C
    (64, 1.875, 0.375),  # E
    (67, 1.875, 0.375),  # G
    (71, 1.875, 0.375),  # B
    # Bar 3: F7 on beat 2
    (65, 3.375, 0.375),  # F
    (69, 3.375, 0.375),  # A
    (71, 3.375, 0.375),  # B
    (76, 3.375, 0.375),  # E
    # Bar 4: G7 on beat 2
    (67, 4.875, 0.375),  # G
    (71, 4.875, 0.375),  # B
    (74, 4.875, 0.375),  # D
    (78, 4.875, 0.375),  # F#
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums in Bars 2-4 (same pattern)
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375),    # Kick on 1
        (42, start + 0.375, 0.75),   # Hihat on 2
        (36, start + 0.75, 1.125),   # Kick on 3
        (42, start + 1.125, 1.5),    # Hihat on 4
    ]
    for note, start_time, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Saxophone (Dante): Motif
# Bar 2: Start the motif
sax_notes = [
    (64, 1.5, 0.375),    # E
    (66, 1.875, 0.375),  # G
    (69, 2.25, 0.375),   # B
    (67, 2.625, 0.375),  # G
    (64, 3.0, 0.375),    # E
    (62, 3.375, 0.375),  # D
    (60, 3.75, 0.375),   # C
    (62, 4.125, 0.375),  # D
    (64, 4.5, 0.375),    # E
    (66, 4.875, 0.375),  # G
    (69, 5.25, 0.375),   # B
    (67, 5.625, 0.375),  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
