
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar structure: 4/4, 160 BPM = 6 beats per second
# Bar duration = 1.5 seconds, beat = 0.25 seconds (160 BPM is 6.4 beats per second? Wait, let's re-calculate.)

# 160 BPM = 160 beats per minute = 2.666... beats per second
# 1 beat = 0.6 seconds
# 1 bar = 4 beats = 2.4 seconds

# Wait! Correction:
# 160 BPM = 160 beats per minute = 160/60 ≈ 2.666 beats per second
# 1 beat = 60/160 = 0.375 seconds
# 1 bar (4 beats) = 1.5 seconds — this matches the timing you provided.

# Bar 1 (0.0 - 1.5s)
drum_notes = [
    (0.0, kick),       # Kick on beat 1
    (0.375, hihat),    # Hihat on 1 & 2
    (0.75, hihat),
    (1.125, hihat),
    (1.5, snare),      # Snare on beat 2
    (1.875, hihat),
    (2.25, hihat),
    (2.625, hihat),
    (3.0, kick),       # Kick on beat 3
    (3.375, hihat),
    (3.75, hihat),
    (4.125, hihat),
    (4.5, snare),      # Snare on beat 4
    (4.875, hihat),
    (5.25, hihat),
    (5.625, hihat),
]

for time, note in drum_notes:
    if note == kick:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    elif note == snare:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    elif note == hihat:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(note_obj)

# Bar 2 (1.5 - 3.0s): Full quartet, sax melody starts
# Melody (D minor key, searching, sparse, one motif)

# Sax tenor: D, F, Bb, D
# Each note gets a quarter note, but spaced with rest
sax_notes = [
    (1.5, 62),  # D4
    (2.25, 65), # F4
    (3.0, 60),  # Bb4
    (3.75, 62), # D4
]

for time, pitch in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Bass: walking line in D minor
# Root, b7, b3, b5 (D, C, F, A)
# Chromatic approaches for each root
bass_notes = [
    (1.5, 62),  # D4
    (1.875, 61), # C4 (chromatic)
    (2.25, 65),  # F4
    (2.625, 64), # E4 (chromatic)
    (3.0, 60),   # Bb4
    (3.375, 59), # A4 (chromatic)
    (3.75, 62),  # D4
    (4.125, 61), # C4 (chromatic)
]

for time, pitch in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comping
# D7 (D, F#, A, C), Dm7 (D, F, A, C)
# Bars 2 and 4

# Bar 2 (1.5 - 3.0s): D7 on beat 2, Dm7 on beat 4
piano_notes = [
    (2.25, 62),  # D4
    (2.25, 67),  # F#4
    (2.25, 69),  # A4
    (2.25, 60),  # C4 (D7)
    (3.0, 62),   # D4
    (3.0, 65),   # F4
    (3.0, 69),   # A4
    (3.0, 60),   # C4 (Dm7)
]

for time, pitch in piano_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Bar 3 (3.0 - 4.5s): Drums continue, but no sax, piano, or bass
# Just drums
drum_notes = [
    (3.0, kick),
    (3.375, hihat),
    (3.75, hihat),
    (4.125, hihat),
    (4.5, snare),
    (4.875, hihat),
    (5.25, hihat),
    (5.625, hihat),
]

for time, note in drum_notes:
    if note == kick:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15)
    elif note == snare:
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    elif note == hihat:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.05)
    drums.notes.append(note_obj)

# Bar 4 (4.5 - 6.0s): Sax melody resolves
# D, F, Bb, D — same motif, but ends on D
sax_notes = [
    (4.5, 62),  # D4
    (5.25, 65), # F4
    (6.0, 60),  # Bb4
    (6.375, 62), # D4
]

for time, pitch in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Bass: walking line again
bass_notes = [
    (4.5, 60),   # Bb4
    (4.875, 59), # A4 (chromatic)
    (5.25, 62),  # D4
    (5.625, 61), # C4 (chromatic)
    (6.0, 65),   # F4
    (6.375, 64), # E4 (chromatic)
]

for time, pitch in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Piano: D7 on beat 2, Dm7 on beat 4 again
piano_notes = [
    (5.25, 62),  # D4
    (5.25, 67),  # F#4
    (5.25, 69),  # A4
    (5.25, 60),  # C4 (D7)
    (6.0, 62),   # D4
    (6.0, 65),   # F4
    (6.0, 69),   # A4
    (6.0, 60),   # C4 (Dm7)
]

for time, pitch in piano_notes:
    note_obj = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save("dante_intro.mid")
