
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + 0.1875, bar1_start + 0.375, bar1_start + 0.5625, bar1_start + 0.75, bar1_start + 0.9375, bar1_start + 1.125, bar1_start + 1.3125, bar1_start + 1.5]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bass line: walking, chromatic approaches, no repeating notes
bass_notes = [
    (bar2_start, 60, 0.75),  # C
    (bar2_start + 0.75, 61, 0.75),  # C#
    (bar2_start + 1.5, 62, 0.75),  # D
    (bar2_start + 2.25, 63, 0.75),  # D#
    (bar3_start, 64, 0.75),  # E
    (bar3_start + 0.75, 65, 0.75),  # F
    (bar3_start + 1.5, 66, 0.75),  # F#
    (bar3_start + 2.25, 67, 0.75),  # G
    (bar4_start, 68, 0.75),  # G#
    (bar4_start + 0.75, 69, 0.75),  # A
    (bar4_start + 1.5, 70, 0.75),  # A#
    (bar4_start + 2.25, 71, 0.75),  # B
]
for start, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (bar2_start + 0.75, 60, 0.25),  # C
    (bar2_start + 0.75, 64, 0.25),  # E
    (bar2_start + 0.75, 67, 0.25),  # G
    (bar2_start + 0.75, 71, 0.25),  # B
    # Bar 3
    (bar3_start + 0.75, 60, 0.25),  # C
    (bar3_start + 0.75, 64, 0.25),  # E
    (bar3_start + 0.75, 67, 0.25),  # G
    (bar3_start + 0.75, 71, 0.25),  # B
    # Bar 4
    (bar4_start + 0.75, 60, 0.25),  # C
    (bar4_start + 0.75, 64, 0.25),  # E
    (bar4_start + 0.75, 67, 0.25),  # G
    (bar4_start + 0.75, 71, 0.25),  # B
]
for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_times = [bar_start + 0.375, bar_start + 1.125]
    snare_times = [bar_start + 0.75, bar_start + 1.5]
    hihat_times = [bar_start + 0.1875, bar_start + 0.375, bar_start + 0.5625, bar_start + 0.75, bar_start + 0.9375, bar_start + 1.125, bar_start + 1.3125, bar_start + 1.5]

    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)

    for t in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)

    for t in hihat_times:
        note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1)
        drums.notes.append(note)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (bar2_start, 66, 0.25),  # D
    (bar2_start + 0.25, 69, 0.25),  # F
    (bar2_start + 0.5, 66, 0.25),  # D
    (bar2_start + 0.75, 69, 0.25),  # F
    (bar3_start, 66, 0.25),  # D
    (bar3_start + 0.25, 69, 0.25),  # F
    (bar3_start + 0.5, 66, 0.25),  # D
    (bar3_start + 0.75, 69, 0.25),  # F
    (bar4_start, 66, 0.25),  # D
    (bar4_start + 0.25, 69, 0.25),  # F
    (bar4_start + 0.5, 66, 0.25),  # D
    (bar4_start + 0.75, 69, 0.25),  # F
]
for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
