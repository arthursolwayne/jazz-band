
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Bass: D2 - G2 - A2 - C3, with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> G7 -> Cm7 -> F7
# Open voicings, resolve on the last chord
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),
    
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),
    
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # D4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Bass: F2 - A2 - C3 - D3
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: F7 -> Bb7 -> Eb7 -> Ab7
piano_notes = [
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),
    
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),
    
    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    
    # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve on the final note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # C4
]
sax.notes.extend(sax_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Bass: D2 - F2 - G2 - A2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
    
    # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    
    # Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),
    
    # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: One final note, for closure
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
