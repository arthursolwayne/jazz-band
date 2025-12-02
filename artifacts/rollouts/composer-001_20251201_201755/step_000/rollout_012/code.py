
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
for bar in range(1):
    kick_time = bar * 1.5
    snare_time = kick_time + 0.75
    for i in range(0, 8):
        hihat_time = kick_time + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (1, 38), (1, 40), (1, 41), (1, 43),
    (1, 43), (1, 41), (1, 40), (1, 38)
]
for i, (pitch, duration) in enumerate(bass_notes):
    start_time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + 0.375)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
chords = [
    [57, 60, 64, 65],  # Fm7
    [62, 65, 67, 69],  # Bb7
    [64, 67, 71, 74]   # E7
]
for i, chord in enumerate(chords):
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5 + i * 1.5, end=1.5 + i * 1.5 + 1.5)
        piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Ab, Bb, C (1.5s), rest, then F, Ab, Bb, C (4.5s)
sax_notes = [
    (57, 0.375), (60, 0.375), (62, 0.375), (64, 0.375),
    (57, 0.375), (60, 0.375), (62, 0.375), (64, 0.375)
]
for i, (pitch, duration) in enumerate(sax_notes):
    start_time = 1.5 + i * 0.375
    if i == 3:
        start_time = 4.5
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time, end=start_time + duration)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    kick_time = 1.5 + bar * 1.5
    snare_time = kick_time + 0.75
    for i in range(0, 8):
        hihat_time = kick_time + i * 0.375
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
