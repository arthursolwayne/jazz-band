
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D (D4) -> F#4 -> B4 -> D5 (whisper to cry)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),  # D3
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=45, start=2.0, end=2.25),  # F3
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.5),  # G3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (D7, Bm7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),  # Bm7
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: C#4 -> A4 -> F#4 -> D4 (variation, build)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),  # C#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # F3
    pretty_midi.Note(velocity=90, pitch=46, start=3.25, end=3.5),  # G3
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # A3
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),  # Bb3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (G7, Dm7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G7
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # Dm7
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: D4 -> F#4 -> B4 -> D5 (return to the opening motif, finished)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D5
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # D3
    pretty_midi.Note(velocity=90, pitch=43, start=4.75, end=5.0),  # Eb3
    pretty_midi.Note(velocity=90, pitch=45, start=5.0, end=5.25),  # F3
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.5),  # G3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (D7, Bm7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=66, start=5.25, end=5.5),  # Bm7
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
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

# Save the MIDI file
midi.write("dante_intro.mid")
