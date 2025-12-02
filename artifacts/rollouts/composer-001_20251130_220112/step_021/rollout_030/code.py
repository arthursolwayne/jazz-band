
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),   # B
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # Eb
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # G
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Dante, motif starting on bar 2, 1 short motif, make it sing
# F - Bb - C - F (motif), then leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=45, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=49, start=2.0, end=2.125),   # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=110, pitch=45, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.125),   # F
    pretty_midi.Note(velocity=110, pitch=49, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=45, start=3.375, end=3.5),   # F
    pretty_midi.Note(velocity=110, pitch=45, start=4.5, end=4.625),   # F
    pretty_midi.Note(velocity=110, pitch=49, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=45, start=4.875, end=5.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hi-hat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for i in range(0, 8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
