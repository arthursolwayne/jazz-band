
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus plays a walking line in Dm, chromatic approach
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane comps on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante's motif (start it, leave it hanging, come back and finish it)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # G
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
