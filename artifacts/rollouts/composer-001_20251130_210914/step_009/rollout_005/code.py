
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
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

# Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),  # C (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=2.5, end=2.75),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=2.75, end=3.0),  # C (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=3.25, end=3.5),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.75),  # C (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=4.0, end=4.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=4.25, end=4.5),  # C (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=4.75, end=5.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # C (3rd)
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D (root)
    pretty_midi.Note(velocity=80, pitch=63, start=5.5, end=5.75),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=5.75, end=6.0),  # C (3rd)
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4.
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=5.75, end=6.0),  # D7
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),  # F#
]

for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (64), B (69), D (62), B (69), F# (64), D (62)

# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo.mid")
