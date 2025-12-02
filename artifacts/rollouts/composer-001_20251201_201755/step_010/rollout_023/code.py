
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass) - Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25), # F (3rd)
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.625), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2 (root)
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (Piano) - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D F Ab C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # C5
    
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # F5
    
    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Dante (Sax) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb4
    
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # A4 (finish)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
