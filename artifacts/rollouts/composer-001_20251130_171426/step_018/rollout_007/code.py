
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),   # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),    # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),    # A#
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),   # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),    # D
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875),    # D#
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),   # E
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),   # F
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=6.0),    # F#
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, measure 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),    # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),     # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),     # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),     # B
    # Bar 3, measure 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),    # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),     # G
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),     # B
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),     # D
    # Bar 4, measure 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),    # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),     # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),     # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),     # B
]
piano.notes.extend(piano_notes)

# Drums in bars 2-4 (same pattern as bar 1, repeated)
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(
            velocity=note.velocity,
            pitch=note.pitch,
            start=note.start + 1.5 + i*1.5,
            end=note.end + 1.5 + i*1.5
        )
        drums.notes.append(new_note)

# Sax (Dante): Melody
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # Bb
    # Bar 3: Return to motif, with variation
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # Bb
    # Bar 4: End with a resolution
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
