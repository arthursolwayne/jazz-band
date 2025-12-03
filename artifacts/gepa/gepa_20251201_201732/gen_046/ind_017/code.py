
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

# Drums - Bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Bar 2 (Fm7 root movement with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.25), # E (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),  # G (fifth)
]
bass.notes.extend(bass_notes)

# Piano - Bar 2 (Fm7 chord, open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0),  # F (C4)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),  # Ab (D4)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # C (G4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # F (C5)
]
piano.notes.extend(piano_notes)

# Sax - Bar 2 (melody, haunting motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # A (E5)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25), # Bb (F5)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # A (E5)
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),  # G (D5)
]
sax.notes.extend(sax_notes)

# Drums - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # Hihat on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - Bar 3 (Abm7 root movement with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # G (D2)
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=4.125), # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # Bb (F2)
]
bass.notes.extend(bass_notes)

# Piano - Bar 3 (Abm7 chord, open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),  # Ab (D4)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),  # Bb (F4)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # Db (A4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Ab (F5)
]
piano.notes.extend(piano_notes)

# Sax - Bar 3 (melody continuation, space and tension)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # G (D5)
    pretty_midi.Note(velocity=110, pitch=58, start=3.375, end=3.75), # F (B4)
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125), # D (A4)
    pretty_midi.Note(velocity=110, pitch=53, start=4.125, end=4.5),  # C (G4)
]
sax.notes.extend(sax_notes)

# Drums - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - Bar 4 (Bbm7 root movement with chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # A (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # Bb (F2)
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # C (G2)
]
bass.notes.extend(bass_notes)

# Piano - Bar 4 (Bbm7 chord, open voicing)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),  # Bb (F4)
    pretty_midi.Note(velocity=100, pitch=54, start=4.5, end=6.0),  # C (G4)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # D (B4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Bb (F5)
]
piano.notes.extend(piano_notes)

# Sax - Bar 4 (melody resolution, leave it hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # C (G4)
    pretty_midi.Note(velocity=110, pitch=52, start=4.875, end=5.25), # Bb (F4)
    pretty_midi.Note(velocity=110, pitch=50, start=5.25, end=5.625), # Ab (D4)
    pretty_midi.Note(velocity=110, pitch=48, start=5.625, end=6.0),  # F (C4)
]
sax.notes.extend(sax_notes)

# Drums - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
