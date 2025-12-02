
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=hihat, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=hihat, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=hihat, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=76, start=2.25, end=2.625),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E (D7)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # F# (D7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D (D7)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif, with space and tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),   # F#
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=hihat, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=hihat, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=hihat, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=hihat, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=snare, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=3.75, end=4.125),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=76, start=5.25, end=5.625),  # D7
    pretty_midi.Note(velocity=95, pitch=79, start=5.25, end=5.625),
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: end with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=hihat, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=hihat, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=hihat, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=hihat, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
