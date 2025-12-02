
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # A (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # F (root)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # A (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),   # F (root)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # D (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # F (root)
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # A (fifth)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last beat of each bar
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # E
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # F
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb
])
# Repeat the same chords on the 2nd and 4th beats of each bar (comping)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # E

    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F

    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25),  # Bb
])
piano.notes.extend(piano_notes)

# Sax (Dante): Start motif, leave it hanging, come back to finish
# Motif: F (60) - Bb (62) - D (65) - F (60) - (leave hanging on D)
# Repeat: D (65) - Bb (62) - F (60) - resolve
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # F

    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    time_start = bar * 1.5
    for beat in [0, 2]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time_start + beat * 0.75, end=time_start + beat * 0.75 + 0.375)
        snare = pretty_midi.Note(velocity=100, pitch=38, start=time_start + (beat + 1) * 0.75, end=time_start + (beat + 1) * 0.75 + 0.375)
        for eighth in range(0, 4):
            hihat = pretty_midi.Note(velocity=100, pitch=42, start=time_start + eighth * 0.375, end=time_start + eighth * 0.375 + 0.375)
            drums.notes.append(hihat)
        drums.notes.append(kick)
        drums.notes.append(snare)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
