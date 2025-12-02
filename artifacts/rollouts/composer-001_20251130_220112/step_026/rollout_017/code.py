
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

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.5),   # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.875),   # Gb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=2.875, end=3.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.625, end=4.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.375),   # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.125, end=5.5),   # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.5, end=6.0),     # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.625),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.625),  # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.125),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.125),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.75, end=5.125),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (start at 1.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),   # G
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),   # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),   # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),# Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),# Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),  # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 2
]
drums.notes.extend(drum_notes)

# Add hi-hat throughout bars 2-4
for bar in range(2, 5):
    for i in range(0, 4):
        start = bar * 1.5 + i * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
        # Add open hi-hat on the 2nd and 4th eighth notes
        if i == 1 or i == 3:
            pretty_midi.Note(velocity=90, pitch=46, start=start, end=end)

drums.notes.extend(hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
