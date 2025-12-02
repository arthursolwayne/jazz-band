
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start on D (Dm7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=2.0),  # D
    # Dm7 on beat 4
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif, but with a twist
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.75),  # E#
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),  # D
    # Dm7 on beat 4
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: finish the motif and leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.5),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4 with 7th chords
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.0),  # D
    # Dm7 on beat 4
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
