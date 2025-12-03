
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line (roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=43, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=70, pitch=39, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=70, pitch=40, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Theme: F - Ab - G - F (rest on the last note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F (rest for 0.375s)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.8125, end=3.0),  # Ab
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
