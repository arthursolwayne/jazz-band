
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat*0.375, end=(beat+1)*0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat*0.375, end=(beat+1)*0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat*0.375, end=(beat+1)*0.375)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25)), # C
    (pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625)), # Eb
    (pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0)),  # F
    (pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75)), # C
    (pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125)), # Eb
    (pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5)),  # F
    (pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875)),  # D
    (pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25)), # C
    (pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625)), # Eb
    (pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0)),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) - Eb (51) - F (52) - Eb (51) - D (50) - C (49)
# First phrase: D - Eb - F (1.5s to 2.625s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=51, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=52, start=2.25, end=2.625),
    # Leave it hanging (no note until 3.75s)
    pretty_midi.Note(velocity=110, pitch=51, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=50, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=49, start=4.5, end=4.875),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(bar*1.5 + beat*0.375), end=(bar*1.5 + (beat+1)*0.375))
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(bar*1.5 + beat*0.375), end=(bar*1.5 + (beat+1)*0.375))
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(bar*1.5 + beat*0.375), end=(bar*1.5 + (beat+1)*0.375))
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
