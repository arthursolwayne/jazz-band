
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

# Drums: Bar 1
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75), # Hihat on &1
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=85, pitch=42, start=1.125, end=1.5),  # Hihat on &2
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # Hihat on &3
    pretty_midi.Note(velocity=95, pitch=38, start=2.25, end=2.625), # Snare on 4
    pretty_midi.Note(velocity=85, pitch=42, start=2.625, end=3.0),  # Hihat on &4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D

    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - sparse, expressive
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody continuation
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),   # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # Hihat on &1
    pretty_midi.Note(velocity=95, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=85, pitch=42, start=4.125, end=4.5),  # Hihat on &2
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # Hihat on &3
    pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.625), # Snare on 4
    pretty_midi.Note(velocity=85, pitch=42, start=5.625, end=6.0),  # Hihat on &4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=83, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=84, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # D

    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - ends on a lingering note
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=83, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # Hihat on &1
    pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=85, pitch=42, start=5.625, end=6.0),  # Hihat on &2
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
