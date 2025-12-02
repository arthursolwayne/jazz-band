
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: walking line in F, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # B
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=3.25, end=3.5),  # C#
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.5),  # Gb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=46, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=44, start=5.5, end=5.75),  # Db
    pretty_midi.Note(velocity=90, pitch=43, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 on 2 (2.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),  # D
    # Bar 3: Bb7 on 2 (3.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=3.5, end=3.75),  # G
    # Bar 4: F7 on 2 (5.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s): Start the motif
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb
    # Bar 3 (3.0 - 4.5s): Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # Eb
    # Bar 4 (4.5 - 6.0s): Finish it
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: continue pattern
for i in range(2, 6):
    for j in range(0, 6):
        start = i * 1.5 + j * 0.375
        if j % 2 == 0:  # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
        else:  # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.375))
    # Hi-hat on every eighth
    for j in range(0, 6):
        start = i * 1.5 + j * 0.375
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
