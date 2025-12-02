
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walk)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2, measure 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # D
    # Bar 2, measure 4: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax melody - continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walk)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # A
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 3, measure 2: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
    # Bar 3, measure 4: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax melody - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Bass line (chromatic walk)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=58, start=4.75, end=5.0),  # A#
    pretty_midi.Note(velocity=80, pitch=59, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),  # C
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 4, measure 2: B7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=78, start=4.75, end=5.0),  # F#
    # Bar 4, measure 4: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Bar 2: 1.5-3.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0-4.5s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5-6.0s
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
