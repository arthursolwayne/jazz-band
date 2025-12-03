
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar timing: 6 seconds total, 1.5 seconds per bar
bar_duration = 1.5
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# --------------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray sets the mood - tight, syncopated, but not too aggressive
drum_notes_bar1 = [
    (0.0, drum_notes['kick'], 1.0),     # Kick on beat 1
    (0.75, drum_notes['hihat'], 0.5),   # Hihat on & of 1
    (1.0, drum_notes['snare'], 1.0),    # Snare on beat 2
    (1.75, drum_notes['hihat'], 0.5),   # Hihat on & of 2
    (2.0, drum_notes['kick'], 1.0),     # Kick on beat 3
    (2.75, drum_notes['hihat'], 0.5),   # Hihat on & of 3
    (3.0, drum_notes['snare'], 1.0),    # Snare on beat 4
    (3.75, drum_notes['hihat'], 0.5),   # Hihat on & of 4
]

for time, note, duration in drum_notes_bar1:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    drums.notes.append(drum_note)

# --------------------------
# Bar 2: Full band enters (1.5 - 3.0s)

# Bass line in D minor: walking bass, roots and fifths with chromatic approaches
# D2-G2, D2, E2, G2, F#2, G2, A2, B2, etc.
bass_notes_bar2 = [
    (1.5, 38, 0.375),  # D2 (root)
    (1.875, 41, 0.375), # F#2 (chromatic approach to G)
    (2.25, 43, 0.375),  # G2 (fifth)
    (2.625, 40, 0.375), # E2 (third)
]

for time, note, duration in bass_notes_bar2:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes_bar2 = [
    (1.5, 55, 0.25),  # D (D4)
    (1.75, 58, 0.25),  # F (F4)
    (2.0, 62, 0.25),   # A (A4)
    (2.25, 60, 0.25),  # C (C4)
]

for time, note, duration in piano_notes_bar2:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# Sax: Introduce a motif - short, haunting, not a scale
# Motif: D - F - A - Bb (sings the D minor scale but ends on Bb, creates tension)
sax_notes_bar2 = [
    (1.5, 62, 0.375),   # A4
    (1.875, 65, 0.375), # C5
    (2.25, 67, 0.375),  # D5
    (2.625, 66, 0.375), # Bb4 (half note, leaves it hanging)
]

for time, note, duration in sax_notes_bar2:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# --------------------------
# Bar 3: Full band (3.0 - 4.5s)

# Bass line: continue walking
bass_notes_bar3 = [
    (3.0, 45, 0.375),  # B2 (eighth note)
    (3.375, 47, 0.375), # D3 (chromatic approach to E)
    (3.75, 49, 0.375),  # E3 (third)
    (4.125, 47, 0.375), # D3 (chromatic approach to E)
]

for time, note, duration in bass_notes_bar3:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# Piano: Gm7 (G, Bb, D, F)
piano_notes_bar3 = [
    (3.0, 67, 0.25),   # G4
    (3.25, 62, 0.25),  # Bb4
    (3.5, 65, 0.25),   # D5
    (3.75, 60, 0.25),  # F4
]

for time, note, duration in piano_notes_bar3:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# Drums: same pattern as bar 1
for time, note, duration in drum_notes_bar1:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time + 1.5, end=time + duration + 1.5)
    drums.notes.append(drum_note)

# Sax: Motif returns, but with a twist — resolve on the final bar
sax_notes_bar3 = [
    (3.0, 62, 0.375),   # A4
    (3.375, 65, 0.375), # C5
    (3.75, 67, 0.375),  # D5
    (4.125, 67, 0.375), # D5 (Holds for resolution)
]

for time, note, duration in sax_notes_bar3:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# --------------------------
# Bar 4: Full band (4.5 - 6.0s)

# Bass line: continue the walking pattern
bass_notes_bar4 = [
    (4.5, 50, 0.375),  # E3 (root)
    (4.875, 52, 0.375), # G3 (chromatic approach to A)
    (5.25, 55, 0.375),  # A3 (fifth)
    (5.625, 52, 0.375), # G3 (chromatic approach to A)
]

for time, note, duration in bass_notes_bar4:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# Piano: Gm7 (G, Bb, D, F)
piano_notes_bar4 = [
    (4.5, 67, 0.25),   # G4
    (4.75, 62, 0.25),  # Bb4
    (5.0, 65, 0.25),   # D5
    (5.25, 60, 0.25),  # F4
]

for time, note, duration in piano_notes_bar4:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# Drums: same pattern as bar 1
for time, note, duration in drum_notes_bar1:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time + 3.0, end=time + duration + 3.0)
    drums.notes.append(drum_note)

# Sax: Return the motif, now resolved — ends on D
sax_notes_bar4 = [
    (4.5, 62, 0.375),   # A4
    (4.875, 65, 0.375), # C5
    (5.25, 67, 0.375),  # D5
    (5.625, 67, 0.375), # D5 (End on D5 for resolution)
]

for time, note, duration in sax_notes_bar4:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
