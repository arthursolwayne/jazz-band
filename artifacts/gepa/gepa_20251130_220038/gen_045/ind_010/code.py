
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=44, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=45, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # Eb
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # F
    # Bar 4: A7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Whisper at first, then a cry. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_intro.mid")
