
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # D2 on 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # D2 on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4

    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # F5

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # Bb4

    # Bar 2: Dm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # C4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A4

    # Bar 3: G7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # F5

    # Bar 4: Cm7 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # Eb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), Eb4 (64), D4 (62), F4 (67) on 1, 2, 3, 4 of bar 2
# Then repeat it slightly altered on bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Eb4 on 2
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D4 on 3
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # F4 on 4

    # Repeat on bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.875),  # D4 on 1
    pretty_midi.Note(velocity=110, pitch=64, start=5.875, end=6.0),    # Eb4 on 2
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)

drums.notes.extend([note for note in drum_notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
