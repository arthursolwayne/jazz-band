
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
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with sax melody
# Sax motif: Fm7 -> Bb -> Eb -> Ab -> Fm7
# Bar 2: Fm7 (F, Ab, Bb, D)
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875)  # F
note2 = pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875)  # Ab
note3 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875)  # Bb
note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)  # D
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Eb -> Ab -> C -> F
note5 = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375)  # Eb
note6 = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375)  # Ab
note7 = pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375)  # C
note8 = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375)  # F
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: Ab -> C -> F -> Bb
note9 = pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875)  # Ab
note10 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875)  # C
note11 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875)  # F
note12 = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875)  # Bb
sax.notes.extend([note9, note10, note11, note12])

# Bass line: Walking line in Fm
# Bar 2: F -> Gb -> Ab -> A
note13 = pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875)
note14 = pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25)
note15 = pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625)
note16 = pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0)
bass.notes.extend([note13, note14, note15, note16])

# Bar 3: Bb -> C -> Db -> D
note17 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375)
note18 = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75)
note19 = pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125)
note20 = pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5)
bass.notes.extend([note17, note18, note19, note20])

# Bar 4: F -> Gb -> Ab -> A
note21 = pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875)
note22 = pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25)
note23 = pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625)
note24 = pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0)
bass.notes.extend([note21, note22, note23, note24])

# Piano comping: 7th chords on 2 and 4
# Bar 2: Fm7 on 2
note25 = pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25)  # F
note26 = pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25)  # Ab
note27 = pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25)  # Bb
note28 = pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25)  # D
piano.notes.extend([note25, note26, note27, note28])

# Bar 3: Fm7 on 2
note29 = pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75)  # F
note30 = pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75)  # Ab
note31 = pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75)  # Bb
note32 = pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75)  # D
piano.notes.extend([note29, note30, note31, note32])

# Bar 4: Fm7 on 2
note33 = pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25)  # F
note34 = pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25)  # Ab
note35 = pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25)  # Bb
note36 = pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25)  # D
piano.notes.extend([note33, note34, note35, note36])

# Bar 2-4: Drums continue
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
