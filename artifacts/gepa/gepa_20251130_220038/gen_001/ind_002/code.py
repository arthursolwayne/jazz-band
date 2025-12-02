
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
    # Bar 1
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

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25), # Gb (chromatic)
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625), # G (3rd)
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # Ab (4th)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=54, start=1.5, end=1.875),  # F7 (Bb)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # F7 (G)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # F7 (C)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=54, start=2.25, end=2.625), # F7 (Bb)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # F7 (F)
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # F7 (G)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # F7 (C)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.375),  # F7 (Bb)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # F7 (F)
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # F7 (G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F7 (C)
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - short, singable, and hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Finalize
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
