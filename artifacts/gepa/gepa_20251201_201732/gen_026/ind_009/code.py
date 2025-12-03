
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with roots and fifths, chromatic approach
bass_notes = [
    # Bar 2: D2 (root of Dm), chromatic approach to Eb2 (D->Eb)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.125),
    # Bar 2: G2 (fifth of Dm)
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # Bar 3: C2 (root of G7, leading to Cm)
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    # Bar 3: F2 (fifth of G7)
    pretty_midi.Note(velocity=100, pitch=41, start=2.875, end=3.25),
    # Bar 4: Bb2 (chromatic approach to Bb2 -> B2)
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.625),
    # Bar 4: F2 (fifth of Bb7)
    pretty_midi.Note(velocity=100, pitch=41, start=3.625, end=4.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C
]
# Bar 3: G7 (G B D F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # F
]
# Bar 4: Cm7 (C Eb G Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: short motif, make it sing. Start it, leave it hanging, come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G (D to G with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue the pattern for bars 2-4
drum_notes = [
    # Kick on 1 and 3 of each bar
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4 of each bar
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
