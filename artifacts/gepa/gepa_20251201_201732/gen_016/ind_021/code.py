
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    time = bar1_start + (i * 0.75)
    kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    time = bar1_start + (i * 0.75) + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    time = bar1_start + (i * 0.375)
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bar2_start = 1.5
bass_notes = [
    # Bar 2: Fm (F, C, Ab)
    # Root (F) on beat 1, chromatic approach on beat 2 (E), 5th (C) on beat 3, root (F) on beat 4
    38, 37, 40, 38,
    # Bar 3: Gm7 (G, D, Bb)
    # Root (G) on beat 1, chromatic approach on beat 2 (F#), 5th (D) on beat 3, root (G) on beat 4
    43, 42, 46, 43,
    # Bar 4: Cm7 (C, G, Eb)
    # Root (C) on beat 1, chromatic approach on beat 2 (B), 5th (G) on beat 3, root (C) on beat 4
    40, 39, 43, 40
]

for i, note in enumerate(bass_notes):
    time = bar2_start + (i * 0.375)
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
bar2_piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    [38, 41, 40, 37],
    # Bar 3: Gm7 (G, Bb, D, F)
    [43, 46, 42, 38],
    # Bar 4: Cm7 (C, Eb, G, Bb)
    [40, 37, 43, 42]
]

for i, chord in enumerate(bar2_piano_notes):
    bar_start = bar2_start + i * 1.5
    for note in chord:
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=bar_start, end=bar_start + 0.75)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm - Ab - G - F
sax_notes = [
    # Bar 2: F (38), Ab (41), G (43), F (38)
    [38, 41, 43, 38],
    # Bar 3: Rest
    [],
    # Bar 4: F (38), Ab (41), G (43), F (38)
    [38, 41, 43, 38]
]

for i, notes in enumerate(sax_notes):
    bar_start = bar2_start + i * 1.5
    for note in notes:
        sax_note = pretty_midi.Note(velocity=110, pitch=note, start=bar_start, end=bar_start + 0.375)
        sax.notes.append(sax_note)

# Drums in bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_3_4_start = 1.5
bar2_3_4_end = 6.0

for bar in range(2, 5):
    bar_start = bar2_3_4_start + (bar - 2) * 1.5
    kick_notes = [36, 36]
    snare_notes = [38, 38]
    hihat_notes = [42] * 8

    for i, note in enumerate(kick_notes):
        time = bar_start + (i * 0.75)
        kick = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
        drums.notes.append(kick)

    for i, note in enumerate(snare_notes):
        time = bar_start + (i * 0.75) + 0.1875
        snare = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
        drums.notes.append(snare)

    for i, note in enumerate(hihat_notes):
        time = bar_start + (i * 0.375)
        hihat = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
