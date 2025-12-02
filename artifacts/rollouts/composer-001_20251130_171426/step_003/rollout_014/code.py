
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    # Root on 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # b9 on 2
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    # b5 on 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    # 7 on 4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    # B7 on 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),
    # D7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in D minor, short and singable
sax_notes = [
    # D (62) on 1
    pretty_midi.Note(velocity=115, pitch=62, start=1.5, end=1.75),
    # F (65) on 2
    pretty_midi.Note(velocity=115, pitch=65, start=1.875, end=2.125),
    # Bb (67) on 3
    pretty_midi.Note(velocity=115, pitch=67, start=2.25, end=2.5),
    # D (62) on 4
    pretty_midi.Note(velocity=115, pitch=62, start=2.625, end=2.875),
    # D (62) on 4 (sustain)
    pretty_midi.Note(velocity=115, pitch=62, start=2.875, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    # Root on 1
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # b9 on 2
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),
    # b5 on 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    # 7 on 4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    # F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),
    # B7 on 3
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.125),
    # D7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in D minor, chromatic approaches
bass_notes = [
    # Root on 1
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    # b9 on 2
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
    # b5 on 3
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),
    # 7 on 4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 1
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    # F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    # B7 on 3
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=5.625),
    # D7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif continuation, resolving on D
sax_notes = [
    # F (65) on 1
    pretty_midi.Note(velocity=115, pitch=65, start=4.5, end=4.75),
    # Bb (67) on 2
    pretty_midi.Note(velocity=115, pitch=67, start=4.875, end=5.125),
    # D (62) on 3
    pretty_midi.Note(velocity=115, pitch=62, start=5.25, end=5.5),
    # D (62) on 4
    pretty_midi.Note(velocity=115, pitch=62, start=5.625, end=5.875),
    # D (62) on 4 (sustain)
    pretty_midi.Note(velocity=115, pitch=62, start=5.875, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
