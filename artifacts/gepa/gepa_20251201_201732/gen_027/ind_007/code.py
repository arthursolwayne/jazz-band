
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(snare_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75 + 0.1875, end=bar1_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(note_obj)

for i, note in enumerate(hihat_notes):
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.1875)
    drums.notes.append(note_obj)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bar2_start = 1.5
bar2_end = 3.0
bar3_start = 3.0
bar3_end = 4.5
bar4_start = 4.5
bar4_end = 6.0

# Fm7 -> Bb7 -> Eb7 -> Am7 (ii-V-I in Fm)
# Roots: F, Bb, Eb, A (MIDI 53, 58, 61, 65)
# Fifths: C, F, Bb, E (MIDI 60, 65, 69, 69)

# Bar 2 - Fm7
bass_notes = [53, 60, 53, 60]  # F, C, F, C (chromatic approach to Bb)
for i, pitch in enumerate(bass_notes):
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.375)
    bass.notes.append(note_obj)

# Bar 3 - Bb7
bass_notes = [58, 65, 58, 65]  # Bb, F, Bb, F (chromatic approach to Eb)
for i, pitch in enumerate(bass_notes):
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.375)
    bass.notes.append(note_obj)

# Bar 4 - Eb7
bass_notes = [61, 69, 61, 69]  # Eb, Bb, Eb, Bb (chromatic approach to A)
for i, pitch in enumerate(bass_notes):
    note_obj = pretty_midi.Note(velocity=90, pitch=pitch, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.375)
    bass.notes.append(note_obj)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2 - Fm7: F, Ab, C, Eb
piano_notes = [53, 61, 65, 64]
for i, pitch in enumerate(piano_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=bar2_start, end=bar2_end)
    piano.notes.append(note_obj)

# Bar 3 - Bb7: Bb, D, F, Ab
piano_notes = [58, 62, 65, 61]
for i, pitch in enumerate(piano_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=bar3_start, end=bar3_end)
    piano.notes.append(note_obj)

# Bar 4 - Eb7: Eb, G, Bb, Db
piano_notes = [61, 67, 58, 60]
for i, pitch in enumerate(piano_notes):
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=bar4_start, end=bar4_end)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bb7 -> Eb7 -> Am7
# Melody: F, Ab, Bb, Eb (starting on F, resolving on Eb)
sax_notes = [53, 61, 58, 64]
sax_durations = [0.5, 0.5, 0.5, 0.5]
for i, (pitch, duration) in enumerate(zip(sax_notes, sax_durations)):
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=bar2_start + i * 0.5, end=bar2_start + i * 0.5 + duration)
    sax.notes.append(note_obj)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75, end=bar_start + i * 0.75 + 0.375)
        drums.notes.append(note_obj)

    for i, note in enumerate(snare_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75 + 0.1875, end=bar_start + i * 0.75 + 0.1875 + 0.375)
        drums.notes.append(note_obj)

    for i, note in enumerate(hihat_notes):
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
        drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
