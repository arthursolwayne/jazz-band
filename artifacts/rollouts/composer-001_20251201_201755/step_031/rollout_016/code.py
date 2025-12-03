
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.0),
    # Bar 3: C (43) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375),
    pretty_midi.Note(velocity=80, pitch=44, start=2.375, end=2.5),
    # Bar 4: G (39) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=39, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=40, start=2.875, end=3.0),
    # Bar 5: D (41) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    # Bar 6: A (45) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=46, start=3.875, end=4.0),
    # Bar 7: E (48) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=48, start=4.0, end=4.375),
    pretty_midi.Note(velocity=80, pitch=47, start=4.375, end=4.5),
    # Bar 8: B (50) with chromatic approach
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),  # E
]
# Bar 3: C7 (C E G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.5),  # Bb
])
# Bar 4: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F
])
# Bar 5: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # C
])
# Bar 6: A7 (A C# E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # G
])
# Bar 7: E7 (E G# B D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.5),  # G#
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.5),  # D
])
# Bar 8: B7 (B D# F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # D#
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # A
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: F - Bb - C - F (F7 chord)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=1.625, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0),  # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.125),  # F
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=61, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.875),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0),  # F
    # Bar 5: Add a twist
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # F
    # Bar 6: Resolve
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=110, pitch=61, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Continue the pattern with fills
# Bar 2: Fill on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),  # Hi-hat on 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Fill on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),  # Hi-hat on 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Fill on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),  # Hi-hat on 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
