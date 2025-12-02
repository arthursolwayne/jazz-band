
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
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (1.5, 49), # F
    (1.875, 50), # Gb
    (2.25, 51), # G
    (2.625, 53), # A
    (2.875, 52), # Ab
    (3.25, 51), # G
    (3.625, 50), # Gb
    (4.0, 49), # F
    (4.375, 51), # G
    (4.75, 52), # Ab
    (5.125, 53), # A
    (5.5, 51), # G
    (5.875, 50), # Gb
    (6.25, 49) # F
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 64), (1.875, 67), (1.875, 69), # F7 (F A C E)
    (2.625, 64), (2.625, 67), (2.625, 69), # F7 again
    # Bar 3
    (3.625, 69), (3.625, 71), (3.625, 72), (3.625, 74), # A7 (A C# E G)
    (4.375, 69), (4.375, 71), (4.375, 72), (4.375, 74), # A7 again
    # Bar 4
    (5.125, 71), (5.125, 74), (5.125, 76), (5.125, 78), # C#7 (C# E G B)
    (5.875, 71), (5.875, 74), (5.875, 76), (5.875, 78) # C#7 again
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66), # D
    (1.75, 69), # F
    (2.0, 64), # F (Fm root)
    (2.25, 69), # F
    (2.5, 66), # D
    (2.75, 69), # F
    (3.0, 64), # F
    (3.25, 72), # A
    (3.5, 69), # F
    (3.75, 67), # E
    (4.0, 64), # F
    (4.25, 69), # F
    (4.5, 67), # E
    (4.75, 64), # F
    (5.0, 66), # D
    (5.25, 69), # F
    (5.5, 64), # F
    (5.75, 69), # F
    (6.0, 66) # D
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
