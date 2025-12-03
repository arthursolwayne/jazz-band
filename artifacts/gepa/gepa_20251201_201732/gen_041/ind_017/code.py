
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 2: F - Ab - D - C
# Bar 3: F - Ab - D - C
# Bar 4: F - Ab - D - C (with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # C2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),   # C2
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),   # C2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: E7 (E, G#, B, D)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # Eb5
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Ab5
    # Bar 4: E7
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # G#4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # D5
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F - Ab - A - Bb (F to Bb, 1/2 step up each)
# Bar 2: F (start), Ab, A, Bb (end)
# Bar 3: rest
# Bar 4: F (start), Ab, A, Bb (end)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # Ab5
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),  # A5
    pretty_midi.Note(velocity=100, pitch=82, start=2.625, end=3.0),   # Bb5
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # Ab5
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625),  # A5
    pretty_midi.Note(velocity=100, pitch=82, start=5.625, end=6.0),   # Bb5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
