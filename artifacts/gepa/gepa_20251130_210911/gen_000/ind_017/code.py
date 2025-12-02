
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # Bb
    # Bar 5 (comp on 2 and 4)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif - D, E, F, D (1.5-2.0s), then leave it hanging, return at 4.5-5.0s
# No scale runs, just a short, singing motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),   # D
    # Return at 4.5-5.0s
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),   # E
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
