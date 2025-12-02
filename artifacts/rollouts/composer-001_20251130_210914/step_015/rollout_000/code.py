
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
    pretty_midi.Note(note_number=36, start=0.0, end=0.375),
    pretty_midi.Note(note_number=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(note_number=38, start=0.75, end=1.125),
    pretty_midi.Note(note_number=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(note_number=42, start=0.0, end=0.375),
    pretty_midi.Note(note_number=42, start=0.375, end=0.75),
    pretty_midi.Note(note_number=42, start=0.75, end=1.125),
    pretty_midi.Note(note_number=42, start=1.125, end=1.5),
    pretty_midi.Note(note_number=42, start=1.5, end=1.875),
    pretty_midi.Note(note_number=42, start=1.875, end=2.25),
    pretty_midi.Note(note_number=42, start=2.25, end=2.625),
    pretty_midi.Note(note_number=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(note_number=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(note_number=70, start=1.875, end=2.25),  # F#
    pretty_midi.Note(note_number=68, start=2.25, end=2.625),  # E
    pretty_midi.Note(note_number=71, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(note_number=72, start=3.0, end=3.375),   # G
    pretty_midi.Note(note_number=73, start=3.375, end=3.75),   # G#
    pretty_midi.Note(note_number=71, start=3.75, end=4.125),   # G
    pretty_midi.Note(note_number=74, start=4.125, end=4.5),    # A
    # Bar 4
    pretty_midi.Note(note_number=74, start=4.5, end=4.875),    # A
    pretty_midi.Note(note_number=75, start=4.875, end=5.25),    # A#
    pretty_midi.Note(note_number=73, start=5.25, end=5.625),    # G#
    pretty_midi.Note(note_number=76, start=5.625, end=6.0),     # Bb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(note_number=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(note_number=76, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(note_number=71, start=1.5, end=1.875),  # G
    pretty_midi.Note(note_number=74, start=1.5, end=1.875),  # A
    # Bar 3
    pretty_midi.Note(note_number=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(note_number=76, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(note_number=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(note_number=74, start=3.0, end=3.375),  # A
    # Bar 4
    pretty_midi.Note(note_number=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(note_number=76, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(note_number=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(note_number=74, start=4.5, end=4.875),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (start at 1.5s)
    pretty_midi.Note(note_number=71, start=1.5, end=1.75),  # G
    pretty_midi.Note(note_number=74, start=1.75, end=2.0),   # A
    pretty_midi.Note(note_number=71, start=2.0, end=2.25),   # G
    pretty_midi.Note(note_number=76, start=2.25, end=2.5),   # Bb
    # Bar 3 (start at 3.0s)
    pretty_midi.Note(note_number=71, start=3.0, end=3.25),   # G
    pretty_midi.Note(note_number=74, start=3.25, end=3.5),   # A
    pretty_midi.Note(note_number=71, start=3.5, end=3.75),   # G
    pretty_midi.Note(note_number=76, start=3.75, end=4.0),   # Bb
    # Bar 4 (start at 4.5s)
    pretty_midi.Note(note_number=71, start=4.5, end=4.75),   # G
    pretty_midi.Note(note_number=74, start=4.75, end=5.0),   # A
    pretty_midi.Note(note_number=71, start=5.0, end=5.25),   # G
    pretty_midi.Note(note_number=76, start=5.25, end=5.5),   # Bb
    pretty_midi.Note(note_number=74, start=5.5, end=5.75),   # A
    pretty_midi.Note(note_number=71, start=5.75, end=6.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
