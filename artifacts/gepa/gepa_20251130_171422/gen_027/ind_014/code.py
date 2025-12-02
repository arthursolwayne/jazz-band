
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Chromatic walking line with approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Sparse, expressive motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Chromatic walking line with approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=66, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=68, start=4.0, end=4.25),  # A#
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # Bb7
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),  # A
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with a glimmer of resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # F
]
sax.notes.extend(sax_notes)

# Drums - continue with the same pattern but keep it tight
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Chromatic walking line with approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # C#
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.5),  # D#
    pretty_midi.Note(velocity=80, pitch=74, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.5),  # C
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums - continue with the same pattern but keep it tight
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
