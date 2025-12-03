
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

# Bass line: Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with a chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.6875),

    # Bar 3: A2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.4375),

    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.1875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # C4

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F4

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C4
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375), # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375), # Bb4
]
piano.notes.extend(piano_notes)

# Drums: Full kit for bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75), # Snare on 4
]
# Hi-hats on every eighth
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5), # Snare on 4
])
for i in range(4):
    start = 2.25 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25), # Snare on 4
])
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Notes in Dm: D, Eb, F, G
# Motif: D, Eb, F, rest, G, rest, D, Eb, rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=1.6875, end=1.875), # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=2.8125, end=3.0), # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # D4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5625, end=3.75), # Eb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
