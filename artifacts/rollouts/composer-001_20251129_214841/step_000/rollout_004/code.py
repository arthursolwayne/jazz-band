
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, tempo=120)]

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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=63, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=61, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=61, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=63, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=61, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),

    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),

    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.25),

    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# You: Tenor sax, short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
