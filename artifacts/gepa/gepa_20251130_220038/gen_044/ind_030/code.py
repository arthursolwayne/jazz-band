
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

## Bass: Walking line, chromatic approaches, no repeats
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

## Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C
    # Bar 3: G7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625),  # F
    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

## Sax: Whisper, then cry — one short motif, leave it hanging, come back and finish it

# Bar 2: Dm7, start with a whisper
sax_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=70, pitch=65, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=70, pitch=62, start=1.75, end=1.875),  # D
    # Bar 3: G7, leave it hanging
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.625),   # D
    # Bar 4: Cm7, finish the motif
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25), # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375), # C
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
