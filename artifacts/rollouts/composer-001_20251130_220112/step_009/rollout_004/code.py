
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=105, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=105, pitch=68, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=105, pitch=69, start=3.0, end=3.375),  # A#
    # Bar 3
    pretty_midi.Note(velocity=105, pitch=70, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=105, pitch=68, start=4.5, end=4.875),  # A
    # Bar 4
    pretty_midi.Note(velocity=105, pitch=66, start=5.25, end=5.625),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    # Hi-hat throughout
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_intro.mid')
