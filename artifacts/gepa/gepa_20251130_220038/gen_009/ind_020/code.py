
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, measure 1, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # D
    # Bar 2, measure 1, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # B
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, measure 1, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # D
    # Bar 3, measure 1, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at bar 3)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G#
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),   # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, measure 1, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # D
    # Bar 4, measure 1, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Motif (start at bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # B
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
for bar in range(2, 4):
    start = 1.5 + bar * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.1875), # Hihat on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125), # Snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375),# Hihat on 2
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125),# Hihat on 3
        pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),  # Snare on 4
        pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.6875), # Hihat on 4
    ]
    drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
