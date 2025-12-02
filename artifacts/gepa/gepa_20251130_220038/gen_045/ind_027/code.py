
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# -------------------
# Bar 1: Drums Only (0.0 - 1.5s)
# Little Ray sets the mood: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 160 BPM = 1.5 seconds per bar, 0.375 seconds per beat

# Time in seconds
time = 0.0

# Bar 1, beats 1-4
for beat in range(4):
    # Kick on 1 and 3 (beat 0 and 2)
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Snare on 2 and 4 (beat 1 and 3)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.375)
        drums.notes.append(note)
    # Hihat on every eighth (at 0.1875, 0.375, 0.5625, 0.75, etc.)
    for e in range(2):  # 2 eighths per beat
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time + e * 0.1875, end=time + e * 0.1875 + 0.1875)
        drums.notes.append(note)
    time += 0.375

# -------------------
# Bar 2: Full Quartet (1.5 - 3.0s)

# Reset time
time = 1.5

# Bass: Marcus - walking line in Fm, chromatic approaches, no repetition
# Fm = F, Ab, Bb, C, Eb, F, G, Ab
# Bass line: F → G → Ab → Bb (chromatic up)
# Then C → Eb → F → G (chromatic up)
# Then Ab → Bb → C → Eb (chromatic up)
# Then F → G → Ab → Bb (chromatic up)

# Bar 2, beats 1-4
for beat in range(4):
    # Note durations are 0.375s
    if beat == 0:
        note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 0.375)  # G
    elif beat == 1:
        note = pretty_midi.Note(velocity=80, pitch=70, start=time, end=time + 0.375)  # Ab
    elif beat == 2:
        note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 0.375)  # Bb
    elif beat == 3:
        note = pretty_midi.Note(velocity=80, pitch=69, start=time, end=time + 0.375)  # C
    bass.notes.append(note)
    time += 0.375

# Piano: Diane - 7th chords on 2 and 4, comping, angry and moving
# Fm7 = F, Ab, C, Eb
# Bar 2: On beat 2 and 4, play Fm7 (Ab in root position)

# Bar 2, beats 2 and 4
for beat in [1, 3]:  # MIDI time is 0-indexed
    # Fm7 chord: F (53), Ab (60), C (60?), Eb (64)
    # Wait, correct MIDI pitches:
    # F = 53
    # Ab = 60
    # C = 60? No — C is 60. Fm7 = F (53), Ab (60), C (60?), Eb (64)
    # C is 60, Eb is 64
    for pitch in [53, 60, 64]:  # F, Ab, Eb
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)
    time += 0.375

# Saxophone: Dante - the melody, short motif, one phrase, make it sing
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F (53) → Gb (54) → F (53) → Gb (54) — suspended, unresolved

# Bar 2, beat 1: Start the motif
note = pretty_midi.Note(velocity=110, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

note = pretty_midi.Note(velocity=110, pitch=54, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

# Bar 2, beat 3: Leave it hanging, don't resolve yet
note = pretty_midi.Note(velocity=110, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

note = pretty_midi.Note(velocity=110, pitch=54, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

# -------------------
# Bar 3: Repeat Bass, Drums, Piano, but no sax

# Bass: F → G → Ab → Bb
time = 3.0
for beat in range(4):
    if beat == 0:
        note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 0.375)  # G
    elif beat == 1:
        note = pretty_midi.Note(velocity=80, pitch=70, start=time, end=time + 0.375)  # Ab
    elif beat == 2:
        note = pretty_midi.Note(velocity=80, pitch=71, start=time, end=time + 0.375)  # Bb
    elif beat == 3:
        note = pretty_midi.Note(velocity=80, pitch=69, start=time, end=time + 0.375)  # C
    bass.notes.append(note)
    time += 0.375

# Drums: Same pattern as bar 1
time = 3.0
for beat in range(4):
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.375)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.375)
        drums.notes.append(note)
    for e in range(2):
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time + e * 0.1875, end=time + e * 0.1875 + 0.1875)
        drums.notes.append(note)
    time += 0.375

# Piano: same as bar 2, but shifted to beat 2 and 4
time = 3.0
for beat in [1, 3]:  # beats 2 and 4
    for pitch in [53, 60, 64]:  # F, Ab, Eb
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)
    time += 0.375

# -------------------
# Bar 4: Saxophone returns, finishes the motif, ends on Eb (64)

time = 4.5
note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

note = pretty_midi.Note(velocity=110, pitch=53, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

note = pretty_midi.Note(velocity=110, pitch=54, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

note = pretty_midi.Note(velocity=110, pitch=64, start=time, end=time + 0.375)
sax.notes.append(note)
time += 0.375

# -------------------
# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
