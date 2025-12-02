
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),   # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=1.0, end=1.375),    # Kick on 3 (syncopated)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif - short, melodic, with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),     # Fm7 - Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),     # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),     # G (tension)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),     # F (resolve)
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),     # D (suspense)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),     # F (return)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),     # Ab
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),     # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.75),     # D
    pretty_midi.Note(velocity=100, pitch=52, start=2.75, end=3.0),     # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),     # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: Same pattern but with a slight push
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),   # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),    # Kick on 3 (syncopated)
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),     # Fm7 - Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),     # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),     # G (tension)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),     # F (resolve)
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),     # D (suspense)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),     # F (return)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),     # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.25, end=3.5),     # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),     # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),     # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.0, end=4.25),     # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),     # Ab
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),     # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Same pattern but with a slightly delayed resolution
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),   # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375),    # Kick on 3 (syncopated)
]

for note in drum_notes:
    drums.notes.append(note)

# Sax: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),     # Fm7 - Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),     # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),     # G (tension)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),     # F (resolve)
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),     # D (suspense)
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),     # F (return)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.75),     # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),     # F
    pretty_midi.Note(velocity=100, pitch=47, start=5.0, end=5.25),     # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5),     # Ab
    pretty_midi.Note(velocity=100, pitch=53, start=5.5, end=5.75),     # D
    pretty_midi.Note(velocity=100, pitch=52, start=5.75, end=6.0),     # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),     # G7
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),     # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),     # D
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
