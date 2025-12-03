
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2 (1.5 - 3.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # A (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0)   # D2 (root)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D) with open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4 (root)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4 (third)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # E4 (fifth)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0)   # G4 (seventh)
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # F (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # A (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5)   # F (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (Bb, D, F, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # F#4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5)   # G4
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s)
# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # A (fifth)
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25), # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # F (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0)   # A (fifth)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (Eb, G, Bb, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0)   # G4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax - short motif, haunting, incomplete
# Bar 2: Start the motif (D4, F4, Bb4) with space
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75)   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 3: Fill in the space, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75)   # A4 (chromatic)
]
sax.notes.extend(sax_notes)

# Bar 4: Return, incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25)   # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (Little Ray)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)   # Kick on 3
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
