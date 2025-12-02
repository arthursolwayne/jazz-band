
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
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 0.375, end=1.5 + 0.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 0.75, end=1.5 + 1.125),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 1.125, end=1.5 + 1.5),  # D

    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 1.5, end=1.5 + 1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 1.875, end=1.5 + 2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 2.25, end=1.5 + 2.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 2.625, end=1.5 + 3.0),  # D

    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 3.0, end=1.5 + 3.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 3.375, end=1.5 + 3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 3.75, end=1.5 + 4.125),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 4.125, end=1.5 + 4.5),  # D

    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 4.5, end=1.5 + 4.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.5 + 4.875, end=1.5 + 5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5 + 5.25, end=1.5 + 5.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5 + 5.625, end=1.5 + 6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125),  # C

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 2.25, end=1.5 + 2.625),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 2.25, end=1.5 + 2.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 2.25, end=1.5 + 2.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 2.25, end=1.5 + 2.625),  # C

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 3.75, end=1.5 + 4.125),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 3.75, end=1.5 + 4.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 3.75, end=1.5 + 4.125),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 3.75, end=1.5 + 4.125),  # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 - 1.5 + beat*0.375, end=bar*1.5 - 1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 - 1.5 + beat*0.375, end=bar*1.5 - 1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=bar*1.5 - 1.5 + beat*0.375, end=bar*1.5 - 1.5 + beat*0.375 + 0.125)
        drums.notes.append(note)

# Sax: Motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.5 + 0.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.125, end=1.5 + 1.5),  # E

    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 2.25, end=1.5 + 2.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 2.625, end=1.5 + 3.0),  # F

    pretty_midi.Note(velocity=100, pitch=62, start=1.5 + 3.75, end=1.5 + 4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 4.125, end=1.5 + 4.5),  # F

    pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 4.875, end=1.5 + 5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 5.25, end=1.5 + 5.625),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 5.625, end=1.5 + 6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
