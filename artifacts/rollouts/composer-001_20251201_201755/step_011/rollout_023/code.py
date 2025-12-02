
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 48), D2 (MIDI 38), F2 (MIDI 48), G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, D), Bb7 (Bb, D, F, Ab), Fm7 (F, Ab, C, D), G7 (G, B, D, F)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Ab
    # Bar 4: Fm7
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: motif
# F (60), Bb (62), F (60), C (64) — short, sing, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # F (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 48), Ab2 (MIDI 40), F2 (MIDI 48), G2 (MIDI 43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
# Already added above

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 48), Ab2 (MIDI 40), F2 (MIDI 48), F2 (MIDI 48)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # F2
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Beyond 6.0, but okay
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
