
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
    # Hihat on every eighth
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
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Fm root (D2)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # Fm fifth (G2)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # Fm root (D2)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # Fm root (D2)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # Fm fifth (G2)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # Fm root (D2)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # Fm root (D2)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # Fm fifth (G2)
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625), # chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Fm root (D2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C
    
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # Ab
    
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(2):
    start = 1.5 + i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for j in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.1875, end=start + j * 0.1875 + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: First motif (1.5 - 2.25s)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # G (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E (Fm9)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D (Fm7)
    
    # Bar 3: Leave it hanging (2.25 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),  # G (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # E (Fm9)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D (Fm7)
    
    # Bar 4: Come back and finish it (3.0 - 3.75s)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # G (Fm3)
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # E (Fm9)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D (Fm7)
    
    # Bar 4: Resolution (3.75 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),  # F (Fm root)
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D (Fm7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # E (Fm9)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
