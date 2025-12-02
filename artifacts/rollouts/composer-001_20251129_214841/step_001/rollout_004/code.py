
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Time signature: 4/4, tempo: 120 BPM
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
midi.tempo_changes = [pretty_midi.TempoChange(120, 0.0)]

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.75
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.25)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.125)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75)),  # C
    (pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0)),  # C#
    (pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5)),  # D#
    (pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=55, start=2.75, end=3.0)),  # F#
    (pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25)),  # G#
    (pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5)),  # A#
    (pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75)),  # B
    (pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)),  # C#
    (pretty_midi.Note(velocity=100, pitch=63, start=4.0, end=4.25)),  # D
    (pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5)),  # D#
    (pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75)),  # E
    (pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0)),  # F#
    (pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25)),  # G#
    (pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5)),  # A#
    (pretty_midi.Note(velocity=100, pitch=73, start=5.5, end=5.75)),  # B
    (pretty_midi.Note(velocity=100, pitch=75, start=5.75, end=6.0)),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.75
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.25)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.25)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.125)
            drums.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# C, E, G, B (Cmaj7) - start on C, end on B, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.6),
    pretty_midi.Note(velocity=110, pitch=64, start=1.6, end=1.7),
    pretty_midi.Note(velocity=110, pitch=67, start=1.7, end=1.8),
    pretty_midi.Note(velocity=110, pitch=71, start=1.8, end=1.9),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=1.9, end=2.0),
    # Come back and finish it
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.1),
    pretty_midi.Note(velocity=110, pitch=64, start=2.1, end=2.2),
    pretty_midi.Note(velocity=110, pitch=67, start=2.2, end=2.3),
    pretty_midi.Note(velocity=110, pitch=71, start=2.3, end=2.4),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
