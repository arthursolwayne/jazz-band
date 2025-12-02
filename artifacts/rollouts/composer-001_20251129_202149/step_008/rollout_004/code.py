
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.6875, end=1.875), # Db
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.0625, end=2.25), # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords, on 2 and 4)
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.75),
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone continues motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75), # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=100, pitch=57, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75), # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano continues comp
piano_notes = [
    # Bar 3: C7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone finishes motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bass line continues
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano continues comp
piano_notes = [
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums continue (Bar 2-4)
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=1.9375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.6875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125), # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.4375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.1875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125), # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=4.9375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.6875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625), # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125), # Hihat on 1
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
