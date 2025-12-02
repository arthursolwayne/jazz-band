
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A
    # Bar 2, beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # A
]
piano.notes.extend(piano_notes)

# Sax: Melody - one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # B (F7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # A
    # Bar 3, beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # B (F7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=75, start=4.125, end=4.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Melody continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # G#
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=75, start=4.875, end=5.25),  # C
    # Bar 4, beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=75, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Melody finish
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
