
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
bar_length = 1.5  # seconds per bar at 160 BPM
note_duration = 0.375  # 1/4 note at 160 BPM

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=note_duration),
              pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 1.0, end=bar_length * 1.0 + note_duration),
              pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 2.0, end=bar_length * 2.0 + note_duration),
              pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 3.0, end=bar_length * 3.0 + note_duration)]

snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 0.5, end=bar_length * 0.5 + note_duration),
               pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 1.5, end=bar_length * 1.5 + note_duration),
               pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 2.5, end=bar_length * 2.5 + note_duration),
               pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 3.5, end=bar_length * 3.5 + note_duration)]

hihat_notes = []
for i in range(8):
    start = bar_length * (i / 4)
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + note_duration / 2))

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = []
root = 50  # D2
fifth = 57  # A2
chromatic = [51, 58, 56, 59, 55, 60, 54, 61]  # Chromatic approaches
for i in range(4):
    start = bar_length * (i + 1)
    if i % 2 == 0:
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=root, start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=fifth, start=start + note_duration * 2, end=start + note_duration * 3))
    else:
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[i % 8], start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[(i + 1) % 8], start=start + note_duration * 2, end=start + note_duration * 3))

bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 -> G7 -> Cm7 -> F7
piano_notes = []
chords = [
    [(60, 64, 67, 70), (64, 67, 70, 72)],  # Dm7: D, F, A, C
    [(67, 71, 74, 76), (71, 74, 76, 79)],  # G7: G, B, D, F
    [(60, 63, 67, 70), (63, 67, 70, 71)],  # Cm7: C, Eb, G, Bb
    [(65, 69, 72, 76), (69, 72, 76, 79)]   # F7: F, A, C, Eb
]
for i in range(4):
    start = bar_length * (i + 1)
    for note in chords[i][0]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + note_duration * 2))
    for note in chords[i][1]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + note_duration * 2, end=start + note_duration * 4))

piano.notes.extend(piano_notes)

# Dante: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar_length * 1.0, end=bar_length * 1.0 + note_duration * 1.5),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=bar_length * 1.5, end=bar_length * 1.5 + note_duration * 1.5),  # A4
    pretty_midi.Note(velocity=110, pitch=62, start=bar_length * 3.0, end=bar_length * 3.0 + note_duration * 1.5),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=bar_length * 3.5, end=bar_length * 3.5 + note_duration * 1.5)   # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = []
for i in range(4):
    start = bar_length * (i + 2)
    if i % 2 == 0:
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=root, start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=fifth, start=start + note_duration * 2, end=start + note_duration * 3))
    else:
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[i % 8], start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[(i + 1) % 8], start=start + note_duration * 2, end=start + note_duration * 3))

bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 -> G7 -> Cm7 -> F7
for i in range(4):
    start = bar_length * (i + 2)
    for note in chords[i][0]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + note_duration * 2))
    for note in chords[i][1]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + note_duration * 2, end=start + note_duration * 4))

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line in Dm, roots and fifths with chromatic approaches
bass_notes = []
for i in range(4):
    start = bar_length * (i + 3)
    if i % 2 == 0:
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=root, start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=80, pitch=fifth, start=start + note_duration * 2, end=start + note_duration * 3))
    else:
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[i % 8], start=start, end=start + note_duration))
        bass_notes.append(pretty_midi.Note(velocity=70, pitch=chromatic[(i + 1) % 8], start=start + note_duration * 2, end=start + note_duration * 3))

bass.notes.extend(bass_notes)

# Diane: open voicings, different chord each bar, resolve on the last
# Bar 4: Dm7 -> G7 -> Cm7 -> F7
for i in range(4):
    start = bar_length * (i + 3)
    for note in chords[i][0]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + note_duration * 2))
    for note in chords[i][1]:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start + note_duration * 2, end=start + note_duration * 4))

piano.notes.extend(piano_notes)

# Bar 4: Dante finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=bar_length * 4.0, end=bar_length * 4.0 + note_duration * 1.5),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=bar_length * 4.5, end=bar_length * 4.5 + note_duration * 1.5)   # A4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 4.0, end=bar_length * 4.0 + note_duration),
              pretty_midi.Note(velocity=100, pitch=36, start=bar_length * 5.0, end=bar_length * 5.0 + note_duration)]
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 4.5, end=bar_length * 4.5 + note_duration),
               pretty_midi.Note(velocity=100, pitch=38, start=bar_length * 5.5, end=bar_length * 5.5 + note_duration)]
hihat_notes = []
for i in range(4):
    start = bar_length * (i + 4)
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + note_duration / 2))

drums.notes.extend(kick_notes)
drums.notes.extend(snare_notes)
drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
