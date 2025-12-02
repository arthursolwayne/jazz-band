
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.125),  # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=2.375, end=2.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.875, end=3.0),  # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (Comp on beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875),
    # Bar 3 (Comp on beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=2.875),
    # Bar 4 (Comp on beat 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875),
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875),  # E
    # Bar 3: Let it hang
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375),  # E
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.875, end=3.0),   # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
]
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
