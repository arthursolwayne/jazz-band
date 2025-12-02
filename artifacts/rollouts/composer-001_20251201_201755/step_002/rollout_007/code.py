
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: Fm7 -> Bb7 -> Eb7 -> Am7 (Fm key)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F# (Fm7)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.25),  # D (Eb7)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # C (Am7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Ab, Bb, Db)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.5),  # Db
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving on bar 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # D

    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G

    # Bar 4: Am7
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=73, start=2.5, end=2.75),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (3.0 - 6.0s)
# Sax continues motif (one more phrase)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F# (Fm7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.75),  # D (Eb7)
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),  # C (Am7)
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F# (Fm7)
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # E (Bb7)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),  # D (Eb7)
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),  # C (Am7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm (F, Ab, Bb, Db) again
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # Db
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolving on bar 4
piano_notes = [
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G

    # Bar 4: Am7
    pretty_midi.Note(velocity=100, pitch=77, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=73, start=3.5, end=3.75),  # E

    # Bar 4: Resolve with a diminished chord
    pretty_midi.Note(velocity=100, pitch=73, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
