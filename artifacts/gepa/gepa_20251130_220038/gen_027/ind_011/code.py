
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus on walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # F
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.0),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F7
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: Dante, melody, one short motif
sax_notes = [
    # Bar 2: Start the motif (1.5 - 2.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Bb
    # Bar 3: Leave it hanging (2.0 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Bb
    # Bar 4: Finish the motif (3.0 - 4.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Bb
    # Bar 4: Continue and resolve (4.0 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    hihat = []
    for i in range(4):
        hihat.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))
    drums.notes.extend([kick, kick2, snare, snare2] + hihat)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
