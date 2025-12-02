
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - short motif, start and leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # D3
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),   # E3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2 (1.875)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # B4
    # Bar 3: F7 on beat 2 (2.625)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F4
    pretty_midi.Note(velocity=90, pitch=68, start=2.625, end=3.0),   # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # C5
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # D#5
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue
drum_notes_bar3 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Bar 3: Sax continues, finish the motif
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D4
]

for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 3: Bass continues
bass_notes_bar3 = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F3
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # G3
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # A3
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5),   # B3
]

for note in bass_notes_bar3:
    bass.notes.append(note)

# Bar 3: Piano continues
piano_notes_bar3 = [
    # Bar 3: F7 on beat 2 (3.75)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),   # F4
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),   # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),   # C5
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),   # D#5
    # Bar 4: G7 on beat 2 (4.875)
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),   # D5
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),   # F#5
]

for note in piano_notes_bar3:
    piano.notes.append(note)

# Bar 4: Drums continue
drum_notes_bar4 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=95, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes_bar4:
    drums.notes.append(note)

# Bar 4: Sax continues
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D4
]

for note in sax_notes_bar4:
    sax.notes.append(note)

# Bar 4: Bass continues
bass_notes_bar4 = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # E3
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # F3
]

for note in bass_notes_bar4:
    bass.notes.append(note)

# Bar 4: Piano continues
piano_notes_bar4 = [
    # Bar 4: G7 on beat 2 (5.25)
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),   # D5
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625),   # F#5
]

for note in piano_notes_bar4:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
