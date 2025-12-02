
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D (D4), F# (F#4), A (A4), C (C5) - short motif, leave it hanging

note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=2.125, end=2.25)
sax.notes.append(note)

# Marcus: Walking bass line in D minor (D, C, Bb, A)
note = pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0)
bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625)
note = pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625)

note = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125)
note = pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125)
note = pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.125)

piano.notes.extend([note for note in [note]*4])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: Repeat the motif, but end on the third note

note = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625)
sax.notes.append(note)

# Marcus: Walking bass line
note = pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=59, start=3.125, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=58, start=3.25, end=3.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.5)
bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.125)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125)

note = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.625)

piano.notes.extend([note for note in [note]*4])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: Finish the motif

note = pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625)
sax.notes.append(note)

# Marcus: Walking bass line
note = pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=4.625, end=4.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=4.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0)
bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625)
note = pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625)
note = pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.625)

note = pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125)  # D7
note = pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125)
note = pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.125)
note = pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.125)

piano.notes.extend([note for note in [note]*4])

# Drums: Bar 3 and 4
for bar in range(2):
    for beat in range(4):
        time = (bar + 2) * 1.5 + beat * 0.375
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

midi.write("dante_russo.mid")
