
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
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + 0.1875, bar1_start + 0.375, bar1_start + 0.5625, bar1_start + 0.75,
               bar1_start + 0.9375, bar1_start + 1.125, bar1_start + 1.3125, bar1_start + 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5
bar_end = 6.0
bass_notes = [
    # Bar 2
    (bar2_start, 48, 100, 0.375),  # F
    (bar2_start + 0.375, 47, 100, 0.375),  # Eb
    (bar2_start + 0.75, 49, 100, 0.375),  # Gb
    (bar2_start + 1.125, 50, 100, 0.375),  # Ab
    # Bar 3
    (bar3_start, 50, 100, 0.375),  # Ab
    (bar3_start + 0.375, 51, 100, 0.375),  # Bb
    (bar3_start + 0.75, 49, 100, 0.375),  # Gb
    (bar3_start + 1.125, 48, 100, 0.375),  # F
    # Bar 4
    (bar4_start, 48, 100, 0.375),  # F
    (bar4_start + 0.375, 47, 100, 0.375),  # Eb
    (bar4_start + 0.75, 49, 100, 0.375),  # Gb
    (bar4_start + 1.125, 50, 100, 0.375),  # Ab
]
for t, p, v, d in bass_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (bar2_start + 0.75, 63, 100, 0.375),  # Bb7
    (bar2_start + 0.75, 60, 100, 0.375),  # F
    (bar2_start + 0.75, 64, 100, 0.375),  # Db
    (bar2_start + 0.75, 67, 100, 0.375),  # G
    # Bar 3
    (bar3_start + 0.75, 63, 100, 0.375),  # Bb7
    (bar3_start + 0.75, 60, 100, 0.375),  # F
    (bar3_start + 0.75, 64, 100, 0.375),  # Db
    (bar3_start + 0.75, 67, 100, 0.375),  # G
    # Bar 4
    (bar4_start + 0.75, 63, 100, 0.375),  # Bb7
    (bar4_start + 0.75, 60, 100, 0.375),  # F
    (bar4_start + 0.75, 64, 100, 0.375),  # Db
    (bar4_start + 0.75, 67, 100, 0.375),  # G
]
for t, p, v, d in piano_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (bar2_start, 64, 100, 0.375),  # Gb
    (bar2_start + 0.75, 62, 100, 0.375),  # E
    # Bar 3
    (bar3_start, 64, 100, 0.375),  # Gb
    (bar3_start + 0.375, 62, 100, 0.375),  # E
    (bar3_start + 0.75, 60, 100, 0.375),  # D
    (bar3_start + 1.125, 62, 100, 0.375),  # E
    # Bar 4
    (bar4_start, 60, 100, 0.375),  # D
    (bar4_start + 0.375, 62, 100, 0.375),  # E
    (bar4_start + 0.75, 64, 100, 0.375),  # Gb
]
for t, p, v, d in sax_notes:
    note = pretty_midi.Note(velocity=v, pitch=p, start=t, end=t + d)
    sax.notes.append(note)

# Drums: continue for bars 2-4
for bar_start in [bar2_start, bar3_start, bar4_start]:
    kick_times = [bar_start + 0.375, bar_start + 1.125]
    snare_times = [bar_start + 0.75, bar_start + 1.5]
    hihat_times = [bar_start + 0.1875, bar_start + 0.375, bar_start + 0.5625, bar_start + 0.75,
                   bar_start + 0.9375, bar_start + 1.125, bar_start + 1.3125, bar_start + 1.5]
    for t in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
        drums.notes.append(note)
    for t in snare_times:
        note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
        drums.notes.append(note)
    for t in hihat_times:
        note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
