
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=75, start=4.5, end=4.875),  # D#
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (Diane)
# 7th chords on 2 and 4, comp on 2 and 4 (not on 1 and 3)
# F7 on 2, Bb7 on 4, etc.
piano_notes = [
    # Bar 2
    # F7: F, A, C, E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    # Bar 3
    # A7: A, C#, E, G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),
    # Bar 4
    # C7: C, E, G, B
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
]
piano.notes.extend(piano_notes)

# Sax (Dante)
# Motif: F, G#, B, F (sings, leaves it hanging)
sax_notes = [
    # Bar 2: F, G#, B
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=71, start=2.125, end=2.5),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.875),
    pretty_midi.Note(velocity=110, pitch=68, start=2.875, end=3.125),
    pretty_midi.Note(velocity=110, pitch=71, start=3.125, end=3.5),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=68, start=3.875, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
