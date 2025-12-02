
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
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)
# Bass line: Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5), # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.25),
    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    # Bar 4: F7 again
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax: Short motif, one phrase that sings
# F - G - A - F (start at bar 2, spread across bars 2-4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
