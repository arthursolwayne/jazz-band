
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375), # E
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=2.625, end=2.875),  # F7
]
piano.notes.extend(piano_notes)

# Sax: Motif - F, G, Ab, F (short and haunting)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.5),  # G#
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.375),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=4.125, end=4.375),  # F7
]
piano.notes.extend(piano_notes)

# Sax: Motif again (with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=5.75),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=5.875),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=5.875),  # F7
]
piano.notes.extend(piano_notes)

# Sax: Motif again (with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=73, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),  # F
]
sax.notes.extend(sax_notes)

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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
