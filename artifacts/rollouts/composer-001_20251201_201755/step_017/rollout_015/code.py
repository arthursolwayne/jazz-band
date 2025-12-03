
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=100, pitch=43, start=1.875, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # D2

    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),   # A2
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # D3 (fifth)
    pretty_midi.Note(velocity=100, pitch=46, start=3.75, end=4.125),  # C#3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # A2

    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),   # D3
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # A3 (fifth)
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # G3 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0)    # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, C#, F#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # D5

    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F#4

    # Bar 4: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),   # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # C#5
]
piano.notes.extend(piano_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),  # Kick on 1
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),  # Snare on 2
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 1.5),     # Hihat on every 8th
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)  # Kick on 3
    ]
    drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),   # C4
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # F#4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),   # D4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0)    # C4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
