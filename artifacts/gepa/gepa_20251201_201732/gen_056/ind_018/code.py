
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # D2 (root, bar 2, beat 1)
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.875),
    # F2 (chromatic approach up)
    pretty_midi.Note(velocity=85, pitch=40, start=1.875, end=2.0),
    # G2 (fifth, bar 2, beat 2)
    pretty_midi.Note(velocity=85, pitch=42, start=2.0, end=2.375),
    # F2 (chromatic approach down)
    pretty_midi.Note(velocity=85, pitch=40, start=2.375, end=2.5),
    # D2 (root, bar 2, beat 3)
    pretty_midi.Note(velocity=85, pitch=38, start=2.5, end=2.875),
    # F2 (chromatic approach up)
    pretty_midi.Note(velocity=85, pitch=40, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last (bar 4)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=73, start=1.5, end=1.875),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=95, pitch=69, start=2.5, end=2.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=72, start=2.5, end=2.875),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.875),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=2.875),  # Ab
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=95, pitch=72, start=3.5, end=3.875),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=74, start=3.5, end=3.875),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.875),  # Bb
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G (Fm7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # A (chromatic)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # F (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # G (hold)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # A (up)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # G (back)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # A (up)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # G (final)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (same pattern, but with a fill on beat 3)
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),
]
drums.notes.extend(drum_notes_bar3)

# Bar 4: Drums (same pattern, but with a fill on beat 4)
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
]
drums.notes.extend(drum_notes_bar4)

# Bar 4: Bass line (reprise with variation)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=85, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=85, pitch=40, start=3.875, end=4.0),
    pretty_midi.Note(velocity=85, pitch=42, start=4.0, end=4.375),
    pretty_midi.Note(velocity=85, pitch=40, start=4.375, end=4.5),
    pretty_midi.Note(velocity=85, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=85, pitch=40, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes_bar4)

# Bar 4: Piano (resolve on Cm7)
piano.notes.extend([
    pretty_midi.Note(velocity=95, pitch=72, start=3.5, end=3.875),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=74, start=3.5, end=3.875),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.5, end=3.875),  # Bb
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
