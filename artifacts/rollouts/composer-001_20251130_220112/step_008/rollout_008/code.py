
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),     # D4
    (1.875, 63),   # Eb4
    (2.25, 64),    # E4
    (2.625, 62),   # D4
    (3.0, 60),     # C4
    (3.375, 61),   # Db4
    (3.75, 62),    # D4
    (4.125, 63),   # Eb4
    (4.5, 64),     # E4
    (4.875, 65),   # F4
    (5.25, 64),    # E4
    (5.625, 62),   # D4
    (6.0, 60)      # C4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 72), (1.5, 76),  # D7: D, F#, A, C#
    (2.25, 67), (2.25, 71), (2.25, 72), (2.25, 76),  # D7 again
    (3.0, 67), (3.0, 71), (3.0, 72), (3.0, 76),  # D7
    (3.75, 67), (3.75, 71), (3.75, 72), (3.75, 76),  # D7
    (4.5, 67), (4.5, 71), (4.5, 72), (4.5, 76),  # D7
    (5.25, 67), (5.25, 71), (5.25, 72), (5.25, 76)   # D7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65),      # E4
    (1.75, 67),     # F#4
    (2.0, 69),      # A4
    (2.25, 65),     # E4 (leave it hanging)
    (3.0, 67),      # F#4
    (3.25, 69),     # A4
    (3.5, 71),      # B4
    (3.75, 69),     # A4
    (4.0, 67),      # F#4
    (4.25, 65),     # E4
    (4.5, 67),      # F#4
    (4.75, 69),     # A4
    (5.0, 67),      # F#4
    (5.25, 65),     # E4
    (5.5, 67),      # F#4
    (5.75, 69)      # A4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
