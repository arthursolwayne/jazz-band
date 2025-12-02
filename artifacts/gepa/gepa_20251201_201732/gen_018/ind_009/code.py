
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, chord each bar, resolve on last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # D5
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # D5
]
sax.notes.extend(sax_notes)

# Bar 3: Full ensemble
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=39, start=4.125, end=4.5),  # Eb2
]
bass.notes.extend(bass_notes)

# Piano: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # D6
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A5
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G5
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A5
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G5
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full ensemble
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
