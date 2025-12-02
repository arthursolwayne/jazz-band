
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
    kick = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75, end=bar1_start + i * 0.75 + 0.375)
    drums.notes.append(kick)

for i, note in enumerate(snare_notes):
    snare = pretty_midi.Note(velocity=100, pitch=note, start=bar1_start + i * 0.75 + 0.1875, end=bar1_start + i * 0.75 + 0.1875 + 0.375)
    drums.notes.append(snare)

for i, note in enumerate(hihat_notes):
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.125)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    64, 65, 62, 60,
    # Bar 3
    62, 64, 65, 67,
    # Bar 4
    67, 65, 64, 62
]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    64, 67, 71, 72,
    # Bar 3 (beat 2)
    64, 67, 71, 72,
    # Bar 4 (beat 2)
    64, 67, 71, 72
]
for i, chord in enumerate(piano_notes):
    start = 1.5 + (i * 0.375) + 0.75
    duration = 0.375
    for note in chord:
        piano_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
        piano.notes.append(piano_note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 chord: F, A, C, E
sax_notes = [
    # Bar 2: F (beat 1)
    71,
    # Bar 3: A (beat 1)
    74,
    # Bar 4: C (beat 1)
    76,
    # Bar 4: E (beat 3)
    79
]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i * 0.375)
    duration = 0.375
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums for bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

for bar_start in [bar2_start, bar3_start, bar4_start]:
    # Kick on 1 and 3
    kick_notes = [36, 36]
    for i, note in enumerate(kick_notes):
        kick = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75, end=bar_start + i * 0.75 + 0.375)
        drums.notes.append(kick)

    # Snare on 2 and 4
    snare_notes = [38, 38]
    for i, note in enumerate(snare_notes):
        snare = pretty_midi.Note(velocity=100, pitch=note, start=bar_start + i * 0.75 + 0.1875, end=bar_start + i * 0.75 + 0.1875 + 0.375)
        drums.notes.append(snare)

    # Hihat on every eighth
    hihat_notes = [42] * 8
    for i, note in enumerate(hihat_notes):
        hihat = pretty_midi.Note(velocity=80, pitch=note, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
