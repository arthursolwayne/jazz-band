
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: 0.0 - 1.5s (Drums only)
# Little Ray sets the mood with a tight groove
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # 1 bar at 160 BPM
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for subbeat in range(2):
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time + subbeat * 0.375, end=time + subbeat * 0.375 + 0.05)
        drums.notes.append(note)

# Bar 2: 1.5 - 3.0s (Full quartet)
# Bass: Walking line in F, chromatic approach to Gm7 (F7)
# F - Gb - G - A - Bb - B - C - D - E - F
# Diane: Comp with 7th chords, on 2 and 4
# You: Motif starts here — F, Ab, Bb, A — leave it hanging
# Little Ray: continues groove

# Bass line (walking line in F)
bass_notes = [
    (1.5, 79),   # F (79)
    (1.875, 77), # Gb (77)
    (2.25, 80),  # G (80)
    (2.625, 82), # A (82)
    (3.0, 81),   # Bb (81)
    (3.375, 83), # B (83)
    (3.75, 84),  # C (84)
    (4.125, 86), # D (86)
    (4.5, 88),   # E (88)
    (4.875, 79)  # F (79)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
# Bb7 (Bb, D, F, Ab) on beat 4
piano_notes = [
    # Beat 2 (1.875 - 2.125)
    (1.875, 79),  # F
    (1.875, 82),  # A
    (1.875, 84),  # C
    (1.875, 81),  # Eb

    # Beat 4 (3.375 - 3.625)
    (3.375, 81),  # Bb
    (3.375, 84),  # D
    (3.375, 79),  # F
    (3.375, 82),  # Ab
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif — F (79), Ab (81), Bb (81), A (82) — leave it hanging
# First note (F)
note = pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.65)
sax.notes.append(note)

# Second note (Ab)
note = pretty_midi.Note(velocity=100, pitch=81, start=1.65, end=1.8)
sax.notes.append(note)

# Third note (Bb)
note = pretty_midi.Note(velocity=100, pitch=81, start=1.8, end=1.95)
sax.notes.append(note)

# Fourth note (A)
note = pretty_midi.Note(velocity=100, pitch=82, start=1.95, end=2.1)
sax.notes.append(note)

# Bar 3: 3.0 - 4.5s (Continuation of quartet)
# Bass: Walking line continues
# Piano: 7th chords on 2 and 4
# Drums: Continue the groove
# Sax: No new notes, just sustain the last note (A) until the end

# Bass line (walking line in F)
bass_notes = [
    (3.0, 84),   # C (84)
    (3.375, 86), # D (86)
    (3.75, 88),  # E (88)
    (4.125, 79), # F (79)
    (4.5, 81),   # G (81)
    (4.875, 82), # A (82)
    (5.25, 81),  # Bb (81)
    (5.625, 83), # B (83)
    (6.0, 84),   # C (84)
    (6.375, 79)  # F (79)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
# Bb7 (Bb, D, F, Ab) on beat 4
piano_notes = [
    # Beat 2 (3.875 - 4.125)
    (3.875, 79),  # F
    (3.875, 82),  # A
    (3.875, 84),  # C
    (3.875, 81),  # Eb

    # Beat 4 (5.375 - 5.625)
    (5.375, 81),  # Bb
    (5.375, 84),  # D
    (5.375, 79),  # F
    (5.375, 82),  # Ab
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Continue the groove
for beat in range(4):
    time = 3.0 + (beat * bar_length / 4)
    if beat % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for subbeat in range(2):
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time + subbeat * 0.375, end=time + subbeat * 0.375 + 0.05)
        drums.notes.append(note)

# Bar 4: 4.5 - 6.0s (Final bar)
# Bass: Walking line continues
# Piano: 7th chords on 2 and 4
# Drums: Continue the groove
# Sax: Sustain the last note (A) until the end

# Bass line (walking line in F)
bass_notes = [
    (4.5, 82),   # A (82)
    (4.875, 81), # Bb (81)
    (5.25, 83),  # B (83)
    (5.625, 84), # C (84)
    (6.0, 86),   # D (86)
    (6.375, 88), # E (88)
    (6.75, 79),  # F (79)
    (7.125, 81), # G (81)
    (7.5, 82),   # A (82)
    (7.875, 79)  # F (79)
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
# Bb7 (Bb, D, F, Ab) on beat 4
piano_notes = [
    # Beat 2 (5.875 - 6.125)
    (5.875, 79),  # F
    (5.875, 82),  # A
    (5.875, 84),  # C
    (5.875, 81),  # Eb

    # Beat 4 (7.375 - 7.625)
    (7.375, 81),  # Bb
    (7.375, 84),  # D
    (7.375, 79),  # F
    (7.375, 82),  # Ab
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: Continue the groove
for beat in range(4):
    time = 4.5 + (beat * bar_length / 4)
    if beat % 2 == 0:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    if beat % 2 == 1:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for subbeat in range(2):
        note = pretty_midi.Note(velocity=80, pitch=hihat, start=time + subbeat * 0.375, end=time + subbeat * 0.375 + 0.05)
        drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
