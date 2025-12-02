
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

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=43, start=3.25, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=40, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=39, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # Eb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # F
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
# Bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=4.0),
]
# Bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
