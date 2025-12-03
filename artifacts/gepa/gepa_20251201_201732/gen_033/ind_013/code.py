
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
    # Kick on 1 and 3 of bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4 of bar 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F (chromatic approach to G)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # A (chromatic approach to Bb)
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=2.75, end=3.0),  # B
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # F (chromatic approach to G)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    # A (chromatic approach to Bb)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb-D-F-A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)
]
piano.notes.extend(piano_notes)

# Sax: continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=4.25, end=4.5),  # B
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # F (chromatic approach to G)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),
    # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),
    # A (chromatic approach to Bb)
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7 (G-Bb-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75)
]
piano.notes.extend(piano_notes)

# Sax: finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.75, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
