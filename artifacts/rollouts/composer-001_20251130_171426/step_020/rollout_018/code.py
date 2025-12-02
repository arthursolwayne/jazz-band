
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante)
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G
    # Bar 3: Motif repeats
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G
    # Bar 4: Motif resolves
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes_bars2_4 = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare 4
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes_bars2_4:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
