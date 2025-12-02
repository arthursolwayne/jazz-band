
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

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=49, start=5.25, end=5.625), # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start motif at bar 2 (1.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # Eb
    # End motif at bar 4 (5.25s)
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125)
# Snare on 2 and 4
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
# Hihat on every eighth
for bar in range(2, 4):
    start_time = 1.5 + bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start_time + i * 0.1875, end=start_time + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
