
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

# Kick on 1 and 3 (0.0 and 0.75s)
for i, note in enumerate(kick_notes):
    time = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on 2 and 4 (0.375 and 1.125s)
for i, note in enumerate(snare_notes):
    time = bar1_start + i * 0.75 + 0.375
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hihat on every eighth note
for i, note in enumerate(hihat_notes):
    time = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: Dm7 (D, F, A, C)
bass_notes_bar2 = [38, 40, 38, 40]
for i, note in enumerate(bass_notes_bar2):
    time = bar2_start + i * 0.75
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Bar 3: G7 (G, B, D, F)
bass_notes_bar3 = [43, 45, 43, 45]
for i, note in enumerate(bass_notes_bar3):
    time = bar3_start + i * 0.75
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Bar 4: Cm7 (C, Eb, G, Bb)
bass_notes_bar4 = [40, 37, 40, 37]
for i, note in enumerate(bass_notes_bar4):
    time = bar4_start + i * 0.75
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes_bar2 = [50, 53, 57, 59]
for i, note in enumerate(piano_notes_bar2):
    time = bar2_start + i * 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Bar 3: G7 (G, B, D, F)
piano_notes_bar3 = [55, 58, 62, 57]
for i, note in enumerate(piano_notes_bar3):
    time = bar3_start + i * 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [52, 55, 59, 55]
for i, note in enumerate(piano_notes_bar4):
    time = bar4_start + i * 0.375
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) -> F (53) -> A (57) -> D (50) - leave it on A (57) for a half note
sax_note1 = pretty_midi.Note(velocity=110, pitch=50, start=bar2_start, end=bar2_start + 0.375)
sax_note2 = pretty_midi.Note(velocity=110, pitch=53, start=bar2_start + 0.375, end=bar2_start + 0.75)
sax_note3 = pretty_midi.Note(velocity=110, pitch=57, start=bar2_start + 0.75, end=bar2_start + 1.125)
sax_note4 = pretty_midi.Note(velocity=110, pitch=50, start=bar2_start + 1.125, end=bar2_start + 1.5)
sax.notes.append(sax_note1)
sax.notes.append(sax_note2)
sax.notes.append(sax_note3)
sax.notes.append(sax_note4)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [bar2_start, bar3_start, bar4_start]:
    # Kick on 1 and 3 (0.0 and 0.75s)
    for i, note in enumerate([36, 36]):
        time = bar_start + i * 0.75
        kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(kick)

    # Snare on 2 and 4 (0.375 and 1.125s)
    for i, note in enumerate([38, 38]):
        time = bar_start + i * 0.75 + 0.375
        snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
        drums.notes.append(snare)

    # Hihat on every eighth note
    for i, note in enumerate([42] * 8):
        time = bar_start + i * 0.375
        hihat = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
