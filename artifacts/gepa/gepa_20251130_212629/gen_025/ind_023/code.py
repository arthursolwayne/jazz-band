
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
drums = pretty_midi.Instrument(program=0, is_drum=True)

# Define drum pitches
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar (in seconds) at 160 BPM
BAR_LENGTH = 6.0 / 4  # 1.5 seconds per bar
BEAT_LENGTH = BAR_LENGTH / 4  # 0.375 seconds per beat

# Bar 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * BAR_LENGTH + beat * BEAT_LENGTH
        # Hi-hat on every eighth
        for i in range(2):
            hihat_time = time + i * (BEAT_LENGTH / 2)
            hihat_note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(hihat_note)

    # Kick on 1 and 3
    kick_times = [0.0, 2.0]
    for kick_time in kick_times:
        kick_note = pretty_midi.Note(velocity=100, pitch=KICK, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick_note)

    # Snare on 2 and 4
    snare_times = [1.0, 3.0]
    for snare_time in snare_times:
        snare_note = pretty_midi.Note(velocity=90, pitch=SNARE, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare_note)

# Bars 2-4: Full ensemble
# Bar 2
bar = 1
time = bar * BAR_LENGTH

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (0.0, 62),    # D
    (0.375, 63),  # Eb
    (0.75, 61),   # C
    (1.125, 61),  # C
    (1.5, 60),    # Bb
    (1.875, 61),  # C
    (2.25, 62),   # D
    (2.625, 63)   # Eb
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + t, end=time + t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Comp on 2 and 4
chord_times = [1.0, 3.0]
for t in chord_times:
    for pitch in [62, 65, 67, 60]:  # D, F, A, C
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + t, end=time + t + 0.1)
        piano.notes.append(note)

# Sax: Motif - start it, leave it hanging
# Dm motif: D (62) -> F (65) -> A (67) -> C (60)
# Played on beats 1 and 3 (staccato), ending on C at beat 3
sax_notes = [
    (0.0, 62, 0.1),  # D
    (0.375, 65, 0.1),  # F
    (1.125, 67, 0.1),  # A
    (1.5, 60, 0.05)   # C (short, unresolved)
]

for t, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + t, end=time + t + duration)
    sax.notes.append(note)

# Bar 3
bar = 2
time = bar * BAR_LENGTH

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (0.0, 60),    # Bb
    (0.375, 61),  # C
    (0.75, 62),   # D
    (1.125, 63),  # Eb
    (1.5, 62),    # D
    (1.875, 61),  # C
    (2.25, 60),   # Bb
    (2.625, 59)   # B
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + t, end=time + t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
chord_times = [1.0, 3.0]
for t in chord_times:
    for pitch in [62, 65, 67, 60]:  # D, F, A, C
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + t, end=time + t + 0.1)
        piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = bar * BAR_LENGTH + beat * BEAT_LENGTH
    # Hi-hat on every eighth
    for i in range(2):
        hihat_time = time + i * (BEAT_LENGTH / 2)
        hihat_note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

    # Kick on 1 and 3
    if beat in [0, 2]:
        kick_note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(kick_note)

    # Snare on 2 and 4
    if beat in [1, 3]:
        snare_note = pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(snare_note)

# Bar 4
bar = 3
time = bar * BAR_LENGTH

# Bass line: Walking line with chromatic approaches
bass_notes = [
    (0.0, 59),    # B
    (0.375, 60),  # Bb
    (0.75, 62),   # D
    (1.125, 63),  # Eb
    (1.5, 62),    # D
    (1.875, 61),  # C
    (2.25, 60),   # Bb
    (2.625, 59)   # B
]

for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time + t, end=time + t + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
chord_times = [1.0, 3.0]
for t in chord_times:
    for pitch in [62, 65, 67, 60]:  # D, F, A, C
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time + t, end=time + t + 0.1)
        piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = bar * BAR_LENGTH + beat * BEAT_LENGTH
    # Hi-hat on every eighth
    for i in range(2):
        hihat_time = time + i * (BEAT_LENGTH / 2)
        hihat_note = pretty_midi.Note(velocity=80, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(hihat_note)

    # Kick on 1 and 3
    if beat in [0, 2]:
        kick_note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1)
        drums.notes.append(kick_note)

    # Snare on 2 and 4
    if beat in [1, 3]:
        snare_note = pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1)
        drums.notes.append(snare_note)

# Add instruments to the PrettyMIDI object
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Write the MIDI to a file
pm.write("dante_intro.mid")
