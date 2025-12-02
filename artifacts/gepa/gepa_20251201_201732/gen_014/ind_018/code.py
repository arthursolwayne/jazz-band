
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # F#2 on 4

    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2 on 1
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75), # A2 on 2
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # C3 on 3
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # B2 on 4

    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C3 on 1
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25), # D3 on 2
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # F3 on 3
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # E3 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # C#4

    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # F#4

    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # B4
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875),

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D4 (62), F#4 (67), A4 (71), Bb4 (70)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=105, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=105, pitch=71, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=105, pitch=70, start=2.25, end=2.5),  # Bb4
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=105, pitch=67, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=105, pitch=71, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=105, pitch=70, start=3.75, end=4.0),  # Bb4
    pretty_midi.Note(velocity=105, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=105, pitch=67, start=4.75, end=5.0),  # F#4
    pretty_midi.Note(velocity=105, pitch=71, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=105, pitch=70, start=5.25, end=5.5),  # Bb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
