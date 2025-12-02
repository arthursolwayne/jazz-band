
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5)),  # C
    # Bar 3
    (pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=2.75)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=58, start=2.75, end=3.0)),  # A
    (pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.25)),  # Ab
    (pretty_midi.Note(velocity=80, pitch=56, start=3.25, end=3.5)),  # G
    # Bar 4
    (pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75)),  # F
    (pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0)),  # Eb
    (pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5)),  # C
    (pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.75)),  # Bb
    (pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0)),  # A
    (pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.25)),  # Ab
    (pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.5)),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75)),  # A
    (pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75)),  # C
    # Bar 3
    (pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75)),  # F
    (pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75)),  # A
    (pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75)),  # C
    # Bar 4
    (pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75)),  # F
    (pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75)),  # A
    (pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75)),  # D
    (pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75)),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=60, pitch=hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Sax (Dante) - short motif, start it, leave it hanging, come back and finish it
# Motif: F, Ab, Bb, F
sax_notes = [
    # Bar 2
    (pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75)),  # F
    (pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0)),  # Eb
    (pretty_midi.Note(velocity=110, pitch=59, start=2.0, end=2.25)),  # Bb
    (pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5)),  # F
    # Bar 3 - leave it hanging
    (pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75)),  # F
    # Bar 4 - come back and finish it
    (pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75)),  # Eb
    (pretty_midi.Note(velocity=110, pitch=59, start=3.75, end=4.0)),  # Bb
    (pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25)),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
