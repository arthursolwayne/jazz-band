
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875)  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=2.1875, end=2.375),# B
    pretty_midi.Note(velocity=80, pitch=52, start=2.375, end=2.5625),# C
    pretty_midi.Note(velocity=80, pitch=53, start=2.5625, end=2.75), # C#
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=3.0)     # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.5, end=1.6875),   # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.6875),   # C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.6875),   # D
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.4375),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.4375)   # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75)  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.1875),   # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5625), # F#
    pretty_midi.Note(velocity=80, pitch=62, start=3.5625, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.9375),  # G#
    pretty_midi.Note(velocity=80, pitch=65, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=4.3125, end=4.5)    # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.1875),   # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),   # G#
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),   # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=3.9375),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.9375),  # G#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9375)   # Bb
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
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
# Sax: Motif completion
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25)  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=5.0625, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.4375),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=5.8125), # C#
    pretty_midi.Note(velocity=80, pitch=55, start=5.8125, end=6.0)    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.6875),   # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.6875),   # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.6875),   # D
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.4375),  # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.4375),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.4375)   # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
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

midi.write("dante_intro.mid")
