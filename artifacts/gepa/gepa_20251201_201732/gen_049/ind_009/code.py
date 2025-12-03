
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # G (D4)
    pretty_midi.Note(velocity=90, pitch=37, start=2.625, end=3.0),  # F (C4)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # Fm7 (C)

    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25), # Ab7 (G)
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # Ab7 (C)
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25), # Ab7 (E)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Ab7 (A)

    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625), # C7 (G)
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # C7 (C)
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625), # C7 (E)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # C7 (Bb)

    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=3.0),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),  # Fm7 (F)
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=3.0, end=3.375),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125), # G (D4)
    pretty_midi.Note(velocity=90, pitch=37, start=4.125, end=4.5),  # F (C4)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.375),  # Fm7 (C)

    pretty_midi.Note(velocity=80, pitch=49, start=3.375, end=3.75), # Ab7 (G)
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.75), # Ab7 (C)
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # Ab7 (E)
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75), # Ab7 (A)

    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # C7 (G)
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # C7 (C)
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125), # C7 (E)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # C7 (Bb)

    pretty_midi.Note(velocity=80, pitch=47, start=4.125, end=4.5),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=37, start=4.125, end=4.5),  # Fm7 (F)
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.875),  # F (C4)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # Ab (E4)
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # G (D4)
    pretty_midi.Note(velocity=90, pitch=37, start=5.625, end=6.0),  # F (C4)
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.875),  # Fm7 (C)

    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # Ab7 (G)
    pretty_midi.Note(velocity=80, pitch=43, start=4.875, end=5.25), # Ab7 (C)
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # Ab7 (E)
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Ab7 (A)

    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625), # C7 (G)
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # C7 (C)
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.625), # C7 (E)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # C7 (Bb)

    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # Fm7 (E)
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # Fm7 (G)
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),  # Fm7 (Bb)
    pretty_midi.Note(velocity=80, pitch=37, start=5.625, end=6.0),  # Fm7 (F)
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
drums.notes.extend(drum_notes)

# Dante: One short motif, start it, leave it hanging. Come back and finish it.
# Motif: Fm (F, Ab, C) in a syncopated rhythm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # Ab (Eb4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # C (Bb4)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F (F4 again)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Ab (Eb4)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # C (Bb4)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
