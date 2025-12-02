
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start and leave hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G#
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25)  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.0625, end=2.25)  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.6875),  # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.6875),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.4375), # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.4375), # F7 (C)
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.4375), # F7 (E)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375)  # F7 (F)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continue the motif, end it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # G#
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75)  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.1875),  # G#
    pretty_midi.Note(velocity=80, pitch=51, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.5625), # A#
    pretty_midi.Note(velocity=80, pitch=53, start=3.5625, end=3.75)  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # F7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.1875),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=3.9375), # F7 (E)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.9375), # F7 (F)
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=3.9375), # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.9375)  # F7 (C)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: variant of the motif, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # G#
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25)  # F
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.0625), # B#
    pretty_midi.Note(velocity=80, pitch=56, start=5.0625, end=5.25)  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # F7 (E)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F7 (F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875),  # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.6875),  # F7 (C)
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.4375), # F7 (E)
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.4375), # F7 (F)
    pretty_midi.Note(velocity=90, pitch=75, start=5.25, end=5.4375), # F7 (Bb)
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.4375)  # F7 (C)
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
