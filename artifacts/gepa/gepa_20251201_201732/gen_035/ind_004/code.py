
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 - 1.5s)
for i in range(0, 4):
    time = i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, roots and fifths with chromatic approaches
# F (F2), C (C3), E (E3), B (B3), D (D3), A (A3), C (C3), G (G3), etc.

# Bar 2 (1.5 - 3.0s)
bar_start = 1.5
note_durations = 0.375  # 1/4 note in 4/4 at 160 BPM

# Roots and fifths: F2 (38), C3 (42), B3 (52), G3 (47), D3 (44), A3 (49), E3 (50), C4 (52), etc.
bass_notes = [
    (38, bar_start + 0.0),   # F2
    (42, bar_start + 0.375), # C3
    (52, bar_start + 0.75),  # B3
    (47, bar_start + 1.125), # G3
    (44, bar_start + 1.5),   # D3
    (49, bar_start + 1.875), # A3
    (50, bar_start + 2.25),  # E3
    (52, bar_start + 2.625)  # C4
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: F7 (F, A, C, E), voicing: A (57), C (52), E (55), F (53)
note_piano = [
    (57, bar_start + 0.0),   # A
    (52, bar_start + 0.0),   # C
    (55, bar_start + 0.0),   # E
    (53, bar_start + 0.0)    # F
]
for pitch, start in note_piano:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    piano.notes.append(note)

# Sax: Motif starts, leaves it hanging
# Notes: F (53), Bb (58), D (55), G (57) — one short motif, make it sing
note_sax = [
    (53, bar_start + 0.0),   # F
    (58, bar_start + 0.375), # Bb
    (55, bar_start + 0.75),  # D
    (57, bar_start + 1.125)  # G
]
for pitch, start in note_sax:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Next walking line
bar_start = 3.0
bass_notes = [
    (44, bar_start + 0.0),   # D3
    (49, bar_start + 0.375), # A3
    (50, bar_start + 0.75),  # E3
    (52, bar_start + 1.125), # C4
    (47, bar_start + 1.5),   # G3
    (53, bar_start + 1.875), # F4
    (55, bar_start + 2.25),  # E4
    (57, bar_start + 2.625)  # G4
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    bass.notes.append(note)

# Piano: Next chord — F7 again, but with different voicing
note_piano = [
    (58, bar_start + 0.0),   # Bb
    (53, bar_start + 0.0),   # F
    (55, bar_start + 0.0),   # E
    (57, bar_start + 0.0)    # G
]
for pitch, start in note_piano:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    piano.notes.append(note)

# Sax: Continue motif, resolve it
note_sax = [
    (53, bar_start + 0.0),   # F
    (58, bar_start + 0.375), # Bb
    (55, bar_start + 0.75),  # D
    (57, bar_start + 1.125), # G
    (53, bar_start + 1.5)    # F
]
for pitch, start in note_sax:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line again
bar_start = 4.5
bass_notes = [
    (53, bar_start + 0.0),   # F4
    (55, bar_start + 0.375), # E4
    (57, bar_start + 0.75),  # G4
    (50, bar_start + 1.125), # E3
    (47, bar_start + 1.5),   # G3
    (53, bar_start + 1.875), # F4
    (55, bar_start + 2.25),  # E4
    (57, bar_start + 2.625)  # G4
]
for pitch, start in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    bass.notes.append(note)

# Piano: Final chord — F7, with a chromatic passing tone on the 3rd beat
note_piano = [
    (57, bar_start + 0.0),   # G
    (53, bar_start + 0.0),   # F
    (55, bar_start + 0.0),   # E
    (58, bar_start + 1.125)  # Bb
]
for pitch, start in note_piano:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + note_durations)
    piano.notes.append(note)

# Sax: Motif returns to F and resolves
note_sax = [
    (53, bar_start + 0.0),   # F
    (58, bar_start + 0.375), # Bb
    (55, bar_start + 0.75),  # D
    (57, bar_start + 1.125), # G
    (53, bar_start + 1.5)    # F
]
for pitch, start in note_sax:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.1)
    sax.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
for i in range(0, 4):
    time = bar_start + i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
