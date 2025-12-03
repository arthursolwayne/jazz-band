
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
    start = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar1_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches, not scales.
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line: F -> A -> D -> C
# Bar 2: F (38)
# Bar 3: A (43)
# Bar 4: D (46)
# Bar 3: Chromatic approach to D (C#, D)
# Bar 4: Half-step approach to C (Bb, C)

# Bar 2
bass_note = pretty_midi.Note(velocity=80, pitch=38, start=bar2_start, end=bar2_start + 0.375)
bass.notes.append(bass_note)

# Bar 3
bass_note = pretty_midi.Note(velocity=80, pitch=43, start=bar3_start, end=bar3_start + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=44, start=bar3_start + 0.1875, end=bar3_start + 0.1875 + 0.1875)
bass.notes.append(bass_note)

# Bar 4
bass_note = pretty_midi.Note(velocity=80, pitch=46, start=bar4_start, end=bar4_start + 0.375)
bass.notes.append(bass_note)
bass_note = pretty_midi.Note(velocity=80, pitch=44, start=bar4_start + 0.1875, end=bar4_start + 0.1875 + 0.1875)
bass.notes.append(bass_note)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Fmaj7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)

# Bar 2
piano_notes = [71, 74, 76, 79]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar2_start, end=bar2_start + 0.375)
    piano.notes.append(piano_note)

# Bar 3
piano_notes = [70, 73, 76, 77]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar3_start, end=bar3_start + 0.375)
    piano.notes.append(piano_note)

# Bar 4
piano_notes = [60, 63, 67, 71]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=bar4_start, end=bar4_start + 0.375)
    piano.notes.append(piano_note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar2_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar2_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar2_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bar 3
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar3_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar3_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar3_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# Bar 4
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i, note in enumerate(kick_notes):
    start = bar4_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    start = bar4_start + i * 0.75 + 0.1875
    snare = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    start = bar4_start + i * 0.375
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.1875)
    drums.notes.append(hihat)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.

# Bar 2: Start motif (F, A, G)
sax_note = pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_start + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=74, start=bar2_start + 0.375, end=bar2_start + 0.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=73, start=bar2_start + 0.75, end=bar2_start + 1.125)
sax.notes.append(sax_note)

# Bar 3: Leave it hanging
# Bar 4: Come back and finish it (F, A, G, F)
sax_note = pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_start + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=74, start=bar4_start + 0.375, end=bar4_start + 0.75)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=73, start=bar4_start + 0.75, end=bar4_start + 1.125)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5)
sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
