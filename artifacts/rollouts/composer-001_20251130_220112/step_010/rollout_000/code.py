
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.25, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=57, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=58, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=90, start=1.75, end=2.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=92, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=94, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=96, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=90, start=3.25, end=3.5),  # F7
    pretty_midi.Note(velocity=90, pitch=92, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=94, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=96, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=90, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=90, pitch=92, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=94, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=96, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # F# (leaving it hanging)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.375),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # E (finishing the motif)
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = 1.5 + (bar - 2) * 1.5
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)
    kick_start = kick_start + 1.125
    kick_end = kick_start + 0.375
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end)

# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = 1.5 + (bar - 2) * 1.5 + 0.75
    snare_end = snare_start + 0.125
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)
    snare_start = snare_start + 1.25
    snare_end = snare_start + 0.125
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_end)

# Hihat on every eighth
for bar in range(2, 5):
    for eighth in range(8):
        hihat_start = 1.5 + (bar - 2) * 1.5 + (eighth * 0.375)
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=hihat_start, end=hihat_end)

drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
