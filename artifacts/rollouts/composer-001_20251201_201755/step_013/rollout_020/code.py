
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F2, Ab2, Bb2, D2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25), # Eb2 (approach)
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # C2 (fifth of Fm)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2 (approach)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75), # Eb2 (approach)
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125), # C2 (fifth of Fm)
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),  # D2 (approach)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Eb2 (approach)
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625), # C2 (fifth of Fm)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2 (approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.5),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=5.0),  # Bb (overlap with G)
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),   # F (resolve)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F (return)
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # F (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
