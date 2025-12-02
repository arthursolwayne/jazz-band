
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)   # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # C#5
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # F5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4 (motif start)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # F#4 (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)   # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Bass (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # C#3 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
piano_notes = [
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),  # F5
    # Bar 4: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5),  # C#5
]
piano.notes.extend(piano_notes)

# Bar 3: Sax (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),   # D4
]
sax.notes.extend(sax_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)   # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Bar 4: D7 (D F# A C#)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),  # C#5
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # F#4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
