
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # F#

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # Ab (chromatic)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # Bb (chromatic)

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # C (chromatic)
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),  # D (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D7: D, F#, A, C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - short, melodic, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F# (grace note)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Ab (chromatic twist)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Ab (ending on a question)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),

# Add the notes to the instruments
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),
])

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_shorter_intro.mid")
