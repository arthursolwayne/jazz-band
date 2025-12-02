
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

# Marcus on bass: Walking line, chromatic approaches, never the same note twice.
# F7 chord: F, A, C, E (root, 3, 5, 7), chromatic approaches to each note.
bass_notes = [
    # Chromatic approach to F
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=1.6875, end=1.875),  # F
    # Chromatic approach to A
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.0625, end=2.25),  # A
    # Chromatic approach to C
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=2.4375, end=2.625),  # C
    # Chromatic approach to E
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=80, pitch=75, start=2.8125, end=3.0),  # E
    # Chromatic approach to F
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.1875),  # F#
    pretty_midi.Note(velocity=80, pitch=77, start=3.1875, end=3.375),  # G
    # Chromatic approach to A
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=80, pitch=80, start=3.5625, end=3.75),  # A
    # Chromatic approach to C
    pretty_midi.Note(velocity=80, pitch=82, start=3.75, end=3.9375),  # B
    pretty_midi.Note(velocity=80, pitch=83, start=3.9375, end=4.125),  # C
    # Chromatic approach to E
    pretty_midi.Note(velocity=80, pitch=85, start=4.125, end=4.3125),  # D
    pretty_midi.Note(velocity=80, pitch=86, start=4.3125, end=4.5),  # E
    # Chromatic approach to F
    pretty_midi.Note(velocity=80, pitch=87, start=4.5, end=4.6875),  # F#
    pretty_midi.Note(velocity=80, pitch=88, start=4.6875, end=4.875),  # G
    # Chromatic approach to A
    pretty_midi.Note(velocity=80, pitch=90, start=4.875, end=5.0625),  # Ab
    pretty_midi.Note(velocity=80, pitch=91, start=5.0625, end=5.25),  # A
    # Chromatic approach to C
    pretty_midi.Note(velocity=80, pitch=93, start=5.25, end=5.4375),  # B
    pretty_midi.Note(velocity=80, pitch=94, start=5.4375, end=5.625),  # C
    # Chromatic approach to E
    pretty_midi.Note(velocity=80, pitch=96, start=5.625, end=5.8125),  # D
    pretty_midi.Note(velocity=80, pitch=97, start=5.8125, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=92, start=1.5, end=1.875),  # E
    # Bar 3: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=92, start=2.25, end=2.625),  # E
    # Bar 4: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=92, start=3.0, end=3.375),  # E
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif begins
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=2.0, end=2.25),  # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.5),  # E
    # Bar 4: Return and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Full rhythm for bars 2-4
drum_notes = []
for bar in range(2, 5):
    start = bar * 1.5
    for beat in [0.0, 1.125]:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + beat, end=start + beat + 0.375))  # Kick
    for beat in [0.75, 1.875]:
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start + beat, end=start + beat + 0.125))  # Snare
    for eighths in range(8):
        drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + eighths * 0.375, end=start + eighths * 0.375 + 0.1875))  # Hihat
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
