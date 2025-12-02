
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax starts with a short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F (66)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A (69)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G (67)
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # F (66)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F (45)
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # F# (46)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # G (47)
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # G# (48)
    pretty_midi.Note(velocity=80, pitch=49, start=2.5, end=2.75),  # A (49)
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # A# (50)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=1.75, end=2.0),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # D (60),
    # Bar 2: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=2.75, end=3.0),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),  # D (60),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A (69)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G (67)
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F (66)
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),   # Ab (68)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.25),  # Bb (51)
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # B (52)
    pretty_midi.Note(velocity=80, pitch=53, start=3.5, end=3.75),  # C (53)
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.0),  # C# (54)
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),  # D (55)
    pretty_midi.Note(velocity=80, pitch=56, start=4.25, end=4.5),  # D# (56)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.5),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # D (60),
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.25, end=4.5),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.5),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=4.25, end=4.5),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # D (60),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax ends with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F (66)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # D (64)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb (62)
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # G (60)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # Bb (57)
    pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0),  # B (58)
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # C (59)
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # C# (60)
    pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=5.75),  # D (61)
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # D# (62)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=4.75, end=5.0),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # D (60),
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=6.0),  # F (53)
    pretty_midi.Note(velocity=90, pitch=57, start=5.75, end=6.0),  # Bb (57)
    pretty_midi.Note(velocity=90, pitch=58, start=5.75, end=6.0),  # B (58)
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=6.0),  # D (60),
]
piano.notes.extend(piano_notes)

# Add drum notes for bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
