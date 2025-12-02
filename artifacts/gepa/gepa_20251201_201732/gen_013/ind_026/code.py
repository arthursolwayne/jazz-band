
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25), # F2 (fifth)
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2 (root)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # F2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D2
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # C2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - Eb4 - D4 (half note on D4, quarter on F4, eighth on Eb4, eighth on D4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=3.0),  # D4 (half note)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.75),  # F4 (quarter note)
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # Eb4 (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # D4 (eighth note)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5 + i*0.375 + 0.375, end=1.5 + i*0.375 + 0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.375, end=1.5 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.375 + 0.1875, end=1.5 + i*0.375 + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.375 + 0.375, end=1.5 + i*0.375 + 0.5625)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i*0.375 + 0.5625, end=1.5 + i*0.375 + 0.75)

# Bar 3
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0 + i*0.375 + 0.375, end=3.0 + i*0.375 + 0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.375, end=3.0 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.375 + 0.1875, end=3.0 + i*0.375 + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.375 + 0.375, end=3.0 + i*0.375 + 0.5625)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i*0.375 + 0.5625, end=3.0 + i*0.375 + 0.75)

# Bar 4
for i in range(4):
    pretty_midi.Note(velocity=100, pitch=36, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5 + i*0.375 + 0.375, end=4.5 + i*0.375 + 0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.375, end=4.5 + i*0.375 + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.375 + 0.1875, end=4.5 + i*0.375 + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.375 + 0.375, end=4.5 + i*0.375 + 0.5625)
    pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i*0.375 + 0.5625, end=4.5 + i*0.375 + 0.75)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
