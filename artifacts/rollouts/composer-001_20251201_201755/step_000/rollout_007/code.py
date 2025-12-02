
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 (root)
    
    # Bar 3 (G7)
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (root)
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.125), # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),  # G2 (root)
    
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # C2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # C2 (root)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D - F - A - C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C5

    # Bar 3: G7 (G - B - D - F)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F5

    # Bar 4: Cm7 (C - Eb - G - Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625), # A4

    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # A4

    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625), # A4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)

    # Hihat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
