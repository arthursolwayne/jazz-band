
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 2
    (42, 1.125, 0.375), # Hihat on 2
    (38, 1.5, 0.375),   # Snare on 4
    (42, 1.5, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (17, 1.5, 0.375),   # D (17) on 1
    (18, 1.875, 0.375), # Eb (18) on 2
    (19, 2.25, 0.375),  # E (19) on 3
    (17, 2.625, 0.375), # D (17) on 4
    (19, 3.0, 0.375),   # E (19) on 1
    (20, 3.375, 0.375), # F (20) on 2
    (21, 3.75, 0.375),  # F# (21) on 3
    (19, 4.125, 0.375), # E (19) on 4
    (21, 4.5, 0.375),   # F# (21) on 1
    (22, 4.875, 0.375), # G (22) on 2
    (23, 5.25, 0.375),  # G# (23) on 3
    (21, 5.625, 0.375)  # F# (21) on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    (53, 1.5, 0.375),   # B7 on 1
    (52, 1.875, 0.375), # Bb7 on 2
    (53, 2.25, 0.375),  # B7 on 3
    (52, 2.625, 0.375), # Bb7 on 4
    (53, 3.0, 0.375),   # B7 on 1
    (52, 3.375, 0.375), # Bb7 on 2
    (53, 3.75, 0.375),  # B7 on 3
    (52, 4.125, 0.375), # Bb7 on 4
    (53, 4.5, 0.375),   # B7 on 1
    (52, 4.875, 0.375), # Bb7 on 2
    (53, 5.25, 0.375),  # B7 on 3
    (52, 5.625, 0.375)  # Bb7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante)
sax_notes = [
    (62, 1.5, 0.375),   # C (62) on 1
    (65, 1.875, 0.375), # E (65) on 2
    (64, 2.25, 0.375),  # D (64) on 3
    (62, 2.625, 0.375), # C (62) on 4
    (67, 3.0, 0.375),   # G (67) on 1
    (69, 3.375, 0.375), # A (69) on 2
    (67, 3.75, 0.375),  # G (67) on 3
    (69, 4.125, 0.375), # A (69) on 4
    (62, 4.5, 0.375),   # C (62) on 1
    (65, 4.875, 0.375), # E (65) on 2
    (64, 5.25, 0.375),  # D (64) on 3
    (62, 5.625, 0.375)  # C (62) on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.375), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.375), # Hihat on 4

    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375), # Hihat on 4

    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
