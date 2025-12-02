
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    (1.5, 45), (1.875, 44), (2.25, 43), (2.625, 42),
    # Bar 3
    (3.0, 41), (3.375, 40), (3.75, 39), (4.125, 38),
    # Bar 4
    (4.5, 37), (4.875, 36), (5.25, 35), (5.625, 34)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# PIANO: 7th chords, comp on 2 and 4
# Fm7 = F Ab C Eb
piano_notes = [
    # Bar 2
    (1.5, 53), (1.625, 60), (1.75, 64), (1.875, 61),
    # Bar 3
    (3.0, 53), (3.125, 60), (3.25, 64), (3.375, 61),
    # Bar 4
    (4.5, 53), (4.625, 60), (4.75, 64), (4.875, 61)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# SAX: Motif - start with F (53), Ab (55), Bb (57), F (53) - leave it hanging
# Play first 3 notes in bar 2, then rest
sax_notes = [
    (1.5, 53), (1.75, 55), (2.0, 57), (2.25, 53),
    (3.0, 53), (3.25, 55), (3.5, 57), (3.75, 53),
    (4.5, 53), (4.75, 55), (5.0, 57), (5.25, 53)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums continue for bars 2-4
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
