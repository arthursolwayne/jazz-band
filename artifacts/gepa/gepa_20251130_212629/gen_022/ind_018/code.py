
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Dm7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),  # Bb (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Drums continue with full pattern
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),# Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 4
]
drums.notes.extend(drums_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums continue with full pattern
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 4
]
drums.notes.extend(drums_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano comping: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums continue with full pattern
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.1875), # Hihat on 4
]
drums.notes.extend(drums_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
