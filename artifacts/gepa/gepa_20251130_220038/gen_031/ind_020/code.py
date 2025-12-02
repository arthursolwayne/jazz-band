
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

# Bass: Walking line in Dm, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.25),  # Db
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.25),  # Db
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=68, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Sax: Motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
