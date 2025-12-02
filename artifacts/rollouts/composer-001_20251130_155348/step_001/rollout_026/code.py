
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2 (1.5 - 3.0s)
# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # F
]

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # C
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]

drums.notes.extend(drum_notes_bar2)

# Bar 3 (3.0 - 4.5s)
# Marcus on bass: walking line, chromatic approaches
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # C
]

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes_bar3 = [
    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # C
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]

drums.notes.extend(drum_notes_bar3)

# Bar 4 (4.5 - 6.0s)
# Marcus on bass: walking line, chromatic approaches
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # Eb
]

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes_bar4 = [
    # Bar 4: Dm7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # C
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

drums.notes.extend(drum_notes_bar4)

# Dante on sax: short motif, make it sing
# Start it, leave it hanging. Come back and finish it.
# One short motif in Dm, starting on bar 2
# First note: D (62)
# Second note: F (65)
# Third note: Bb (67)
# Fourth note: D (62)

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),  # D
]

sax.notes.extend(sax_notes)

bass.notes.extend(bass_notes + bass_notes_bar3 + bass_notes_bar4)
piano.notes.extend(piano_notes + piano_notes_bar3 + piano_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
