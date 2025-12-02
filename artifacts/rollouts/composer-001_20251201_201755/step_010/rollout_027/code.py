
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) chromatic up to E2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),
    # Bar 3: A2 (fifth of D) chromatic down to G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.875),
    # Bar 4: D2 (root) chromatic up to E2
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=39, start=3.375, end=3.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),
    # Bar 4: Cmaj7 (C-E-G-B)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D-F#-G)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish the motif (D-F#-G)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
