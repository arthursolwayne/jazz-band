
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

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
    (36, 1.5, 0.375),  # F
    (37, 1.875, 0.375), # Gb
    (38, 2.25, 0.375),  # G
    (39, 2.625, 0.375), # Ab
    (40, 3.0, 0.375),   # A
    (41, 3.375, 0.375), # Bb
    (42, 3.75, 0.375),  # B
    (43, 4.125, 0.375), # C
    (44, 4.5, 0.375),   # C#
    (45, 4.875, 0.375), # D
    (46, 5.25, 0.375),  # D#
    (47, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (59, 1.875, 0.375), # F7 (F, A, C, E)
    (61, 1.875, 0.375),
    (64, 1.875, 0.375),
    (65, 1.875, 0.375),
    (59, 2.625, 0.375),
    (61, 2.625, 0.375),
    (64, 2.625, 0.375),
    (65, 2.625, 0.375),
    # Bar 3: D7 on 2 and 4
    (62, 3.375, 0.375), # D7 (D, F#, A, C#)
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375),
    (62, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (69, 4.125, 0.375),
    # Bar 4: B7 on 2 and 4
    (67, 4.875, 0.375), # B7 (B, D#, F#, A)
    (69, 4.875, 0.375),
    (71, 4.875, 0.375),
    (72, 4.875, 0.375),
    (67, 5.625, 0.375),
    (69, 5.625, 0.375),
    (71, 5.625, 0.375),
    (72, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray)
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante)
sax_notes = [
    (66, 1.5, 0.375),  # F
    (67, 1.875, 0.375), # G
    (68, 2.25, 0.375),  # A
    (69, 2.625, 0.375), # Bb
    (66, 3.0, 0.375),   # F
    (67, 3.375, 0.375), # G
    (68, 3.75, 0.375),  # A
    (69, 4.125, 0.375), # Bb
    (66, 4.5, 0.375),   # F
    (67, 4.875, 0.375), # G
    (68, 5.25, 0.375),  # A
    (69, 5.625, 0.375)  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
