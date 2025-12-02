
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drums_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875), # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.4375, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=2.8125), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.8125, end=3.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 1
    pretty_midi.Note(velocity=95, pitch=70, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.6875),  # C
    # Bar 2: G7 on 2
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=1.875, end=2.0625),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=1.875, end=2.0625),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=1.875, end=2.0625),  # F
    # Bar 2: Dm7 on 3
    pretty_midi.Note(velocity=95, pitch=70, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.4375),  # C
    # Bar 2: G7 on 4
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=2.625, end=2.8125),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=2.625, end=2.8125),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # E (Dm)
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.0625, end=2.25),  # F
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.8125), # G
    pretty_midi.Note(velocity=110, pitch=63, start=2.8125, end=3.0),   # F#
    # Bar 4: End with a question
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.5625, end=3.75),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.1875, end=3.375), # F#
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5625), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.9375, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.3125), # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.3125, end=4.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Dm7 on 1
    pretty_midi.Note(velocity=95, pitch=70, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.1875),  # C
    # Bar 3: G7 on 2
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=3.375, end=3.5625),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=3.375, end=3.5625),  # F
    # Bar 3: Dm7 on 3
    pretty_midi.Note(velocity=95, pitch=70, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=3.9375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.9375),  # C
    # Bar 3: G7 on 4
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.3125),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=4.125, end=4.3125),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=4.125, end=4.3125),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=4.125, end=4.3125),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue the motif, leave it hanging
sax_notes = [
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=110, pitch=63, start=3.5625, end=3.75),  # F#
    # Bar 4: End with a question
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=3.9375, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.3125, end=4.5),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=5.8125), # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=5.8125, end=6.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Dm7 on 1
    pretty_midi.Note(velocity=95, pitch=70, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.6875),  # C
    # Bar 4: G7 on 2
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=4.875, end=5.0625),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.0625),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=4.875, end=5.0625),  # F
    # Bar 4: Dm7 on 3
    pretty_midi.Note(velocity=95, pitch=70, start=5.25, end=5.4375),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.4375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.4375),  # C
    # Bar 4: G7 on 4
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=5.8125),  # G
    pretty_midi.Note(velocity=85, pitch=79, start=5.625, end=5.8125),  # B
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=75, pitch=74, start=5.625, end=5.8125),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: End with a question
sax_notes = [
    # Bar 4: End with a question
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # E
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.8125, end=6.0),   # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.8125, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]

for note in drums_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
