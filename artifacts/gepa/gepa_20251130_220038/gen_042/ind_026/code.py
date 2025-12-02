
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody - start with a whisper, build tension
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=85, pitch=72, start=1.75, end=2.0),

    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=85, pitch=72, start=2.75, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax melody - build tension and emotion
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=85, pitch=72, start=3.25, end=3.5),

    pretty_midi.Note(velocity=85, pitch=62, start=4.25, end=4.5),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=85, pitch=72, start=4.25, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Drum fill in bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),     # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax melody - resolve with emotional clarity
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=95, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=95, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=5.75, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass - walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=80, pitch=48, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=85, pitch=72, start=4.75, end=5.0),

    pretty_midi.Note(velocity=85, pitch=62, start=5.75, end=6.0),  # D7
    pretty_midi.Note(velocity=85, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=85, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=85, pitch=72, start=5.75, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drum fill in bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),     # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
