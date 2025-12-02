
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F2, G2, Ab2, Bb2, etc.)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Bb2
    pretty_midi.Note(velocity=100, pitch=37, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Bb2
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Bb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings (Fm7, Bb7, Eb7, Ab7)
# Comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=1.875),  # Eb5
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F5
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Ab5
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # Bb5
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=4.875),  # D5
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax motif - short and haunting (F, Ab, Bb)
# Start on 1.5s (Bar 2), leave it hanging, come back and finish on 4.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Ab5
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Bb5
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F5
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    # Hihat every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
