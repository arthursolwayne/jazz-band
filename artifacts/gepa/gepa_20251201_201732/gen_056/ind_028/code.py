
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
    pretty_midi.Note(velocity=110, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=110, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=115, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=115, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# F - G - Bb - A - F - G - Bb - Ab
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7sus4 (F, Bb, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),   # Bb
    pretty_midi.Note(velocity=70, pitch=52, start=1.5, end=1.75),   # C
    pretty_midi.Note(velocity=70, pitch=51, start=1.5, end=1.75),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Start of the motif
# F (D4), Ab (E4), D (F4), rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F (D4)
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # Ab (E4)
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # D (F4)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: F - Bb - Eb - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=4.125, end=4.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bar 3: Bb7sus4 (Bb, D, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=70, pitch=53, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=70, pitch=55, start=3.0, end=3.25),   # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue the motif
# Bb (E4), F (D4), rest, rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: F - G - Bb - A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bar 4: F7sus4 (F, Bb, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=70, pitch=52, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=70, pitch=51, start=4.5, end=4.75),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish the motif
# F (D4), rest, rest, rest
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fill in bar 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=115, pitch=38, start=4.75, end=4.875),
    pretty_midi.Note(velocity=115, pitch=38, start=5.875, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
