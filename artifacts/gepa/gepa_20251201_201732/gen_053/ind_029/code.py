
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, roots and fifths with chromatic approaches)
bass_notes = [
    # Bar 2: F -> C -> F -> B♭
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),

    # Bar 3: B♭ -> F -> B♭ -> E♭
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),

    # Bar 4: E♭ -> B♭ -> E♭ -> A♭
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=70, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane on piano (open voicings, different chord each bar, resolve on last)
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),

    # Bar 3: B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),

    # Bar 4: E♭maj7 (E♭, G, B♭, D)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Little Ray on drums (Bar 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

# Dante on sax (motif: F - B♭ - D - F)
# Start on beat 1 of bar 2, leave it hanging on beat 3, come back on beat 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625),  # B♭
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.25),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
