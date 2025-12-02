
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Snare on 2 and 4
    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hi-hats on every eighth
    for i in range(8):
        time = start + i * 0.375
        note_obj = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar_start = 1.5

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Dm7: D, F, A, C
# Root on beat 1, fifth on beat 2, chromatic approach on beat 3, root on beat 4
for bar in range(3):
    start = bar_start + bar * 1.5
    root = pretty_midi.Note(velocity=80, pitch=38, start=start, end=start + 0.25)
    fifth = pretty_midi.Note(velocity=80, pitch=43, start=start + 0.375, end=start + 0.625)
    chromatic = pretty_midi.Note(velocity=80, pitch=44, start=start + 0.75, end=start + 1.0)
    root2 = pretty_midi.Note(velocity=80, pitch=38, start=start + 1.125, end=start + 1.375)
    bass.notes.extend([root, fifth, chromatic, root2])

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
for note, time in zip([38, 41, 43, 45], [bar_start + 0.0, bar_start + 0.0, bar_start + 0.0, bar_start + 0.0]):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start, end=bar_start + 0.5)
    piano.notes.append(note_obj)
# Bar 3: Gm7 (G, Bb, D, F)
for note, time in zip([43, 46, 48, 50], [bar_start + 1.5, bar_start + 1.5, bar_start + 1.5, bar_start + 1.5]):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + 1.5, end=bar_start + 2.0)
    piano.notes.append(note_obj)
# Bar 4: Am7 (A, C, E, G)
for note, time in zip([45, 48, 52, 55], [bar_start + 3.0, bar_start + 3.0, bar_start + 3.0, bar_start + 3.0]):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + 3.0, end=bar_start + 3.5)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3):
    start = bar_start + bar * 1.5
    # Kick on 1 and 3
    kick_notes = [36, 36]
    kick_times = [start + 0.0, start + 0.75]
    for note, time in zip(kick_notes, kick_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Snare on 2 and 4
    snare_notes = [38, 38]
    snare_times = [start + 0.375, start + 1.125]
    for note, time in zip(snare_notes, snare_times):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(note_obj)
    # Hi-hats on every eighth
    for i in range(8):
        time = start + i * 0.375
        note_obj = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note_obj)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D, E, F, G, A, Bb, C, D
# Motif: D, F, G, C (D, F, G, C)
# Bar 2: Start the motif
for note, time in zip([38, 41, 43, 45], [bar_start + 0.0, bar_start + 0.25, bar_start + 0.5, bar_start + 0.75]):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.2)
    sax.notes.append(note_obj)
# Bar 3: Leave it hanging (no notes)
# Bar 4: Come back and finish it
for note, time in zip([38, 41, 43, 45], [bar_start + 3.0, bar_start + 3.25, bar_start + 3.5, bar_start + 3.75]):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.2)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
