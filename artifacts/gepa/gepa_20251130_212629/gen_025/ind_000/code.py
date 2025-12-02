
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.6875),    # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.6875, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),     # G
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),    # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.1875, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),  # Ab
    pretty_midi.Note(velocity=90, pitch=41, start=2.5625, end=2.75),   # G
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=2.9375),   # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=39, start=2.9375, end=3.125),  # E
    pretty_midi.Note(velocity=90, pitch=40, start=3.125, end=3.3125),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=3.3125, end=3.5),    # G
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),    # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.1875),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.1875),  # D
    # Bar 2 (beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # D
    # Bar 3 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9375),  # D
    # Bar 3 (beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.9375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.75, end=4.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.9375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.9375),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.1875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.9375),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.9375),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.1875),  # Ab
]
sax.notes.extend(sax_notes)

# Add drum fills in bar 2 and 3
drum_notes = [
    # Bar 2 fill
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),  # Hi-hat
    # Bar 3 fill
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),  # Hi-hat
]
drums.notes.extend(drum_notes)

# Add final snare on beat 4 of bar 4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),  # Snare
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
