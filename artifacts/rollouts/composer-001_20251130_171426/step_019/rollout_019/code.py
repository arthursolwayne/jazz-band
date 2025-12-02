
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.625)   # E
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=1.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=2.375, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=2.875, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.875),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.0, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=4.375, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=58, start=4.875, end=5.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.625, end=1.75),  # Eb

    # Bar 3: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),

    # Bar 4: Comp on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
