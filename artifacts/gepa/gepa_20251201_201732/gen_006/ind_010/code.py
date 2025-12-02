
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

# Drums - Bar 1
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

# Bass - Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: D2 (38), F#2 (41), G2 (43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),  # G2
    pretty_midi.Note(velocity=100, pitch=37, start=3.375, end=3.75),  # C2 chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=100, pitch=44, start=5.625, end=6.0),  # A2 chromatic approach
]
bass.notes.extend(bass_notes)

# Piano - Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Dmaj7 (D, F#, A, C#)
# Bar 3: Bm7b5 (B, D, F, A)
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    # Bar 2: Dmaj7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C#4
    # Bar 3: Bm7b5
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F4
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A4
    # Bar 4: G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F4
]
piano.notes.extend(piano_notes)

# Drums - Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.875)
drums.notes.extend(drum_notes)

# Sax - Dante (Tenor, one short motif, make it sing)
# Bar 2: Start with a motif (D4, F#4, A4)
# Bar 3: Leave it hanging (hold A4)
# Bar 4: Come back and finish it (B4, D5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.375),  # A4 (hold)
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5625),  # B4
    pretty_midi.Note(velocity=100, pitch=77, start=3.5625, end=3.75),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
