
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

# Bar 2: Start of the melody, sax enters
# Fm7 (F, Ab, Bb, D) - 7th chord
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (tenor sax is transposed)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # D
]
sax.notes.extend(sax_notes)

# Marcus on bass - walking line, chromatic approaches
# Fm7 - F, Ab, Bb, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=1.5, end=1.75),  # F (bass is in concert pitch)
    pretty_midi.Note(velocity=80, pitch=48, start=1.75, end=2.0),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # G (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane on piano - 7th chords comp on 2 and 4
# Fm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the melody, sax plays the motif again but altered
# Fm7 but with a chromatic twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),  # Gb (chromatic twist)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # D
]
sax.notes.extend(sax_notes)

# Marcus continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # A (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=52, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # F#
]
bass.notes.extend(bass_notes)

# Diane continues comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Sax finishes the motif, returns to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Marcus ends the walking line on F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # F
]
bass.notes.extend(bass_notes)

# Diane ends with Fm7 on 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Drums continue the pattern for the full 6 seconds
# Extend the drum pattern to fill the 6 seconds
extended_drum_notes = []
for note in drum_notes:
    extended_note = pretty_midi.Note(
        velocity=note.velocity,
        pitch=note.pitch,
        start=note.start + 3.0,
        end=note.end + 3.0
    )
    extended_drum_notes.append(extended_note)
drums.notes.extend(extended_drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
