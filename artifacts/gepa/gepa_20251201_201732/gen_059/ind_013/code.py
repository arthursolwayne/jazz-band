
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

# Bar 2: Full ensemble
# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 - Root
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 - 3rd
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 - 5th
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # E2 - Chromatic approach
]
bass.notes.extend(bass_notes)

# Piano - Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dmaj7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Dmaj7 (A)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # Dmaj7 (D)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Dmaj7 (C#)

    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # D7 (F#)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D7 (C#)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # D7 (D)
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D7 (F)

    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # Dm7 (C#)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Dm7 (E)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # Dm7 (F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Dm7 (A)

    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Dmaj7 (F#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Dmaj7 (A)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # Dmaj7 (D)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Dmaj7 (C#)
]
piano.notes.extend(piano_notes)

# Sax - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),   # F4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),   # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),   # A4
]
sax.notes.extend(sax_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
