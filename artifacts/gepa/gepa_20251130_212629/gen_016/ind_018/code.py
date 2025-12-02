
import pretty_midi

# Initialize the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

#-------------------------
# Bar 1: Little Ray (drums) alone (0.0 - 1.5s)
#-------------------------
# Kick on beats 1 and 3, snare on 2 and 4, hihat on every eighth
# Add some syncopation and dynamic variation

# 0.0 - 1.5s
# Bar divisions: 0.0 to 0.375, 0.375 to 0.75, 0.75 to 1.125, 1.125 to 1.5

# Kick on 1 and 3 (0.0 and 0.75)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4 (0.375 and 1.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hats on every eighth note
for i in range(4):
    start = i * 0.375
    end = start + 0.375
    velocity = 95 if i % 2 == 0 else 105  # Alternating velocity for syncopation
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=HIHAT, start=start, end=end))

#-------------------------
# Bar 2-4: Full quartet (1.5 - 6.0s)
#-------------------------

#-------------------------
# BASS: Marcus - Walking line, chromatic approaches, no repeats, F key
#-------------------------
# F7 chord: F, A, C, E, G, Bb, D (F7 = F, A, C, E, Bb)
# Walking bass lines in F: F, G, A, Bb, C, D, E, F
# Add chromatic passing tones for tension

# Bar 2 (1.5 - 3.0s)
# Bass line: F (1.5), Gb (1.575), G (1.65), A (1.725), Bb (1.8), B (1.875), C (1.95), D (2.025), E (2.1), F (3.0)
bass_notes = [
    (1.5, 77, 100),  # F
    (1.575, 78, 85), # Gb
    (1.65, 79, 90),  # G
    (1.725, 80, 95), # A
    (1.8, 81, 100),  # Bb
    (1.875, 82, 90), # B
    (1.95, 83, 85),  # C
    (2.025, 85, 100),# D
    (2.1, 87, 90),   # E
    (3.0, 77, 100),  # F
]
for start, pitch, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Bar 3 (3.0 - 4.5s)
# Chromatic line: F, Gb, G, Ab, A, Bb, B, C
bass_notes = [
    (3.0, 77, 100),  # F
    (3.075, 78, 85), # Gb
    (3.15, 79, 90),  # G
    (3.225, 80, 85), # Ab
    (3.3, 81, 90),   # A
    (3.375, 81, 85), # Bb
    (3.45, 82, 90),  # B
    (3.525, 83, 95), # C
    (4.5, 77, 100),  # F
]
for start, pitch, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Bar 4 (4.5 - 6.0s)
# Bass line: F, G, Ab, A, Bb, B, C, D
bass_notes = [
    (4.5, 77, 100),  # F
    (4.575, 79, 90), # G
    (4.65, 80, 85),  # Ab
    (4.725, 81, 90), # A
    (4.8, 81, 85),   # Bb
    (4.875, 82, 90), # B
    (4.95, 83, 95),  # C
    (5.025, 85, 100),# D
    (6.0, 77, 100),  # F
]
for start, pitch, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

#-------------------------
# PIANO: Diane - 7th chords, comp on 2 and 4, emotion
#-------------------------
# F7 = F, A, C, E, Bb (F7 = F, A, C, E, Bb)
# Comp on 2 and 4

# Bar 2 (1.5 - 3.0s)
# 2nd beat (1.875 - 2.25s): F7 chord
piano_notes = [
    (1.875, 77, 110), # F
    (1.875, 82, 110), # A
    (1.875, 83, 110), # C
    (1.875, 87, 110), # E
    (1.875, 79, 105), # Bb
]
for start, pitch, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Bar 3 (3.0 - 4.5s)
# 2nd beat (3.375 - 3.75s): F7 chord
piano_notes = [
    (3.375, 77, 110), # F
    (3.375, 82, 110), # A
    (3.375, 83, 110), # C
    (3.375, 87, 110), # E
    (3.375, 79, 105), # Bb
]
for start, pitch, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

# Bar 4 (4.5 - 6.0s)
# 4th beat (5.25 - 5.625s): F7 chord
piano_notes = [
    (5.25, 77, 110), # F
    (5.25, 82, 110), # A
    (5.25, 83, 110), # C
    (5.25, 87, 110), # E
    (5.25, 79, 105), # Bb
]
for start, pitch, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

#-------------------------
# SAX: Dante - Melody (start on 2nd beat of bar 2)
#-------------------------
# Simple, haunting motif
# Start on A (82) in bar 2, beat 2 (1.875)
# Motif: A (82), Bb (81), C (83), D (85) - ascending with a pause

# Bar 2 (1.875 - 3.0s)
sax_notes = [
    (1.875, 82, 100), # A
    (2.25, 81, 100),  # Bb
    (2.625, 83, 100), # C
    (3.0, 85, 100),   # D
]
for start, pitch, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375))

#-------------------------
# Add the instruments to the MIDI file
#-------------------------
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
