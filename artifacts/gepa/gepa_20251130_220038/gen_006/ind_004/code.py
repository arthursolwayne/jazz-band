
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Dm7 -> G7 -> Cm7 -> F7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G (G7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C (Cm7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F (F7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line starting on D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # Dm7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # Dm7: F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # Dm7: A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # Dm7: C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G7: G
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # G7: B
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=3.0),  # G7: D
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # G7: F
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif starting one half-step up
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb (Dm7 shifted up)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # A (G7 shifted up)
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),  # Bb (Cm7 shifted up)
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # E (F7 shifted up)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line starting on Eb
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),  # Ebm7: Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.75),  # Ebm7: G
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.75),  # Ebm7: Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # Ebm7: D
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # Am7: A
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # Am7: C
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),  # Am7: E
    pretty_midi.Note(velocity=100, pitch=75, start=4.125, end=4.5),  # Am7: G
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution — back to Dm7, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G (G7)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C (Cm7)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # F (F7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line starting on D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # Dm7: D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # Dm7: F
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # Dm7: A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # Dm7: C
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # G7: G
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # G7: B
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # G7: D
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),  # G7: F
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Bar start is the first beat of the bar
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),  # Hihat on 4

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
