
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
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare_2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare_4 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat_1 = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    hihat_2 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat_3 = pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat_4 = pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    
    drums.notes.extend([kick_1, kick_3, snare_2, snare_4, hihat_1, hihat_2, hihat_3, hihat_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# Fm7: F, Ab, Bb, D
# Walking line in Fm: F, Gb, G, Ab, Bb, B, C, Db, D, Eb, E, F
bass_notes = [76, 75, 77, 78, 74, 76, 77, 78, 79, 77, 79, 80]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, D
# Bb7: Bb, D, F, Ab
# D7: D, F#, A, C
# Fm7 (bar 2), Bb7 (bar 3), D7 (bar 4)
chords = [
    [76, 81, 78, 73],  # Fm7
    [78, 73, 76, 81],  # Bb7
    [73, 77, 79, 75],  # D7
]
for bar_idx, chord in enumerate(chords):
    for note in chord:
        start = 1.5 + (bar_idx * 1.5) + 0.75  # 2nd beat
        end = start + 0.375
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)
    for note in chord:
        start = 1.5 + (bar_idx * 1.5) + 1.125  # 4th beat
        end = start + 0.375
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Gb, Bb, Ab -> F, Gb, Bb, Ab
# Bar 2: F, Gb, Bb, Ab
# Bar 3: rest
# Bar 4: F, Gb, Bb, Ab

# Bar 2
sax_notes = [76, 75, 78, 77]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# Bar 4
sax_notes = [76, 75, 78, 77]
for i, note in enumerate(sax_notes):
    start = 4.5 + (i * 0.375)
    end = start + 0.375
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
