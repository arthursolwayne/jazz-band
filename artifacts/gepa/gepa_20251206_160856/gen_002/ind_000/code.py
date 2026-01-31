
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2 (F - C)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),    # F (D2)
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # F
    # Bar 3 (Bb - F)
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),   # Bb
    # Bar 4 (C - G)
    pretty_midi.Note(velocity=90, pitch=49, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A (C5)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C (B4)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # E (D5)
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb (G4)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # D (A4)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F (A4)
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Ab (C5)
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C (B4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # E (D5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G (E5)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # B (F5)
]
piano.notes.extend(piano_notes)

# Sax: Motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif (F, G, Bb, A)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F (A4)
    pretty_midi.Note(velocity=110, pitch=55, start=1.875, end=2.25), # G (B4)
    pretty_midi.Note(velocity=110, pitch=51, start=2.25, end=2.625), # Bb (G4)
    pretty_midi.Note(velocity=110, pitch=50, start=2.625, end=3.0),  # A (F4)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=50, start=3.0, end=3.375),  # A
    # Bar 4: Come back and finish (turn around)
    pretty_midi.Note(velocity=110, pitch=50, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=110, pitch=57, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    hihat_notes = [
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375)
        for i in range(4)
    ]
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
