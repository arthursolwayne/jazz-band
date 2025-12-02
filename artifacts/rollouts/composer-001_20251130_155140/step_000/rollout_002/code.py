
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

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 48, 100), (1.75, 49, 100), (2.0, 50, 100), (2.25, 51, 100),  # Bar 2
    (2.5, 51, 100), (2.75, 50, 100), (3.0, 49, 100), (3.25, 48, 100),  # Bar 3
    (3.5, 48, 100), (3.75, 49, 100), (4.0, 50, 100), (4.25, 51, 100),  # Bar 4
    (4.5, 51, 100), (4.75, 50, 100), (5.0, 49, 100), (5.25, 48, 100)   # Bar 4
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (2.0, 64, 100), (2.25, 67, 100), (2.5, 71, 100), (2.75, 69, 100),
    # Bar 3: B7 on beat 2
    (3.0, 76, 100), (3.25, 79, 100), (3.5, 83, 100), (3.75, 81, 100),
    # Bar 4: E7 on beat 2
    (4.0, 72, 100), (4.25, 76, 100), (4.5, 80, 100), (4.75, 78, 100)
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Drums continue with same pattern
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

# Sax (Dante): One short motif, leave it hanging, come back and finish it
# Bar 2: Motif starts
motif = [(2.0, 64, 100), (2.25, 66, 100), (2.5, 67, 100)]  # F, G, G#
for time, pitch, vel in motif:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: Finish the motif
finish = [(4.0, 64, 100), (4.25, 62, 100), (4.5, 60, 100)]  # F, Eb, D
for time, pitch, vel in finish:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
