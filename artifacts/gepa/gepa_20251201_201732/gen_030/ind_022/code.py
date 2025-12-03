
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

# Bar 2: Full ensemble
# Diane: Cmaj7 (C-E-G-B) -> Fmaj7 (F-A-C-E) -> G7 (G-B-D-F) -> Am7 (A-C-E-G)
piano_notes = [
    # Bar 2: Cmaj7 (C-E-G-B)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.75), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.75), # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.75), # B

    # Bar 3: Fmaj7 (F-A-C-E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.75), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.0 + 0.75), # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.0 + 0.75), # E

    # Bar 4: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.75), # B
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.5 + 0.75), # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.5 + 0.75), # F

    # Bar 4: Am7 (A-C-E-G)
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.0 + 0.75), # A
    pretty_midi.Note(velocity=100, pitch=72, start=6.0, end=6.0 + 0.75), # C
    pretty_midi.Note(velocity=100, pitch=76, start=6.0, end=6.0 + 0.75), # E
    pretty_midi.Note(velocity=100, pitch=79, start=6.0, end=6.0 + 0.75), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Marcus: Walking bass line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D -> E -> F -> G
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.375), # D
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=1.875 + 0.375), # E
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.25 + 0.375), # F (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=2.625 + 0.375), # G

    # Bar 3: A -> B -> C -> D
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.0 + 0.375), # A
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.375 + 0.375), # B
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=3.75 + 0.375), # C (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.125 + 0.375), # D

    # Bar 4: F -> G -> A -> B
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.5 + 0.375), # F
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=4.875 + 0.375), # G
    pretty_midi.Note(velocity=100, pitch=45, start=5.25, end=5.25 + 0.375), # A
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=5.625 + 0.375), # B
]

for note in bass_notes:
    bass.notes.append(note)

# Dante: Tenor sax motif in D (D4-F4-G4-A4)
# Start with a short motif, leave it hanging, then come back to finish it
sax_notes = [
    # Bar 2: D4 -> F4 -> G4 -> A4 (start it)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5), # A4

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5), # D4 (repeat motif)
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.25), # A4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),

    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),    # Hihat on 8th
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),

    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),    # Hihat on 8th
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),

    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),   # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),    # Hihat on 8th
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
