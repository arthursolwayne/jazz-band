
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
    # Kick on beat 1
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    # Snare on beat 2
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    # Kick on beat 3
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),
    # Snare on beat 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif intro (F - G - Bb - F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.8125)  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=46, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=70, pitch=47, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=70, pitch=48, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=70, pitch=49, start=2.0625, end=2.25),  # G#
    pretty_midi.Note(velocity=70, pitch=50, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=70, pitch=51, start=2.4375, end=2.625), # A#
    pretty_midi.Note(velocity=70, pitch=52, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=70, pitch=53, start=2.8125, end=3.0)    # B
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 & 4 with 7th chords
piano_notes = [
    # Bar 2, beat 2 (G7)
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.0625),  # B
    pretty_midi.Note(velocity=80, pitch=77, start=1.875, end=2.0625),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.0625),  # F
    # Bar 2, beat 4 (C7)
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.8125),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=2.8125),  # B
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.3125)  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=52, start=3.0, end=3.1875),   # Bb
    pretty_midi.Note(velocity=70, pitch=53, start=3.1875, end=3.375), # B
    pretty_midi.Note(velocity=70, pitch=55, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=70, pitch=56, start=3.5625, end=3.75),  # C#
    pretty_midi.Note(velocity=70, pitch=57, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=70, pitch=58, start=3.9375, end=4.125), # D#
    pretty_midi.Note(velocity=70, pitch=59, start=4.125, end=4.3125), # E
    pretty_midi.Note(velocity=70, pitch=60, start=4.3125, end=4.5)    # F
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 & 4 with 7th chords
piano_notes = [
    # Bar 3, beat 2 (D7)
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.5625),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5625),  # C
    # Bar 3, beat 4 (G7)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.3125),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.3125),  # B
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.3125),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.3125),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a question (Bb on beat 3, rest on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=60, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=70, pitch=61, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=70, pitch=62, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=70, pitch=63, start=5.0625, end=5.25),  # G#
    pretty_midi.Note(velocity=70, pitch=64, start=5.25, end=5.4375),  # A
    pretty_midi.Note(velocity=70, pitch=65, start=5.4375, end=5.625), # A#
    pretty_midi.Note(velocity=70, pitch=66, start=5.625, end=5.8125), # B
    pretty_midi.Note(velocity=70, pitch=67, start=5.8125, end=6.0)    # C
]
bass.notes.extend(bass_notes)

# Piano: Comping on 2 & 4 with 7th chords
piano_notes = [
    # Bar 4, beat 2 (A7)
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625),  # C#
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0625),  # E
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.0625),  # G
    # Bar 4, beat 4 (C7)
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=5.8125),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=5.8125),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=5.8125),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=5.8125),  # B
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 4, beat 1
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    # Bar 4, beat 3
    pretty_midi.Note(velocity=80, pitch=36, start=5.25, end=5.625),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
    # Hi-hat on every 8th
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
