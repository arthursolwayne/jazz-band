
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet
# Sax: start with a short motif - C (60) to E (64) to B (67) to D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C minor with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5)   # D#
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2: C7 (C, E, B, D)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    # Bar 2, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5)
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the quartet
# Sax: Repeat the motif but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.25, end=3.5)   # G#
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3, beat 2: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),
    # Bar 3, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5)
]
piano.notes.extend(piano_notes)

# Bar 4: Continue the quartet
# Sax: Repeat the motif again, but with a slight push
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=68, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.25),  # A#
    pretty_midi.Note(velocity=80, pitch=72, start=4.25, end=4.5)   # Bb
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    # Bar 4, beat 4: C7 again
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5)
]
piano.notes.extend(piano_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
