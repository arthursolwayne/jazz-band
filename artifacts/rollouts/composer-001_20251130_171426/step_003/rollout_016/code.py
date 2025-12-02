
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    # Fm root (F) on 1
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    # Bb on 2 (chromatic approach to F)
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    # Ab on 3 (chromatic approach to F)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    # F on 4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    # D on 1 (chromatic approach to Eb)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    # Eb on 2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    # C on 3 (chromatic approach to Bb)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),
    # Bb on 4
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),
    # Ab on 1 (chromatic approach to G)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    # G on 2
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    # E on 3 (chromatic approach to F)
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.625),
    # F on 4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Diane: Piano comping on 2 and 4 with 7th chords
# Fm7 = F, Ab, Bb, D
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, D
# Ab7 = Ab, C, Eb, G
piano_notes = [
    # Bar 2: Fm7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # Bar 3: Bb7 on 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    # Bar 4: Eb7 on 2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    # Bar 4: Ab7 on 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),
    # Bar 5: Fm7 on 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    # Bar 5: Bb7 on 4
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0)
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax – motif: F, Ab, Bb, G
# Start on beat 1 of bar 2, leave it hanging, come back on beat 3 of bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),  # G
    # Repeat motif on beat 3 of bar 4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0)   # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
