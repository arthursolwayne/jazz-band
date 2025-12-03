
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

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 4):
    start = bar1_start + i * 0.375
    end = start + 0.125
    hihat_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend([kick1, kick2, snare1, snare2] + hihat_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = []
# Root F (MIDI 53) and fifth C (MIDI 60)
# Chromatic approach to F
bass_notes.append(pretty_midi.Note(velocity=100, pitch=52, start=bar2_start, end=bar2_start + 0.375))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=bar2_start + 0.375, end=bar2_start + 0.75))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 0.75, end=bar2_start + 1.125))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=59, start=bar2_start + 1.125, end=bar2_start + 1.5))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=53, start=bar2_start + 1.5, end=bar2_start + 1.875))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=54, start=bar2_start + 1.875, end=bar2_start + 2.25))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 2.25, end=bar2_start + 2.625))
bass_notes.append(pretty_midi.Note(velocity=100, pitch=59, start=bar2_start + 2.625, end=bar2_start + 3.0))

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start, end=bar2_end),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start, end=bar2_end),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=bar2_start, end=bar2_end),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start, end=bar2_end),  # Eb
]

# Bar 3: Bb7 (Bb, D, F, Ab) - open voicing
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.5, end=bar2_end),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.5, end=bar2_end),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.5, end=bar2_end),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 1.5, end=bar2_end),  # Ab
]

# Bar 4: Cm7 (C, Eb, G, Bb) - open voicing
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=72, start=bar2_start + 3.0, end=bar2_end),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 3.0, end=bar2_end),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=bar2_start + 3.0, end=bar2_end),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 3.0, end=bar2_end),  # Bb
]

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_drums_start = bar2_start
bar3_drums_start = bar2_start + 1.5
bar4_drums_start = bar2_start + 3.0

# Bar 2
kick1_bar2 = pretty_midi.Note(velocity=100, pitch=36, start=bar2_drums_start, end=bar2_drums_start + 0.375)
snare1_bar2 = pretty_midi.Note(velocity=100, pitch=38, start=bar2_drums_start + 0.75, end=bar2_drums_start + 0.875)
hihat_notes_bar2 = []
for i in range(0, 4):
    start = bar2_drums_start + i * 0.375
    end = start + 0.125
    hihat_notes_bar2.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 3
kick1_bar3 = pretty_midi.Note(velocity=100, pitch=36, start=bar3_drums_start, end=bar3_drums_start + 0.375)
snare1_bar3 = pretty_midi.Note(velocity=100, pitch=38, start=bar3_drums_start + 0.75, end=bar3_drums_start + 0.875)
hihat_notes_bar3 = []
for i in range(0, 4):
    start = bar3_drums_start + i * 0.375
    end = start + 0.125
    hihat_notes_bar3.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 4
kick1_bar4 = pretty_midi.Note(velocity=100, pitch=36, start=bar4_drums_start, end=bar4_drums_start + 0.375)
snare1_bar4 = pretty_midi.Note(velocity=100, pitch=38, start=bar4_drums_start + 0.75, end=bar4_drums_start + 0.875)
hihat_notes_bar4 = []
for i in range(0, 4):
    start = bar4_drums_start + i * 0.375
    end = start + 0.125
    hihat_notes_bar4.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

drums.notes.extend([kick1_bar2, snare1_bar2] + hihat_notes_bar2 + [kick1_bar3, snare1_bar3] + hihat_notes_bar3 + [kick1_bar4, snare1_bar4] + hihat_notes_bar4)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), Ab (60), C (72), Eb (67)
# Start it on bar 2, leave it hanging, come back on bar 4

# Bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=60, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5)
]

# Bar 4
sax_notes += [
    pretty_midi.Note(velocity=110, pitch=65, start=bar4_drums_start, end=bar4_drums_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=60, start=bar4_drums_start + 0.375, end=bar4_drums_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=72, start=bar4_drums_start + 0.75, end=bar4_drums_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=67, start=bar4_drums_start + 1.125, end=bar4_drums_start + 1.5)
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
