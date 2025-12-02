
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)
# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Dm7
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # F
    # Bar 3 (2.25s)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # Dm7
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # A
    # Bar 4 (3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # Dm7
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C
    # Bar 3 (2.25s)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # F
    # Bar 4 (3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # C
    # Bar 3 (2.25s)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),  # C
    # Bar 4 (3.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),  # C
]
piano.notes.extend(piano_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
