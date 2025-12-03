
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) chromatic approach
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # B2 (MIDI 46) chromatic approach
    pretty_midi.Note(velocity=100, pitch=46, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: Motif, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),    # F#4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line
bass_notes = [
    # A2 (MIDI 45)
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    # C#3 (MIDI 48) chromatic approach
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.625),
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=100, pitch=38, start=3.625, end=4.0),
    # F#2 (MIDI 41) chromatic approach
    pretty_midi.Note(velocity=100, pitch=41, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B-D-F#-A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line
bass_notes = [
    # F#2 (MIDI 41)
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),
    # A2 (MIDI 45) chromatic approach
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.125),
    # B2 (MIDI 47)
    pretty_midi.Note(velocity=100, pitch=47, start=5.125, end=5.5),
    # D3 (MIDI 50) chromatic approach
    pretty_midi.Note(velocity=100, pitch=50, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: D7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),    # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),  # F#4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
