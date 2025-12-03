
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Marcus: Walking line, roots and fifths with chromatic approaches
# F7 chord: F, A, C, E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # Ab (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # G (F5)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano - Diane: Open voicing, F7 (F, A, C, E) with extension
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax - Dante: Motif, one short phrase with tension and resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G (F7 tension)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G#
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A (resolution)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # G# (suspension)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, Bb7 chord (Bb, D, F, Ab)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=3.0, end=3.375),  # Bb (D2)
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # C (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # B (Bb5)
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, build tension
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # F (Bb7 root)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # G (tension)
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # A (tension)
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # G (suspension)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, Eb7 chord (Eb, G, Bb, Db)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # Eb (D2)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # F# (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625), # F (Eb5)
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Resolve the motif, complete the phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=58, start=4.5, end=4.875),  # Eb (Eb7 root)
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.25),  # F (tension)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # G (tension)
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),   # F (resolution)
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
