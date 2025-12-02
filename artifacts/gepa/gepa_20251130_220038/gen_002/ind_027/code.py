
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),   # Gb
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s - 2.25s) - Bbm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Db
    # Bar 3 (2.25s - 3.0s) - Dm7 (F, Ab, Bb, C)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),  # C
    # Bar 4 (3.0s - 3.75s) - Gm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # Db
    # Bar 4 (3.75s - 4.5s) - Cm7 (F, Ab, Bb, C)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # C
    # Bar 4 (4.5s - 5.25s) - Bbm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # Db
    # Bar 4 (5.25s - 6.0s) - Fm7 (F, Ab, Bb, C)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=6.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing
# Motif: F (71), Ab (69), Bb (67), F (71)
# Start at 1.5s, play first note (F), leave it hanging, come back and finish
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),   # F
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
