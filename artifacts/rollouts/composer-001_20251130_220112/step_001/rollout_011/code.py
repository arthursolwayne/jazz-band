
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # Ab
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),   # F#
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=57, start=1.5, end=1.875),   # F7 - F
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.875),   # F7 - A
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),   # F7 - C
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),   # F7 - Eb
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),   # F7 - Eb
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),   # F7 - A
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),   # F7 - C
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),   # F7 - Eb
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),   # F7 - Eb
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.875),   # F7 - A
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),   # F7 - C
    pretty_midi.Note(velocity=95, pitch=78, start=4.5, end=4.875),   # F7 - Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, first two notes of motif (F, Ab)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Bar 3, leave it hanging (no notes)
    # Bar 4, come back and finish (Ab, F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
