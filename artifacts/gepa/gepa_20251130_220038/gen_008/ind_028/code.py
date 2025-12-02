
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

# Define time in seconds for each beat
beat = 0.375  # 160 BPM, 4/4 time
bar = beat * 4  # 1.5 seconds per bar

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.375, end=0.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.125, end=1.25),
    # Hi-hat on every eighth
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Saxophone motif - F, G, A#, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # A#
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0)   # C
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # A#
    pretty_midi.Note(velocity=90, pitch=51, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=54, start=2.375, end=2.5),  # C#
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.0),  # A#
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.0),  # C
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.5),  # A#
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.5),  # C
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.0),  # A#
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.0),  # C
]
piano.notes.extend(piano_notes)

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
# Saxophone continues motif, variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # A#
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=3.875),  # A#
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0)   # C
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=56, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=57, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625),  # A#
    pretty_midi.Note(velocity=90, pitch=61, start=3.625, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # C#
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.375, end=3.5),  # A#
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.5),  # C
]
piano.notes.extend(piano_notes)

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
# Saxophone motif returns, resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # A#
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.125),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=5.375, end=5.5),   # F
]
sax.notes.extend(sax_notes)

# Bass line - walking, chromatic
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.75),  # A#
    pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.125),  # C#
    pretty_midi.Note(velocity=90, pitch=65, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.0),  # A#
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.0),  # C
]
piano.notes.extend(piano_notes)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.75, end=5.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("f_intro.mid")
