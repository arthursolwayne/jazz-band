
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1875),  # A
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.1875),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.0),   # E
    # Bar 2, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=74, start=2.0, end=2.1875),  # G
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.1875),  # B
    pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=2.0, end=2.1875),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif repeats, but ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375), # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.5625, end=3.75), # D
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.1875),   # D
    pretty_midi.Note(velocity=80, pitch=74, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=80, pitch=77, start=3.5625, end=3.75),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: A7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5625),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.5625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.5625),  # E
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.5625),  # G
    # Bar 3, beat 4: B7 (B, D, F, A)
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.9375),   # B
    pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=3.9375),   # D
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=3.9375),   # F
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=3.9375),   # A
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif ends, resolves to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # F
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=80, pitch=73, start=4.6875, end=4.875), # G
    pretty_midi.Note(velocity=80, pitch=75, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=76, start=5.0625, end=5.25),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0625),  # C
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.0625),  # E
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=90, pitch=83, start=4.875, end=5.0625),  # B
    # Bar 4, beat 4: D7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.4375),   # D
    pretty_midi.Note(velocity=90, pitch=80, start=5.25, end=5.4375),   # F
    pretty_midi.Note(velocity=90, pitch=82, start=5.25, end=5.4375),   # A
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.4375),   # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
for bar in range(2, 4):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + (i * 0.1875)
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
    drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
                        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
                        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
                        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)])
    for i in range(8):
        start = bar_start + (i * 0.1875)
        end = start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
