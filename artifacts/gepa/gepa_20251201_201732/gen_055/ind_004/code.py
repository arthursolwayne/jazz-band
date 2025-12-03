
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line (F2 to Bb2, MIDI 38 to 43)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # Bb2 (fourth)
]

piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E) open voicing
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # E (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # C (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # A (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F (Fmaj7)

    # Bar 3: Bm7 (B, D, F#, A) open voicing
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625), # A (Bm7)
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # F# (Bm7)
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # D (Bm7)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # B (Bm7)

    # Bar 4: Em7 (E, G, B, D) open voicing
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # D (Em7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # B (Em7)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # G (Em7)
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # E (Em7)
]

# Dante - Sax melody (Bar 2-3)
# Motif: F - A - Bb - F (phrase)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # F4
]

# Bar 4: Drums again, more energy
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=110, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # C3 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # Bb2 (fourth)
])

# Piano - Comp on 2 and 4
piano_notes.extend([
    # Bar 4: Fmaj7 (F, A, C, E) open voicing
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # E (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # C (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # A (Fmaj7)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),  # F (Fmaj7)
])

# Dante - Sax (Bar 4: leave it hanging and come back)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F4 (repeat)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # Bb4
])

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
