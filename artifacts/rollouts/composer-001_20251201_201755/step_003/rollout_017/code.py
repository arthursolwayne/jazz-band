
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36, 36, 36, 36]
snare_notes = [38, 38, 38, 38]
hihat_notes = [42, 42, 42, 42]

# Time for each beat: 0.375s
for i in range(4):
    kick_time = i * 0.375
    kick_note = pretty_midi.Note(velocity=100, pitch=kick_notes[i], start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    snare_time = (i + 1) * 0.375
    snare_note = pretty_midi.Note(velocity=100, pitch=snare_notes[i], start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare_note)

    for j in range(2):
        hihat_time = i * 0.375 + j * 0.1875
        hihat_note = pretty_midi.Note(velocity=100, pitch=hihat_notes[i], start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 - Bb2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    [53, 55, 53, 56],  # F2, G2, F2, Ab2
    # Bar 3
    [56, 58, 56, 59],  # Ab2, Bb2, Ab2, B2
    # Bar 4
    [59, 56, 59, 60],  # B2, Ab2, B2, C3
]
for bar_idx in range(3):
    for note_idx in range(4):
        note = bass_notes[bar_idx][note_idx]
        time = 1.5 + bar_idx * 1.5 + note_idx * 0.375
        bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
        bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    # Bar 2
    [53, 58, 60, 64],  # F, A, C, E
    # Bar 3
    [57, 62, 64, 67],  # Bb, D, F, Ab
    # Bar 4
    [60, 64, 67, 71],  # C, E, G, B
]
for bar_idx in range(3):
    for note in piano_notes[bar_idx]:
        time = 1.5 + bar_idx * 1.5
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 1.5)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - F - Ab (F2, Bb2, F2, Ab2)
# Play on beat 1 of bar 2, repeat on beat 3 of bar 3
sax_notes = [
    # Bar 2
    [53, 57, 53, 56],  # F2, Bb2, F2, Ab2
    # Bar 3
    [53, 57, 53, 56],  # F2, Bb2, F2, Ab2
]
for bar_idx in range(2):
    for note_idx in range(4):
        note = sax_notes[bar_idx][note_idx]
        time = 1.5 + bar_idx * 1.5 + note_idx * 0.375
        sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
        sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
