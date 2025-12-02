
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F, chromatic approach on beat 3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # Bb
    # Bar 3: C7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: Melody - whisper, then cry
# Bar 2: Start of motif (F, Bb, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.65),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.65, end=1.8),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.8, end=2.0),    # G
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Return to finish (F, Bb, G, A)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.15),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.15, end=3.3),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.3, end=3.45),    # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.45, end=3.6),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Bass: Walking line in F, chromatic approach on beat 3
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # Bb
    # Bar 4: C7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),   # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: Melody - finish the motif
sax_notes = [
    # Bar 3: Rest (nothing)
    # Bar 4: End of motif
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.15),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.15, end=3.3),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.3, end=3.45),    # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.45, end=3.6),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
