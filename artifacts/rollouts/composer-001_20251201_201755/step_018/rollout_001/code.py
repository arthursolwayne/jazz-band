
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (D2) on beat 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bb (E2) on beat 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # Ab (D#2) chromatic approach on beat 3
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),
    # F (D2) on beat 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=2.0),  # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.5),  # Ab
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=75, start=2.5, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Little Ray on drums (Bar 2-4)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=3.0),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.0),
]
drums.notes.extend(drum_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # Gm (Fm7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # Gm (Bb7)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # A
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # Gm (Am7)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
