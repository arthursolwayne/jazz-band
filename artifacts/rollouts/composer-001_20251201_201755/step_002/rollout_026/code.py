
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano chords (open voicings, resolve on the last beat of the bar)
piano_notes = [
    # Bar 2: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=3.0),

    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=4.5),
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=4.5),

    # Bar 4: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=6.0),
    pretty_midi.Note(velocity=80, pitch=77, start=4.5, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums in Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Sax melody (Bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # E4
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # D4

    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # G4

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
