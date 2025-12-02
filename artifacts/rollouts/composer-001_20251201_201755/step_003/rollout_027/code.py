
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

# Hihat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar1_start + i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bar 2 (1.5 - 3.0s)
# Bass: walking line, D2-G2 (MIDI 38-43), roots and fifths with chromatic approaches
# Root: D2 (38), chromatic approach: C#2 (37)
bass_note1 = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875)
bass_note2 = pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125)
bass_note3 = pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5)
bass_note4 = pretty_midi.Note(velocity=90, pitch=38, start=2.5, end=2.875)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D-F#-A-C)
piano_note1 = pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.0)  # D
piano_note2 = pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.0)  # F#
piano_note3 = pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0)  # A
piano_note4 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0)  # C
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), E4 (64), F#4 (66), D4 (62)
sax_note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75)
sax_note2 = pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0)
sax.notes.extend([sax_note1, sax_note2])

# Drums: same pattern as bar 1
bar2_start = 1.5
bar2_end = 3.0

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.875, end=bar2_start + 2.0)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar2_start + i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 3 (3.0 - 4.5s)
# Bass: walking line (D2-G2), roots and fifths with chromatic approaches
# Root: G2 (43), chromatic approach: F#2 (42)
bass_note1 = pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375)
bass_note2 = pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.625)
bass_note3 = pretty_midi.Note(velocity=90, pitch=47, start=3.625, end=4.0)
bass_note4 = pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.375)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bm7 (B-D-F#-A)
piano_note1 = pretty_midi.Note(velocity=100, pitch=56, start=3.0, end=3.5)  # B
piano_note2 = pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.5)  # D
piano_note3 = pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5)  # F#
piano_note4 = pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.5)  # A
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Drums: same pattern
bar3_start = 3.0
bar3_end = 4.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.875, end=bar3_start + 2.0)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar3_start + i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 4 (4.5 - 6.0s)
# Bass: walking line (D2-G2), roots and fifths with chromatic approaches
# Root: D2 (38), chromatic approach: C#2 (37)
bass_note1 = pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875)
bass_note2 = pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.125)
bass_note3 = pretty_midi.Note(velocity=90, pitch=43, start=5.125, end=5.5)
bass_note4 = pretty_midi.Note(velocity=90, pitch=38, start=5.5, end=5.875)
bass.notes.extend([bass_note1, bass_note2, bass_note3, bass_note4])

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C-E-G-B)
piano_note1 = pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0)  # C
piano_note2 = pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0)  # E
piano_note3 = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0)  # G
piano_note4 = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0)  # B
piano.notes.extend([piano_note1, piano_note2, piano_note3, piano_note4])

# Sax: Finish the motif
# D4 (62) at the end, resolving the hanging note from bar 2
sax_note3 = pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75)
sax.notes.append(sax_note3)

# Drums: same pattern
bar4_start = 4.5
bar4_end = 6.0

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.875, end=bar4_start + 2.0)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar4_start + i * 0.375
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.125))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
