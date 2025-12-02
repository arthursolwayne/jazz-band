
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)
# SAX: Tenor sax melody in Dm, one short motif, start it, leave it hanging, finish it
# Dm7: D F A C
sax_notes = [
    # Bar 2: D (D4), F (F4), Bb (Bb4), D (D4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D4

    # Bar 3: A (A4), C (C5), E (E4), A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # A4

    # Bar 4: D (D4), F (F4), D (D4), C (C4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C4
]

for note in sax_notes:
    sax.notes.append(note)

# BASS: Marcus, walking line, chromatic approaches, no repeated notes
# Dm7: D F A C
bass_notes = [
    # Bar 2: D, Eb, F, G
    pretty_midi.Note(velocity=70, pitch=45, start=1.5, end=1.875),  # D3
    pretty_midi.Note(velocity=70, pitch=46, start=1.875, end=2.25),  # Eb3
    pretty_midi.Note(velocity=70, pitch=47, start=2.25, end=2.625),  # F3
    pretty_midi.Note(velocity=70, pitch=48, start=2.625, end=3.0),   # G3

    # Bar 3: A, Bb, C, D
    pretty_midi.Note(velocity=70, pitch=49, start=3.0, end=3.375),  # A3
    pretty_midi.Note(velocity=70, pitch=50, start=3.375, end=3.75),  # Bb3
    pretty_midi.Note(velocity=70, pitch=51, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=70, pitch=52, start=4.125, end=4.5),   # D4

    # Bar 4: Eb, F, G, A
    pretty_midi.Note(velocity=70, pitch=53, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=70, pitch=54, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=70, pitch=55, start=5.25, end=5.625),  # G4
    pretty_midi.Note(velocity=70, pitch=56, start=5.625, end=6.0),   # A4
]

for note in bass_notes:
    bass.notes.append(note)

# PIANO: Diane, 7th chords, comp on 2 and 4
# Dm7: D F A C
piano_notes = [
    # Bar 2: Dm7 on 2 & 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # C5

    # Bar 3: Dm7 on 2 & 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.25),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.875, end=4.25),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=5.375, end=5.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=5.375, end=5.75),  # C5

    # Bar 4: Dm7 on 2 & 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C5
    pretty_midi.Note(velocity=90, pitch=62, start=6.375, end=6.75),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=6.375, end=6.75),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=6.375, end=6.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=6.375, end=6.75),  # C5
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
