
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
bar_length = 1.5  # seconds
for beat in [0, 2]:  # 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(kick)
for beat in [1, 3]:  # 2 and 4
    snare = pretty_midi.Note(velocity=110, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(snare)
for beat in range(8):  # every eighth note
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.1875, end=(beat + 1) * 0.1875)
    drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches, Dm7
bass_notes = [
    # Bar 2
    (0.0, 62),  # D
    (0.375, 60),  # C
    (0.75, 62),  # D
    (1.125, 64),  # E
    # Bar 3
    (1.5, 64),  # E
    (1.875, 62),  # D
    (2.25, 60),  # C
    (2.625, 59),  # Bb
    # Bar 4
    (3.0, 59),  # Bb
    (3.375, 60),  # C
    (3.75, 62),  # D
    (4.125, 64),  # E
    # Bar 5
    (4.5, 64),  # E
    (4.875, 62),  # D
    (5.25, 60),  # C
    (5.625, 62),  # D
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (1.5, 62), (1.5, 67), (1.5, 72), (1.5, 76),
    # Bar 3: G7
    (3.0, 67), (3.0, 72), (3.0, 76), (3.0, 79),
    # Bar 4: Cm7
    (4.5, 60), (4.5, 65), (4.5, 70), (4.5, 74),
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: Motif - short, singable, leaves it hanging
# Dm7 - D, F, Ab, C (Dm7)
sax_notes = [
    (1.5, 62),  # D
    (1.625, 64),  # E
    (1.75, 62),  # D
    (1.875, 63),  # Eb
    (2.0, 62),  # D
    (2.125, 64),  # E
    (2.25, 62),  # D
    (2.375, 65),  # F
    (2.5, 62),  # D
    (2.625, 64),  # E
    (2.75, 62),  # D
    (2.875, 63),  # Eb
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
