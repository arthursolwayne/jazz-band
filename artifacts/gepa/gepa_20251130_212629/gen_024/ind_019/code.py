
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat
    pretty_midi.Note(velocity=85, pitch=38, start=0.75, end=1.125),  # Snare
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=2.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # C

    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # C

    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.75),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0),  # Hihat
    pretty_midi.Note(velocity=85, pitch=38, start=2.0, end=2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),  # Hihat
    pretty_midi.Note(velocity=90, pitch=36, start=2.5, end=2.875),  # Kick
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),  # Hihat
    pretty_midi.Note(velocity=85, pitch=38, start=3.0, end=3.375),  # Snare
]
drums.notes.extend(drum_notes_bar2)

# Sax: Melody, 1 short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # C

    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
