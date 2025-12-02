
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (1, 57),  # D
    (1, 58),  # Eb
    (1, 59),  # E
    (1, 57),  # D
    (1, 60),  # F
    (1, 61),  # Gb
    (1, 62),  # G
    (1, 60),  # F
    (1, 63),  # Ab
    (1, 64),  # Bb
    (1, 65),  # B
    (1, 63),  # Ab
    (1, 66),  # B
    (1, 67),  # C
    (1, 68),  # C#
    (1, 66),  # B
]
for i, (time, pitch) in enumerate(bass_notes):
    start = 1.5 + time * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 at beat 2
    (1, 62),  # D
    (1, 67),  # G
    (1, 69),  # Bb
    (1, 64),  # F
    # Bar 3: Dm7 at beat 2
    (1, 62),
    (1, 67),
    (1, 69),
    (1, 64),
    # Bar 4: Dm7 at beat 2
    (1, 62),
    (1, 67),
    (1, 69),
    (1, 64),
]
for i, (time, pitch) in enumerate(piano_notes):
    start = 1.5 + (time + i // 4 * 4) * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    (0, 62),  # D
    (0.5, 65),  # F
    (1, 64),  # Eb
    (1.5, 62),  # D
    (2, 67),  # G
    (2.5, 65),  # F
    (3, 64),  # Eb
    (3.5, 62),  # D
    (4, 67),  # G
    (4.5, 65),  # F
    (5, 64),  # Eb
    (5.5, 62),  # D
]
for time, pitch in sax_notes:
    start = 1.5 + time * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums: continue through bar 4
for bar in range(2, 4):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(1.5 + bar * 1.5 + beat * 0.375), end=(1.5 + bar * 1.5 + (beat + 1) * 0.375))
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(1.5 + bar * 1.5 + beat * 0.375), end=(1.5 + bar * 1.5 + (beat + 1) * 0.375))
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(1.5 + bar * 1.5 + beat * 0.375), end=(1.5 + bar * 1.5 + (beat + 1) * 0.375))
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
