
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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
# Bass line: walking line with chromatic approach
bass_notes = [
    # Bar 2: D - C# - B - C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    # Bar 2: C#7 on beat 3
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=2.875),  # C#
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=2.875),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.875),  # C#
]
piano.notes.extend(piano_notes)

# Sax: short motif, starts on beat 2 of bar 2
sax_notes = [
    # Bar 2: B (beat 2)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.125),
    # Bar 2: D (beat 3)
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.875),
    # Bar 3: B (beat 2)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.625),
    # Bar 3: F# (beat 3)
    pretty_midi.Note(velocity=110, pitch=66, start=4.125, end=4.375),
    # Bar 4: D (beat 2)
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.125),
    # Bar 4: B (beat 3)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.875)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line with chromatic approach
bass_notes = [
    # Bar 3: D - C# - B - C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: D7 on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    # Bar 3: C#7 on beat 3
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.375),  # C#
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.375),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.375),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.375),  # C#
]
piano.notes.extend(piano_notes)

# Sax: continue motif
sax_notes = [
    # Bar 3: C# (beat 1)
    pretty_midi.Note(velocity=110, pitch=61, start=3.0, end=3.25),
    # Bar 3: D (beat 2)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.625),
    # Bar 3: B (beat 3)
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.375),
    # Bar 3: F# (beat 4)
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking line with chromatic approach
bass_notes = [
    # Bar 4: D - C# - B - C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 1
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # D
    # Bar 4: C#7 on beat 3
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=5.875),  # C#
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=5.875),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=5.875),  # C#
]
piano.notes.extend(piano_notes)

# Sax: finish motif
sax_notes = [
    # Bar 4: C# (beat 1)
    pretty_midi.Note(velocity=110, pitch=61, start=4.5, end=4.75),
    # Bar 4: D (beat 2)
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.125),
    # Bar 4: B (beat 3)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.875),
    # Bar 4: C (beat 4)
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
