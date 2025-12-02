
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
    # Hi-hat on every eighth
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

# Bar 2: Full ensemble
# SAX: Tenor sax motif (F - G - Ab - Bb)
# Start on beat 1, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=85, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=83, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=2.0625, end=2.25), # Bb
]
sax.notes.extend(sax_notes)

# BASS: Walking line in F
# F - Gb - G - A (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.0625, end=2.25), # A
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 on beat 2 (1.875 - 2.0625)
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.0625), # D
    # Bb7 on beat 4 (2.25 - 2.4375)
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.4375), # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375), # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full ensemble
# SAX: Repeat the motif starting on beat 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=85, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=2.8125), # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=2.8125, end=3.0), # Bb
]
sax.notes.extend(sax_notes)

# BASS: Walking line in F
# F - Gb - G - A (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.4375, end=2.625), # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.8125, end=3.0), # A
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 on beat 2 (2.625 - 2.8125)
    pretty_midi.Note(velocity=80, pitch=57, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.8125), # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.8125), # D
    # Bb7 on beat 4 (3.0 - 3.1875)
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.1875), # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875), # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full ensemble
# SAX: Repeat the motif starting on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=85, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=83, start=3.375, end=3.5625), # Ab
    pretty_midi.Note(velocity=100, pitch=82, start=3.5625, end=3.75), # Bb
]
sax.notes.extend(sax_notes)

# BASS: Walking line in F
# F - Gb - G - A (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.1875, end=3.375), # Gb
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.5625, end=3.75), # A
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 on beat 2 (3.375 - 3.5625)
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.5625), # D
    # Bb7 on beat 4 (3.75 - 3.9375)
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=3.9375), # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375), # G
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.9375, end=4.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    # Hi-hat on every eighth
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
