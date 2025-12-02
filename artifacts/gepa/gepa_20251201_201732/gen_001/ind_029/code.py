
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
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # Ab (fifth, chromatic approach from G)
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),
    # F (root again)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0)   # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.375),
    # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),
    # F (root again)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),
    # Ab (fifth)
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Bbm7 (Bb, Db, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, resolve on Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.5)    # Bb (sustained)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),
    # F (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),
    # Ab (fifth, chromatic approach from G)
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),
    # D (chromatic approach from C#)
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=6.0)
]
piano.notes.extend(piano_notes)

# Sax: End with a simple resolution on Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0)  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hats on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
