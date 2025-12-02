
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX - Melody starts here
sax_notes = [
    # Tenor sax: short motif, chromatic approach
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# BASS - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # E (3rd)
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F (4th)
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=2.75, end=3.0),  # D (root)
]
bass.notes.extend(bass_notes)

# PIANO - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # C
    # Bar 2: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX - Motif returns with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# BASS - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# PIANO - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # C
    # Bar 3: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX - Motif resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# BASS - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=80, pitch=45, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# PIANO - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # C
    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Bar 2: 1.5-3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0-4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hi-hat
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5-6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hi-hat
]
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
