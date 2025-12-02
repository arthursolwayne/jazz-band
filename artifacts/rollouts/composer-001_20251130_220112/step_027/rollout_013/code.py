
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # Fm7 (F, Ab, Bb, D)
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875), # D
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),   # G
    pretty_midi.Note(velocity=80, pitch=37, start=2.0, end=2.1875), # Eb
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 2, beat 2 (Dm7)
    pretty_midi.Note(velocity=80, pitch=62, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=80, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.6875, end=1.875), # C
    # Bar 2, beat 4 (Fm7)
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.1875), # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.1875), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.1875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.1875), # A
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif (repeats, but with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75), # F
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=80, pitch=38, start=3.5625, end=3.75), # F#
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 3, beat 2 (Fm7)
    pretty_midi.Note(velocity=80, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.1875, end=3.375), # A
    # Bar 3, beat 4 (Bbmaj7)
    pretty_midi.Note(velocity=80, pitch=67, start=3.5625, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.5625, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=74, start=3.5625, end=3.75), # G
]
piano.notes.extend(piano_notes)

# Drums continue (Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax ends the motif with a suspension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.1875), # F
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.1875), # A
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 4, beat 2 (Fm7)
    pretty_midi.Note(velocity=80, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.6875, end=4.875), # A
    # Bar 4, beat 4 (Bbmaj7)
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.1875), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=5.0, end=5.1875), # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.1875), # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.0, end=5.1875), # G
]
piano.notes.extend(piano_notes)

# Drums continue (Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
