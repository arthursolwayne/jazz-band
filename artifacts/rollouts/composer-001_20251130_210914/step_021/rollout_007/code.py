
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.375), # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=2.75), # Bb
    pretty_midi.Note(velocity=90, pitch=86, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=90, pitch=88, start=2.875, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 (1.5 - 1.75)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # D
    # G7 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),   # B
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.5),   # F#
    # Cm7 (2.75 - 3.0)
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),   # Bb
]
piano.notes.extend(piano_notes)

# Dante: Motif - Start it, leave it hanging, come back and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> F -> G -> Bb (first four notes), then D -> F -> G -> C (to resolve)
# Play the first four notes on the first beat, then rest, then play the resolution on the last beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),   # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),   # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=3.875, end=4.0),   # G
    pretty_midi.Note(velocity=90, pitch=81, start=4.0, end=4.125),   # A
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=86, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=90, pitch=88, start=4.375, end=4.5),   # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # G7 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),   # B
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=90, pitch=79, start=3.25, end=3.5),   # F#
    # Cm7 (4.0 - 4.25)
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.25),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),   # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25),   # Bb
]
piano.notes.extend(piano_notes)

# Drum fill in bar 3 (3.0 - 4.5s)
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125),   # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.375, end=5.5),   # G
    pretty_midi.Note(velocity=90, pitch=81, start=5.5, end=5.625),   # A
    pretty_midi.Note(velocity=90, pitch=83, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=86, start=5.75, end=5.875),  # D
    pretty_midi.Note(velocity=90, pitch=88, start=5.875, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Cm7 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),   # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),   # Bb
    # F7 (5.5 - 5.75)
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),   # C
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75),   # E
]
piano.notes.extend(piano_notes)

# Drum fill in bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
