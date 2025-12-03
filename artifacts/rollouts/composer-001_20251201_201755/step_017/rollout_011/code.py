
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
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Bar 2: F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0),
    # Bar 2: G2 (43)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    # Bar 2: Bb2 (42)
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.75),
    
    # Bar 3: D2 (38)
    pretty_midi.Note(velocity=80, pitch=38, start=2.75, end=3.125),
    # Bar 3: F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=3.125, end=3.375),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75),
    # Bar 3: Bb2 (42)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    
    # Bar 4: D2 (38)
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
    # Bar 4: F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.75),
    # Bar 4: G2 (43)
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.125),
    # Bar 4: Bb2 (42)
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),
    
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.25),
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.25),
    
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.75),
    pretty_midi.Note(velocity=100, pitch=63, start=4.125, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif start (Dm scale: D-F-G)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),
    
    # Bar 3: Leave it hanging, no notes
    
    # Bar 4: Come back and finish it (A-Bb-D)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
drums.notes.extend(drum_notes[6:])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
