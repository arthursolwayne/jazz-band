
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=2.0),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=2.0, end=2.5),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=3.0),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=3.0, end=3.5),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=4.0),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.0, end=4.5),  # E2
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=5.0),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=5.0, end=5.5),  # F#2
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # E4
]
# Bar 3: G7 (G, B, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F4
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=77, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F4 - Bb4 - D5 - F5 (sings, no scale runs)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),   # Bb4
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # D5
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=3.0),   # F5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.125),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.375),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0),   # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.625),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=3.875),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.5),   # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.375),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),  # Hihat on &
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.0),   # Hihat on &
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
