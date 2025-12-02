
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full band
# Marcus (bass) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Diane (piano) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F# (7th)
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B (7th)
    # Bar 4: C7 on 2
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # E (7th)
]
piano.notes.extend(piano_notes)

# Little Ray (drums) - continues with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3 (Bar 2)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4 (Bar 2)
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Kick on 1 and 3 (Bar 3)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 (Bar 3)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    # Kick on 1 and 3 (Bar 4)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4 (Bar 4)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

# Dante (sax) - motif in F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F (beat 1)
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # G (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # E (beat 3)
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # F (beat 4)
    # Return in bar 3 with variation
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F (beat 1)
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),   # E (beat 3)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # F (beat 4)
    # Final statement in bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_in_f.mid")
