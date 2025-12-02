
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
    # Hihat on every eighth
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

# Bass line - walking line in D minor, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2 - 2nd beat: D7
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # D
    # Bar 3 - 2nd beat: Bm7b5
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # A
    # Bar 4 - 2nd beat: G7
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # F
]

piano.notes.extend(piano_notes)

# Saxophone: Motif - whisper, then cry
# Bar 2: Start the motif
# D (62) -> F (65) -> D# (63) -> F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
    # Let it hang
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),
    # Bar 3: Answer the question
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),
    # Bar 4: Echo the cry
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=63, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),
]

sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_moment.mid")
