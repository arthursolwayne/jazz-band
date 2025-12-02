
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
drum_note_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_note_2 = pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75)
drum_note_3 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_note_4 = pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
drums.notes.extend([drum_note_1, drum_note_2, drum_note_3, drum_note_4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=79, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=80, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.25), # D#
    pretty_midi.Note(velocity=80, pitch=83, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=84, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A7
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # C7
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.25), # D7
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625), # B7
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0),  # C#7
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375), # E7
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # A7
    pretty_midi.Note(velocity=100, pitch=84, start=3.75, end=4.125), # F7
    pretty_midi.Note(velocity=100, pitch=78, start=4.125, end=4.5),  # B7
    pretty_midi.Note(velocity=100, pitch=80, start=4.5, end=4.875),  # C#7
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25), # A7
    pretty_midi.Note(velocity=100, pitch=84, start=5.25, end=5.625), # F7
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # B7
]
piano.notes.extend(piano_notes)

# Drums (Little Ray)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    # Bar 4 (fill)
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    # Bar 4 (end)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    # Bar 4 (final kick)
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
drums.notes.extend(drum_notes)

# Sax (Dante's motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),   # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
