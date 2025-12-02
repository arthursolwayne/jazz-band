
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),   # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),   # D2 -> Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),   # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.5),   # F2
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),   # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.75, end=3.0),   # D2 -> Eb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),    # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),    # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),    # C#4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif - G4, A4, B4, C#4 (D minor pentatonic), start, leave hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # C#4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: D7 walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.25),   # G2
    pretty_midi.Note(velocity=100, pitch=45, start=3.25, end=3.5),   # A2
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.75),   # F2
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.0),   # D2 -> Eb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),   # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.25, end=4.5),   # D2 -> Eb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Bm7b5 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),    # B4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),    # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),    # F#4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),    # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif continuation - G4, F#4, E4, D4 (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),   # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # E4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: D7 walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.75),   # D2 -> Eb2
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),   # D2
    pretty_midi.Note(velocity=100, pitch=40, start=5.0, end=5.25),   # D2 -> Eb2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.5),   # G2
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.75),   # F2
    pretty_midi.Note(velocity=100, pitch=40, start=5.75, end=6.0),   # D2 -> Eb2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),    # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),    # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),    # C#4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Repeat motif but resolve more
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),   # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),   # A4
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),   # B4
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),   # C#4
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),   # G4 again
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),   # D4 (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
