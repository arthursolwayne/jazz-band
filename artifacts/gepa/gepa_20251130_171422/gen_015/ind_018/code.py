
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time constants
BAR_DURATION = 1.5  # 1.5 seconds per bar at 160 BPM
BEAT_DURATION = 0.375  # 0.375 seconds per beat

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
drum_notes_bar1 = [
    # Kick on beat 1 and 3
    (bar1_start + 0.0, drum_notes['kick']),
    (bar1_start + 0.75, drum_notes['kick']),
    # Snare on beat 2 and 4
    (bar1_start + 0.375, drum_notes['snare']),
    (bar1_start + 1.125, drum_notes['snare']),
    # Hihat on every eighth
    (bar1_start + 0.0, drum_notes['hihat']),
    (bar1_start + 0.375, drum_notes['hihat']),
    (bar1_start + 0.75, drum_notes['hihat']),
    (bar1_start + 1.125, drum_notes['hihat']),
]

for time, note in drum_notes_bar1:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5

# SAX: Dante's motif (melody in F major, with chromatic tension)
# F - Bb - C - D - F (motif)
# Start on beat 1, end on beat 2.5, leave it hanging
sax_notes = [
    # Bar 2, beat 1 (F)
    (bar2_start + 0.0, 71, 0.5),
    # Bar 2, beat 2 (Bb)
    (bar2_start + 0.375, 70, 0.5),
    # Bar 2, beat 2.5 (C)
    (bar2_start + 0.75, 69, 0.5),
    # Bar 2, beat 3 (D)
    (bar2_start + 1.125, 71, 0.5),
    # Bar 2, beat 3.5 (F)
    (bar2_start + 1.5, 71, 0.5),
    # Bar 3, beat 1 (F)
    (bar2_start + 1.875, 71, 0.5),
]

for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# BASS: Marcus's walking line (chromatic approaches)
# F - G - Ab - A - Bb - C - Db - D - Eb - F
bass_notes = [
    (bar2_start + 0.0, 65, 0.375),
    (bar2_start + 0.375, 66, 0.375),
    (bar2_start + 0.75, 67, 0.375),
    (bar2_start + 1.125, 67, 0.375),
    (bar2_start + 1.5, 66, 0.375),
    (bar2_start + 1.875, 68, 0.375),
    (bar2_start + 2.25, 68, 0.375),
    (bar2_start + 2.625, 69, 0.375),
    (bar2_start + 3.0, 65, 0.375),
]

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# PIANO: Diane's comping (7th chords on 2 and 4)
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # F7 on beat 2: F, A, C, Eb
    (bar2_start + 0.375, 65, 0.375),
    (bar2_start + 0.375, 68, 0.375),
    (bar2_start + 0.375, 69, 0.375),
    (bar2_start + 0.375, 67, 0.375),
    
    # Bb7 on beat 4: Bb, D, F, Ab
    (bar2_start + 1.125, 70, 0.375),
    (bar2_start + 1.125, 73, 0.375),
    (bar2_start + 1.125, 69, 0.375),
    (bar2_start + 1.125, 71, 0.375),
]

for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Bar 3: Drums, Bass, Piano, Sax continue
# Bar 4: Same pattern, but sax resolves the motif
bar3_start = 3.0
bar4_start = 4.5

# Drums: same pattern
for time, note in drum_notes_bar1:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time + bar3_start, end=time + bar3_start + 0.125)
    drums.notes.append(dr)

for time, note in drum_notes_bar1:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time + bar4_start, end=time + bar4_start + 0.125)
    drums.notes.append(dr)

# Bass: same pattern, offset
for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + bar3_start, end=time + bar3_start + duration)
    bass.notes.append(note)

for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + bar4_start, end=time + bar4_start + duration)
    bass.notes.append(note)

# Piano: same pattern, offset
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + bar3_start, end=time + bar3_start + duration)
    piano.notes.append(note)

for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time + bar4_start, end=time + bar4_start + duration)
    piano.notes.append(note)

# Sax: resolution of motif in bar 4
sax_notes_bar4 = [
    (bar4_start + 0.0, 71, 0.5),  # F
    (bar4_start + 0.375, 70, 0.5),  # Bb
    (bar4_start + 0.75, 69, 0.5),  # C
    (bar4_start + 1.125, 71, 0.5),  # D
    (bar4_start + 1.5, 71, 0.5),   # F
]

for time, pitch, duration in sax_notes_bar4:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
print("MIDI file saved as 'dante_introduction.mid'")
