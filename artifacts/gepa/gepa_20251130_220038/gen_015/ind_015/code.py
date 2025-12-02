
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
# Dm7: D, F, A, C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # E
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=52, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # D#
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=54, start=3.25, end=3.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=54, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # E#
    pretty_midi.Note(velocity=80, pitch=54, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=56, start=4.25, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=80, pitch=56, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=58, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=57, start=5.75, end=6.0),  # G#
    pretty_midi.Note(velocity=80, pitch=58, start=6.0, end=6.25),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=6.25, end=6.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# Bar 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # C
    # Bar 3 - comp on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # C
    # Bar 4 - comp on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # C
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
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: Your motif - start it, leave it hanging, come back and finish it
# Dm7: D, F, A, C
# Motif: D, F, A, C, D, F, A, C (hanging on A)

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # C
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
