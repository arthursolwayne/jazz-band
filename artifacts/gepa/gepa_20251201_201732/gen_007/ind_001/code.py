
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
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Fm: F, Bb, Eb, Ab, Db, Gb (Fm7 is F, Ab, Bb, Db)
# Bar 2: F (root) -> Eb (fifth) -> D (chromatic approach to Eb)
# Bar 3: Bb (root) -> Ab (fifth) -> G (chromatic approach to Ab)
# Bar 4: Eb (root) -> Db (fifth) -> C (chromatic approach to Db)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=61, start=4.125, end=4.5),  # Db
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    # Bar 5: return to F for resolution
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),  # F
]
bass.notes.extend(bass_notes)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, Bb, Db)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
# Bar 5: Fm7 again for resolution
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # Db
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # Ab
    # Bar 4: Eb7
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),  # Db
    # Bar 5: Fm7
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # Db
]
piano.notes.extend(piano_notes)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm: F, Ab, Bb, Db
# Motif: F - Ab - Bb - Eb (with a chromatic flourish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=70, start=2.75, end=3.0),  # F (resolve)
    # Repeat the motif with slight variation
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # E (chromatic)
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.25),  # F (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_intro.mid")
