
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D minor, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),   # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),
    
    # Bar 3: 7th chord on G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax motif
# Start with a phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.65),   # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=1.65, end=1.8),   # A
    pretty_midi.Note(velocity=100, pitch=68, start=1.8, end=1.95),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.95, end=2.1),   # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.1, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.4),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=2.4, end=2.55),   # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=2.55, end=2.7),   # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.7, end=2.85),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.85, end=3.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),   # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),   # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: 7th chord on G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),
    
    # Bar 4: 7th chord on Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Full bar of kick, snare, hihat
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante: Continue motif, leave it open-ended
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.15),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=3.15, end=3.3),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.3, end=3.45),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=3.45, end=3.6),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.6, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=3.9),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.9, end=4.05),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=4.05, end=4.2),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.2, end=4.35),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=4.35, end=4.5),   # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: 7th chord on Dm7 (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Full bar of kick, snare, hihat
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.65),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.65, end=4.8),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=4.8, end=4.95),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.95, end=5.1),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=5.1, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.4),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=5.4, end=5.55),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.55, end=5.7),   # D
    pretty_midi.Note(velocity=100, pitch=68, start=5.7, end=5.85),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.85, end=6.0),   # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
