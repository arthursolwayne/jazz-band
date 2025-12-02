
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

# Drums in Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D (return)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # D (end)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking in D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=45, start=2.75, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0),  # D7 again
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Saxophone motif again, transposed up a whole step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking in D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.5),  # D7 again
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Saxophone motif again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line (walking in D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=45, start=5.75, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D7 again
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in Bars 2-4
drum_notes = []

# Bar 2
for i in range(4):
    start = 1.5 + (i * 0.375)
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat

# Bar 3
for i in range(4):
    start = 3.0 + (i * 0.375)
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat

# Bar 4
for i in range(4):
    start = 4.5 + (i * 0.375)
    if i % 2 == 0:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))  # Kick
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))  # Hihat

for note in drum_notes:
    drums.notes.append(note)

# Add snare on 3 of each bar (1.75, 3.75, 5.75)
snare_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.125)
]

for note in snare_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
