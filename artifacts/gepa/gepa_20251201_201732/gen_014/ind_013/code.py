
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0), # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D-F-A-C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # C5

    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # B4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625), # F4

    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0), # Bb4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - G (start), leave it hanging on G
# Then return and finish it with A - Bb - C - D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0), # G4

    # Leave it hanging on G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75), # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.875, end=3.0), # C4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # D4 (root)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # F4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # A4 (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5), # G4 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings
piano_notes = [
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375), # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F4

    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # Bb4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D4 (root)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F4 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # A4 (fifth)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0), # G4 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings
piano_notes = [
    # Bar 4: Cm7 (C-Eb-G-Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # Bb4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
