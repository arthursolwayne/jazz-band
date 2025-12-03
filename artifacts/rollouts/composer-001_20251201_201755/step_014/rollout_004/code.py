
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Start of the melody
# Sax - short motif: D4, F4, G4, F4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line: D2, E2, F2, G2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=39, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=40, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Dm7 (F, A, D, G) open voicing, on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.625, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=1.625, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=1.625, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),    # F4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),    # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),    # D4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),    # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue the melody
# Sax - repeat the motif with a slight variation: D4, F4, G4, F4 (same)
for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line: A2, Bb2, B2, C2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Dm7 -> Gm7 (F, A, D, G -> Bb, D, G, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),     # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),     # D4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),     # G4
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),     # C5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Continue the melody
# Sax - repeat the motif again: D4, F4, G4, F4 (same)
for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line: D2, E2, F2, G2
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=39, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Gm7 -> Dm7 (Bb, D, G, C -> F, A, D, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=3.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=3.625, end=3.875),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=3.625, end=3.875),  # G4
    pretty_midi.Note(velocity=100, pitch=79, start=3.625, end=3.875),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),     # F4
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),     # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),     # D4
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),     # G4
]

for note in piano_notes:
    piano.notes.append(note)

# Drums - continue the same pattern
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
