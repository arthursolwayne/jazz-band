
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - chromatic walking line, no repeating notes
bass_line = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),   # A#
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_line)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),   # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),   # F7
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Saxophone - short motif, whisper then cry
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),   # G
    pretty_midi.Note(velocity=100, pitch=59, start=1.6875, end=1.875),  # E
    # Bar 3: Continue the motif, leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),   # G
    pretty_midi.Note(velocity=100, pitch=59, start=2.4375, end=2.625),  # E
    # Bar 4: Return and finish it, build it like a cry
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=100, pitch=59, start=3.1875, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.9375),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.3125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.5),    # G
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
