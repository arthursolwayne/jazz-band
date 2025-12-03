
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),
    # Bar 3: A2 (root), B2 (chromatic approach), D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=46, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.5),
    # Bar 4: D2 (root), F#2 (chromatic approach), G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=40, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=2.0),
    pretty_midi.Note(velocity=70, pitch=57, start=1.5, end=2.0),
    # Bar 3: A7 (A-C#-E-G)
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=70, pitch=64, start=2.5, end=3.0),
    # Bar 4: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=4.0),
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=4.0),
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=4.0),
    pretty_midi.Note(velocity=70, pitch=57, start=3.5, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
