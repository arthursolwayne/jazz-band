
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G#
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C#
    # Bar 3, beat 2: G7
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # D#
    # Bar 4, beat 2: Am7
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),   # A
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3 of each bar
kick_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in kick_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
