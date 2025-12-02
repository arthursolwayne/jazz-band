
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus
bass_notes = [
    # Walking line in Fm
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # Db
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Comp on 2 and 4 with F7 chords
    # Bar 2 (1.5-2.25)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # D
    # Bar 3 (2.25-3.0)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # D
    # Bar 4 (3.0-3.75)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D
    # Bar 4 (3.75-4.5)
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # D
    # Bar 4 (4.5-5.25)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # D
    # Bar 4 (5.25-6.0)
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    # Motif: F, Gb, Bb, Ab (start on 1.5s)
    pretty_midi.Note(velocity=110, pitch=57, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0),  # Ab
    # Leave it hanging
    # Return on 3.0s
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=58, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.125, end=4.5),  # Ab
    # Final note
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.875),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
