
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),    # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),    # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.75),     # Fm root (D2)
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0),     # Fm fifth (G2)
    pretty_midi.Note(velocity=80, pitch=37, start=2.0, end=2.25),     # Chromatic approach (C#2)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.5),     # Fm root (D2)
    
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.75),     # Fm root (F2)
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),     # Fm fifth (A2)
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),     # Chromatic approach (G#2)
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),     # Fm root (F2)
    
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.75),     # Fm root (D2)
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.0),     # Fm fifth (G2)
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25),     # Chromatic approach (F2)
    pretty_midi.Note(velocity=80, pitch=38, start=4.25, end=4.5),     # Fm root (D2)
    
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.75),     # Fm root (F2)
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0),     # Fm fifth (A2)
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),     # Chromatic approach (Bb2)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.5),     # Fm root (F2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),     # F (F4)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),     # Ab (Ab4)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),     # C (C5)
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.75),     # D (D5)
    
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.75),     # G (G4)
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),     # Bb (Bb4)
    pretty_midi.Note(velocity=90, pitch=59, start=2.5, end=2.75),     # D (D5)
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.75),     # F (F5)
    
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.75),     # C (C5)
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75),     # Eb (Eb5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),     # G (G5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),     # Bb (Bb5) – duplicate to ensure it's heard

    # Bar 4: Fm7 again (resolution)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),     # F (F4)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),     # Ab (Ab4)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),     # C (C5)
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.75),     # D (D5)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),     # G4 (start of motif)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),     # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),     # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),     # Bb4
    
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),     # C5 (return and finish)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),     # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),     # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),     # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),    # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),    # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.375),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
