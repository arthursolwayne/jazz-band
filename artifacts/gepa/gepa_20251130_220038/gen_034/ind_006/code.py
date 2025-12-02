
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approach, no repetition
# F7 chord: F A C E
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=75, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=78, start=4.25, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=80, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=81, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.5),  # G#
    pretty_midi.Note(velocity=90, pitch=83, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (beat 1)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),  # E
    # Bar 3 (beat 2)
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # E
    # Bar 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.25),  # E
]
piano.notes.extend(piano_notes)

# Sax - the melody: whisper at first, then a cry
# F Ab Bb C
# Start with a short motif, leave it hanging, then return and finish it
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.6875),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=2.6875, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.6875),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=3.6875, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.1875, end=4.375),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.375, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=4.6875, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=5.0, end=5.1875),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.1875, end=5.375),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.6875),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("whisper_cry.mid")
