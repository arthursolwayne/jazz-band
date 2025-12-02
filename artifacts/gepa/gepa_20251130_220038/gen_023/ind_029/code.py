
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
    # Hi-hat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),   # A#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - comp on 2 and 4, 7th chords
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=95, pitch=59, start=1.875, end=2.25),  # E7
    pretty_midi.Note(velocity=95, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),
    # Bar 2, beat 4
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),   # Bb7
    pretty_midi.Note(velocity=95, pitch=68, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0),
    # Bar 3, beat 2
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # Bb7
    pretty_midi.Note(velocity=95, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),
    # Bar 3, beat 4
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),   # Bb7
    pretty_midi.Note(velocity=95, pitch=68, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=70, start=4.125, end=4.5),
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),
    # Bar 4, beat 2
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # Bb7
    pretty_midi.Note(velocity=95, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25),
    # Bar 4, beat 4
    pretty_midi.Note(velocity=95, pitch=59, start=5.625, end=6.0),   # E7
    pretty_midi.Note(velocity=95, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - short motif, one phrase, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # A
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
