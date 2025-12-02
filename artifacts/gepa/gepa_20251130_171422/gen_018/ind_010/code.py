
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with sparse, syncopated rhythm
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Saxophone: Motif begins (D4, F#4, G4, A4) with dynamic shading
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=85, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=75, pitch=69, start=2.25, end=2.5),  # A4
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=45, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=72, pitch=46, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=74, pitch=47, start=2.0, end=2.25),  # E3
    pretty_midi.Note(velocity=76, pitch=49, start=2.25, end=2.5),  # G3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with emotional shading
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=65, pitch=71, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=60, pitch=64, start=1.5, end=1.75),  # F#4

    pretty_midi.Note(velocity=85, pitch=67, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=75, pitch=72, start=2.0, end=2.25),  # C5
    pretty_midi.Note(velocity=70, pitch=76, start=2.0, end=2.25),  # E5
    pretty_midi.Note(velocity=65, pitch=69, start=2.0, end=2.25),  # A4
]
piano.notes.extend(piano_notes)

# Drums: Continue with kick, snare, hihat, but with variation
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.75),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Saxophone: Motif returns with slight variation
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=85, pitch=66, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=75, pitch=69, start=3.75, end=4.0),  # A4
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=49, start=3.0, end=3.25),  # G3
    pretty_midi.Note(velocity=72, pitch=50, start=3.25, end=3.5),  # Ab3
    pretty_midi.Note(velocity=74, pitch=51, start=3.5, end=3.75),  # A3
    pretty_midi.Note(velocity=76, pitch=53, start=3.75, end=4.0),  # C4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with emotional shading
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=70, pitch=72, start=3.0, end=3.25),  # C5
    pretty_midi.Note(velocity=65, pitch=76, start=3.0, end=3.25),  # E5
    pretty_midi.Note(velocity=60, pitch=69, start=3.0, end=3.25),  # A4

    pretty_midi.Note(velocity=85, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=75, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=70, pitch=71, start=3.5, end=3.75),  # B4
    pretty_midi.Note(velocity=65, pitch=64, start=3.5, end=3.75),  # F#4
]
piano.notes.extend(piano_notes)

# Drums: Continue with kick, snare, hihat, with a fill
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.75),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),  # Snare on 4 with a fill
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Saxophone: Motif resolves with a sustained note
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),  # D4
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=53, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=72, pitch=54, start=4.75, end=5.0),  # Db4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords with emotional shading
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=65, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=60, pitch=64, start=4.5, end=4.75),  # F#4

    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=75, pitch=67, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=70, pitch=71, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=65, pitch=64, start=4.75, end=5.0),  # F#4
]
piano.notes.extend(piano_notes)

# Drums: Final bar with a loose feel
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.375, end=5.75),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.75),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
