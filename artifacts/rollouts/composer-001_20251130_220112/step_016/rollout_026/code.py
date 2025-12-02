
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F#
    # Bar 3: C7 (C E G Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # Bb
    # Bar 4: D7 again with chromatic passing
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F#
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (D G Bb)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # F#
    # Bar 4: Come back and finish it (C D G)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: continue for bars 2-4
# Bar 2 (1.5 - 3.0s)
for start in [1.5, 1.875, 2.25, 2.625]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
for start in [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125]:
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)  # Hi-hat on every eighth

# Bar 3 (3.0 - 4.5s)
for start in [3.0, 3.375, 3.75, 4.125]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
for start in [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]:
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)  # Hi-hat on every eighth

# Bar 4 (4.5 - 6.0s)
for start in [4.5, 4.875, 5.25, 5.625]:
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)  # Kick on 1 and 3
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)  # Snare on 2 and 4
for start in [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]:
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875)  # Hi-hat on every eighth

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
