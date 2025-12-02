
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

# Bassline: Walking in F, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F - Gb - G - A
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),  # A

    # Bar 3: Bb - B - C - D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # D

    # Bar 4: Eb - E - F - G
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 1
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=70, pitch=76, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=70, pitch=74, start=1.5, end=1.875),  # C

    # Bar 2: comp on beat 2
    pretty_midi.Note(velocity=70, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=70, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=70, pitch=74, start=1.875, end=2.25),  # C

    # Bar 3: Bb7 on beat 1
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=70, pitch=71, start=3.0, end=3.375),  # F

    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=70, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=70, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=70, pitch=71, start=3.375, end=3.75),  # F

    # Bar 4: Eb7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=70, pitch=67, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=68, start=4.5, end=4.875),  # B

    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=70, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=70, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=70, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=70, pitch=68, start=4.875, end=5.25),  # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: F - G - Bb
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.0, end=2.25),  # Bb

    # Bar 3: Rest
    pretty_midi.Note(velocity=0, pitch=0, start=3.0, end=3.5),  # Rest

    # Bar 4: F - G - Bb (finish the motif)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=72, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=5.0, end=5.25),  # Bb
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)

drums.notes.extend(
    [pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375) for bar_start in [1.5, 3.0, 4.5]],
    [pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5) for bar_start in [1.5, 3.0, 4.5]],
    [pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875) for bar_start in [1.5, 3.0, 4.5]],
    [pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0) for bar_start in [1.5, 3.0, 4.5]],
    [pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.1875, end=bar_start + i * 0.1875 + 0.1875) for bar_start in [1.5, 3.0, 4.5] for i in range(8)]
)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
