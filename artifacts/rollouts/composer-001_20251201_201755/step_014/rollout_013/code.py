
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line (roots and fifths with chromatic approaches)
# Bar 2: F (root), G (fifth), E (chromatic approach), F (resolve)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # E2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0)   # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F (root)
    pretty_midi.Note(velocity=95, pitch=82, start=1.5, end=3.0),  # A (third)
    pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=3.0),  # C (fifth)
    pretty_midi.Note(velocity=85, pitch=91, start=1.5, end=3.0)   # E (seventh)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (77), A (82), Eb (80), F (77)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=82, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=80, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=2.625, end=3.0)   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Bb (root), D (fifth), C (chromatic), Bb (resolve)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # D2
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # C2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5)   # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),  # Bb (root)
    pretty_midi.Note(velocity=95, pitch=75, start=3.0, end=4.5),  # D (third)
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=4.5),  # F (fifth)
    pretty_midi.Note(velocity=85, pitch=73, start=3.0, end=4.5)   # Ab (seventh)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif with variation, end on A
# Motif: Bb (70), D (75), Ab (73), A (82)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=75, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=73, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=110, pitch=82, start=4.125, end=4.5)   # A
]
sax.notes.extend(sax_notes)

# Drums: Repeat pattern from bar 1
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: C (root), E (fifth), D (chromatic), C (resolve)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # E2
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),  # D2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0)   # C2
]
bass.notes.extend(bass_notes)

# Piano: C7 (C, E, G, B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C (root)
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=6.0),  # E (third)
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=6.0),  # G (fifth)
    pretty_midi.Note(velocity=85, pitch=79, start=4.5, end=6.0)   # B (seventh)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, end on F
# Motif: C (69), E (74), Bb (70), F (77)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=5.625, end=6.0)   # F
]
sax.notes.extend(sax_notes)

# Drums: Repeat pattern from bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
