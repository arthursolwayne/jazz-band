
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # D
    # Bar 3: D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif: D - F# - G - Bb, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=75, start=1.875, end=2.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),   # G#
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # D
    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif: D - F# - G - Bb, then leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.375), # G
    pretty_midi.Note(velocity=110, pitch=75, start=3.375, end=3.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Return to complete the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=110, pitch=75, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.125),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
