
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # seconds
for i in range(4):
    time = i * bar_length / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 2)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_length / 4, end=time + bar_length / 2)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_length / 2, end=time + 3 * bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + 3 * bar_length / 4, end=time + bar_length)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    (1.5, 62, 100),  # C3
    (2.0, 63, 100),  # C#3
    (2.5, 64, 100),  # D3
    (3.0, 65, 100),  # D#3
    (3.5, 66, 100),  # E3
    (4.0, 67, 100),  # F3
    (4.5, 68, 100),  # F#3
    (5.0, 69, 100),  # G3
    (5.5, 70, 100),  # G#3
    (6.0, 71, 100),  # A3
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.5)
    bass.notes.append(note)

# Piano - Diane
piano_notes = [
    (1.5, 60, 100),  # C4
    (1.75, 64, 100),  # E4
    (2.0, 67, 100),  # G4
    (2.25, 71, 100),  # B4
    (2.5, 72, 100),  # C5
    (2.75, 76, 100),  # E5
    (3.0, 79, 100),  # G5
    (3.25, 84, 100),  # B5
    (3.5, 80, 100),  # C6
    (3.75, 84, 100),  # E6
    (4.0, 87, 100),  # G6
    (4.25, 92, 100),  # B6
    (4.5, 93, 100),  # C7
    (4.75, 97, 100),  # E7
    (5.0, 100, 100),  # G7
    (5.25, 104, 100),  # B7
    (5.5, 105, 100),  # C8
    (5.75, 109, 100),  # E8
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Saxophone - Dante
sax_notes = [
    (1.5, 62, 100),  # C4
    (1.75, 66, 100),  # E4
    (2.0, 67, 100),  # F4
    (2.25, 69, 100),  # G4
    (2.5, 66, 100),  # E4
    (2.75, 64, 100),  # D4
    (3.0, 62, 100),  # C4
    (3.25, 66, 100),  # E4
    (3.5, 67, 100),  # F4
    (3.75, 69, 100),  # G4
    (4.0, 66, 100),  # E4
    (4.25, 64, 100),  # D4
    (4.5, 62, 100),  # C4
    (4.75, 66, 100),  # E4
    (5.0, 67, 100),  # F4
    (5.25, 69, 100),  # G4
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums continue in bars 2-4
for i in range(4):
    time = 1.5 + i * bar_length / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 4, end=time + bar_length / 2)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_length / 4, end=time + bar_length / 2)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + bar_length / 2, end=time + 3 * bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time + 3 * bar_length / 4, end=time + bar_length)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
