
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
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 54, 100), (1.75, 53, 100), (2.0, 55, 100), (2.25, 57, 100),
    # Bar 3
    (2.5, 59, 100), (2.75, 57, 100), (3.0, 55, 100), (3.25, 53, 100),
    # Bar 4
    (3.5, 51, 100), (3.75, 53, 100), (4.0, 55, 100), (4.25, 57, 100)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.75, 64, 100), (1.75, 67, 100), (1.75, 69, 100), (1.75, 71, 100),
    # Bar 3
    (2.25, 64, 100), (2.25, 67, 100), (2.25, 69, 100), (2.25, 71, 100),
    # Bar 4
    (3.75, 64, 100), (3.75, 67, 100), (3.75, 69, 100), (3.75, 71, 100)
]
for time, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25)
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
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(hihat)

# Sax: Melody - Whisper, then cry. One short motif, start it, leave it hanging, come back and finish it
# Fm: F, Ab, Bb, C, Eb, G, Ab, Bb
sax_notes = [
    # Bar 2: Start the motif
    (1.5, 64, 100), (1.625, 67, 100), (1.75, 65, 100),  # F, Ab, Bb
    # Bar 3: Leave it hanging
    (2.5, 67, 100), (2.625, 64, 100), (2.75, 62, 100),  # Ab, F, Eb
    # Bar 4: Come back and finish it
    (3.5, 64, 100), (3.625, 67, 100), (3.75, 65, 100), (4.0, 62, 100)  # F, Ab, Bb, Eb
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
