
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
for bar in range(1):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1, 57), (1, 58), (1, 59), (1, 60), # Dm7
    (1, 60), (1, 61), (1, 62), (1, 63), # G7
    (1, 63), (1, 62), (1, 61), (1, 60), # Cm7
    (1, 60), (1, 59), (1, 58), (1, 57)  # F7
]
for i, (pitch, duration) in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=i * 0.375 + 1.5, end=i * 0.375 + 1.5 + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2, 60), (2, 67), (2, 64), (2, 67), # Dm7
    # Bar 3
    (2, 67), (2, 74), (2, 71), (2, 74), # G7
    # Bar 4
    (2, 60), (2, 67), (2, 64), (2, 67)  # Dm7
]
for i, (pitch, duration) in enumerate(piano_notes):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=i * 0.375 + 1.5, end=i * 0.375 + 1.5 + 0.25)
    piano.notes.append(note)

# Sax: Motif - 4 notes, start on D, move to F, G, A, then leave it hanging
sax_notes = [
    (62, 0.5), (65, 0.5), (67, 0.5), (69, 0.5)
]
for i, (pitch, duration) in enumerate(sax_notes):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=i * 0.5 + 1.5, end=i * 0.5 + 1.5 + duration)
    sax.notes.append(note)

# Drums: Full kit
for bar in range(2, 4):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar * 1.5 + beat * 0.375, end=bar * 1.5 + beat * 0.375 + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
