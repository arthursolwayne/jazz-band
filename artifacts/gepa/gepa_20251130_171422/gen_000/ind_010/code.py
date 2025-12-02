
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
drums_notes = [
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
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# SAX: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # D
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),  # D
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat (on beat 2)
    pretty_midi.Note(velocity=90, pitch=45, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=1.75, end=2.0),  # D
    # Bar 2 - 4th beat (on beat 4)
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Drums for Bar 2
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drums_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# SAX: Motif repeats but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # D
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),  # D
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat (on beat 2)
    pretty_midi.Note(velocity=90, pitch=45, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=3.25, end=3.5),  # D
    # Bar 3 - 4th beat (on beat 4)
    pretty_midi.Note(velocity=90, pitch=45, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.25, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Drums for Bar 3
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drums_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# SAX: Motif returns to start, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # D
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.75),  # D
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat (on beat 2)
    pretty_midi.Note(velocity=90, pitch=45, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.75, end=5.0),  # D
    # Bar 4 - 4th beat (on beat 4)
    pretty_midi.Note(velocity=90, pitch=45, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=5.75, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=5.75, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Drums for Bar 4
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drums_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
