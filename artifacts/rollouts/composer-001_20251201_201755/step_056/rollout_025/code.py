
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
snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)
drums.notes.extend([snare1, snare2])

# Hi-hat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar1_start + i * 0.375
    end = start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start, end=bar2_start + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 0.75, end=bar2_start + 1.125),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar2_start + 1.125, end=bar2_start + 1.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=bar2_start + 1.5, end=bar2_start + 1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar2_start + 1.875, end=bar2_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=bar2_start + 2.25, end=bar2_start + 2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar2_start + 2.625, end=bar2_start + 3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_end),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start, end=bar2_end),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start, end=bar2_end),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=bar2_start, end=bar2_end),  # C#5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start, end=bar2_start + 0.75),  # B4
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start + 2.25, end=bar2_start + 3.0),  # B4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=bar3_start, end=bar3_start + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar3_start + 0.375, end=bar3_start + 0.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=bar3_start + 0.75, end=bar3_start + 1.125),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar3_start + 1.125, end=bar3_start + 1.5),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=bar3_start + 1.5, end=bar3_start + 1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar3_start + 1.875, end=bar3_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=bar3_start + 2.25, end=bar3_start + 2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar3_start + 2.625, end=bar3_start + 3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=bar3_start, end=bar3_end),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=bar3_start, end=bar3_end),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=bar3_start, end=bar3_end),  # F#5
    pretty_midi.Note(velocity=100, pitch=79, start=bar3_start, end=bar3_end),  # A5
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=bar3_start, end=bar3_start + 0.75),  # D5
    pretty_midi.Note(velocity=110, pitch=69, start=bar3_start + 1.125, end=bar3_start + 1.5),  # B5
    pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 2.25, end=bar3_start + 3.0),  # D5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=bar4_start, end=bar4_start + 0.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=bar4_start + 0.75, end=bar4_start + 1.125),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar4_start + 1.125, end=bar4_start + 1.5),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=bar4_start + 1.5, end=bar4_start + 1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=bar4_start + 1.875, end=bar4_start + 2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=bar4_start + 2.25, end=bar4_start + 2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=41, start=bar4_start + 2.625, end=bar4_start + 3.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start, end=bar4_end),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=bar4_start, end=bar4_end),  # B5
    pretty_midi.Note(velocity=100, pitch=79, start=bar4_start, end=bar4_end),  # D6
    pretty_midi.Note(velocity=100, pitch=74, start=bar4_start, end=bar4_end),  # F5
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=bar4_start, end=bar4_start + 0.75),  # B5
    pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 1.125, end=bar4_start + 1.5),  # D5
    pretty_midi.Note(velocity=110, pitch=65, start=bar4_start + 2.25, end=bar4_start + 3.0),  # B4
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar4_notes = []
for i in range(0, 4):
    start = bar4_start + i * 0.375
    end = start + 0.125
    bar4_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))
drums.notes.extend(bar4_notes)

kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)
drums.notes.extend([kick1, kick2])

snare1 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare2 = pretty_midi.Note(velocity=110, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)
drums.notes.extend([snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
