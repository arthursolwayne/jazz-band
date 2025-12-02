
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F#4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),   # D3
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25),  # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),   # F3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=70, pitch=67, start=1.5, end=1.875),  # A4 (D7)
    pretty_midi.Note(velocity=70, pitch=64, start=1.5, end=1.875),  # F4 (D7)
    pretty_midi.Note(velocity=70, pitch=69, start=1.5, end=1.875),  # C#5 (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # A4 (D7)
    pretty_midi.Note(velocity=70, pitch=64, start=2.25, end=2.625), # F4 (D7)
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.625), # C#5 (D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but shift up a half step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # B4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.375),   # F3
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75),  # F#3
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # G3
    pretty_midi.Note(velocity=80, pitch=51, start=4.125, end=4.5),   # G#3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.375),  # B4 (E7)
    pretty_midi.Note(velocity=70, pitch=66, start=3.0, end=3.375),  # G4 (E7)
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),  # D5 (E7)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # E4
    pretty_midi.Note(velocity=70, pitch=69, start=3.75, end=4.125), # B4 (E7)
    pretty_midi.Note(velocity=70, pitch=66, start=3.75, end=4.125), # G4 (E7)
    pretty_midi.Note(velocity=70, pitch=71, start=3.75, end=4.125), # D5 (E7)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif again, but end on a suspended note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F#4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),   # D3
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # E3
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # F3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.875),  # A4 (D7)
    pretty_midi.Note(velocity=70, pitch=64, start=4.5, end=4.875),  # F4 (D7)
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),  # C#5 (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.625), # A4 (D7)
    pretty_midi.Note(velocity=70, pitch=64, start=5.25, end=5.625), # F4 (D7)
    pretty_midi.Note(velocity=70, pitch=69, start=5.25, end=5.625), # C#5 (D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
drum_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    # Bar 4 (4.5 - 6.0s)
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
