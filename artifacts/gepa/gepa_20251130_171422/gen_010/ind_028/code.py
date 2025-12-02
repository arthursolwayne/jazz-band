
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bars 2-4 (1.5 - 6.0s)
# Start with sax melody
sax_notes = [
    # Bar 2: F7, Bb, A, G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75), # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5), # G
    # Bar 3: D, E, F
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0), # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25), # F
    # Bar 4: G, A, Bb, F
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0), # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F - Eb - D - C
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25), # D
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5), # C
    # Bar 3: Bb - A - G - F
    pretty_midi.Note(velocity=80, pitch=57, start=2.5, end=2.75), # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5), # F
    # Bar 4: Eb - D - C - Bb
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75), # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.25), # C
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.5), # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=57, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5), # F
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5), # F
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=58, start=2.75, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0), # C
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5), # C
    # Bar 4: Bb7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.25, end=4.5), # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5), # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.25, end=4.5), # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5), # A
]

for note in piano_notes:
    piano.notes.append(note)

# Add more drum fills in bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.25, end=3.625),
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=4.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=5.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
