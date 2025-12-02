
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Time in seconds for each beat: 0.375s (since 160 BPM = 60/160 = 0.375 per beat)
for i in range(4):
    time = i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.375)
        drums.notes.append(note)
    if i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hi-hat on every 8th
    hihat_start = time
    hihat_end = hihat_start + 0.1875  # 1/8 note
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)
    # Next 8th
    hihat_start = time + 0.1875
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

#---------------------------
# BASS: Marcus (walking line, roots and fifths, chromatic approaches)
# Key: F Major (I = F, ii = Gm, iii = Am, IV = C, V = D7, vi = Em)
# Bar 2: Cmaj7 (F7 comp) → Bass plays F, C, G, Bb
# Bar 3: Gm7 (F7 comp) → Bass plays G, D, Bb, C
# Bar 4: Cmaj7 (F7 comp) → Bass plays C, G, E, F

# Bar 2: Cmaj7 (F7 comp), F as root
for i in range(4):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=75, pitch=65 + i, start=time, end=time + 0.375)
    bass.notes.append(note)

# Bar 3: Gm7 (F7 comp), G as root
for i in range(4):
    time = 1.5 + 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=75, pitch=71 + i, start=time, end=time + 0.375)
    bass.notes.append(note)

# Bar 4: Cmaj7 (F7 comp), C as root
for i in range(4):
    time = 1.5 + 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=75, pitch=60 + i, start=time, end=time + 0.375)
    bass.notes.append(note)

#---------------------------
# PIANO: Diane (open voicings, different chord each bar, resolve on the last)

# Bar 2: Cmaj7 (F7 comp) → C E G B
note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.5 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375)
piano.notes.extend([note1, note2, note3, note4])

# Bar 3: Gm7 (F7 comp) → G Bb D F
note1 = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=70, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
note4 = pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 1.5, end=1.5 + 1.5 + 0.375)
piano.notes.extend([note1, note2, note3, note4])

# Bar 4: Cmaj7 (F7 comp) → C E G B
note1 = pretty_midi.Note(velocity=100, pitch=60, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
note2 = pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
note3 = pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
note4 = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 3.0, end=1.5 + 3.0 + 0.375)
piano.notes.extend([note1, note2, note3, note4])

#---------------------------
# SAX: You (Dante) — short motif, singable, leave it hanging in bar 2

# Bar 2: Motif: F - Bb - C - F (rest)
note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.1875)
note2 = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.375, end=1.5 + 0.5625)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.75, end=1.5 + 0.9375)
note4 = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.125, end=1.5 + 1.3125)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Motif continuation — leave it hanging, do not resolve
note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.5, end=1.5 + 1.5 + 0.1875)
note2 = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 1.5 + 0.375, end=1.5 + 1.5 + 0.5625)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.5 + 0.75, end=1.5 + 1.5 + 0.9375)
note4 = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 1.5 + 1.125, end=1.5 + 1.5 + 1.3125)
sax.notes.extend([note1, note2, note3, note4])

# Bar 4: Return to the motif, finish it — F - Bb - C - F
note1 = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 3.0, end=1.5 + 3.0 + 0.1875)
note2 = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 3.0 + 0.375, end=1.5 + 3.0 + 0.5625)
note3 = pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 3.0 + 0.75, end=1.5 + 3.0 + 0.9375)
note4 = pretty_midi.Note(velocity=110, pitch=65, start=1.5 + 3.0 + 1.125, end=1.5 + 3.0 + 1.3125)
sax.notes.extend([note1, note2, note3, note4])

#---------------------------
# DRUMS: Bar 2-4: Full kit, kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Bar 2 (1.5 - 3.0s)
for i in range(4):
    time = 1.5 + i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.375)
        drums.notes.append(note)
    if i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hi-hat on every 8th
    hihat_start = time
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)
    hihat_start = time + 0.1875
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5s)
for i in range(4):
    time = 3.0 + i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.375)
        drums.notes.append(note)
    if i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hi-hat on every 8th
    hihat_start = time
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)
    hihat_start = time + 0.1875
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0s)
for i in range(4):
    time = 4.5 + i * 0.375
    if i % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=KICK, start=time, end=time + 0.375)
        drums.notes.append(note)
    if i % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=SNARE, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hi-hat on every 8th
    hihat_start = time
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)
    hihat_start = time + 0.1875
    hihat_end = hihat_start + 0.1875
    note = pretty_midi.Note(velocity=100, pitch=HIHAT, start=hihat_start, end=hihat_end)
    drums.notes.append(note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
