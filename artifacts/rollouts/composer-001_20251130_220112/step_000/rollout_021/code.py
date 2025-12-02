
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
for beat in [0, 2]:  # 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [1, 3]:  # 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in range(4):  # every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=beat * 0.375, end=beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F
f = 71
bass_notes = [f, f+1, f-2, f+2, f, f+1, f-2, f+2]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.125
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Bars 2-4, 2 and 4
# Bar 2, beat 2: F7 = F, A, C, E
# Bar 2, beat 4: Bb7 = Bb, D, F, Ab
# Bar 3, beat 2: C7 = C, E, G, B
# Bar 3, beat 4: G7 = G, B, D, F
# Bar 4, beat 2: Am7 = A, C, E, G
# Bar 4, beat 4: D7 = D, F#, A, C
chord_notes = [
    [71, 74, 72, 76],  # F7
    [70, 73, 71, 69],  # Bb7
    [72, 76, 74, 79],  # C7
    [76, 79, 72, 74],  # G7
    [77, 79, 76, 74],  # Am7
    [74, 77, 79, 72],  # D7
]
for i, chord in enumerate(chord_notes):
    start = 1.5 + (i % 2) * 0.75 + 0.375  # beats 2 and 4 in bars 2, 3, 4
    end = start + 0.5
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Sax: motif starting on F (71)
# Phrase: F - Bb - C - F (ascending, then descending)
# Start on beat 2 of bar 2, play F (71) for 0.5s
# Then Bb (70) for 0.5s
# Then C (72) for 0.5s
# Then F (71) for 0.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.75),
    pretty_midi.Note(velocity=110, pitch=70, start=2.75, end=3.25),
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.25),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet
# Bass: walking line
bass_notes = [f, f+1, f-2, f+2, f, f+1, f-2, f+2]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    end = start + 0.125
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Bar 3, beat 2: C7 = C, E, G, B
# Bar 3, beat 4: G7 = G, B, D, F
chord_notes = [
    [72, 76, 74, 79],  # C7
    [76, 79, 72, 74],  # G7
]
for i, chord in enumerate(chord_notes):
    start = 3.0 + (i % 2) * 0.75 + 0.375  # beats 2 and 4 in bar 3
    end = start + 0.5
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Drums: same pattern
for beat in [0, 2]:  # 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=3.0 + beat * 0.375, end=3.0 + beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [1, 3]:  # 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=3.0 + beat * 0.375, end=3.0 + beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in range(4):  # every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=3.0 + beat * 0.375, end=3.0 + beat * 0.375 + 0.125)
    drums.notes.append(note)

# Bar 4: Full quartet
# Bass: walking line
bass_notes = [f, f+1, f-2, f+2, f, f+1, f-2, f+2]
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    end = start + 0.125
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
# Bar 4, beat 2: Am7 = A, C, E, G
# Bar 4, beat 4: D7 = D, F#, A, C
chord_notes = [
    [77, 79, 76, 74],  # Am7
    [74, 77, 79, 72],  # D7
]
for i, chord in enumerate(chord_notes):
    start = 4.5 + (i % 2) * 0.75 + 0.375  # beats 2 and 4 in bar 4
    end = start + 0.5
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Drums: same pattern
for beat in [0, 2]:  # 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=4.5 + beat * 0.375, end=4.5 + beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in [1, 3]:  # 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=4.5 + beat * 0.375, end=4.5 + beat * 0.375 + 0.125)
    drums.notes.append(note)
for beat in range(4):  # every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=4.5 + beat * 0.375, end=4.5 + beat * 0.375 + 0.125)
    drums.notes.append(note)

# Sax: second motif, variation
# Phrase: F - Bb - C - F (ascending, then descending)
# Start on beat 2 of bar 4, play F (71) for 0.5s
# Then Bb (70) for 0.5s
# Then C (72) for 0.5s
# Then F (71) for 0.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.75),
    pretty_midi.Note(velocity=110, pitch=70, start=5.75, end=6.25),
    pretty_midi.Note(velocity=110, pitch=72, start=6.25, end=6.75),
    pretty_midi.Note(velocity=110, pitch=71, start=6.75, end=7.25),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
