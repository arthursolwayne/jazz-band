
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full band enters (1.5 - 3.0s)
# Sax: short motif starting on D (D4=62) with chromatic approach
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # C4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D4 (main note)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # E4 (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4 (hang)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C4 (resolve)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D4 (end)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in D minor (D, F, G, A)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=2.125, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),  # A4
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # A4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, D7 (D, F#, A, C) and G7 (G, B, D, F)
# Bar 2: D7 on 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C4
]

# Bar 3: G7 on 2 (2.25s)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F4
])

# Bar 4: D7 on 2 (3.25s)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C4
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Sax continues (3.0 - 4.5s)
# Repeat the motif with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass continues walking line (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.25),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),  # A4
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.625, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),  # A4
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.125),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.25),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=4.375, end=4.5),  # A4
]

for note in bass_notes:
    bass.notes.append(note)

# Piano continues 7th chords on 2 and 4 (Bar 4: G7 on 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_russo_intro.mid')
