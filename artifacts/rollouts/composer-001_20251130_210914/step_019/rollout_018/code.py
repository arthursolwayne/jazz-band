
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2: Start of the melody
# Bass: walking line in Fm
bass_notes = [7, 9, 10, 7, 8, 10, 11, 8, 9, 10, 11, 9, 10, 11, 12, 10]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 0.75  # On beat 2
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 1.5  # On beat 4
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: Melody in Fm
# Motif: Fm - G - Ab - F
sax_notes = [7, 8, 9, 7]
for i, pitch in enumerate(sax_notes):
    start = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch + 24, start=start, end=start + 0.375)
    sax.notes.append(note)

# Bar 3: Continue the melody and add a second phrase
# Motif: Bb - B - C - Bb
sax_notes = [10, 11, 12, 10]
for i, pitch in enumerate(sax_notes):
    start = 1.5 + 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch + 24, start=start, end=start + 0.375)
    sax.notes.append(note)

# Bar 4: Continue the melody and resolve
# Motif: F - G - Ab - F
sax_notes = [7, 8, 9, 7]
for i, pitch in enumerate(sax_notes):
    start = 1.5 + 3.0 + (i * 0.375)
    note = pretty_midi.Note(velocity=110, pitch=pitch + 24, start=start, end=start + 0.375)
    sax.notes.append(note)

# Bass: Walking line in Fm (Continuation)
bass_notes = [10, 11, 12, 10, 11, 12, 13, 11, 12, 13, 14, 12, 13, 14, 15, 13]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 0.75 + 1.5  # On beat 2 of bar 3
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 1.5 + 1.5  # On beat 4 of bar 3
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 3.0 + 0.75  # On beat 2 of bar 4
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

piano_notes = [7, 11, 10, 13]  # F7
for i, pitch in enumerate(piano_notes):
    start = 1.5 + 3.0 + 1.5  # On beat 4 of bar 4
    note = pretty_midi.Note(velocity=100, pitch=pitch + 24, start=start, end=start + 0.375)
    piano.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
