
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
for bar in [0]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, never the same note twice
# Fm: F, Ab, Bb, D, Eb, G, Ab, Bb
bass_notes = [75, 70, 71, 68, 72, 69, 70, 71]
for bar in [1, 2, 3]:
    for beat in range(4):
        note = pretty_midi.Note(velocity=100, pitch=bass_notes[bar*4 + beat], 
                                start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# Ab7 = Ab, C, Eb, G
piano_notes = [
    # Bar 2: Fm7 on 2 and 4
    (75, 70, 71, 72),  # 2
    (75, 70, 71, 72),  # 4
    # Bar 3: Bb7 on 2 and 4
    (71, 68, 75, 70),  # 2
    (71, 68, 75, 70),  # 4
    # Bar 4: Eb7 on 2 and 4
    (69, 72, 71, 67),  # 2
    (69, 72, 71, 67),  # 4
]
for i, chord in enumerate(piano_notes):
    beat = i // 2
    bar = 1 + i // 4
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, 
                                start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [1, 2, 3]:
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, F (start) -> Bb, Ab, F (end)
motif = [75, 70, 71, 75, 71, 70, 75]
for i, pitch in enumerate(motif):
    bar = 1 if i < 4 else 3
    beat = i % 4 if bar == 1 else (i - 4) % 4
    start = bar * 1.5 + beat * 0.375
    if i < 4:
        end = start + 0.1
    else:
        end = start + 0.1
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
