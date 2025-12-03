
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (F2 to Bb2, MIDI 53 to 57)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),   # F2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),   # F2
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # F2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625),  # Bb2
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),   # F2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) -> F (F, Ab, C, Eb) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # Ab4

    # Bar 3: Bb7 (Bb, Db, F, Ab) -> Bb (Bb, Db, F, Ab) - open voicing
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Db4

    # Bar 4: Cm7 (C, Eb, G, Bb) -> C (C, Eb, G, Bb) - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=6.0),  # Eb4
]

piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5)

drums.notes.extend(drum_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, Bb4, F4 (bar 2), then repeat on bar 4

sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # F4

    # Bar 3: Leave it hanging (nothing)
]

# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25),  # Ab4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # F4
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
