
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    # Bar 2, 2nd beat: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    # Bar 2, 4th beat: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: short motif in F, starting on 2nd beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    # Bar 3, 2nd beat: F7
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    # Bar 3, 4th beat: Bb7
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: short motif in F, starting on 2nd beat
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (comping)
piano_notes = [
    # Bar 4, 2nd beat: F7
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    # Bar 4, 4th beat: Bb7
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: finish the motif (Bar 4, 2nd beat)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and Bar 4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
