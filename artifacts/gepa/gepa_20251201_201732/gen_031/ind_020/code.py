
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in F (D2 to G2, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Bb (E2)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # F (D#2)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # C (F2)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E (E5)

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # D (D5)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # F (F5, same as D5?)

    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # E (E5)
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # G (G5)
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # B (B5)
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # G (G4)

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F (F4)

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # G (G4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
