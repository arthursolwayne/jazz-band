
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

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    # Bar 3 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    # Bar 4 (D7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # G
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # D
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875), # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),   # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),   # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),   # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),   # Snare on 4
]
drums.notes.extend(drum_notes)

# Add hihat on every eighth for bars 2-4
for bar in range(2, 5):
    for eighth in range(0, 4):
        start = 1.5 + (bar - 2) * 1.5 + eighth * 0.375
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
