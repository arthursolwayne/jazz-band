
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with a motif
# F (F4), G (G4), A (A4), Bb (Bb4), C (C5), D (D5), Eb (Eb5), F (F5)
# Start on F, move up slowly, build tension

# Bar 2 (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),   # F4
    pretty_midi.Note(velocity=100, pitch=73, start=1.625, end=1.75),  # G4
    pretty_midi.Note(velocity=100, pitch=75, start=1.875, end=2.0),   # A4
    pretty_midi.Note(velocity=100, pitch=76, start=2.125, end=2.25),  # Bb4
]

# Bar 3 (3.0 - 4.5s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.125),   # C5
    pretty_midi.Note(velocity=100, pitch=79, start=3.125, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=3.375, end=3.5),   # Eb5
    pretty_midi.Note(velocity=100, pitch=82, start=3.625, end=3.75),  # F5
])

# Bar 4 (4.5 - 6.0s)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.625),   # C5 (rest before)
    pretty_midi.Note(velocity=100, pitch=75, start=4.625, end=4.75),  # A4
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.0),   # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.125, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5),   # F4 again
])

for note in sax_notes:
    sax.notes.append(note)

# Marcus (Bass) - Walking line with chromatic approaches
# Bar 2 (F, G, Ab, A, Bb, B, C, Db)
# Bar 3 (C, D, Eb, E, F, F#, G, Ab)
# Bar 4 (G, A, Bb, B, C, C#, D, Eb)
# All notes in F minor, walking line with chromatic approach

bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.625),  # F3
    pretty_midi.Note(velocity=80, pitch=55, start=1.625, end=1.75),  # G3
    pretty_midi.Note(velocity=80, pitch=56, start=1.875, end=2.0),   # Ab3
    pretty_midi.Note(velocity=80, pitch=57, start=2.125, end=2.25),  # A3
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.125),  # Bb3
    pretty_midi.Note(velocity=80, pitch=59, start=3.125, end=3.25),  # B3
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.5),   # C3
    pretty_midi.Note(velocity=80, pitch=61, start=3.625, end=3.75),  # Db3
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.625),  # C3
    pretty_midi.Note(velocity=80, pitch=62, start=4.625, end=4.75),  # D3
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.0),   # Eb3
    pretty_midi.Note(velocity=80, pitch=65, start=5.125, end=5.25),  # E3
    pretty_midi.Note(velocity=80, pitch=58, start=5.375, end=5.5),   # Bb3
]

for note in bass_notes:
    bass.notes.append(note)

# Diane (Piano) - 7th chords on 2 and 4, comping and keeping motion
# Bar 2: F7 on 2, Am7 on 4
# Bar 3: Bb7 on 2, Dm7 on 4
# Bar 4: C7 on 2, E7 on 4

# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # F7 on 2 (1.875 - 2.0)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # C5
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # E5
    # Am7 on 4 (2.625 - 2.75)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=2.75),  # A3
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.75),  # E4
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),  # F4
]

# Bar 3 (3.0 - 4.5s)
piano_notes.extend([
    # Bb7 on 2 (3.375 - 3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),   # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),   # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.5),   # F4
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5),   # A4
    # Dm7 on 4 (4.125 - 4.25)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.25),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.25),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25),  # Bb4
])

# Bar 4 (4.5 - 6.0s)
piano_notes.extend([
    # C7 on 2 (4.875 - 5.0)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),   # C4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),   # E4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),   # G4
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0),   # B4
    # E7 on 4 (5.625 - 5.75)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.75),  # E4
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=5.75),  # G4
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=5.75),  # B4
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=5.75),  # D5
])

for note in piano_notes:
    piano.notes.append(note)

# Continue drum pattern for bars 2-4
# Bar 2 (1.5 - 3.0s)
for i in range(4):
    offset = 1.5 + i * 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=offset, end=offset + 0.375))

# Kick on 1 and 3 of bar 2 (1.5 and 2.25)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))

# Snare on 2 and 4 of bar 2 (1.875 and 2.625)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75))

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    offset = 3.0 + i * 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=offset, end=offset + 0.375))

# Kick on 1 and 3 of bar 3 (3.0 and 3.75)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))

# Snare on 2 and 4 of bar 3 (3.375 and 4.125)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25))

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    offset = 4.5 + i * 0.375
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=offset, end=offset + 0.375))

# Kick on 1 and 3 of bar 4 (4.5 and 5.25)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))

# Snare on 2 and 4 of bar 4 (4.875 and 5.625)
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))
drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75))

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
