
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starting at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),    # Fm7 (Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),    # E (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),    # F (resolution)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),    # G (extension)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),    # F (hold)
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0)     # E (suspense)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),    # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),    # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0)     # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=2.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=2.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),    # C
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=3.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0)     # C
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),    # E (resolution)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),    # F (return)
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),    # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),    # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),    # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0)     # F (close)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),    # G
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.5),    # Ab
    pretty_midi.Note(velocity=90, pitch=44, start=5.5, end=5.75),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0)     # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=5.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=4.75, end=5.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),    # C
    # Bar 4: Fm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=44, start=5.75, end=6.0),    # F
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=6.0),    # Eb
    pretty_midi.Note(velocity=90, pitch=47, start=5.75, end=6.0),    # Ab
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0)     # C
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
