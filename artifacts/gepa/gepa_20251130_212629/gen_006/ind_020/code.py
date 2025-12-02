
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
# Sax motif: F (G7) -> A (Bb7) -> C (D7) -> Eb (E7)
# Start with F (G7) on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.75),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=87, start=1.75, end=2.0),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=89, start=2.0, end=2.25),  # C (D7)
    pretty_midi.Note(velocity=100, pitch=91, start=2.25, end=2.5),  # Eb (E7)
]

# Bass: Walking line in F
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # Bb
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=1.75, end=2.0),  # F
    # Bar 3: C7 on beat 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # B
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats the motif a third higher (F -> A -> C -> Eb)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=87, start=3.25, end=3.5),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=89, start=3.5, end=3.75),  # C (D7)
    pretty_midi.Note(velocity=100, pitch=91, start=3.75, end=4.0),  # Eb (E7)
])

# Bass: Walking line in F
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # Bb
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=77, start=3.25, end=3.5),  # Ab
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=4.0, end=4.25),  # E
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax repeats the motif a third higher (F -> A -> C -> Eb)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.75),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=87, start=4.75, end=5.0),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=89, start=5.0, end=5.25),  # C (D7)
    pretty_midi.Note(velocity=100, pitch=91, start=5.25, end=5.5),  # Eb (E7)
])

# Bass: Walking line in F
# F -> G -> A -> Bb -> C -> D -> Eb -> F
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.5),  # Bb
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # C
    # Bar 4: F7 on beat 4 (already covered)
])

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
