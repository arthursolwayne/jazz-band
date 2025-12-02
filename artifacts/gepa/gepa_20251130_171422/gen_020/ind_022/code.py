
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, space, rhythmic variation
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=64, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=64, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: chromatic walking, melodic
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=38, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.0),  # G#
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.25),  # A#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.625),  # C#
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=2.875),  # D#
    pretty_midi.Note(velocity=90, pitch=48, start=2.875, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=49, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5),  # G#
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=90, pitch=54, start=3.625, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=90, pitch=56, start=3.875, end=4.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=2.0),  # B (F7 chord)
    pretty_midi.Note(velocity=70, pitch=48, start=1.5, end=2.0),  # E
    pretty_midi.Note(velocity=70, pitch=44, start=1.5, end=2.0),  # A
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=80, pitch=53, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=70, pitch=48, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=70, pitch=44, start=2.0, end=2.5),  # A
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=70, pitch=48, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=70, pitch=44, start=2.5, end=3.0),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone: concise, emotive motif
sax_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # G
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # Bb
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
