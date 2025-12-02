
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
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Start on F (70) and walk up
bass_notes = [
    (1.5, 70), (1.75, 71), (2.0, 72), (2.25, 74),
    (2.5, 76), (2.75, 77), (3.0, 78), (3.25, 79),
    (3.5, 81), (3.75, 82), (4.0, 83), (4.25, 84),
    (4.5, 86), (4.75, 87), (5.0, 88), (5.25, 89)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, E♭), B♭7 (B♭, D, F, A), E7 (E, G#, B, D), A7 (A, C#, E, G)
piano_notes = [
    # Bar 2
    (1.5, 70), (1.5, 69), (1.5, 72), (1.5, 64),
    (2.0, 67), (2.0, 69), (2.0, 72), (2.0, 69),
    # Bar 3
    (2.5, 69), (2.5, 67), (2.5, 72), (2.5, 68),
    (3.0, 69), (3.0, 67), (3.0, 72), (3.0, 68),
    # Bar 4
    (3.5, 72), (3.5, 74), (3.5, 77), (3.5, 72),
    (4.0, 72), (4.0, 74), (4.0, 77), (4.0, 72)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif - start with F (70), then B♭ (72), then F (70), leave it hanging
# Then come back and finish with E♭ (69), resolving down to D (67)
sax_notes = [
    # First motif (bar 2)
    (1.5, 70), (1.5, 72), (1.5, 70),
    # Leave it hanging (bar 2)
    (2.75, 70),
    # Come back and finish (bar 3)
    (3.0, 69), (3.25, 67)
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
