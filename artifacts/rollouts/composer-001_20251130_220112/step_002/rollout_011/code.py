
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25), # chromatic
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75), # chromatic
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # chromatic
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=39, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on 1
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # D
    # Bar 2: Bbm7 on 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Db
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # F
    # Bar 2: Fm7 on 3
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625),  # D
    # Bar 2: Cm7 on 4
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),  # G
    # Bar 3: Dm7 on 1
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),  # A
    # Bar 3: Bbm7 on 2
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # F
    # Bar 3: Fm7 on 3
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # D
    # Bar 3: Cm7 on 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # G
    # Bar 4: Fm7 on 1
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # D
    # Bar 4: Bbm7 on 2
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),  # F
    # Bar 4: Fm7 on 3
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625),  # D
    # Bar 4: Cm7 on 4
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - D - Bb (Fm scale)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=105, pitch=46, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=1.75, end=2.0),  # Ab
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=105, pitch=53, start=3.0, end=3.25),  # D
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=105, pitch=48, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=105, pitch=46, start=5.5, end=5.75),  # F
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
