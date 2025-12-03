
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
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

# -----------------------------
# BAR 1: Little Ray alone (0.0 - 1.5 seconds)
# Drums only — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time per beat is 0.375s (160 BPM = 60/160 = 0.375 per beat)
# Bar is 1.5s (4 beats)

bar1_start = 0.0

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar1_start + 0.75, end=bar1_start + 0.75 + 0.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar1_start + 0.375, end=bar1_start + 0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar1_start + 1.125, end=bar1_start + 1.125 + 0.375))

# Hi-hat on every eighth note
for i in range(8):
    start = bar1_start + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=start + 0.375))

# -----------------------------
# BAR 2: Full quartet (1.5 - 3.0 seconds)
bar2_start = 1.5

# Bass: Walking line in F, roots and fifths with chromatic approaches
# F (F2), C (C3), B (B2), E (E3), D (D3), A (A3), G (G3), D (D3), F (F3)
# MIDI notes: F2=53, C3=60, B2=59, E3=64, D3=62, A3=69, G3=67, D3=62, F3=65
bass_notes = [
    (53, bar2_start, bar2_start + 0.375),
    (60, bar2_start + 0.375, bar2_start + 0.375 + 0.375),
    (59, bar2_start + 0.75, bar2_start + 0.75 + 0.375),
    (64, bar2_start + 1.125, bar2_start + 1.125 + 0.375),
    (62, bar2_start + 1.5, bar2_start + 1.5 + 0.375),
    (69, bar2_start + 1.875, bar2_start + 1.875 + 0.375),
    (67, bar2_start + 2.25, bar2_start + 2.25 + 0.375),
    (62, bar2_start + 2.625, bar2_start + 2.625 + 0.375),
    (65, bar2_start + 3.0, bar2_start + 3.0 + 0.375)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E) -> open voicing
piano_notes = [
    (65, bar2_start, bar2_start + 0.375),  # F3
    (69, bar2_start, bar2_start + 0.375),  # A3
    (72, bar2_start, bar2_start + 0.375),  # C4
    (76, bar2_start, bar2_start + 0.375),  # E4
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif — start with F (F4 = 79), then G (G4 = 80), then F again
# Start on beat 1, end on beat 2.5 (leaving it hanging)
sax_notes = [
    (79, bar2_start, bar2_start + 0.375),  # F4
    (80, bar2_start + 0.375, bar2_start + 0.375 + 0.375),  # G4
    (79, bar2_start + 0.75, bar2_start + 0.75 + 0.375),  # F4
    (80, bar2_start + 1.125, bar2_start + 1.125 + 0.375),  # G4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# -----------------------------
# BAR 3: Full quartet (3.0 - 4.5 seconds)
bar3_start = 3.0

# Bass: Walking line again
bass_notes = [
    (53, bar3_start, bar3_start + 0.375),
    (60, bar3_start + 0.375, bar3_start + 0.375 + 0.375),
    (59, bar3_start + 0.75, bar3_start + 0.75 + 0.375),
    (64, bar3_start + 1.125, bar3_start + 1.125 + 0.375),
    (62, bar3_start + 1.5, bar3_start + 1.5 + 0.375),
    (69, bar3_start + 1.875, bar3_start + 1.875 + 0.375),
    (67, bar3_start + 2.25, bar3_start + 2.25 + 0.375),
    (62, bar3_start + 2.625, bar3_start + 2.625 + 0.375),
    (65, bar3_start + 3.0, bar3_start + 3.0 + 0.375)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: C7 (C, E, G, B) -> open voicing
piano_notes = [
    (67, bar3_start, bar3_start + 0.375),  # C4
    (72, bar3_start, bar3_start + 0.375),  # E4
    (76, bar3_start, bar3_start + 0.375),  # G4
    (80, bar3_start, bar3_start + 0.375),  # B4
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Second half of motif — F (F4) and back to G (G4) with resolution
sax_notes = [
    (79, bar3_start + 1.5, bar3_start + 1.5 + 0.375),  # F4
    (80, bar3_start + 1.875, bar3_start + 1.875 + 0.375),  # G4
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# -----------------------------
# BAR 4: Full quartet (4.5 - 6.0 seconds)
bar4_start = 4.5

# Bass: Walking line again
bass_notes = [
    (53, bar4_start, bar4_start + 0.375),
    (60, bar4_start + 0.375, bar4_start + 0.375 + 0.375),
    (59, bar4_start + 0.75, bar4_start + 0.75 + 0.375),
    (64, bar4_start + 1.125, bar4_start + 1.125 + 0.375),
    (62, bar4_start + 1.5, bar4_start + 1.5 + 0.375),
    (69, bar4_start + 1.875, bar4_start + 1.875 + 0.375),
    (67, bar4_start + 2.25, bar4_start + 2.25 + 0.375),
    (62, bar4_start + 2.625, bar4_start + 2.625 + 0.375),
    (65, bar4_start + 3.0, bar4_start + 3.0 + 0.375)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: Bm7 (B, D, F#, A) -> open voicing
piano_notes = [
    (79, bar4_start, bar4_start + 0.375),  # B4
    (82, bar4_start, bar4_start + 0.375),  # D5
    (86, bar4_start, bar4_start + 0.375),  # F#5
    (90, bar4_start, bar4_start + 0.375),  # A5
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: Resolution — complete the motif with a C (C5 = 84)
sax_notes = [
    (84, bar4_start + 1.5, bar4_start + 1.5 + 0.375),  # C5
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# -----------------------------
# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
