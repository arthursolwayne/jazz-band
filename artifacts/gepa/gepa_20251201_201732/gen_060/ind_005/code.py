
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

# Bass: Walking line (F2-C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root), F#2 (chromatic approach), C3 (fifth), B2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=80, start=2.625, end=3.0),
    # Bar 3: Bb2 (root), Bb2 (chromatic approach), F3 (fifth), E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),
    # Bar 4: Ab2 (root), G2 (chromatic approach), D3 (fifth), C3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=80, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=83, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=3.375),
    # Bar 4: Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=83, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - C - F (octave up)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=81, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
