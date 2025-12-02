
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

# Bar 2: Everyone in. Sax takes the melody.
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Start with a whisper: D (62), Eb (63), F (65), G (67)
# Then a cry: Ab (69), Bb (70), C (72), D (62)
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=85, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.0625, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=2.8125), # C
    pretty_midi.Note(velocity=115, pitch=62, start=2.8125, end=3.0), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
# Dm: D, Eb, F, G, Ab, Bb, C
# Bar 2: D -> Eb -> F -> G
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=70, pitch=63, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=70, pitch=65, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=70, pitch=67, start=2.0625, end=2.25),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, Ab, C
# Bar 2: Chord on beat 2 (1.875) and beat 4 (2.25)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.4375),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet
# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=85, pitch=63, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.5625, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.9375), # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=3.9375, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=115, pitch=62, start=4.3125, end=4.5), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
# Bar 3: G -> Ab -> Bb -> C
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=70, pitch=69, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=70, pitch=70, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=70, pitch=72, start=3.5625, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, Ab, C
# Bar 3: Chord on beat 2 (3.375) and beat 4 (3.75)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=3.9375),
]
piano.notes.extend(piano_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 3: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
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

# Bar 4: Full quartet
# Sax: Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=85, pitch=63, start=4.6875, end=4.875), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=95, pitch=67, start=5.0625, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.4375), # Ab
    pretty_midi.Note(velocity=105, pitch=70, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=5.8125), # C
    pretty_midi.Note(velocity=115, pitch=62, start=5.8125, end=6.0), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Dm, chromatic approaches
# Bar 4: C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=72, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=70, pitch=62, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=70, pitch=63, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=70, pitch=65, start=5.0625, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, Ab, C
# Bar 4: Chord on beat 2 (4.875) and beat 4 (5.25)
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.4375),
]
piano.notes.extend(piano_notes)

# Drums: kick=36, snare=38, hihat=42
# Bar 4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.1875),
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

midi.write("dante_introduction.mid")
