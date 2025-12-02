
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2: Everyone in
# Sax starts motif, bass walks, piano comps, drums continue

# Sax motif
# Dm7 -> F -> Eb -> C -> Dm7
notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=59, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # G
]
sax.notes.extend(notes)

# Bass line (walking in Dm)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),   # D7: D, F, A, C
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),   # D7
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),   # D7
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0),
]
piano.notes.extend(piano_notes)

# Drums continue
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
