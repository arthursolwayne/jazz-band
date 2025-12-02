
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# BAR 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (F2, G2, A2, C3)
bass_notes = [
    (1.5, 78), (1.875, 80), (2.25, 82), (2.625, 84)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (1.5, 77), (1.5, 69), (1.5, 65), (1.5, 67),
    (1.875, 77), (1.875, 69), (1.875, 65), (1.875, 67),
    (2.25, 77), (2.25, 69), (2.25, 65), (2.25, 67),
    (2.625, 77), (2.625, 69), (2.625, 65), (2.625, 67)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Melody (F, G, Bb, A)
sax_notes = [
    (1.5, 84), (1.875, 87), (2.25, 81), (2.625, 81)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# BAR 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (Bb2, D2, F2, A2)
bass_notes = [
    (3.0, 81), (3.375, 65), (3.75, 77), (4.125, 82)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 81), (3.0, 69), (3.0, 77), (3.0, 74),
    (3.375, 81), (3.375, 69), (3.375, 77), (3.375, 74),
    (3.75, 81), (3.75, 69), (3.75, 77), (3.75, 74),
    (4.125, 81), (4.125, 69), (4.125, 77), (4.125, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Melody (Bb, C, D, F)
sax_notes = [
    (3.0, 81), (3.375, 84), (3.75, 87), (4.125, 84)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# BAR 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (C2, Bb2, D2, F2)
bass_notes = [
    (4.5, 65), (4.875, 81), (5.25, 69), (5.625, 77)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    (4.5, 65), (4.5, 69), (4.5, 72), (4.5, 81),
    (4.875, 65), (4.875, 69), (4.875, 72), (4.875, 81),
    (5.25, 65), (5.25, 69), (5.25, 72), (5.25, 81),
    (5.625, 65), (5.625, 69), (5.625, 72), (5.625, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Melody (C, Bb, A, F)
sax_notes = [
    (4.5, 84), (4.875, 81), (5.25, 81), (5.625, 84)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
