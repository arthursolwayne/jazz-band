
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: start a motif, leave it hanging

# D7 chord = D F# A C#
# Motif: D, F#, A, F#, G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line with chromatic approaches
# D, E, F#, G, G#, A, B, C#, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=71, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=73, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=74, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7 on 2 (1.625 - 1.875)
# G7 on 4 (2.0 - 2.25)
piano_notes = [
    # D7 chord: D, F#, A, C#
    pretty_midi.Note(velocity=90, pitch=62, start=1.625, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.625, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.625, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.625, end=1.875),
    # G7 chord: G, B, D, F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=73, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: return to the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),   # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line with chromatic approaches
# D, E, F#, G, G#, A, B, C#, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=71, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=73, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=74, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.125),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7 on 2 (3.125 - 3.375)
# G7 on 4 (3.5 - 3.75)
piano_notes = [
    # D7 chord: D, F#, A, C#
    pretty_midi.Note(velocity=90, pitch=62, start=3.125, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.125, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.125, end=3.375),
    pretty_midi.Note(velocity=90, pitch=74, start=3.125, end=3.375),
    # G7 chord: G, B, D, F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=73, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: return to the motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),   # F#
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.125),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line with chromatic approaches
# D, E, F#, G, G#, A, B, C#, D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=64, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=70, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=71, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=73, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=74, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.625),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# D7 on 2 (4.625 - 4.875)
# G7 on 4 (5.0 - 5.25)
piano_notes = [
    # D7 chord: D, F#, A, C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.875),
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.625, end=4.875),
    # G7 chord: G, B, D, F#
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=73, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),     # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),     # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),     # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75),    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),     # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
