
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

# Bass line (Marcus) - Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A (fifth)
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # F (root)
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25), # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # A (fifth)
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab (E4)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D (G4)
    
    # Bar 3 (3.0 - 4.5s) - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb (D4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D (F4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F (E4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab (E4)
    
    # Bar 4 (4.5 - 6.0s) - Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Eb (D#4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb (F4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # D (F4)
]
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25),  # A (A4)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # G (G4)
    
    # Bar 3 (3.0 - 4.5s) - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75),  # A (A4)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),  # G (G4)
    
    # Bar 4 (4.5 - 6.0s) - Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=70, start=4.875, end=5.25),  # A (A4)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # G (G4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
