
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
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.append(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # E2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # D2
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # C2
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25), # Db2
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C5
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G Bb D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F5
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C Eb G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Dante - short motif, make it sing
# Motif: D4 (62), F4 (65), D4 (62), G4 (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0)
drums.notes.append(drum_notes)
# Bar 3
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5)
drums.notes.append(drum_notes)
# Bar 4
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)
drums.notes.append(drum_notes)
drum_notes = pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0)
drums.notes.append(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
