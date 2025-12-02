
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (roots and fifths with chromatic approaches)
# F7 (F, C, E, A) -> Bb7 (Bb, F, Ab, Db) -> C7 (C, G, B, E) -> D7 (D, A, C, F#)
bass_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # C (C2)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # E (E2)
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # A (A2)

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb (Bb2)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F (F2)
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # Ab (Ab2)
    pretty_midi.Note(velocity=100, pitch=75, start=4.125, end=4.5),   # Db (Db2)

    # Bar 4 (C7)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C (C2)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G (G2)
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # B (B2)
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),   # E (E2)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, Db, F, Ab)
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=6.0),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=6.0),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=6.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=6.0),  # E (E5)

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=6.0),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=6.0),  # Db (Db5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=6.0),  # F (F5)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=6.0),  # Ab (Ab5)

    # Bar 4 (C7)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=6.0),  # C (C5)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=6.0),  # E (E5)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=6.0),  # G (G5)
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=6.0),  # B (B5)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (F5) -> G (G5) -> E (E5) -> F (F5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.625),  # F (F5)
    pretty_midi.Note(velocity=100, pitch=81, start=1.625, end=1.75),  # G (G5)
    pretty_midi.Note(velocity=100, pitch=77, start=1.75, end=1.875),  # E (E5)
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.0),   # F (F5)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
