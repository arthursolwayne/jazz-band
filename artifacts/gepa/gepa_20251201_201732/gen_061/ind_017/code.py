
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm (F, Ab, D, C), chromatic approach on first beat of bar 2
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # C2 (octave)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # C2 (octave)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=39, start=4.5, end=4.875),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Ab2 (fifth)
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # C2 (octave)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Fm7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2 (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # Eb5
    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab5
    # Bar 4 (Eb7)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Bb5
    pretty_midi.Note(velocity=100, pitch=75, start=4.5, end=4.875),  # D5
    # Bar 4 (Ab7)
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),  # Ab4
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Db5
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),  # E5
]
piano.notes.extend(piano_notes)

# Dante: Short motif, start it, leave it hanging, come back and finish it
# Fm motif: F, Ab, C, Bb (octave) — short, singable, unique
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C5
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # Ab4
    # Bar 4: Come back and finish it (add Bb5)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),  # Bb5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
