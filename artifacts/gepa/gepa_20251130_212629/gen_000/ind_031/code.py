
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
drum_notes = [
    (36, 0.0),   # Kick on 1
    (38, 0.5),   # Snare on 2
    (42, 0.0),   # Hihat on 1
    (42, 0.25),  # Hihat on 1+
    (42, 0.5),   # Hihat on 2
    (42, 0.75),  # Hihat on 2+
    (36, 1.0),   # Kick on 3
    (38, 1.5),   # Snare on 4
    (42, 1.0),   # Hihat on 3
    (42, 1.25),  # Hihat on 3+
    (42, 1.5),   # Hihat on 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    (45, 1.5),   # F (root)
    (47, 1.75),  # Ab (b9)
    (49, 2.0),   # C (11)
    (48, 2.25),  # Bb (7)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: Comping on 2 and 4 with F7 chords (F, A, C, Eb)
piano_notes = [
    (53, 1.75),  # A (F7)
    (55, 1.75),  # C (F7)
    (50, 1.75),  # F (F7)
    (52, 1.75),  # Eb (F7)
    (53, 2.25),  # A (F7)
    (55, 2.25),  # C (F7)
    (50, 2.25),  # F (F7)
    (52, 2.25),  # Eb (F7)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Dante: Saxophone melody (short motif, starts on 1.5s)
sax_notes = [
    (60, 1.5),   # C (Fm3)
    (62, 1.875), # Eb (Fm5)
    (64, 2.25),  # F (Fm root)
    (60, 2.625), # C (Fm3)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm
bass_notes = [
    (48, 3.0),   # Bb (7)
    (45, 3.25),  # F (root)
    (47, 3.5),   # Ab (b9)
    (49, 3.75),  # C (11)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: Comping on 2 and 4 with F7 chords
piano_notes = [
    (53, 3.25),  # A (F7)
    (55, 3.25),  # C (F7)
    (50, 3.25),  # F (F7)
    (52, 3.25),  # Eb (F7)
    (53, 3.75),  # A (F7)
    (55, 3.75),  # C (F7)
    (50, 3.75),  # F (F7)
    (52, 3.75),  # Eb (F7)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0),   # Kick on 1
    (38, 3.5),   # Snare on 2
    (42, 3.0),   # Hihat on 1
    (42, 3.25),  # Hihat on 1+
    (42, 3.5),   # Hihat on 2
    (42, 3.75),  # Hihat on 2+
    (36, 4.0),   # Kick on 3
    (38, 4.5),   # Snare on 4
    (42, 4.0),   # Hihat on 3
    (42, 4.25),  # Hihat on 3+
    (42, 4.5),   # Hihat on 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    (49, 4.5),   # C (11)
    (48, 4.75),  # Bb (7)
    (45, 5.0),   # F (root)
    (47, 5.25),  # Ab (b9)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Diane: Comping on 2 and 4 with F7 chords
piano_notes = [
    (53, 4.75),  # A (F7)
    (55, 4.75),  # C (F7)
    (50, 4.75),  # F (F7)
    (52, 4.75),  # Eb (F7)
    (53, 5.25),  # A (F7)
    (55, 5.25),  # C (F7)
    (50, 5.25),  # F (F7)
    (52, 5.25),  # Eb (F7)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5),   # Kick on 1
    (38, 5.0),   # Snare on 2
    (42, 4.5),   # Hihat on 1
    (42, 4.75),  # Hihat on 1+
    (42, 5.0),   # Hihat on 2
    (42, 5.25),  # Hihat on 2+
    (36, 5.5),   # Kick on 3
    (38, 6.0),   # Snare on 4
    (42, 5.5),   # Hihat on 3
    (42, 5.75),  # Hihat on 3+
    (42, 6.0),   # Hihat on 4
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Dante: Saxophone melody (repeat of motif, finishes on 6.0s)
sax_notes = [
    (60, 4.5),   # C (Fm3)
    (62, 4.875), # Eb (Fm5)
    (64, 5.25),  # F (Fm root)
    (60, 5.625), # C (Fm3)
    (62, 6.0),   # Eb (Fm5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
