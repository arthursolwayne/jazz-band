
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 48, 100),  # F3
    (1.875, 49, 100),  # F#3
    (2.25, 50, 100),  # G3
    (2.625, 51, 100),  # G#3
    (3.0, 52, 100),  # A3
    (3.375, 53, 100),  # A#3
    (3.75, 54, 100),  # B3
    (4.125, 55, 100),  # C4
    (4.5, 56, 100),  # C#4
    (4.875, 57, 100),  # D4
    (5.25, 58, 100),  # D#4
    (5.625, 59, 100),  # E4
    (6.0, 60, 100)    # F4
]
for start, pitch, velocity in bass_notes:
    bass_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
# Bar 2 (1.5 - 3.0s): F7
piano_notes = [
    (1.5, 60, 100),  # F4
    (1.5, 64, 100),  # A4
    (1.5, 65, 100),  # A#4
    (1.5, 67, 100),  # C#5
    # Bar 3 (3.0 - 4.5s): B7
    (3.0, 69, 100),  # B4
    (3.0, 72, 100),  # D5
    (3.0, 73, 100),  # D#5
    (3.0, 76, 100),  # F#5
    # Bar 4 (4.5 - 6.0s): E7
    (4.5, 64, 100),  # A4
    (4.5, 67, 100),  # C#5
    (4.5, 68, 100),  # D5
    (4.5, 71, 100),  # F5
]
for start, pitch, velocity in piano_notes:
    piano_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Drums: continue with kick, snare, hihat for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax (Dante): Start the motif, leave it hanging, come back and finish it
# F7 (F4, A4, C#5, E5)
sax_notes = [
    (1.5, 60, 100),  # F4
    (1.5, 64, 100),  # A4
    (1.5, 67, 100),  # C#5
    (1.5, 69, 100),  # E5
    # Leave it hanging
    (2.625, 60, 100),  # F4
    (2.625, 64, 100),  # A4
    (2.625, 67, 100),  # C#5
    (3.0, 60, 100),  # F4
    (3.0, 64, 100),  # A4
    (3.0, 67, 100),  # C#5
    (3.0, 69, 100),  # E5
    (4.5, 60, 100),  # F4
    (4.5, 64, 100),  # A4
    (4.5, 67, 100),  # C#5
    (4.5, 69, 100),  # E5
    (5.625, 60, 100),  # F4
    (5.625, 64, 100),  # A4
    (5.625, 67, 100),  # C#5
    (6.0, 60, 100),  # F4
    (6.0, 64, 100),  # A4
    (6.0, 67, 100),  # C#5
    (6.0, 69, 100)   # E5
]
for start, pitch, velocity in sax_notes:
    sax_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
