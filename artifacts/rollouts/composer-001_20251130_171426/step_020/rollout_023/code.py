
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

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2 (1.5 - 3.0s)
# Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0), # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2 (1.5 - 3.0s)
# 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (2.25)
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # D
    # F7 on 4 (3.0)
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 2 (1.5 - 3.0s)
# Melody: F, Ab, Bb, D (motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=44, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=41, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=42, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (3.0 - 4.5s)
# Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5), # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3 (3.0 - 4.5s)
# 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (3.75)
    pretty_midi.Note(velocity=100, pitch=44, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # D
    # F7 on 4 (4.5)
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 3 (3.0 - 4.5s)
# Rest, leave it hanging
# No notes here

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (4.5 - 6.0s)
# Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875), # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0), # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4 (4.5 - 6.0s)
# 7th chords on 2 and 4
piano_notes = [
    # F7 on 2 (5.25)
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # D
    # F7 on 4 (6.0)
    pretty_midi.Note(velocity=100, pitch=44, start=6.0, end=6.375), # F
    pretty_midi.Note(velocity=90, pitch=49, start=6.0, end=6.375), # A
    pretty_midi.Note(velocity=90, pitch=50, start=6.0, end=6.375), # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=6.0, end=6.375), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 4 (4.5 - 6.0s)
# Return to complete the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=44, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=41, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=42, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0), # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
