
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # Eb (chromatic approach)
]

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # D
]

# Dante: Motif - one short phrase, start it, leave it hanging, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (Fm7 9th)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=1.875), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F (root)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Eb (b7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D (9th again)
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Marcus: Fm root, chromatic approach to Bb, Ab, G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # Gb (chromatic approach to Bb)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),   # G (chromatic approach to F)
]

# Diane: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Ab
]

# Dante: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G (fifth)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),   # F (root)
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Eb (b7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # F (root)
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # G (fifth)
]

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)   # Hihat on 4
]
drums.notes.extend(drum_notes)

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Marcus: Ab (chromatic approach to G), G, F, chromatic approach to Eb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0),   # Gb (chromatic approach to Eb)
]

# Diane: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # Db
]

# Dante: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Eb (b7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # F (root)
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # D (9th)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # G (fifth)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # F (root)
]

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)   # Hihat on 4
]
drums.notes.extend(drum_notes)

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
