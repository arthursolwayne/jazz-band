
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, space, and rhythmic variation

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add tension with dynamic variation and space

drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif: concise, memorable, emotionally resonant

# Saxophone motif: Fm7 -> Bb -> Eb -> Ab -> G -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=80, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=84, start=2.75, end=3.0),  # F
    # Repeat the motif with variation
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=80, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=84, start=4.25, end=4.5),
    # Final repetition
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=80, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=84, start=5.75, end=6.0),
]

sax.notes.extend(sax_notes)

# Bass line: chromatic approach, melodic, active, not just walking

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C
]

bass.notes.extend(bass_notes)

# Piano comping: 7th chords, on 2 and 4, with emotional shading

piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=84, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=80, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # D
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=84, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=80, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=84, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=80, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),
]

piano.notes.extend(piano_notes)

# Add some dynamic variation in piano
for note in piano.notes:
    if note.start >= 1.5 and note.start < 3.0:
        note.velocity = 80
    elif note.start >= 3.0 and note.start < 5.0:
        note.velocity = 90
    else:
        note.velocity = 100

midi.instruments.extend([sax, bass, piano, drums])
