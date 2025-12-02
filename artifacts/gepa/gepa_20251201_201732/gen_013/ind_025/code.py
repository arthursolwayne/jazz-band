
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full band enters

# Bass - Bar 2 (F2, G2, A2, C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # G2 (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 2: Fmaj9 (F, A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (octave 3)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 2: Melody motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # Bb (F7)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # G (F7)
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # F (resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Full band

# Bass - Bar 3 (A2, Bb2, B2, C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Bb2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # A2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),  # Bb2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 3: Amaj7 (A, C#, E, G#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # A (octave 3)
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=4.5),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # G#
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 3: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # Bb (F7)
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125), # G (F7)
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),  # F (resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full band

# Bass - Bar 4 (C3, D3, Eb3, C3)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25), # D3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # C3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),  # D3
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - Bar 4: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=6.0),  # D (octave 3)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C#
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Bar 4: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25), # Bb (F7)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625), # G (F7)
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),  # F (resolution)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
