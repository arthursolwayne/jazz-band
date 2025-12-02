
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7 on beat 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),  # C
    # G7 on beat 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=2.75),  # F
]
piano.notes.extend(piano_notes)

# Dante: Saxophone motif (Dm melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.1875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.1875, end=2.375),# F
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5625),# D
    pretty_midi.Note(velocity=110, pitch=64, start=2.5625, end=2.75), # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),    # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7 on beat 2 (3.375 - 3.5)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),  # C
    # G7 on beat 4 (4.125 - 4.25)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.25),  # F
]
piano.notes.extend(piano_notes)

# Dante: Saxophone motif (Dm melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.6875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.6875, end=3.875),# F
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0625),# D
    pretty_midi.Note(velocity=110, pitch=64, start=4.0625, end=4.25), # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),    # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4 (Dm7 on 2, G7 on 4)
piano_notes = [
    # Dm7 on beat 2 (4.875 - 5.0)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),  # C
    # G7 on beat 4 (5.625 - 5.75)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=5.75),  # F
]
piano.notes.extend(piano_notes)

# Dante: Saxophone motif (Dm melody)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.1875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.1875, end=5.375),# F
    pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5625),# D
    pretty_midi.Note(velocity=110, pitch=64, start=5.5625, end=5.75), # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),    # G
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: Full bar (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full bar (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
