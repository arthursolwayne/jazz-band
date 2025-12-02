
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D, F, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0), # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625), # D
    # Bar 2, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0), # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0), # F
]
piano.notes.extend(piano_notes)

# Dante: Melody starts on bar 2, beat 1
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> Eb -> F -> D (sax)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Dm (D, F, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5), # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # D
    # Bar 3, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5), # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5), # F
]
piano.notes.extend(piano_notes)

# Dante: Motif continuation (F -> G -> A -> F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5), # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Dm (D, F, G, Bb)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0), # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625), # D
    # Bar 4, beat 4 (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0), # F
]
piano.notes.extend(piano_notes)

# Dante: Motif continuation (Bb -> D -> Eb -> D) - resolves the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0), # D
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
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
