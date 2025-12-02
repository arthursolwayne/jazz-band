
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

# Bass line - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.375),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=2.375, end=2.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.875, end=3.0),  # D
    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.375),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # C
    # Bar 3 - Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # C
    # Bar 4 - Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),  # C
]
piano.notes.extend(piano_notes)

# Sax - motif in Dm, sparse and with space
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # C
    # Let it hang
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
