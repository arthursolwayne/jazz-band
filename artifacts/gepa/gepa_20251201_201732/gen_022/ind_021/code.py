
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: A7 (A C# E G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # C#4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # G4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75), # C#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # C#4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # C2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # D2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.875),  # B4
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=82, start=4.875, end=5.25), # B4
    pretty_midi.Note(velocity=100, pitch=78, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=100, pitch=82, start=5.625, end=6.0),  # B4
]
sax.notes.extend(sax_notes)

# Drum fill for bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hi-hat
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
