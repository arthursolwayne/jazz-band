
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=1.5, end=1.875),
    # Chromatic approach to Bb (fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0),
    # Bb (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.375),
    # Chromatic approach to Eb (third)
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.625),
    # Eb (third)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=2.0),
    # Bar 3: Gm7 (G, Bb, D, E)
    pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.5),
    pretty_midi.Note(velocity=100, pitch=44, start=2.0, end=2.5),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=45, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=47, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=48, start=2.5, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, haunting and incomplete
# Start on Bb (Fm scale degree 2), then move to D (scale degree 6)
# Leave it hanging on the last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=41, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=43, start=2.0, end=2.375),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
