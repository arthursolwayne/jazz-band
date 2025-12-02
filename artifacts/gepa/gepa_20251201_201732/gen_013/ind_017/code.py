
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
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)
drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth note
hihat_notes = []
for i in range(0, 4):
    hihat_start = bar1_start + i * 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    hihat_notes.append(hihat)
drums.notes.extend(hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 2: F - Ab - D - C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=35, start=bar2_start, end=bar2_start + 0.375),  # F2
    pretty_midi.Note(velocity=90, pitch=32, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=bar2_start + 0.75, end=bar2_start + 1.125),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5),   # C2
    pretty_midi.Note(velocity=90, pitch=35, start=bar2_start + 1.5, end=bar2_start + 1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=32, start=bar2_start + 1.875, end=bar2_start + 2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=bar2_start + 2.25, end=bar2_start + 2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar2_start + 2.625, end=bar2_start + 3.0),   # C2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, one chord per bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=35, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=32, start=bar2_start, end=bar2_start + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=38, start=bar2_start, end=bar2_start + 0.375),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.875, end=bar2_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth note
for i in range(0, 4):
    hihat_start = bar2_start + i * 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    hihat_notes.append(hihat)
drums.notes.extend(hihat_notes)

# Dante: Tenor sax motif (F, Gb, Ab, Bb)
# Start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=41, start=bar2_start, end=bar2_start + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=40, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Gb4
    pretty_midi.Note(velocity=110, pitch=39, start=bar2_start + 0.75, end=bar2_start + 1.125),  # Ab4
    pretty_midi.Note(velocity=110, pitch=37, start=bar2_start + 1.125, end=bar2_start + 1.5),   # Bb4
    pretty_midi.Note(velocity=110, pitch=41, start=bar2_start + 2.25, end=bar2_start + 2.625),  # F4
    pretty_midi.Note(velocity=110, pitch=40, start=bar2_start + 2.625, end=bar2_start + 3.0),   # Gb4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 3: Ab - D - C - F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=32, start=bar3_start, end=bar3_start + 0.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=bar3_start + 0.375, end=bar3_start + 0.75),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar3_start + 0.75, end=bar3_start + 1.125),  # C2
    pretty_midi.Note(velocity=90, pitch=35, start=bar3_start + 1.125, end=bar3_start + 1.5),   # F2
    pretty_midi.Note(velocity=90, pitch=32, start=bar3_start + 1.5, end=bar3_start + 1.875),  # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.25),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar3_start + 2.25, end=bar3_start + 2.625),  # C2
    pretty_midi.Note(velocity=90, pitch=35, start=bar3_start + 2.625, end=bar3_start + 3.0),   # F2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, one chord per bar, resolve on the last
# Bar 3: Ab7 (Ab, C, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=32, start=bar3_start, end=bar3_start + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=38, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=35, start=bar3_start, end=bar3_start + 0.375),  # F
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.875, end=bar3_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth note
for i in range(0, 4):
    hihat_start = bar3_start + i * 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    hihat_notes.append(hihat)
drums.notes.extend(hihat_notes)

# Dante: Tenor sax motif (Ab, Bb, C, D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=39, start=bar3_start, end=bar3_start + 0.375),  # Ab4
    pretty_midi.Note(velocity=110, pitch=37, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Bb4
    pretty_midi.Note(velocity=110, pitch=40, start=bar3_start + 0.75, end=bar3_start + 1.125),  # C4
    pretty_midi.Note(velocity=110, pitch=41, start=bar3_start + 1.125, end=bar3_start + 1.5),   # D4
    pretty_midi.Note(velocity=110, pitch=39, start=bar3_start + 2.25, end=bar3_start + 2.625),  # Ab4
    pretty_midi.Note(velocity=110, pitch=37, start=bar3_start + 2.625, end=bar3_start + 3.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Marcus: Walking bass line in Fm (F, Ab, D, C)
# Bar 4: D - C - F - Ab
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=bar4_start, end=bar4_start + 0.375),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar4_start + 0.375, end=bar4_start + 0.75),  # C2
    pretty_midi.Note(velocity=90, pitch=35, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F2
    pretty_midi.Note(velocity=90, pitch=32, start=bar4_start + 1.125, end=bar4_start + 1.5),   # Ab2
    pretty_midi.Note(velocity=90, pitch=38, start=bar4_start + 1.5, end=bar4_start + 1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=36, start=bar4_start + 1.875, end=bar4_start + 2.25),  # C2
    pretty_midi.Note(velocity=90, pitch=35, start=bar4_start + 2.25, end=bar4_start + 2.625),  # F2
    pretty_midi.Note(velocity=90, pitch=32, start=bar4_start + 2.625, end=bar4_start + 3.0),   # Ab2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, one chord per bar, resolve on the last
# Bar 4: D7 (D, F, Ab, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar4_start, end=bar4_start + 0.375),  # D
    pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=32, start=bar4_start, end=bar4_start + 0.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=bar4_start, end=bar4_start + 0.375),  # C
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.75 + 0.375)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.875, end=bar4_start + 1.875 + 0.375)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth note
for i in range(0, 4):
    hihat_start = bar4_start + i * 0.375
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.125)
    hihat_notes.append(hihat)
drums.notes.extend(hihat_notes)

# Dante: Tenor sax motif (F, Gb, Ab, Bb) - finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=41, start=bar4_start, end=bar4_start + 0.375),  # F4
    pretty_midi.Note(velocity=110, pitch=40, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Gb4
    pretty_midi.Note(velocity=110, pitch=39, start=bar4_start + 0.75, end=bar4_start + 1.125),  # Ab4
    pretty_midi.Note(velocity=110, pitch=37, start=bar4_start + 1.125, end=bar4_start + 1.5),   # Bb4
    pretty_midi.Note(velocity=110, pitch=35, start=bar4_start + 2.25, end=bar4_start + 2.625),  # F3
    pretty_midi.Note(velocity=110, pitch=34, start=bar4_start + 2.625, end=bar4_start + 3.0),   # Gb3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('four_bar_intro.mid')
