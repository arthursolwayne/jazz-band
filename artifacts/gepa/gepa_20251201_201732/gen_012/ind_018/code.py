
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

# Marcus on bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F - G - E - F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=73, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),

    # Bar 3: Bb - A - G - Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),

    # Bar 4: D - C - Bb - D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),
]

bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.5 + 0.375),

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.375),

    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.5 + 0.375),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.375),
]

piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),

drums.notes.extend(drum_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: First phrase of motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # E (rest)
]

# Bar 3: Silence (space)
# Bar 4: Return and finish the motif
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # E
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
