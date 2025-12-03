
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with a motif, bass walks, piano comps
# Sax motif: D4 - F4 - G4 - A4 (D, F, G, A), played on 1, 2, 3, 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4 on 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A4 on 4
]
sax.notes.extend(sax_notes)

# Bass line: D2 - F2 - G2 - A2 (D, F, G, A), walking with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano comp: Dmaj7 (D, F#, A, C#) on bar 2, G7 (G, B, D, F) on bar 4
piano_notes = [
    # Bar 2 - Dmaj7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C#5
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # F#4
    # Bar 4 - G7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F4
]
piano.notes.extend(piano_notes)

# Bar 3: Sax returns with extension of motif
# Sax plays D4 - F4 - G4 - D4 (motif + resolution)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F4 on 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G4 on 3
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4 on 4
]
sax.notes.extend(sax_notes)

# Bass line: D2 - F2 - G2 - D2 (walking with resolution)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2
]
bass.notes.extend(bass_notes)

# Piano comp: G7 (G, B, D, F) on bar 3, Dmaj7 (D, F#, A, C#) on bar 4
piano_notes = [
    # Bar 3 - G7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # F4
    # Bar 4 - Dmaj7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F#4
]
piano.notes.extend(piano_notes)

# Bar 4: Drums again
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
