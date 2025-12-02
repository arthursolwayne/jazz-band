
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - Gb - G - A
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # A

    # Bar 3: Bb - B - C - D
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),  # D

    # Bar 4: Eb - E - F - G
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.875), # E

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375), # F

    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875), # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts (F D G)
    pretty_midi.Note(velocity=110, pitch=52, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=54, start=1.875, end=2.0), # G

    # Bar 3: Leave it hanging (C)
    pretty_midi.Note(velocity=110, pitch=57, start=3.0, end=3.1875), # C

    # Bar 4: Come back and finish it (F D G)
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=110, pitch=50, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=54, start=4.875, end=5.0), # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
