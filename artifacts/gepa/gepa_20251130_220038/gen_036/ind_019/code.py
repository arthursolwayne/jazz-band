
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: Fm7 -> Bb7
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),  # F
    # Bar 3: Bb7 -> Eb7
    pretty_midi.Note(velocity=90, pitch=41, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=40, start=2.375, end=2.5),  # D
    # Bar 4: Eb7 -> Am7
    pretty_midi.Note(velocity=90, pitch=37, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=35, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=90, pitch=36, start=2.875, end=3.0),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comps on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=73, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=85, pitch=71, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.0, end=2.25),  # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=85, pitch=74, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=2.75),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante): Melody
# Bar 2: Start the motif
# Bar 3: Develop it
# Bar 4: Resolve it

# Bar 2: Fm7 (F, Ab, C, Eb)
# Melody: F, Ab, E, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=95, pitch=66, start=1.625, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # C
    # Bar 3: Bb7 (Bb, D, F, Ab)
    # Melody: Bb, D, F
    pretty_midi.Note(velocity=105, pitch=73, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=95, pitch=71, start=2.375, end=2.5),  # F
    # Bar 4: Eb7 (Eb, G, Bb, D)
    # Melody: G, D
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=105, pitch=68, start=2.625, end=2.875),  # D
    # End on a rest
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
