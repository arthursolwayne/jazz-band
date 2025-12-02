
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

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 48),  # F
    (1.875, 49), # F#
    (2.25, 50),  # G
    (2.625, 51), # G#
    (3.0, 52),   # A
    (3.375, 53), # A#
    (3.75, 54),  # Bb
    (4.125, 55), # B
    (4.5, 57),   # C
    (4.875, 58), # C#
    (5.25, 59),  # D
    (5.625, 60), # D#
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 60), (1.5, 64), (1.5, 67), (1.5, 70),  # F7
    (2.25, 60), (2.25, 64), (2.25, 67), (2.25, 70),  # F7
    (3.0, 62), (3.0, 66), (3.0, 69), (3.0, 72),  # Ab7
    (3.75, 62), (3.75, 66), (3.75, 69), (3.75, 72),  # Ab7
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 70),  # F7
    (5.25, 60), (5.25, 64), (5.25, 67), (5.25, 70),  # F7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Ab, Bb, F
sax_notes = [
    (1.5, 60),  # F
    (1.75, 67),  # Ab
    (2.0, 62),  # Bb
    (2.25, 60), # F
    (3.0, 60),  # F
    (3.25, 67),  # Ab
    (3.5, 62),  # Bb
    (3.75, 60)  # F
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
