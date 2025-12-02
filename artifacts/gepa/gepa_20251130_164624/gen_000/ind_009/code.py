
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Bass line: Walking line with chromatic approaches
bass_notes = [
    # Bar 2: Fm7 -> Bb7
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # G
    # Bar 3: Bb7 -> Eb7
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # B
    # Bar 4: Eb7 -> Fm7
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=55, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C
    # Bar 3: Bb7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
    # Bar 4: Eb7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=6.375, end=6.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=6.375, end=6.75),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=6.375, end=6.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=6.375, end=6.75),  # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # A
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
bar2_drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(bar2_drum_notes)

bar3_drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(bar3_drum_notes)

bar4_drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(bar4_drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_shot.mid")
