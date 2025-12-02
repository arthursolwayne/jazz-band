
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # Eb2 on 3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 on 4
]

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4
    # G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F4
    # Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb4
    # Dm7 again, resolving
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C4
]

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F4 (start of motif)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # F4 (finish motif)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # G4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=2.875), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # A4 (finish)
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125), # Eb2 on 3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2 on 4
])

# Diane: Open voicings
piano_notes.extend([
    # G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F4
    # Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # Bb4
    # Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C4
    # G7 again
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # F4
])

# Dante: Continue motif with variation
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25), # G4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.375), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.375, end=4.5),  # A4 (finish)
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line
bass_notes.extend([
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # Eb2 on 3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2 on 4
])

# Diane: Open voicings
piano_notes.extend([
    # Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb4
    # Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C4
    # G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F4
    # Dm7 again, resolving
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C4
])

# Dante: Final variation of motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.25), # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.75), # G4 (return)
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=5.875), # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.875, end=6.0),  # A4 (finish)
])

# Drums: Bar 3-4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
])

# Add all notes to their respective instruments
for note in drum_notes:
    drums.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
