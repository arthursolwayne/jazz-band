
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - F, Ab, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # D
]

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5),  # A
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # Eb
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but with a slight variation
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # D
]

# Bass: Walking line in F
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # A
]

# Piano: 7th chords on 2 and 4
piano_notes += [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # Eb
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif with a resolution
sax_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # D
]

# Bass: Walking line in F
bass_notes += [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5),  # A
]

# Piano: 7th chords on 2 and 4
piano_notes += [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),  # Eb
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Drums for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(2):
    for note in drum_notes:
        new_note = note.copy()
        new_note.start += 1.5
        new_note.end += 1.5
        drums.notes.append(new_note)

# Bar 3 (3.0 - 4.5s)
for i in range(2):
    for note in drum_notes:
        new_note = note.copy()
        new_note.start += 3.0
        new_note.end += 3.0
        drums.notes.append(new_note)

# Bar 4 (4.5 - 6.0s)
for i in range(2):
    for note in drum_notes:
        new_note = note.copy()
        new_note.start += 4.5
        new_note.end += 4.5
        drums.notes.append(new_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
