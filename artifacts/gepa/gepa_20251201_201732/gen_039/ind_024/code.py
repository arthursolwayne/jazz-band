
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (D2)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Gb (D#2)
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),
    # C (A2)
    pretty_midi.Note(velocity=90, pitch=45, start=2.125, end=2.5),
    # D (B2)
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.875),
    # F (D2)
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # D
    # Bar 3: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=2.125, end=2.5),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=2.125, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=2.125, end=2.5),  # C
    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.875, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.875, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.3125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125)
]
drums.notes.extend(drum_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Gb - F - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.6875, end=1.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.6875),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
