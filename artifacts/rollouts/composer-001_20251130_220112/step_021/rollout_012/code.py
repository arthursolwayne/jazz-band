
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),  # Fm7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),
    # Bar 2, beat 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=61, start=2.5, end=2.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.0),  # Gb
    pretty_midi.Note(velocity=80, pitch=52, start=4.0, end=4.25),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),
    # Bar 3, beat 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=61, start=4.0, end=4.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0),  # F (held)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=6.0),  # Db
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),
    # Bar 4, beat 4: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=80, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=5.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("dante_intro.mid")
