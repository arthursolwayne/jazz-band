
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

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus) – walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # Eb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),   # Eb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) – 7th chords on 2 and 4, comping
# Bar 2: Dm7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=95, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # F
    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # F
    # Bar 4: Dm7 on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) – melody: whisper to cry
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.25),   # Bb
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # C
    # Bar 4: Resolve the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.125),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save as MIDI file
midi.write("dante_intro.mid")
