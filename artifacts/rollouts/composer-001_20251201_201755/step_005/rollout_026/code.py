
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

# Bass (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm root (F2), approach from E
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # E2
    pretty_midi.Note(velocity=110, pitch=72, start=1.6875, end=2.0),  # F2
    # Bar 2: Cm7, root (C2), approach from B
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1875),  # B2
    pretty_midi.Note(velocity=110, pitch=70, start=2.1875, end=2.5),  # C2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, A♭, C, E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.5),  # F2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.5),  # A♭2
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=2.5),  # C2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.5),  # E♭2
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # A♭3
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # B♭3
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # A♭3
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Dm7, root (D2), approach from C
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # C2
    pretty_midi.Note(velocity=110, pitch=70, start=3.1875, end=3.5),  # D2
    # Bar 3: G7, root (G2), approach from F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.6875),  # F2
    pretty_midi.Note(velocity=110, pitch=68, start=3.6875, end=4.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=4.0),  # G2
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.0),  # B2
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.0),  # D2
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.0),  # F2
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.25),  # B♭3
    pretty_midi.Note(velocity=110, pitch=68, start=3.25, end=3.5),  # A3
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # A♭3
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Cm7, root (C2), approach from B
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875),  # B2
    pretty_midi.Note(velocity=110, pitch=70, start=4.6875, end=5.0),  # C2
    # Bar 4: Fm7, root (F2), approach from E
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875),  # E2
    pretty_midi.Note(velocity=110, pitch=72, start=5.1875, end=5.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, A♭, C, E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.5),  # F2
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.5),  # A♭2
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=5.5),  # C2
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.5),  # E♭2
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # B♭3
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A♭3
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # A♭3
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # G3
]
sax.notes.extend(sax_notes)

# Drums: Bar 3-4
# Bar 3: kick on 1 and 3
drum_notes = [
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
