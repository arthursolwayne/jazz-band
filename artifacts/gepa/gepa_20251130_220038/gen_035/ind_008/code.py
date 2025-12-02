
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
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Sax: motif starts here
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=38, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D

    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # D
]
piano.notes.extend(piano_notes)

# Drums: same pattern
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

# Bar 3 (3.0 - 4.5s)
# Sax: repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # D

    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=80, pitch=38, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # D

    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # D
]
piano.notes.extend(piano_notes)

# Drums: same pattern
for bar in range(3, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
