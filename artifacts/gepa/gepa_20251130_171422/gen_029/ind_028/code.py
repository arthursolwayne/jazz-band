
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
# Vary dynamics: kick at 40, snare at 60, hihat at 80
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    (36, bar1_start + 0.0, 0.375, 40),     # Kick on 1
    (38, bar1_start + 0.375, 0.375, 60),   # Snare on 2
    (42, bar1_start + 0.0, 0.125, 80),     # Hihat on 1
    (42, bar1_start + 0.125, 0.125, 80),   # Hihat on &1
    (42, bar1_start + 0.25, 0.125, 80),    # Hihat on 2
    (42, bar1_start + 0.375, 0.125, 80),   # Hihat on &2
    (42, bar1_start + 0.5, 0.125, 80),     # Hihat on 3
    (42, bar1_start + 0.625, 0.125, 80),   # Hihat on &3
    (42, bar1_start + 0.75, 0.125, 80),    # Hihat on 4
    (42, bar1_start + 0.875, 0.125, 80),   # Hihat on &4
    (36, bar1_start + 0.75, 0.375, 40),    # Kick on 3
    (38, bar1_start + 0.875, 0.375, 60),   # Snare on 4
]
for note in drum_notes:
    dr = pretty_midi.Note(velocity=note[3], pitch=note[0], start=note[1], end=note[2])
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif (Fm): F, Ab, Bb, D, F
# Phrase: F (start), Ab (ask), Bb (answer), D (resolve), F (return)
# Slight rubato in the first note, then into the rhythm
bar2_start = 1.5
note_duration = 0.375
notes = [
    (65, bar2_start + 0.0, note_duration, 90),     # F (start)
    (62, bar2_start + 0.375, note_duration, 85),   # Ab (ask)
    (62, bar2_start + 0.75, note_duration, 85),    # Bb (answer)
    (67, bar2_start + 1.125, note_duration, 90),   # D (resolve)
    (65, bar2_start + 1.5, note_duration, 90),     # F (return)
    (62, bar2_start + 1.875, note_duration, 85),   # Ab (ask)
    (62, bar2_start + 2.25, note_duration, 85),    # Bb (answer)
    (67, bar2_start + 2.625, note_duration, 90),   # D (resolve)
    (65, bar2_start + 3.0, note_duration, 90),     # F (return)
    (62, bar2_start + 3.375, note_duration, 85),   # Ab (ask)
    (62, bar2_start + 3.75, note_duration, 85),    # Bb (answer)
    (67, bar2_start + 4.125, note_duration, 90),   # D (resolve)
    (65, bar2_start + 4.5, note_duration, 90),     # F (return)
]
for note in notes:
    n = pretty_midi.Note(velocity=note[3], pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass line: chromatic descending approach, then walking
bass_notes = [
    (44, bar2_start + 0.0, note_duration, 60),    # C
    (43, bar2_start + 0.375, note_duration, 55),  # Bb
    (42, bar2_start + 0.75, note_duration, 50),   # A
    (41, bar2_start + 1.125, note_duration, 45),  # G
    (43, bar2_start + 1.5, note_duration, 50),    # Bb
    (44, bar2_start + 1.875, note_duration, 55),  # C
    (45, bar2_start + 2.25, note_duration, 60),   # C#
    (46, bar2_start + 2.625, note_duration, 65),  # D
    (43, bar2_start + 3.0, note_duration, 50),    # Bb
    (44, bar2_start + 3.375, note_duration, 55),  # C
    (45, bar2_start + 3.75, note_duration, 60),   # C#
    (46, bar2_start + 4.125, note_duration, 65),  # D
    (43, bar2_start + 4.5, note_duration, 50),    # Bb
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=note[3], pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano comping: 7th chords on 2 and 4
# Fm7 = F, Ab, C, D
# Bb7 = Bb, D, F, Ab
piano_notes = [
    (64, bar2_start + 0.0, 0.375, 60),     # F
    (61, bar2_start + 0.0, 0.375, 65),     # Ab
    (60, bar2_start + 0.0, 0.375, 70),     # C
    (62, bar2_start + 0.0, 0.375, 65),     # D
    (62, bar2_start + 0.375, 0.375, 50),   # Rest
    (62, bar2_start + 0.75, 0.375, 60),    # Bb
    (64, bar2_start + 0.75, 0.375, 65),    # D
    (61, bar2_start + 0.75, 0.375, 70),    # F
    (60, bar2_start + 0.75, 0.375, 65),    # Ab
    (62, bar2_start + 1.125, 0.375, 50),   # Rest
    (64, bar2_start + 1.5, 0.375, 60),     # F
    (61, bar2_start + 1.5, 0.375, 65),     # Ab
    (60, bar2_start + 1.5, 0.375, 70),     # C
    (62, bar2_start + 1.5, 0.375, 65),     # D
    (62, bar2_start + 1.875, 0.375, 50),   # Rest
    (62, bar2_start + 2.25, 0.375, 60),    # Bb
    (64, bar2_start + 2.25, 0.375, 65),    # D
    (61, bar2_start + 2.25, 0.375, 70),    # F
    (60, bar2_start + 2.25, 0.375, 65),    # Ab
    (62, bar2_start + 2.625, 0.375, 50),   # Rest
    (64, bar2_start + 3.0, 0.375, 60),     # F
    (61, bar2_start + 3.0, 0.375, 65),     # Ab
    (60, bar2_start + 3.0, 0.375, 70),     # C
    (62, bar2_start + 3.0, 0.375, 65),     # D
    (62, bar2_start + 3.375, 0.375, 50),   # Rest
    (62, bar2_start + 3.75, 0.375, 60),    # Bb
    (64, bar2_start + 3.75, 0.375, 65),    # D
    (61, bar2_start + 3.75, 0.375, 70),    # F
    (60, bar2_start + 3.75, 0.375, 65),    # Ab
    (62, bar2_start + 4.125, 0.375, 50),   # Rest
    (64, bar2_start + 4.5, 0.375, 60),     # F
    (61, bar2_start + 4.5, 0.375, 65),     # Ab
    (60, bar2_start + 4.5, 0.375, 70),     # C
    (62, bar2_start + 4.5, 0.375, 65),     # D
]
for note in piano_notes:
    n = pretty_midi.Note(velocity=note[3], pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(n)

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Add some dynamic variation and fill
for bar in range(2, 5):
    bar_start = bar2_start + (bar - 2) * 1.5
    kick = pretty_midi.Note(velocity=60 if bar % 2 == 0 else 50, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=70 if bar % 2 == 0 else 60, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat = []
    for i in range(0, 4):
        hihat_note = pretty_midi.Note(velocity=80 if i % 2 == 0 else 75, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.125)
        hihat.append(hihat_note)
    drums.notes.append(kick)
    drums.notes.append(snare)
    for h in hihat:
        drums.notes.append(h)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
