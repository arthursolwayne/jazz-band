
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
# Bass: Chromatic walking line on Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4, Dm7 chords
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.999), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.999), # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=2.999), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.999), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - D, E, F#, D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75), # D (rest for tension)
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.9375), # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.9375, end=3.125), # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.3125), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=3.3125, end=3.5), # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)
# Bass: Chromatic walking line on Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4, Dm7 chords
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.499), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.499), # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.499), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.499), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation - D, F#, D, Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=110, pitch=70, start=3.5625, end=3.75), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.3125, end=4.5), # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: Chromatic walking line on Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4, Dm7 chords
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.999), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.999), # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=5.999), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=5.999), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif resolution - D, Bb, D, G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=110, pitch=70, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.8125, end=6.0), # G
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
