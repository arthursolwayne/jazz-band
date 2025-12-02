
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375)
kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 1.125, end=bar1_start + 1.5)
drums.notes.extend([kick1, kick2])

# Snare on 2 and 4
snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.875)
snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.875, end=bar1_start + 2.0)
drums.notes.extend([snare1, snare2])

# Hihat on every eighth
hihat_notes = [bar1_start + i * 0.375 for i in range(4)]
for h in hihat_notes:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Sax melody: C - E - G - B, then rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + 1.125, end=bar2_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C (C - B - D - E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=61, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=64, start=bar2_start + 1.125, end=bar2_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# C7 on beat 2
for note in [60, 64, 67, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar2_start + 0.75, end=bar2_start + 1.125))
# C7 on beat 4
for note in [60, 64, 67, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar2_start + 1.875, end=bar2_start + 2.25))
piano.notes.extend(piano_notes)

# Drums: continue same pattern
bar2_kicks = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 1.125, end=bar2_start + 1.5)
]
bar2_snare = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.75, end=bar2_start + 0.875)
]
bar2_hihat = [bar2_start + i * 0.375 for i in range(4)]
for h in bar2_hihat:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)
drums.notes.extend(bar2_kicks)
drums.notes.extend(bar2_snare)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Sax: Rest and then repeat motif, but with a twist (D - F - A - B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + 1.125, end=bar3_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=65, start=bar3_start + 1.5, end=bar3_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=bar3_start + 1.875, end=bar3_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + 2.25, end=bar3_start + 2.625)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach (C - B - D - E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=61, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=64, start=bar3_start + 1.125, end=bar3_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
for note in [62, 65, 69, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar3_start + 0.75, end=bar3_start + 1.125))
for note in [62, 65, 69, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar3_start + 1.875, end=bar3_start + 2.25))
piano.notes.extend(piano_notes)

# Drums: continue same pattern
bar3_kicks = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 1.125, end=bar3_start + 1.5)
]
bar3_snare = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.75, end=bar3_start + 0.875)
]
bar3_hihat = [bar3_start + i * 0.375 for i in range(4)]
for h in bar3_hihat:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)
drums.notes.extend(bar3_kicks)
drums.notes.extend(bar3_snare)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Sax: Complete the motif (C - E - G - B), but with a brief space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=64, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=71, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approach (C - B - D - E)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=61, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=64, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
for note in [60, 64, 67, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar4_start + 0.75, end=bar4_start + 1.125))
for note in [60, 64, 67, 71]:
    piano_notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bar4_start + 1.875, end=bar4_start + 2.25))
piano.notes.extend(piano_notes)

# Drums: continue same pattern
bar4_kicks = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 1.125, end=bar4_start + 1.5)
]
bar4_snare = [
    pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.75, end=bar4_start + 0.875)
]
bar4_hihat = [bar4_start + i * 0.375 for i in range(4)]
for h in bar4_hihat:
    hihat = pretty_midi.Note(velocity=100, pitch=42, start=h, end=h + 0.125)
    drums.notes.append(hihat)
drums.notes.extend(bar4_kicks)
drums.notes.extend(bar4_snare)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
