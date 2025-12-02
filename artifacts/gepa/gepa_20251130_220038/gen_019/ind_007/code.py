
import pretty_midi

# Create a new MIDI file with the desired tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# --- BAR 1: DRUMS ONLY (0.0 - 1.5s) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            hihat_time = time + eighth * 0.1875
            note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(note)

# --- BAR 2: FULL QUARTET (1.5 - 3.0s) ---
# Sax: Melody starts, a four-note motif in D minor, a bit dissonant, with space

sax_notes = [
    (1.5, 62, 0.4),   # D4 (root)
    (2.0, 64, 0.4),   # F#4 (3rd)
    (2.5, 65, 0.4),   # G4 (4th)
    (3.0, 62, 0.4)    # D4 (return to root)
]

for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bass: Walking line in D minor, chromatic approach to D
bass_notes = [
    (1.5, 62, 0.25),   # D2
    (1.75, 61, 0.25),  # C#2 (chromatic)
    (2.0, 60, 0.25),   # C2
    (2.25, 62, 0.25),  # D2
    (2.5, 64, 0.25),   # F#2 (3rd)
    (2.75, 63, 0.25),  # G#2 (chromatic)
    (3.0, 64, 0.25),   # F#2
    (3.25, 62, 0.25)   # D2
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: 7th chords on beats 2 and 4
# Dm7 = D, F, A, C
# G7 = G, B, D, F
# Bm7 = B, D, F#, A
# F#7 = F#, A#, C#, E

piano_notes = [
    # Bar 2: Dm7 on beat 2
    (2.0, 62, 0.25),   # D4
    (2.0, 65, 0.25),   # F4
    (2.0, 69, 0.25),   # A4
    (2.0, 67, 0.25),   # C4
    # G7 on beat 4
    (3.0, 71, 0.25),   # G4
    (3.0, 76, 0.25),   # B4
    (3.0, 62, 0.25),   # D4
    (3.0, 74, 0.25)    # F4
]

for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# --- BAR 3: FULL QUARTET (3.0 - 4.5s) ---
# Sax: Repeat the motif, but with a slight variation, adding space in the second note

sax_notes = [
    (3.0, 62, 0.4),   # D4
    (3.5, 64, 0.4),   # F#4
    (4.0, 62, 0.4),   # D4 (skip G4 for space)
    (4.5, 62, 0.4)    # D4
]

for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bass: Walking line again, with chromatic passing tones
bass_notes = [
    (3.0, 62, 0.25),   # D2
    (3.25, 61, 0.25),  # C#2
    (3.5, 60, 0.25),   # C2
    (3.75, 62, 0.25),  # D2
    (4.0, 64, 0.25),   # F#2
    (4.25, 63, 0.25),  # G#2
    (4.5, 64, 0.25),   # F#2
    (4.75, 62, 0.25)   # D2
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Bm7 on beat 2, F#7 on beat 4
piano_notes = [
    # Bm7 on beat 2
    (3.5, 71, 0.25),   # B4
    (3.5, 62, 0.25),   # D4
    (3.5, 67, 0.25),   # F#4
    (3.5, 69, 0.25),   # A4
    # F#7 on beat 4
    (4.5, 74, 0.25),   # F#4
    (4.5, 78, 0.25),   # A#4
    (4.5, 76, 0.25),   # C#4
    (4.5, 71, 0.25)    # E4
]

for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# --- BAR 4: FULL QUARTET (4.5 - 6.0s) ---
# Sax: Full motif again, resolving with a long note on the last bar
sax_notes = [
    (4.5, 62, 0.4),   # D4
    (5.0, 64, 0.4),   # F#4
    (5.5, 65, 0.4),   # G4
    (6.0, 62, 0.4)    # D4 (longer note)
]

for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bass: Walking line again
bass_notes = [
    (4.5, 62, 0.25),   # D2
    (4.75, 61, 0.25),  # C#2
    (5.0, 60, 0.25),   # C2
    (5.25, 62, 0.25),  # D2
    (5.5, 64, 0.25),   # F#2
    (5.75, 63, 0.25),  # G#2
    (6.0, 64, 0.25),   # F#2
    (6.25, 62, 0.25)   # D2
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano: Dm7 on beat 2, G7 on beat 4
piano_notes = [
    # Dm7 on beat 2
    (5.0, 62, 0.25),   # D4
    (5.0, 65, 0.25),   # F4
    (5.0, 69, 0.25),   # A4
    (5.0, 67, 0.25),   # C4
    # G7 on beat 4
    (6.0, 71, 0.25),   # G4
    (6.0, 76, 0.25),   # B4
    (6.0, 62, 0.25),   # D4
    (6.0, 74, 0.25)    # F4
]

for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Drums: same pattern as bar 1
for bar in range(2, 3):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.15)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.15)
            drums.notes.append(note)
        for eighth in range(2):
            hihat_time = time + eighth * 0.1875
            note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
