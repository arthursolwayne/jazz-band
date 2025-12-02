
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # A (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # F (root)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C (root)
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # E (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # C (root)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # A (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # F (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E
]
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F
])
# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # Ab
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, F (start), leave it hanging on the next bar, come back to finish on bar 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F (come back)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
