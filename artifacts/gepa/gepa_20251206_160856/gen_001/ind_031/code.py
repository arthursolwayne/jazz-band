
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
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.125))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line: walking line in F, roots and fifths with chromatic approaches
bar2_start = 1.5

bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start, end=bar2_start + 0.375),    # F
    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 0.375, end=bar2_start + 0.75),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=bar2_start + 0.75, end=bar2_start + 1.125),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start + 1.125, end=bar2_start + 1.5),  # F

    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 1.5, end=bar2_start + 1.875),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 1.875, end=bar2_start + 2.25),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 2.25, end=bar2_start + 2.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start + 2.625, end=bar2_start + 3.0),  # F

    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start + 3.0, end=bar2_start + 3.375),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 3.375, end=bar2_start + 3.75),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=bar2_start + 3.75, end=bar2_start + 4.125),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start + 4.125, end=bar2_start + 4.5),  # F

    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 4.5, end=bar2_start + 4.875),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 4.875, end=bar2_start + 5.25),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=bar2_start + 5.25, end=bar2_start + 5.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=bar2_start + 5.625, end=bar2_start + 6.0),  # F
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last beat
bar2_start = 1.5

# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=bar2_start, end=bar2_start + 0.375),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start, end=bar2_start + 0.375),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=bar2_start, end=bar2_start + 0.375),  # E
]

# Bar 3: Gm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=47, start=bar2_start + 1.5, end=bar2_start + 1.875),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=bar2_start + 1.5, end=bar2_start + 1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start + 1.5, end=bar2_start + 1.875),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=bar2_start + 1.5, end=bar2_start + 1.875),  # D
])

# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start + 3.0, end=bar2_start + 3.375),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=bar2_start + 3.0, end=bar2_start + 3.375),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=bar2_start + 3.0, end=bar2_start + 3.375),  # G
    pretty_midi.Note(velocity=100, pitch=61, start=bar2_start + 3.0, end=bar2_start + 3.375),  # Bb
])

# Bar 4 resolve on F
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start + 4.5, end=bar2_start + 4.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=bar2_start + 4.5, end=bar2_start + 4.875),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=bar2_start + 4.5, end=bar2_start + 4.875),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=bar2_start + 4.5, end=bar2_start + 4.875),  # E
])

piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, G, F, G -> F, E, F, E

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=bar2_start + 0.375, end=bar2_start + 0.75),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=bar2_start + 1.125, end=bar2_start + 1.5),  # G

    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start + 3.0, end=bar2_start + 3.375),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=bar2_start + 3.375, end=bar2_start + 3.75),  # E
    pretty_midi.Note(velocity=100, pitch=45, start=bar2_start + 3.75, end=bar2_start + 4.125),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=bar2_start + 4.125, end=bar2_start + 4.5),  # E
]

sax.notes.extend(sax_notes)

# Drums for bars 2-4: same pattern as bar 1, repeated
for i in range(2, 4):
    bar_start = 1.5 + i * 1.5
    bar_end = bar_start + 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    hihat_notes = []
    for j in range(0, 4):
        hihat_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + j * 0.375, end=bar_start + j * 0.375 + 0.125))
    drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
