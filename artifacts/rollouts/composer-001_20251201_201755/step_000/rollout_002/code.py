
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (2nd beat has chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=52, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=50, start=2.375, end=2.625),
    # Bar 3: A (2nd beat has chromatic approach)
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=56, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.625),
    # Bar 4: D (2nd beat has chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=49, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.375),
    pretty_midi.Note(velocity=100, pitch=50, start=4.375, end=4.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Bar 3: Am7 (A-C-E-G)
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),
    # Bar 4: D7 (D-F#-A-C)
    pretty_midi.Note(velocity=100, pitch=50, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=53, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=57, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50) - F# (53) - A (57) - D (50), played over 1.5 to 2.625
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=53, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=57, start=1.75, end=1.875),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=2.75),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
