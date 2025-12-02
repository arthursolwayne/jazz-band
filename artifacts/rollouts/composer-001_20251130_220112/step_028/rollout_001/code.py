
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
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # D
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: motif (D, Gb, F, Eb) - short and expressive
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.0625, end=2.25), # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # D
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: motif repeat with variation (D, Gb, F, Eb) - ends on Eb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375), # Gb
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.5625, end=3.75), # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: motif end (D, Gb, F, Eb) - resolves on Eb with a slight pull
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.6875, end=4.875), # Gb
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.0625, end=5.25), # Eb
]
sax.notes.extend(sax_notes)

# Drums in bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
