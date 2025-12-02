
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=70, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 62, 100),  # D
    (1.875, 61, 100),  # C#
    (2.25, 64, 100),  # E
    (2.625, 62, 100),  # D
    (3.0, 65, 100),  # F#
    (3.375, 64, 100),  # E
    (3.75, 62, 100),  # D
    (4.125, 60, 100),  # C
    # Bar 3 (3.0 - 4.5s)
    (4.5, 62, 100),  # D
    (4.875, 61, 100),  # C#
    (5.25, 64, 100),  # E
    (5.625, 62, 100),  # D
    (6.0, 65, 100),  # F#
    (6.375, 64, 100),  # E
    (6.75, 62, 100),  # D
    (7.125, 60, 100),  # C
    # Bar 4 (4.5 - 6.0s)
    (7.5, 62, 100),  # D
    (7.875, 61, 100),  # C#
    (8.25, 64, 100),  # E
    (8.625, 62, 100),  # D
    (9.0, 65, 100),  # F#
    (9.375, 64, 100),  # E
    (9.75, 62, 100),  # D
    (10.125, 60, 100)  # C
]
for note in bass_notes:
    start, pitch, velocity = note
    bass_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5 + 0.375, 62, 100),  # D7: D, F#, A, C
    (1.5 + 0.75, 64, 100),
    (1.5 + 0.75, 67, 100),
    (1.5 + 0.75, 60, 100),
    (1.5 + 1.125, 62, 100),
    (1.5 + 1.125, 64, 100),
    (1.5 + 1.125, 67, 100),
    (1.5 + 1.125, 60, 100),
    # Bar 3 (3.0 - 4.5s)
    (3.0 + 0.375, 62, 100),
    (3.0 + 0.75, 64, 100),
    (3.0 + 0.75, 67, 100),
    (3.0 + 0.75, 60, 100),
    (3.0 + 1.125, 62, 100),
    (3.0 + 1.125, 64, 100),
    (3.0 + 1.125, 67, 100),
    (3.0 + 1.125, 60, 100),
    # Bar 4 (4.5 - 6.0s)
    (4.5 + 0.375, 62, 100),
    (4.5 + 0.75, 64, 100),
    (4.5 + 0.75, 67, 100),
    (4.5 + 0.75, 60, 100),
    (4.5 + 1.125, 62, 100),
    (4.5 + 1.125, 64, 100),
    (4.5 + 1.125, 67, 100),
    (4.5 + 1.125, 60, 100)
]
for note in piano_notes:
    start, pitch, velocity = note
    piano_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(piano_note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=70, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (66), A (69), D (62) - D (62), C (60), B (59), D (62)
sax_notes = [
    (1.5, 62, 100),  # D
    (1.875, 66, 100),  # F#
    (2.25, 69, 100),  # A
    (2.625, 62, 100),  # D
    (3.0, 60, 100),  # C
    (3.375, 59, 100),  # B
    (3.75, 62, 100),  # D
    (4.125, 62, 100),  # D
    (4.5, 66, 100),  # F#
    (4.875, 69, 100),  # A
    (5.25, 62, 100),  # D
    (5.625, 60, 100),  # C
    (6.0, 59, 100),  # B
    (6.375, 62, 100)  # D
]
for note in sax_notes:
    start, pitch, velocity = note
    sax_note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
