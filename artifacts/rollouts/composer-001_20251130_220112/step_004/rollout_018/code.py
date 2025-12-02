
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

# Bar 2: Everyone in
# Saxophone: Dm7 (D F A C) - motif: D, F, A, F, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),
]

# Bass: walking line in Dm
# D -> C -> Bb -> A -> G -> F -> E -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=58, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=60, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5),
]

# Piano: Dm7 comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),
    # Bar 2, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),
]

# Bar 3: Saxophone continues motif
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=65, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
])

# Bass: walking line in Dm
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=58, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=65, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=60, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5),
])

# Piano: Dm7 comp on 2 and 4
piano_notes.extend([
    # Bar 3, beat 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875),
    # Bar 3, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),
])

# Bar 4: Saxophone ends motif
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=65, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
])

# Bass: walking line in Dm
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=60, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=65, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=59, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=62, start=4.375, end=4.5),
])

# Piano: Dm7 comp on 2 and 4
piano_notes.extend([
    # Bar 4, beat 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),
    # Bar 4, beat 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375),
])

# Add all notes to respective instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
