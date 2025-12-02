
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.875)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=36, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=35, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=37, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=37, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=36, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=37, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=39, start=4.5, end=4.75),  # A#
    pretty_midi.Note(velocity=80, pitch=37, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=35, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=34, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=37, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=39, start=5.75, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # B
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # B
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # C#
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # C#
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=70, pitch=38, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=70, pitch=38, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=6.0),
    pretty_midi.Note(velocity=90, pitch=36, start=4.625, end=4.875),
    pretty_midi.Note(velocity=70, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=36, start=5.5, end=5.75),
    pretty_midi.Note(velocity=70, pitch=38, start=5.75, end=6.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
