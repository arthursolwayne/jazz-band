
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
    # Kick on beat 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on beat 2 and 4
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=70, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=70, pitch=51, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=70, pitch=53, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=70, pitch=55, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=70, pitch=57, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=70, pitch=58, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=70, pitch=59, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=70, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=70, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=70, pitch=64, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Kick on beat 1 and 3 of each bar
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on beat 2 and 4 of each bar
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),
    # Hi-hat on every eighth of each bar
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
