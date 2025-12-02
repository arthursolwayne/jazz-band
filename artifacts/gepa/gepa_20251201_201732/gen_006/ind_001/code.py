
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # F (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=1.875),
    # Bb (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=46, start=1.875, end=2.25),
    # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),
    # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: motif in Fm, start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=58, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bb (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=3.375),
    # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),
    # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.75, end=4.125),
    # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.0),
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=55, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=58, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bb (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=46, start=4.5, end=4.875),
    # Ab (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),
    # F (root)
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),
    # Bb (fifth)
    pretty_midi.Note(velocity=100, pitch=46, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=45, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=49, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: motif continuation and resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=58, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: 3.0 - 4.5s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: 4.5 - 6.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")
