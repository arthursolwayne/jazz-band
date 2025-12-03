
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
hihat_times = [bar1_start + 0.375 * i for i in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Marcus: Walking bass line in Fm (F2, Ab2, D2, G2, etc.)
bass_notes = [
    (bar2_start + 0.375, 36),  # F2
    (bar2_start + 0.75, 40),  # Ab2
    (bar2_start + 1.125, 38), # D2
    (bar2_start + 1.5, 43),   # G2
    (bar2_start + 1.875, 36), # F2
    (bar2_start + 2.25, 40),  # Ab2
    (bar2_start + 2.625, 38), # D2
    (bar2_start + 3.0, 43)    # G2
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bbm7 (Bb, Db, F, G)
# Bar 4: Eb7 (Eb, G, Bb, D)
# Comp on 2 and 4

# Bar 2: Fm7
diane_notes = [
    (bar2_start + 0.75, 71), # F (C4)
    (bar2_start + 0.75, 67), # Ab (E4)
    (bar2_start + 0.75, 60), # C (C4)
    (bar2_start + 0.75, 62), # D (D4)
]

for start, pitch in diane_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.2)
    piano.notes.append(note)

# Bar 3: Bbm7
bar3_start = 3.0
bar3_end = 4.5
diane_notes = [
    (bar3_start + 0.75, 70), # Bb (Bb4)
    (bar3_start + 0.75, 66), # Db (Db4)
    (bar3_start + 0.75, 69), # F (F4)
    (bar3_start + 0.75, 67), # G (G4)
]

for start, pitch in diane_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.2)
    piano.notes.append(note)

# Bar 4: Eb7
bar4_start = 4.5
bar4_end = 6.0
diane_notes = [
    (bar4_start + 0.75, 67), # Eb (Eb4)
    (bar4_start + 0.75, 71), # G (G4)
    (bar4_start + 0.75, 70), # Bb (Bb4)
    (bar4_start + 0.75, 69), # D (D4)
]

for start, pitch in diane_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.2)
    piano.notes.append(note)

# Dante: Tenor sax melody (start in bar 2)
# Motif: F - Ab - D - F (intervallic movement, not scales)
sax_notes = [
    (bar2_start, 64),   # F (F4)
    (bar2_start + 0.5, 61), # Ab (Ab4)
    (bar2_start + 0.75, 67), # D (D4)
    (bar2_start + 1.5, 64), # F (F4)
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.2)
    sax.notes.append(note)

# Bar 3 and 4: Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar3_start = 3.0
bar3_end = 4.5
kick_times = [bar3_start + 0.375, bar3_start + 1.125]
snare_times = [bar3_start + 0.75, bar3_start + 1.5]
hihat_times = [bar3_start + 0.375 * i for i in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

bar4_start = 4.5
bar4_end = 6.0
kick_times = [bar4_start + 0.375, bar4_start + 1.125]
snare_times = [bar4_start + 0.75, bar4_start + 1.5]
hihat_times = [bar4_start + 0.375 * i for i in range(4)]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
