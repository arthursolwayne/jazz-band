
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # Gb (b9)
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # Ab (3rd)
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # Bb (4th)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),   # B (5th)
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # C (6th)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # C# (b7)
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # D (octave)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),   # Eb (9th)
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # E (11th)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # F (octave + root)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # Gb (octave + b9)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (C7)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb

    # Bar 3, beat 2 (Ab7)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # E

    # Bar 4, beat 2 (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif starting on beat 1 of bar 2, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),   # Gb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.375),  # C
]

sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_intro.mid")
