
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
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane starts with a 7th chord on 2 and 4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            # Dm7 chord: D, F, A, C
            for pitch in [22, 25, 27, 29]:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)

# Marcus: Walking line, chromatic approaches, Dm bass line
# Dm bass line: D, C, Eb, F
bass_notes = [22, 21, 23, 25]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[beat % 4], start=time, end=time + 0.125)
        bass.notes.append(note)

# Sax: Motif, one short phrase, make it sing
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [22, 23, 25, 27, 29, 30, 31]
# Motif: D -> Eb -> F -> D (hanging)
sax_notes = [22, 23, 25, 22]
for i, pitch in enumerate(sax_notes):
    time = 1.5 + i * 0.75
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Little Ray continues with the same pattern through bar 4
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        # Hihat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
