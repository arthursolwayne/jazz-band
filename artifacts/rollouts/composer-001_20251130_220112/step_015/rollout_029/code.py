
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # G#
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),  # A#
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # D7 - F
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.875),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=1.875),  # D7 - C
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.375),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # D7 - F
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=76, start=3.0, end=3.375),  # D7 - C
    pretty_midi.Note(velocity=95, pitch=70, start=4.5, end=4.875),  # D7 - D
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # D7 - F
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875),  # D7 - A
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),  # D7 - C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),   # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # C
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
