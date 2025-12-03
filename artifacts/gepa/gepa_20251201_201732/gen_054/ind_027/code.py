
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (3rd octave)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # Ab
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm melody: F, Ab, Bb, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F (rest in between)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2, G2, Ab2, A2)
# Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif on the last bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 & 3, snare on 2 & 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
