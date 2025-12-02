
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane on piano (open voicings, comp on 2 and 4)
piano_notes = [
    # Bar 2: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C#5
    # Bar 2: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.5),  # C#5
]

# Marcus on bass (walking line, roots and fifths, chromatic approaches)
bass_notes = [
    # Bar 2: D (root), F# (fifth), E (chromatic approach), G (root)
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # F#2
    pretty_midi.Note(velocity=100, pitch=49, start=2.0, end=2.25),  # E2
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.5),  # G2
]

# Dante on sax (short motif, start it, leave it hanging)
sax_notes = [
    # Bar 2: D (start), B (chromatic), A (resolve), leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=63, start=1.75, end=2.0),  # B4
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.5),  # A4
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane on piano (open voicings, comp on 2 and 4)
piano_notes.extend([
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.25),  # F5
    # Bar 3: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.0),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.0),  # F5
])

# Marcus on bass (walking line, roots and fifths, chromatic approaches)
bass_notes.extend([
    # Bar 3: G (root), B (fifth), A (chromatic approach), D (root)
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.25),  # G2
    pretty_midi.Note(velocity=100, pitch=54, start=3.25, end=3.5),  # B2
    pretty_midi.Note(velocity=100, pitch=53, start=3.5, end=3.75),  # A2
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0),  # D2
])

# Dante on sax (short motif, continue it, resolve it)
sax_notes.extend([
    # Bar 3: D (start), B (chromatic), A (resolve), C (finish it)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=63, start=3.25, end=3.5),  # B4
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # C5
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane on piano (open voicings, comp on 2 and 4)
piano_notes.extend([
    # Bar 4: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.75),  # F5
    # Bar 4: comp on 2 and 4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.5),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.5),  # F5
])

# Marcus on bass (walking line, roots and fifths, chromatic approaches)
bass_notes.extend([
    # Bar 4: G (root), B (fifth), A (chromatic approach), D (root)
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=4.75),  # G2
    pretty_midi.Note(velocity=100, pitch=54, start=4.75, end=5.0),  # B2
    pretty_midi.Note(velocity=100, pitch=53, start=5.0, end=5.25),  # A2
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.5),  # D2
])

# Dante on sax (short motif, finish it, leave it open)
sax_notes.extend([
    # Bar 4: G (start), B (chromatic), A (resolve), D (finish it)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=68, start=4.75, end=5.0),  # B4
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=110, pitch=59, start=5.25, end=6.0),  # D4
])

# Add all notes to their instruments
piano.notes.extend(piano_notes)
bass.notes.extend(bass_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
