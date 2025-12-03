
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
# Bass: C2 (D2 is the root of D minor, so start with C2 as chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # C2 (approach to D2)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # D2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # Eb2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb2 (chromatic approach to B2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=45, start=4.125, end=4.5),  # C#2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> G7 (V of C)
# Bar 3: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (chromatic approach to G2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # Bb2 (fifth)
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0),  # A2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Cmaj7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Sax: End motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4 (overlap)
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4 (overlap)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
