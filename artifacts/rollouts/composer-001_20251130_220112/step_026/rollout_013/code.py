
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 2: D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 on 1, G7 on 2, Cm7 on 3, F7 on 4
piano_notes = [
    # Dm7 (1)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),  # D
    # G7 (2)
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=1.875, end=2.25),  # F
    # Cm7 (3)
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),  # Bb
    # F7 (4)
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=77, start=2.625, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
for bar in range(1):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: Motif in Dm, start on bar 2
# Motif: D - Eb - F - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.0625, end=2.25),
    # Rest of bar
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=100, pitch=64, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=60, start=2.8125, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 3: D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 on 1, G7 on 2, Cm7 on 3, F7 on 4
piano_notes = [
    # Dm7 (1)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # D
    # G7 (2)
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75),  # F
    # Cm7 (3)
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # Bb
    # F7 (4)
    pretty_midi.Note(velocity=80, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5),  # E
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
for bar in range(1):
    start = 3.0 + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: Motif in Dm, start on bar 3
# Motif: D - Eb - F - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75),
    # Rest of bar
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.3125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    # Bar 4: D - C - Eb - F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 on 1, G7 on 2, Cm7 on 3, F7 on 4
piano_notes = [
    # Dm7 (1)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.875),  # D
    # G7 (2)
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25),  # F
    # Cm7 (3)
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # Bb
    # F7 (4)
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=77, start=5.625, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
for bar in range(1):
    start = 4.5 + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Sax: Motif in Dm, start on bar 4
# Motif: D - Eb - F - C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.0625, end=5.25),
    # Rest of bar
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=64, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=60, start=5.8125, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
