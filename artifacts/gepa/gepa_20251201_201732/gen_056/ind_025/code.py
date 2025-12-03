
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=75, pitch=49, start=2.25, end=2.625), # C#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=3.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: short motif, concise, melodic
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # D4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # F2 (root of Gm7)
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75), # C3 (fifth)
    pretty_midi.Note(velocity=75, pitch=71, start=3.75, end=4.125), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=4.5),  # F5
]
piano.notes.extend(piano_notes)

# Sax: continuation of the motif with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: root and fifth with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25), # C3 (fifth)
    pretty_midi.Note(velocity=75, pitch=71, start=5.25, end=5.625), # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # F2 (root)
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar
# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Snare on 3
    pretty_midi.Note(velocity=100, pitch=36, start=6.0, end=6.375), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125), # Hihat on 4
    pretty_midi.Note(velocity=90, pitch=38, start=7.125, end=7.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
