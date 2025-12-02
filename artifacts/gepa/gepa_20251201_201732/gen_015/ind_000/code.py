
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625), # Eb2 on 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on last
piano_notes = [
    # Bar 2: Dm9 (D, F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # E5
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # F5
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 2 - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D (62) - Eb (63) - F (64) - Rest - D (62) - A (67) - Bb (69) - C (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=63, start=1.875, end=2.25), # Eb4 on 2
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625), # F4 on 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4 on 4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # A4 on 4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # Bb4 on 4
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),  # C5 on 4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=39, start=3.75, end=4.125), # Eb2 on 3
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F5
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # B4
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 3 - Continue the motif, lean into the tension
# Dm scale: D, Eb, F, G, A, Bb, C
# Continue the motif on the next bar
# D (62) - Eb (63) - F (64) - G (67) - A (69) - Bb (71) - C (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.75), # Eb4 on 2
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125), # F4 on 3
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G4 on 4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=80, pitch=39, start=5.25, end=5.625), # Eb2 on 3
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings
piano_notes = [
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # B4
    # Resolution
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Sax: Bar 4 - End on a strong note, resolution
# D (62) - Eb (63) - F (64) - G (67) - A (69) - Bb (71) - C (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=63, start=4.875, end=5.25), # Eb4 on 2
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.625), # F4 on 3
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G4 on 4
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
