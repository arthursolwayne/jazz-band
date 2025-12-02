
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (F2 - Bb2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # Ab2 on 2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625), # Bb2 on 3
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=2.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 2: Dante - motif starts (F4, Ab4, Bb4, F4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),   # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Little Ray - fill and rhythm (no change from bar 1)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Marcus - walking line (F2, G2, Ab2, Bb2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125), # Ab2 on 3
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),  # Bb2 on 4
]
bass.notes.extend(bass_notes)

# Bar 3: Diane - open voicings (Bb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Bar 3: Dante - continues motif (F4, F4, F4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125),  # F4
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Little Ray - fill and rhythm (no change from bar 1)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Marcus - walking line (Bb2, C2, D2, Eb2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Bb2 on 1
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # C2 on 2
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # D2 on 3
    pretty_midi.Note(velocity=100, pitch=61, start=5.625, end=6.0),  # Eb2 on 4
]
bass.notes.extend(bass_notes)

# Bar 4: Diane - open voicings (Eb7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 4: Dante - motif returns with variation (F4, G4, Ab4, Bb4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.625),  # Ab4
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
