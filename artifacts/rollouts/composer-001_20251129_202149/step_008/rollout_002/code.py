
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0)   # D4
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # C3
    pretty_midi.Note(velocity=80, pitch=47, start=2.5, end=2.75),  # B2
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0)   # C3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # B4
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B4
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5)   # D4
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # C3
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # B2
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5)   # C3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # B4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C4
    pretty_midi.Note(velocity=100, pitch=59, start=5.75, end=6.0)   # B3
]
sax.notes.extend(sax_notes)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # D3
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # C3
    pretty_midi.Note(velocity=80, pitch=47, start=5.5, end=5.75),  # B2
    pretty_midi.Note(velocity=80, pitch=46, start=5.75, end=6.0)   # A2
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # B4
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # B4
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
