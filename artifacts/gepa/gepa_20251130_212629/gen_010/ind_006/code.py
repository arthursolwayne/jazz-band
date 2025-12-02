
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif, ends on a held note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # D (held)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=54, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.25, end=3.5),  # A7
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0),  # A7
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.375),  # kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=bar + 0.75, end=bar + 1.125),  # snare on 2
        pretty_midi.Note(velocity=100, pitch=42, start=bar, end=bar + 1.5),    # hihat on every 8th
        pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.375, end=bar + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=bar + 0.75, end=bar + 1.125),
        pretty_midi.Note(velocity=100, pitch=42, start=bar + 1.125, end=bar + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=bar + 1.125, end=bar + 1.5),  # kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D (sustained)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # C#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp (7th chords on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=5.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
