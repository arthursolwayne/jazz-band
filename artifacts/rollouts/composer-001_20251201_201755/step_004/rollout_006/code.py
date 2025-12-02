
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), E2 (chromatic), F2 (fifth), D2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
]

# Piano: Open voicings, different chord each bar
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C#4
]

# Sax: Motif starts
# D4, F#4, Bb4, D4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 3: Bb2 (chromatic), C2 (root), D2 (fifth), Bb2
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),
]

# Piano: Open voicings, different chord each bar
# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75),  # Ab4
]

# Sax: Motif continues
# Bb4, D4, F4, Bb4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 4: F2 (root), G2 (chromatic), A2 (fifth), F2
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),
]

# Piano: Open voicings, different chord each bar
# Bar 4: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # E4
]

# Sax: Motif ends
# F4, A4, C5, F4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
