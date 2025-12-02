
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Start motif (F7 -> Ab7 -> Bb7 -> D7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=1.6875, end=1.875), # Ab7
    pretty_midi.Note(velocity=100, pitch=81, start=1.875, end=2.0625), # Bb7
    pretty_midi.Note(velocity=100, pitch=86, start=2.0625, end=2.25), # D7
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=80, pitch=58, start=2.0625, end=2.25), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.4375, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=2.8125), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.8125, end=3.0), # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: 2nd beat (start=1.875)
piano_notes = [
    # F7 chord: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.0625), # Eb
    # Bar 3: 2nd beat (start=2.8125)
    pretty_midi.Note(velocity=90, pitch=53, start=2.8125, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=58, start=2.8125, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.8125, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.8125, end=3.0), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Repeat motif but leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.1875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=3.1875, end=3.375), # Ab7
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.5625), # Bb7
    pretty_midi.Note(velocity=100, pitch=86, start=3.5625, end=3.75), # D7
    # Leave it hanging on the D7
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=4.5), # D7
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=80, pitch=58, start=3.5625, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=3.9375), # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.9375, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.3125), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=4.3125, end=4.5), # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3: 2nd beat (start=3.8125)
piano_notes = [
    # F7 chord: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=53, start=3.8125, end=4.0), # F
    pretty_midi.Note(velocity=90, pitch=58, start=3.8125, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.8125, end=4.0), # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.8125, end=4.0), # Eb
    # Bar 4: 2nd beat (start=4.8125)
    pretty_midi.Note(velocity=90, pitch=53, start=4.8125, end=5.0), # F
    pretty_midi.Note(velocity=90, pitch=58, start=4.8125, end=5.0), # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.8125, end=5.0), # C
    pretty_midi.Note(velocity=90, pitch=63, start=4.8125, end=5.0), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.6875),  # F7
    pretty_midi.Note(velocity=100, pitch=80, start=4.6875, end=4.875), # Ab7
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.0625), # Bb7
    pretty_midi.Note(velocity=100, pitch=86, start=5.0625, end=5.25), # D7
    # Finish on a strong note (C)
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=6.0), # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=58, start=5.0625, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=5.8125), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=5.8125, end=6.0), # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4: 2nd beat (start=5.8125)
piano_notes = [
    # F7 chord: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=53, start=5.8125, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=58, start=5.8125, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.8125, end=6.0), # C
    pretty_midi.Note(velocity=90, pitch=63, start=5.8125, end=6.0), # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
