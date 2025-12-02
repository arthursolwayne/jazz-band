
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4 (next bar)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) -> F2 (MIDI 41) -> G2 (MIDI 43) -> C2 (MIDI 36) -> D2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4 (octave down)
    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # F4
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Bb4
    # F7: F, A, C, E
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # C4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # E4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First phrase: D4, F4, G4, D4 (start at 1.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    # Leave it hanging
    # Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 41) -> A2 (MIDI 45) -> B2 (MIDI 46) -> E2 (MIDI 40)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: G7 -> Cm7 -> F7 -> Dm7
piano_notes = [
    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F4
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    # F7: F, A, C, E
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # E4
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # C4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) -> F2 (MIDI 41) -> G2 (MIDI 43) -> C2 (MIDI 36)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 -> G7 -> Cm7 -> F7
piano_notes = [
    # Dm7: D, F, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C4
    # G7: G, B, D, F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # F4
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
    # F7: F, A, C, E
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # E4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
