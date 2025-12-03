
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
bar_length = 1.5
for i in range(4):
    time = i * bar_length / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + bar_length / 2, end=time + bar_length / 2 + bar_length / 4)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + bar_length)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C
# Bar 2: F -> Gb (chromatic approach) -> Ab -> A
# Bar 3: D -> Eb (chromatic approach) -> C -> C
# Bar 4: F -> Gb (chromatic approach) -> Ab -> A
for i in range(3):
    bar_start = 1.5 + i * bar_length
    if i == 0:
        notes = [38, 37, 43, 44]
    elif i == 1:
        notes = [50, 49, 48, 48]
    else:
        notes = [38, 37, 43, 44]
    for note in notes:
        start = bar_start
        end = start + bar_length / 4
        bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
        bass.notes.append(bass_note)
        start += bar_length / 4

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: Ab7 (Ab, C, Eb, G)
chords = [
    [58, 60, 65, 63],     # Fm7
    [60, 63, 67, 62],     # Cm7
    [65, 68, 71, 67]      # Ab7
]
for i, chord in enumerate(chords):
    bar_start = 1.5 + i * bar_length
    for note in chord:
        start = bar_start + bar_length / 2
        end = start + bar_length / 2
        piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
        piano.notes.append(piano_note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, D (Fm scale, but with a twist)
# Bar 2: Play F, Ab, C
# Bar 3: Rest
# Bar 4: Play D, F, Ab, C (finish the motif)
sax_notes = [
    [58, 60, 65],        # Bar 2: F, Ab, C
    [],                  # Bar 3: Rest
    [67, 58, 60, 65]     # Bar 4: D, F, Ab, C
]
for i, notes in enumerate(sax_notes):
    bar_start = 1.5 + i * bar_length
    for note in notes:
        start = bar_start
        end = start + bar_length / 4
        sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
        sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
