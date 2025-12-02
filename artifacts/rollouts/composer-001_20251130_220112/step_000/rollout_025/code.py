
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
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches
bass_notes = [62, 60, 59, 57, 55, 53, 52, 50, 48, 47, 45, 43, 42, 40, 38, 37, 35, 33, 32, 30]
for i, note in enumerate(bass_notes):
    time = 1.5 + (i % 4) * 0.375
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5 + 0.75, 62), (1.5 + 0.75, 67), (1.5 + 0.75, 69), (1.5 + 0.75, 72),
    (1.5 + 1.5, 62), (1.5 + 1.5, 67), (1.5 + 1.5, 69), (1.5 + 1.5, 72),
    # Bar 3
    (1.5 + 2.25, 62), (1.5 + 2.25, 67), (1.5 + 2.25, 69), (1.5 + 2.25, 72),
    (1.5 + 3.0, 62), (1.5 + 3.0, 67), (1.5 + 3.0, 69), (1.5 + 3.0, 72),
    # Bar 4
    (1.5 + 3.75, 62), (1.5 + 3.75, 67), (1.5 + 3.75, 69), (1.5 + 3.75, 72),
    (1.5 + 4.5, 62), (1.5 + 4.5, 67), (1.5 + 4.5, 69), (1.5 + 4.5, 72)
]
for time, pitch in piano_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C
# Motif: D -> F -> A -> rest -> D again
sax_notes = [
    (1.5, 62), (1.5 + 0.375, 65), (1.5 + 0.75, 69), (1.5 + 1.5, 62),
    (1.5 + 2.25, 62), (1.5 + 2.625, 65), (1.5 + 3.0, 69), (1.5 + 3.375, 62)
]
for time, pitch in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Drums: continue for bars 2-4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.075)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
