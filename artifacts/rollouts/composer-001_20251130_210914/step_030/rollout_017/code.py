
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bb -> Ab -> F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125), # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=3.125, end=3.25), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=4.125, end=4.25), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.125), # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25), # Bb
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.5), # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0), # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    time = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=time + 0.75, end=time + 1.125)
# Snare on 2 and 4
for bar in range(2, 4):
    time = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=time + 0.75, end=time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=time + 1.875, end=time + 2.0)
# Hihat on every eighth
for bar in range(2, 4):
    time = 1.5 + (bar - 2) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.1875, end=time + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
