
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
    pretty_midi.Note(start=0.0, end=0.375, pitch=36, velocity=100),
    pretty_midi.Note(start=1.125, end=1.5, pitch=36, velocity=100),
    # Snare on 2 and 4
    pretty_midi.Note(start=0.75, end=1.125, pitch=38, velocity=110),
    pretty_midi.Note(start=1.875, end=2.25, pitch=38, velocity=110),
    # Hi-hat on every eighth
    pretty_midi.Note(start=0.0, end=0.375, pitch=42, velocity=80),
    pretty_midi.Note(start=0.375, end=0.75, pitch=42, velocity=80),
    pretty_midi.Note(start=0.75, end=1.125, pitch=42, velocity=80),
    pretty_midi.Note(start=1.125, end=1.5, pitch=42, velocity=80),
    pretty_midi.Note(start=1.5, end=1.875, pitch=42, velocity=80),
    pretty_midi.Note(start=1.875, end=2.25, pitch=42, velocity=80),
    pretty_midi.Note(start=2.25, end=2.625, pitch=42, velocity=80),
    pretty_midi.Note(start=2.625, end=3.0, pitch=42, velocity=80)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(start=1.5, end=1.875, pitch=48, velocity=80),  # F
    pretty_midi.Note(start=1.875, end=2.25, pitch=49, velocity=80),  # Gb
    pretty_midi.Note(start=2.25, end=2.625, pitch=50, velocity=80),  # G
    pretty_midi.Note(start=2.625, end=3.0, pitch=51, velocity=80)   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(start=1.875, end=2.25, pitch=64, velocity=90),  # F
    pretty_midi.Note(start=1.875, end=2.25, pitch=69, velocity=90),  # Bb
    pretty_midi.Note(start=1.875, end=2.25, pitch=71, velocity=90),  # C
    pretty_midi.Note(start=1.875, end=2.25, pitch=76, velocity=90),  # E
    # Bar 2, beat 4: A7
    pretty_midi.Note(start=2.625, end=3.0, pitch=69, velocity=90),   # A
    pretty_midi.Note(start=2.625, end=3.0, pitch=74, velocity=90),   # C#
    pretty_midi.Note(start=2.625, end=3.0, pitch=76, velocity=90),   # E
    pretty_midi.Note(start=2.625, end=3.0, pitch=81, velocity=90),   # G
]
piano.notes.extend(piano_notes)

# Sax: Melody, one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(start=1.5, end=1.875, pitch=66, velocity=100),  # A
    pretty_midi.Note(start=1.875, end=2.25, pitch=69, velocity=100),  # C
    pretty_midi.Note(start=2.25, end=2.625, pitch=71, velocity=100),  # D
    pretty_midi.Note(start=2.625, end=3.0, pitch=66, velocity=100),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(start=3.0, end=3.375, pitch=51, velocity=80),   # Ab
    pretty_midi.Note(start=3.375, end=3.75, pitch=52, velocity=80),  # Bb
    pretty_midi.Note(start=3.75, end=4.125, pitch=53, velocity=80),  # B
    pretty_midi.Note(start=4.125, end=4.5, pitch=55, velocity=80)    # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7
    pretty_midi.Note(start=3.375, end=3.75, pitch=62, velocity=90),  # D
    pretty_midi.Note(start=3.375, end=3.75, pitch=67, velocity=90),  # F#
    pretty_midi.Note(start=3.375, end=3.75, pitch=69, velocity=90),  # G
    pretty_midi.Note(start=3.375, end=3.75, pitch=74, velocity=90),  # B
    # Bar 3, beat 4: G7
    pretty_midi.Note(start=4.125, end=4.5, pitch=67, velocity=90),   # G
    pretty_midi.Note(start=4.125, end=4.5, pitch=72, velocity=90),   # B
    pretty_midi.Note(start=4.125, end=4.5, pitch=74, velocity=90),   # C#
    pretty_midi.Note(start=4.125, end=4.5, pitch=79, velocity=90),   # D
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(start=3.0, end=3.375, pitch=69, velocity=100),  # C
    pretty_midi.Note(start=3.375, end=3.75, pitch=71, velocity=100),  # D
    pretty_midi.Note(start=3.75, end=4.125, pitch=69, velocity=100),  # C
    pretty_midi.Note(start=4.125, end=4.5, pitch=71, velocity=100),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(start=4.5, end=4.875, pitch=36, velocity=100),  # Kick on 1
    pretty_midi.Note(start=5.625, end=6.0, pitch=36, velocity=100),  # Kick on 3
    pretty_midi.Note(start=4.875, end=5.25, pitch=38, velocity=110),  # Snare on 2
    pretty_midi.Note(start=6.0, end=6.375, pitch=38, velocity=110),   # Snare on 4
    pretty_midi.Note(start=4.5, end=4.875, pitch=42, velocity=80),
    pretty_midi.Note(start=4.875, end=5.25, pitch=42, velocity=80),
    pretty_midi.Note(start=5.25, end=5.625, pitch=42, velocity=80),
    pretty_midi.Note(start=5.625, end=6.0, pitch=42, velocity=80),
    pretty_midi.Note(start=6.0, end=6.375, pitch=42, velocity=80),
    pretty_midi.Note(start=6.375, end=6.75, pitch=42, velocity=80)
]
drums.notes.extend(drum_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(start=4.5, end=4.875, pitch=55, velocity=80),   # C
    pretty_midi.Note(start=4.875, end=5.25, pitch=57, velocity=80),  # D
    pretty_midi.Note(start=5.25, end=5.625, pitch=59, velocity=80),  # Eb
    pretty_midi.Note(start=5.625, end=6.0, pitch=60, velocity=80)    # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: B7
    pretty_midi.Note(start=4.875, end=5.25, pitch=71, velocity=90),  # B
    pretty_midi.Note(start=4.875, end=5.25, pitch=76, velocity=90),  # D
    pretty_midi.Note(start=4.875, end=5.25, pitch=78, velocity=90),  # E
    pretty_midi.Note(start=4.875, end=5.25, pitch=83, velocity=90),  # F#
    # Bar 4, beat 4: F7
    pretty_midi.Note(start=6.0, end=6.375, pitch=64, velocity=90),   # F
    pretty_midi.Note(start=6.0, end=6.375, pitch=69, velocity=90),   # Bb
    pretty_midi.Note(start=6.0, end=6.375, pitch=71, velocity=90),   # C
    pretty_midi.Note(start=6.0, end=6.375, pitch=76, velocity=90),   # E
]
piano.notes.extend(piano_notes)

# Sax: Finale of the motif
sax_notes = [
    pretty_midi.Note(start=4.5, end=4.875, pitch=66, velocity=100),  # A
    pretty_midi.Note(start=4.875, end=5.25, pitch=69, velocity=100),  # C
    pretty_midi.Note(start=5.25, end=5.625, pitch=71, velocity=100),  # D
    pretty_midi.Note(start=5.625, end=6.0, pitch=66, velocity=100),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
