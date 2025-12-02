
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # F2 on 4
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 on 1
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75), # A2 on 2
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # C3 on 3
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # B2 on 4
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # C3 on 1
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # D3 on 2
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # F3 on 3
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),  # E3 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C4
]
# Bar 3: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
])
# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F4
])
# Bar 5: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # B4
])
# Bar 6: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # C4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - D5 (start on 1.5s, end on 2.25s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4 (repeat)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A4
]
sax.notes.extend(sax_notes)

# Drums: Continue the pattern
# Bar 2
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
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
