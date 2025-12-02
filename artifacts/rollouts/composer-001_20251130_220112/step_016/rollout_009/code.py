
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0)   # F#
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # D
    # Bar 3: G7
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875), # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.875), # E
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=2.875), # G
    # Bar 4: Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # C
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First statement
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # A
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.4375, end=2.625), # A
    # Second statement, finish the motif
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25), # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=5.4375, end=5.625), # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.8125, end=6.0), # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
