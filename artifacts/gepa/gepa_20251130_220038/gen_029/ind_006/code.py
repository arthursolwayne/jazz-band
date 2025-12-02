
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
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 46),  # D
    (1.875, 48), # Eb
    (2.25, 50),  # F
    (2.625, 48), # Eb
    (2.875, 50), # F
    (3.25, 52),  # G
    (3.625, 50), # F
    (4.0, 48),   # Eb
    (4.375, 50), # F
    (4.75, 52),  # G
    (5.125, 53), # G#
    (5.5, 50),   # F
    (5.875, 48), # Eb
    (6.25, 50),  # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 69), (1.5, 71),  # F7
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 71),  # F7
    (3.0, 62), (3.0, 67), (3.0, 69), (3.0, 71),  # F7
    (3.75, 62), (3.75, 67), (3.75, 69), (3.75, 71),  # F7
    (4.5, 62), (4.5, 67), (4.5, 69), (4.5, 71),  # F7
    (5.25, 62), (5.25, 67), (5.25, 69), (5.25, 71),  # F7
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 66),  # Bb
    (1.75, 69),  # D
    (2.0, 66),  # Bb
    (2.25, 69),  # D
    (2.5, 66),  # Bb
    (2.75, 69),  # D
    (3.0, 66),  # Bb
    (3.25, 69),  # D
    (3.5, 66),  # Bb
    (3.75, 69),  # D
    (4.0, 66),  # Bb
    (4.25, 69),  # D
    (4.5, 66),  # Bb
    (4.75, 69),  # D
    (5.0, 66),  # Bb
    (5.25, 69),  # D
    (5.5, 66),  # Bb
    (5.75, 69),  # D
    (6.0, 66),  # Bb
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Continue pattern
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

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
