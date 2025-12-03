
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),   # F2 on 1
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # F2 on 3
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),   # A2 on 4
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),   # F2 on 1
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # F2 on 3
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),   # A2 on 4
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # F2 on 1
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # G2 on 2
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # F2 on 3
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),   # A2 on 4
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=65, start=1.5, end=1.875),  # F4 (F)
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),  # A4 (A)
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875),  # C5 (C)
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # E5 (E)

    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),  # C5 (C)
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # Eb5 (Eb)
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625),  # G5 (G)
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # Bb5 (Bb)

    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=95, pitch=68, start=3.0, end=3.375),   # A4 (A)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # C5 (C)
    pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.375),   # E5 (E)
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),   # G5 (G)

    # Bar 5: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # D4 (D)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # F#4 (F#)
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.125),  # A4 (A)
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # C5 (C)

    # Bar 6: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),   # G5 (G)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # Bb5 (Bb)
    pretty_midi.Note(velocity=85, pitch=76, start=4.5, end=4.875),   # D5 (D)
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),   # F5 (F)

    # Bar 7: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=71, start=5.25, end=5.625),  # Bb5 (Bb)
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # D5 (D)
    pretty_midi.Note(velocity=85, pitch=69, start=5.25, end=5.625),  # F5 (F)
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # Ab5 (Ab)

    # Bar 8: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=6.0),   # F4 (F)
    pretty_midi.Note(velocity=90, pitch=68, start=5.625, end=6.0),   # A4 (A)
    pretty_midi.Note(velocity=85, pitch=72, start=5.625, end=6.0),   # C5 (C)
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),   # E5 (E)
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4 - A4 - Bb4 - F4 (hanging on the last note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),   # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.625, end=1.75),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),   # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),   # F4 (hang)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),   # F4 (return)
    pretty_midi.Note(velocity=100, pitch=68, start=3.125, end=3.25),   # A4
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),   # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),   # F4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),    # Hihat on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),    # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),    # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
