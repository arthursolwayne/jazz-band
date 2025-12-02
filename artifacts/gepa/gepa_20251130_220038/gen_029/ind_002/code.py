
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
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 2: Full quartet (1.5 - 3.0s)
start = 1.5
# Marcus - walking line in Fm (F, Eb, D, C, Bb, A, G, F)
bass_notes = [77, 74, 73, 72, 70, 69, 67, 77]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    bass.notes.append(note)

# Diane - 7th chords on 2 and 4
# Fm7 on beat 2, Bb7 on beat 4
# Fm7: F, Ab, Bb, D (77, 70, 72, 69)
# Bb7: Bb, D, F, Ab (72, 69, 77, 70)
chord1 = [77, 70, 72, 69]
chord2 = [72, 69, 77, 70]
for i, chord in enumerate([chord1, chord2]):
    for note in chord:
        n = pretty_midi.Note(velocity=100, pitch=note, start=start + (i + 1) * 0.375, end=start + (i + 1) * 0.375 + 0.1875)
        piano.notes.append(n)

# Dante - motif: F (77), Ab (70), G (67), F (77)
sax_notes = [77, 70, 67, 77]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
start = 3.0
# Marcus - walking line (F, Eb, D, C, Bb, A, G, F)
bass_notes = [77, 74, 73, 72, 70, 69, 67, 77]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    bass.notes.append(note)

# Diane - 7th chords on 2 and 4
# Fm7 on beat 2, Bb7 on beat 4
for i, chord in enumerate([chord1, chord2]):
    for note in chord:
        n = pretty_midi.Note(velocity=100, pitch=note, start=start + (i + 1) * 0.375, end=start + (i + 1) * 0.375 + 0.1875)
        piano.notes.append(n)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 4: Full quartet (4.5 - 6.0s)
start = 4.5
# Marcus - walking line (F, Eb, D, C, Bb, A, G, F)
bass_notes = [77, 74, 73, 72, 70, 69, 67, 77]
for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    bass.notes.append(note)

# Diane - 7th chords on 2 and 4
# Fm7 on beat 2, Bb7 on beat 4
for i, chord in enumerate([chord1, chord2]):
    for note in chord:
        n = pretty_midi.Note(velocity=100, pitch=note, start=start + (i + 1) * 0.375, end=start + (i + 1) * 0.375 + 0.1875)
        piano.notes.append(n)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 8):
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    drums.notes.append(hihat)
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
drums.notes.extend([kick1, kick2, snare1, snare2])

# Dante - motif: F (77), Ab (70), G (67), F (77)
sax_notes = [77, 70, 67, 77]
for i, pitch in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
