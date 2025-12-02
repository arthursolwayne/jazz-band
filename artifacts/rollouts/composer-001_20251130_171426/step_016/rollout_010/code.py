
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax: Short motif in D, start on beat 1
# Motif: D (D4) -> E (E4) -> B (B3) -> D (D4) -> B (B3) -> D (D4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # B3
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]

sax.notes.extend(sax_notes)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # D3
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Eb3
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # F3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G3
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # Ab3
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # A3
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),  # Bb3
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # B3
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C4
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # C#4
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # D4
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C#5
    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F#4
    # Bar 4: B7 (B, D#, F#, A#)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D#5
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F#5
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # A#5
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
