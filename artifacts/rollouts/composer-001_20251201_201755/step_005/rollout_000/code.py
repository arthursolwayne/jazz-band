
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Piano comping (Fm7 -> Am7 -> Dm7 -> Gm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.75), # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Piano comping (Fm7 -> Am7 -> Dm7 -> Gm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (F2 - C3, MIDI 53 - 60)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # Ab2
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),  # Bb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Piano comping (Fm7 -> Am7 -> Dm7 -> Gm7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax (Dante) - Motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # Gm (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # D (Ab2)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # Gm (C3)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D (Bb2)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Gm (F)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # D (A)
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # Gm (C)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D (D)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # Gm (F)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D (A)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # Gm (C)
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D (D)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
