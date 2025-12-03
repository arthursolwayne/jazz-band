
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

# Bass: Marcus - walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) -> Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),
    # Bar 3: A2 (fifth) -> Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.875),
    # Bar 4: D2 (root) -> Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=39, start=3.25, end=3.625),
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=2.0),  # C#
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5),  # F
])
# Bar 4: D7 (D-F#-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # C
])
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (67) -> A (70) -> D (62) (half note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.75),
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.75),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
