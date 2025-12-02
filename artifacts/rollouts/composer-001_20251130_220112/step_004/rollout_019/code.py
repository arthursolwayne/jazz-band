
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Ab

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # B

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # C

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - Motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes_continued = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),  # Hi-hat

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),  # Hi-hat

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),  # Hi-hat
]
for note in drum_notes_continued:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
