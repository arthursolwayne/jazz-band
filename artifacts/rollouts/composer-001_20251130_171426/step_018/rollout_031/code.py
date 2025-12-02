
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts here
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on F (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F
    # Bar 3 - 7th chord on D (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # E
    # Bar 4 - 7th chord on F (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 - 7th chord on D (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # E
    # Bar 4 - 7th chord on F (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4 - 7th chord on F (F7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
]
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare
])
# Hi-hats on every eighth
for i in range(3.0, 6.0, 0.125):
    if i % 1.0 != 0:
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=i, end=i + 0.125))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
