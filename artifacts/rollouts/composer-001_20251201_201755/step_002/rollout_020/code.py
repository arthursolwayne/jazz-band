
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
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36, 36]
snare_notes = [38, 38]
hihat_notes = [42] * 8

for i in range(2):
    kick_time = bar1_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in range(2):
    snare_time = bar1_start + i * 0.75 + 0.25
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = bar1_start + i * 0.125
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: walking line on Fm (F, Ab, D, Eb)
# Fm root = 53, Ab = 57, D = 50, Eb = 51
# Chromatic approaches: E (50) to F (53), Gb (54) to Ab (57), C (48) to D (50), D (50) to Eb (51)
# Walking bass line
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=57, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=51, start=bar2_start + 1.125, end=bar2_start + 1.5),
]

# Diane: open voicings, resolve on the last chord
# Bar 2: Fm7
# F (53), Ab (57), C (48), D (50)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=bar2_start, end=bar2_end),
    pretty_midi.Note(velocity=90, pitch=57, start=bar2_start, end=bar2_end),
    pretty_midi.Note(velocity=90, pitch=48, start=bar2_start, end=bar2_end),
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start, end=bar2_end),
]

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    kick_time = bar2_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in range(2):
    snare_time = bar2_start + i * 0.75 + 0.25
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = bar2_start + i * 0.125
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Marcus: walking line on Fm (F, Ab, D, Eb)
# Chromatic approaches: E to F, Gb to Ab, C to D, D to Eb
bass_notes += [
    pretty_midi.Note(velocity=90, pitch=53, start=bar3_start, end=bar3_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=54, start=bar3_start + 0.375, end=bar3_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=57, start=bar3_start + 0.75, end=bar3_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 1.125, end=bar3_start + 1.5),
]

# Diane: open voicings, resolve on the last chord
# Bar 3: Fm7 -> Gm7
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=53, start=bar3_start, end=bar3_end),
    pretty_midi.Note(velocity=90, pitch=57, start=bar3_start, end=bar3_end),
    pretty_midi.Note(velocity=90, pitch=48, start=bar3_start, end=bar3_end),
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start, end=bar3_end),
]

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    kick_time = bar3_start + i * 0.75
    kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick)

for i in range(2):
    snare_time = bar3_start + i * 0.75 + 0.25
    snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(snare)

for i in range(8):
    hihat_time = bar3_start + i * 0.125
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(hihat)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Marcus: walking line on Fm (F, Ab, D, Eb)
# Chromatic approaches: E to F, Gb to Ab, C to D, D to Eb
bass_notes += [
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start, end=bar4_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=51, start=bar4_start + 0.375, end=bar4_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=53, start=bar4_start + 0.75, end=bar4_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=57, start=bar4_start + 1.125, end=bar4_start + 1.5),
]

# Diane: open voicings, resolve on the last chord
# Bar 4: Fm7 -> F7
piano_notes += [
    pretty_midi.Note(velocity=90, pitch=53, start=bar4_start, end=bar4_end),
    pretty_midi.Note(velocity=90, pitch=57, start=bar4_start, end=bar4_end),
    pretty_midi.Note(velocity=90, pitch=48, start=bar4_start, end=bar4_end),
    pretty_midi.Note(velocity=90, pitch=55, start=bar4_start, end=bar4_end),
]

# Dante's sax line: one short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (53), Ab (57), Bb (58), F (53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=bar2_start, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=57, start=bar2_start + 0.375, end=bar2_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=58, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=53, start=bar4_start, end=bar4_start + 0.375)
]

# Add notes to instruments
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)
drums.notes.extend(drums.notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
