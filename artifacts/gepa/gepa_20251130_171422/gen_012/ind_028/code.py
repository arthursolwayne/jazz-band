
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Dm7 -> F7 -> Bb7 -> G7
# Dm7: D, F, A, C
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab
# G7: G, B, D, F
# Short motif: D -> F -> Bb -> G (melodic line, 4 notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
# Dm: D-F-A-C
# Walking line: D -> F -> A -> C -> D -> F -> A -> C (chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),  # D5 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Dm7 on 2: D, F, A, C
# G7 on 4: G, B, D, F
piano_notes = [
    # Dm7 on 2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # C5
    # G7 on 4 (beat 4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
# Dm: D-F-A-C
# Walking line: D -> F -> A -> C -> D -> F -> A -> C (chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # D5 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 on 2: F, A, C, E
# Bb7 on 4: Bb, D, F, Ab
piano_notes = [
    # F7 on 2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # E5
    # Bb7 on 4 (beat 4)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F5
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Ab4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif, but slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
# Dm: D-F-A-C
# Walking line: D -> F -> A -> C -> D -> F -> A -> C (chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=6.375, end=6.75),  # B4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=6.75, end=7.125),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=7.125, end=7.5),  # D5 (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# G7 on 2: G, B, D, F
# C7 on 4: C, E, G, B
piano_notes = [
    # G7 on 2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # D5
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # F5
    # C7 on 4 (beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=6.0, end=6.375),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=6.0, end=6.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.375),  # B4
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
