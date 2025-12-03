
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

# Drums - Bar 1
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

# Bass - Bar 2 (Walking line, roots and fifths with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625), # A (fifth)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # Bb (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2 (Open voicings, different chord each bar, resolve on the last)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 2 (Motif: F - G - Ab - A, with a rest on the last note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # G (fifth)
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # Ab (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3 (Open voicings)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=4.5),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 3 (Motif repeats, but with a variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bass - Bar 4 (Walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # G (fifth)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # F (root)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # Eb (chromatic approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4 (Open voicings, resolving on the last chord)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 4 (Motif again, but with resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
