
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Bb, D, F#, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=100, pitch=86, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=88, start=1.875, end=2.0625), # F#
    pretty_midi.Note(velocity=100, pitch=89, start=2.0625, end=2.25), # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line (D, Eb, F#, G)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # F#
    pretty_midi.Note(velocity=100, pitch=66, start=2.0625, end=2.25), # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=100, pitch=86, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=88, start=3.375, end=3.5625), # F#
    pretty_midi.Note(velocity=100, pitch=89, start=3.5625, end=3.75), # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line (G, A, B, C)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.5625, end=3.75), # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0),
    # D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.75),
]
piano.notes.extend(piano_notes)

# Drum fill on 3rd bar
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a sustained note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line (C, D, Eb, F)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.75),
    # D7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.125),
]
piano.notes.extend(piano_notes)

# Drum fill on 4th bar
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
