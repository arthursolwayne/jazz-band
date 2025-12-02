
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1, 1, 1.5, 2.0),  # F2
    (1, 1, 1.5, 2.0),  # Bb2
    (1, 1, 1.5, 2.0),  # C3
    (1, 1, 1.5, 2.0),  # F2
    (1, 1, 1.5, 2.0),  # G2
    (1, 1, 1.5, 2.0),  # Bb2
    (1, 1, 1.5, 2.0),  # C3
    (1, 1, 1.5, 2.0),  # F2
]
for i, (pitch, velocity, start, end) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7
for pitch in [56, 60, 64, 67]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5, end=2.0)
    piano.notes.append(note)
# Bar 3: Bb7
for pitch in [59, 62, 66, 69]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=2.0, end=2.5)
    piano.notes.append(note)
# Bar 4: C7
for pitch in [60, 64, 67, 71]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=2.5, end=3.0)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66) -> G (67) -> Bb (69) -> F (66)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0)
sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1, 1, 3.0, 3.5),  # F2
    (1, 1, 3.0, 3.5),  # Bb2
    (1, 1, 3.0, 3.5),  # C3
    (1, 1, 3.0, 3.5),  # F2
    (1, 1, 3.0, 3.5),  # G2
    (1, 1, 3.0, 3.5),  # Bb2
    (1, 1, 3.0, 3.5),  # C3
    (1, 1, 3.0, 3.5),  # F2
]
for i, (pitch, velocity, start, end) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7
for pitch in [59, 62, 66, 69]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=3.0, end=3.5)
    piano.notes.append(note)
# Bar 4: C7
for pitch in [60, 64, 67, 71]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=3.5, end=4.0)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 3) * 0.375, end=(beat + 4) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(beat + 3) * 0.375, end=(beat + 4) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=(beat + 3) * 0.375, end=(beat + 4) * 0.375)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1, 1, 4.5, 5.0),  # F2
    (1, 1, 4.5, 5.0),  # Bb2
    (1, 1, 4.5, 5.0),  # C3
    (1, 1, 4.5, 5.0),  # F2
    (1, 1, 4.5, 5.0),  # G2
    (1, 1, 4.5, 5.0),  # Bb2
    (1, 1, 4.5, 5.0),  # C3
    (1, 1, 4.5, 5.0),  # F2
]
for i, (pitch, velocity, start, end) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch + 24, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fmaj7
for pitch in [56, 60, 64, 67]:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=4.5, end=5.0)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66) -> G (67) -> Bb (69) -> F (66)
note = pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0)
sax.notes.append(note)

# Bar 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=(beat + 4.5) * 0.375, end=(beat + 5.0) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=110, pitch=38, start=(beat + 4.5) * 0.375, end=(beat + 5.0) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=(beat + 4.5) * 0.375, end=(beat + 5.0) * 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_piece.mid")
