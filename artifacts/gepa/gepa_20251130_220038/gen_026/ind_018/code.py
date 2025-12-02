
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

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=51, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = []
# Bar 2 (1.5 - 3.0s)
# F7 (F, A, C, E)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875))
# Bar 3 (3.0 - 4.5s)
# B7 (B, D#, F#, A)
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=83, start=3.0, end=3.375))
# Bar 4 (4.5 - 6.0s)
# F7 again
piano_notes.append(pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875))
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # G#
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
