
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: F -> Gb -> G -> Ab
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # Ab
    # Bar 3: Bb -> B -> C -> C#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # C#
    # Bar 4: D -> Eb -> E -> F
    pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),  # D
    # Bar 3: Bb7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # G
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),  # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # Bb
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])

# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
