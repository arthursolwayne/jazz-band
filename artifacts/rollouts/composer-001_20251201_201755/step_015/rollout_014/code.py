
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (Bass): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.75),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.5),  # C3 (root)
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.75),  # D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=54, start=2.75, end=3.0),  # Db3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane (Piano): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # C4
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # F4
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # C4
]
piano.notes.extend(piano_notes)

# Little Ray (Drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
]
drums.notes.extend(drum_notes)

# Dante (Sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # E4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
