
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # B (D7)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # D (D7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Bb (D7)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # E (D7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # B (D7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # D (D7)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),   # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),   # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),   # Db (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),   # D
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (bar 2: 2nd beat, bar 3: 2nd beat)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # B (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # F# (D7)
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.25),  # C# (D7)
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),  # A (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # B (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # F# (D7)
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # C# (D7)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A (D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but end on a different note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),   # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75),   # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),   # Db (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=4.0, end=4.25),   # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (bar 3: 2nd beat)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),  # B (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # F# (D7)
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75),  # C# (D7)
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),  # A (D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif, resolve on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),   # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),   # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),   # Db (chromatic)
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),   # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),   # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (bar 4: 2nd beat)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),  # B (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # F# (D7)
    pretty_midi.Note(velocity=90, pitch=72, start=5.0, end=5.25),  # C# (D7)
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # A (D7)
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 3-4
for bar in [3, 4]:
    start = (bar - 1) * 1.5
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125), # Snare on 2
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 1.5),     # Hihat on every 8th
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),  # Kick on 3
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
