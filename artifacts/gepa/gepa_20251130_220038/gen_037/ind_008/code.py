
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # D
    # Bar 4: Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D
    # Fills on 2 and 4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),   # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # Bb
    # Bar 3: Develop the motif
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # Bb
    # Bar 4: Resolve with tension
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.25, end=4.5),  # D
    # End with a whisper
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.75, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 2
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_moment.mid")
