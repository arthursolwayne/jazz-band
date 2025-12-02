
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25), # Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=3.0), # Dm7 again on 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Dante: Melody (Dm scale with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75), # Dm7
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.5), # Dm7 again on 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # F
]
for note in bass_notes:
    bass.notes.append(note)

# Dante: Melody (Dm scale with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25), # Dm7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=6.0), # Dm7 again on 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Dante: Melody (Dm scale with a twist)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
