
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2

    # Bar 3 (G7)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # G2

    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano (open voicings, different chord each bar, resolve on the last)
# Bar 2: Dm7 -> D F A C
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C5
]

# Bar 3: G7 -> G B D F
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F5
])

# Bar 4: Cm7 -> C Eb G Bb
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
])

piano.notes.extend(piano_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2 and 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Hihat on 1 and 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start + 2.25, end=start + 2.625)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0)
])

# Sax: Melody (Dm scale with chromatic approaches)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.125), # Eb4 (chromatic approach)
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.5),  # F4

    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.5),  # A4

    # Bar 4: Return to the beginning and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.125), # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=5.125, end=5.5),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=6.0),    # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
