
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
bar2_drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875) # Hihat on 4
]
for note, start, duration in bar2_drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bass (Marcus)
bass_notes = [
    (60, 1.5, 0.375),  # C4 on 1
    (61, 1.875, 0.375), # C#4 on 2
    (62, 2.25, 0.375),  # D4 on 3
    (63, 2.625, 0.375)  # D#4 on 4
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano (Diane)
piano_notes = [
    (71, 1.5, 0.375),  # G4 on 1
    (70, 1.875, 0.375), # F#4 on 2
    (69, 2.25, 0.375),  # F4 on 3
    (71, 2.625, 0.375)  # G4 on 4
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax (Dante)
sax_notes = [
    (66, 1.5, 0.375),  # E4 on 1
    (68, 1.875, 0.375), # F#4 on 2
    (69, 2.25, 0.375),  # G4 on 3
    (66, 2.625, 0.375)  # E4 on 4
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
bar3_drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875) # Hihat on 4
]
for note, start, duration in bar3_drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bass (Marcus)
bar3_bass_notes = [
    (64, 3.0, 0.375),  # E4 on 1
    (65, 3.375, 0.375), # F4 on 2
    (67, 3.75, 0.375),  # G4 on 3
    (68, 4.125, 0.375)  # G#4 on 4
]
for note, start, duration in bar3_bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano (Diane)
bar3_piano_notes = [
    (72, 3.0, 0.375),  # A4 on 1
    (71, 3.375, 0.375), # G4 on 2
    (69, 3.75, 0.375),  # F4 on 3
    (72, 4.125, 0.375)  # A4 on 4
]
for note, start, duration in bar3_piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax (Dante)
bar3_sax_notes = [
    (67, 3.0, 0.375),  # F#4 on 1
    (69, 3.375, 0.375), # G4 on 2
    (71, 3.75, 0.375),  # A4 on 3
    (67, 4.125, 0.375)  # F#4 on 4
]
for note, start, duration in bar3_sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
bar4_drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in bar4_drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bass (Marcus)
bar4_bass_notes = [
    (69, 4.5, 0.375),  # G4 on 1
    (71, 4.875, 0.375), # A4 on 2
    (72, 5.25, 0.375),  # A#4 on 3
    (71, 5.625, 0.375)  # A4 on 4
]
for note, start, duration in bar4_bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano (Diane)
bar4_piano_notes = [
    (72, 4.5, 0.375),  # A4 on 1
    (71, 4.875, 0.375), # G4 on 2
    (69, 5.25, 0.375),  # F4 on 3
    (72, 5.625, 0.375)  # A4 on 4
]
for note, start, duration in bar4_piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax (Dante)
bar4_sax_notes = [
    (71, 4.5, 0.375),  # A4 on 1
    (69, 4.875, 0.375), # F#4 on 2
    (67, 5.25, 0.375),  # F4 on 3
    (66, 5.625, 0.375)  # E4 on 4
]
for note, start, duration in bar4_sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
