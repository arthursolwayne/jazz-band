
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),   # D#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (C7: C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Bar 2, beat 4 (C7 again)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
    # Bar 3, beat 2 (Am7: A C E G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    # Bar 3, beat 4 (Am7 again)
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),
    # Bar 4, beat 2 (D7: D F# A C#)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
    # Bar 4, beat 4 (D7 again)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - motif in C, short and singable
sax_notes = [
    # Bar 2, beat 1: C (60)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    # Bar 2, beat 2: E (64)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),
    # Bar 2, beat 3: G (67)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # Bar 2, beat 4: C (60) - leave it hanging
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),
    # Bar 3, beat 1: C (60) - come back and finish it
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),
    # Bar 3, beat 2: E (64)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),
    # Bar 3, beat 3: G (67)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    # Bar 3, beat 4: C (60)
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),
    # Bar 4, beat 1: C (60)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),
    # Bar 4, beat 2: E (64)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),
    # Bar 4, beat 3: G (67)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),
    # Bar 4, beat 4: C (60) - finish it
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
