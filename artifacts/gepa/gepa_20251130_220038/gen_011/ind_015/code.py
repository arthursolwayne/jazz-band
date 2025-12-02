
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # G#

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.0),  # C

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.75),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # D
    # Bar 3 (3.0 - 4.5s)
    # F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # D
    # Bar 4 (4.5 - 6.0s)
    # F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Start on F (65), move to A (68), then Bb (69), back to F (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),
    # Repeat the motif
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),
    # Final statement of the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),  # Snare on 4
]
for i in range(2):
    for j in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=1.5 + i * 1.5 + j, end=1.5 + i * 1.5 + j + 0.125))

# Bar 3 (3.0 - 4.5s)
for i in range(2):
    for j in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=3.0 + i * 1.5 + j, end=3.0 + i * 1.5 + j + 0.125))

# Bar 4 (4.5 - 6.0s)
for i in range(2):
    for j in [0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]:
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=4.5 + i * 1.5 + j, end=4.5 + i * 1.5 + j + 0.125))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
