
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

# Drums - Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for note_number in [36, 38, 42]:
    for i in range(4):
        start = i * 0.375
        duration = 0.375
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass - Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Dm7: D, A, F, C
# Walking line: D, F, G, A, Bb, A, G, F, D, F, G, A, Bb, A, G, F

bass_notes = [38, 41, 43, 45, 46, 45, 43, 41, 38, 41, 43, 45, 46, 45, 43, 41]
for note, start in zip(bass_notes, [1.5 + i * 0.375 for i in range(16)]):
    duration = 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(note_obj)

# Piano - Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
# Comp on 2 and 4

# Bar 2 (1.5s - 3.0s)
chords_bar2 = [38, 41, 45, 48]
for note in chords_bar2:
    start = 1.5 + 0.75
    duration = 0.75
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Bar 3 (3.0s - 4.5s)
chords_bar3 = [43, 46, 49, 52]
for note in chords_bar3:
    start = 3.0 + 0.75
    duration = 0.75
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Bar 4 (4.5s - 6.0s)
chords_bar4 = [48, 51, 55, 58]
for note in chords_bar4:
    start = 4.5 + 0.75
    duration = 0.75
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(note_obj)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (38), F (41), Eb (49), D (38)
# Play D, F, Eb, then D again at the end of bar 4

# Bar 2
sax_notes = [38, 41, 49]
for note, start in zip(sax_notes, [1.5 + i * 0.375 for i in range(3)]):
    duration = 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bar 3
sax_notes = [41, 49, 38]
for note, start in zip(sax_notes, [3.0 + i * 0.375 for i in range(3)]):
    duration = 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

# Bar 4
sax_notes = [49]
for note, start in zip(sax_notes, [4.5 + 0.375]):
    duration = 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
