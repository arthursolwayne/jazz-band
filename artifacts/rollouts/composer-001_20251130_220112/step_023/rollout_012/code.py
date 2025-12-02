
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
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=73, start=2.625, end=3.0),  # G#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=1.875, end=2.25),  # E
    # Bar 2, beat 4: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=3.0),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif (start on 3rd beat)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),   # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=3.375, end=3.75),  # E
    # Bar 3, beat 4: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.5),   # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=75, start=3.75, end=4.125),  # A#
    pretty_midi.Note(velocity=110, pitch=74, start=4.125, end=4.5),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # B#
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=4.875, end=5.25),  # E
    # Bar 4, beat 4: F7 (F A C E)
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=5.625, end=6.0),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=77, start=5.625, end=6.0),   # B
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3-4
# Kick on 1 and 3
drum_notes = [
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

midi.write("dante_intro.mid")
