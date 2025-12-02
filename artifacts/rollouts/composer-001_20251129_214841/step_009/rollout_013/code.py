
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    # Bar 3
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    # Bar 4
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375)  # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.375), # C
    (64, 1.875, 0.375), # E
    (67, 1.875, 0.375), # G
    (71, 1.875, 0.375), # B
    # Bar 3
    (62, 3.375, 0.375), # D
    (66, 3.375, 0.375), # F#
    (69, 3.375, 0.375), # A
    (73, 3.375, 0.375), # C#
    # Bar 4
    (64, 4.875, 0.375), # E
    (68, 4.875, 0.375), # G#
    (71, 4.875, 0.375), # B
    (76, 4.875, 0.375)  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125))

# Sax (Dante) - Melody
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # E
    (65, 2.25, 0.375),  # F
    (62, 2.625, 0.375), # D
    # Bar 3
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (64, 3.75, 0.375),  # E
    (62, 4.125, 0.375), # D
    # Bar 4
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375), # D
    (64, 5.25, 0.375),  # E
    (62, 5.625, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
