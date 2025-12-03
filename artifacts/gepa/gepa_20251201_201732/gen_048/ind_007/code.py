
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)    # Hihat
]
drums.notes.extend(drum_notes)

# Bar 2: Full band (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625), # F2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
piano_notes = [
    # Bar 2: D7sus4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=3.0),  # D5

    # Bar 3: G7#9
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F5 (#9)

    # Bar 4: Bm7b5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # E5
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # G5
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)    # Hihat
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)    # Hihat
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)    # Hihat
]
drums.notes.extend(drum_notes)

# Sax: Melody in Bar 2-4
# Motif: D4 - F4 - G4 - E4 (upbeat, then resolving)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.75), # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # E4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
