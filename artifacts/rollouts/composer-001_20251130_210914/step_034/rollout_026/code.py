
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

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=53, start=2.625, end=3.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # E
    # Bar 2, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # E
    # Bar 3, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # E
    # Bar 3, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # E
    # Bar 4, beat 2 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # E
    # Bar 4, beat 4 (F7)
    pretty_midi.Note(velocity=90, pitch=53, start=6.0, end=6.375),  # G
    pretty_midi.Note(velocity=90, pitch=55, start=6.0, end=6.375),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=6.0, end=6.375),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=6.0, end=6.375),  # E
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2, beat 1: F (48)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),
    # Bar 2, beat 2: Ab (50)
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    # Bar 2, beat 3: Bb (52)
    pretty_midi.Note(velocity=100, pitch=52, start=2.625, end=3.0),
    # Bar 2, beat 4: C (55)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    # Bar 3, beat 1: F (48)
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),
    # Bar 3, beat 2: Ab (50)
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125),
    # Bar 3, beat 3: Bb (52)
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),
    # Bar 3, beat 4: C (55)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    # Bar 4, beat 1: F (48)
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25),
    # Bar 4, beat 2: Ab (50)
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625),
    # Bar 4, beat 3: Bb (52)
    pretty_midi.Note(velocity=100, pitch=52, start=5.625, end=6.0),
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
