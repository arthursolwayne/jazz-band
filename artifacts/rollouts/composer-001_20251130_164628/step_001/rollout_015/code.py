
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.875, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.625),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=2.875),
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # G
    # Bar 3 (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.3125),  # G
    # Bar 4 (come back and finish it)
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.6875, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hihat on every eighth
    for eighth in range(0, 8):
        start = start_time + eighth * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_shorter_intro.mid")
