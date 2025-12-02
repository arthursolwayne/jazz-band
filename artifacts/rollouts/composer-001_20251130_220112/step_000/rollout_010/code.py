
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # Eb
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # Eb
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif, make it sing
# Motif: F - Bb - D - Eb
# Start on bar 2, beat 1
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0),   # Eb
    # Repeat motif with slight variation on bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5),   # Eb
    # End with a suspended resolution
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.0),   # Eb
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
