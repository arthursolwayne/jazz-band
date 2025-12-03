
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: walking bass line starting on D2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0), # C2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, one chord per bar, resolve on the last
# Bar 2: Dm7 in open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0), # D4 (root)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0), # G4 (fifth)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0), # Bb4 (minor third)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0), # C4 (seventh)
]
piano.notes.extend(piano_notes)

# Dante: Start the motif on the 3rd beat, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0), # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking bass line starting on C2 (MIDI 37)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=3.0, end=3.375), # C2
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.75, end=4.125), # F2
    pretty_midi.Note(velocity=80, pitch=37, start=4.125, end=4.5), # C2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicing, Bb7 in 2nd bar, resolve on F7 in 4th bar
# Bar 3: Bb7 in open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5), # Bb3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5), # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5), # G4
]
piano.notes.extend(piano_notes)

# Dante: Continue the motif, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125), # C5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking bass line starting on F2 (MIDI 40)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=80, pitch=37, start=4.875, end=5.25), # C2
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=6.0), # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Diane: Open voicing, F7 in 4th bar
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0), # F3
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0), # A4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0), # D5
]
piano.notes.extend(piano_notes)

# Dante: Finish the motif, leave the last note hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25), # C5
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0), # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
