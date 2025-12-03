
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Bar 2: G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    # Bar 3: F#2 (chromatic approach)
    pretty_midi.Note(velocity=85, pitch=42, start=2.25, end=2.625),
    # Bar 3: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
    # Bar 4: A2 (chromatic approach)
    pretty_midi.Note(velocity=85, pitch=45, start=3.0, end=3.375),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    # Bar 4: F#2 (chromatic approach)
    pretty_midi.Note(velocity=85, pitch=42, start=3.75, end=4.125),
    # Bar 4: G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
    # Bar 5: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # Bar 5: G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),
    # Bar 6: F#2 (chromatic approach)
    pretty_midi.Note(velocity=85, pitch=42, start=5.25, end=5.625),
    # Bar 6: D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # C
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # F
])
# Bar 4: A7 (A C# E G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),  # G
])
# Bar 5: D7 (D F# A C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C
])
# Bar 6: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # F
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F#4 (Diatonic), A4 (Diatonic), D5 (Root), G4 (Fifth)
# Bar 2: Start motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # A4
]
# Bar 3: Leave it hanging
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=79, start=3.0, end=3.25),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),  # G4
])
# Bar 5: Echo the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=76, start=4.75, end=5.0),  # A4
])
# Bar 6: Finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.5),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=5.5, end=5.75),  # G4
])
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0)
]
# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375)
])
# Hihat on every eighth
for i in range(1, 6):
    start = 1.5 + (i - 1) * 0.375
    end = start + 0.1875
    drum_notes.extend([
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
    ])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
