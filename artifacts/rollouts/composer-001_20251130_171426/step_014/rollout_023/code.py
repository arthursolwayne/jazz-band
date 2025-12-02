
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice.
# Dm7 = D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D (chromatic approach on downbeats)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 2
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 chord: D F A C
# Motif: D -> F -> A -> C -> A -> F -> D (descending 3rds, then resolve)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.0625, end=2.25),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625), # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add remaining drum hits
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),   # Kick
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.25),  # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=70, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=70, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=70, pitch=42, start=2.625, end=3.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),   # Kick
    pretty_midi.Note(velocity=95, pitch=38, start=3.375, end=3.75),  # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=70, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=70, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=70, pitch=42, start=4.125, end=4.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),   # Kick
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.25),  # Snare
    pretty_midi.Note(velocity=70, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=70, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=70, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=70, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
