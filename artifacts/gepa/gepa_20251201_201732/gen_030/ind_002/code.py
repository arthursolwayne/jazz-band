
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Marcus: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # C (G2)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Bb (F#2)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # F (D2)

    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C (G2)
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75), # F (B2)
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125), # Eb (A2)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # C (G2)

    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # F (B2)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25), # Bb (E3)
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Ab (D3)
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # F (B2)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Eb (Eb4)

    # Bar 3: Bb7 (Bb D F Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # Ab (Ab4)

    # Bar 4: Gm7 (G Bb D F)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F (F4)
]
piano.notes.extend(piano_notes)

# You: Tenor sax, short motif starting on beat 1 of bar 2
# Motif: F -> Bb -> C -> Eb (F7)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # C (C4)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F (F4)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # C (C4)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # Bb (Bb4)
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),   # F (F4)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
