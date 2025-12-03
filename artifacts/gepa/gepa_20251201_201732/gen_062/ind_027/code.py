
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)
# Bass (Marcus): Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm root (F2) to D2 (fifth), chromatic approach on D2
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # F2
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # E2
    # Bar 3: Ab (Ab2) to G2 (fifth), chromatic approach on G2
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # G2
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),  # Ab2
    pretty_midi.Note(velocity=100, pitch=73, start=4.125, end=4.5),  # G2
    # Bar 4: Cm (C2) to G2 (fifth), chromatic approach on G2
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B2
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C2
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # B2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # Eb
]
# Bar 3: Ab7 (Ab, C, Eb, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # G
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (77), Ab (74), F (77), Eb (69) — melodic, singable, open-ended.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=77, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
