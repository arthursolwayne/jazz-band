
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2: F - G - F - E (root, fifth, root, chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # E2

    # Bar 3: C - B - C - Bb (root, chromatic approach, root, chromatic approach)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # C3
    pretty_midi.Note(velocity=100, pitch=75, start=3.375, end=3.75), # B3
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # Bb3

    # Bar 4: F - G - F - E (root, fifth, root, chromatic approach)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # F2
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0)   # E2
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),

    # Bar 3: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.5),
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.5),

    # Bar 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=5.0)
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif: F - G - A - F (motif starts)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),

    # Bar 3: Leave it hanging (rest)
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=73, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.0),

    # Bar 4: Come back and finish it (F - G - A - Bb)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=73, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
