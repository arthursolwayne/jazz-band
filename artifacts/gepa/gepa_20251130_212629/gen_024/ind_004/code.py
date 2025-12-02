
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Set the key to Dm (D minor)
key = 'Dm'

# Bar 1: Drums only (0.0 - 1.5s)
# Build tension with syncopation and dynamic velocity
bar_duration = 1.5  # seconds per bar
bar1_start = 0.0
bar1_end = bar_duration

# Drums in Bar 1
# Kick on 1, snare on 2, hihat on every eighth
# Add some syncopation and velocity variation
drum_notes_bar1 = [
    (bar1_start + 0.0, drum_notes['kick'], 100),  # Kick on beat 1
    (bar1_start + 0.0, drum_notes['hihat'], 90),  # Hihat on downbeat
    (bar1_start + 0.125, drum_notes['hihat'], 85),  # Hihat on 1&
    (bar1_start + 0.25, drum_notes['hihat'], 80),  # Hihat on 2
    (bar1_start + 0.375, drum_notes['snare'], 95),  # Snare on 2+
    (bar1_start + 0.5, drum_notes['hihat'], 85),  # Hihat on 2&
    (bar1_start + 0.75, drum_notes['hihat'], 80),  # Hihat on 3
    (bar1_start + 0.875, drum_notes['kick'], 100),  # Kick on beat 3
    (bar1_start + 1.0, drum_notes['hihat'], 90),  # Hihat on 3&
    (bar1_start + 1.125, drum_notes['hihat'], 85),  # Hihat on 4
    (bar1_start + 1.25, drum_notes['hihat'], 80),  # Hihat on 4-
    (bar1_start + 1.375, drum_notes['snare'], 95),  # Snare on beat 4
    (bar1_start + 1.5, drum_notes['hihat'], 85)   # Hihat on 4&
]

for time, note, velocity in drum_notes_bar1:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.05))

# Bar 2-4: Full quartet (1.5 - 6.0s)

bar2_start = 1.5
bar4_end = 6.0

# Marcus - Bass: Walking line in Dm
# Dm7: D F A C
# Walking line in Dm, chromatic approaches, no repeats
bass_notes = [
    (bar2_start + 0.0, 50, 80),    # D
    (bar2_start + 0.25, 49, 85),   # C# (chromatic approach)
    (bar2_start + 0.5, 52, 80),    # F
    (bar2_start + 0.75, 51, 85),   # E (chromatic approach)
    (bar2_start + 1.0, 55, 80),    # A
    (bar2_start + 1.25, 54, 85),   # G# (chromatic approach)
    (bar2_start + 1.5, 57, 80),    # C
    (bar2_start + 1.75, 56, 85),   # Bb (chromatic approach)
    (bar2_start + 2.0, 50, 80),    # D
    (bar2_start + 2.25, 49, 85),   # C#
    (bar2_start + 2.5, 52, 80),    # F
    (bar2_start + 2.75, 51, 85),   # E
    (bar2_start + 3.0, 55, 80),    # A
    (bar2_start + 3.25, 54, 85),   # G#
    (bar2_start + 3.5, 57, 80),    # C
    (bar2_start + 3.75, 56, 85),   # Bb
    (bar2_start + 4.0, 50, 80),    # D
    (bar2_start + 4.25, 49, 85),   # C#
    (bar2_start + 4.5, 52, 80),    # F
    (bar2_start + 4.75, 51, 85),   # E
    (bar2_start + 5.0, 55, 80),    # A
    (bar2_start + 5.25, 54, 85),   # G#
    (bar2_start + 5.5, 57, 80),    # C
    (bar2_start + 5.75, 56, 85),   # Bb
]

for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Diane - Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# F7 = F A C E
# A7 = A C E G
# C7 = C E G Bb
# Comp on beats 2 and 4
piano_notes = [
    (bar2_start + 0.5, 62, 100),  # F (Dm7) on beat 2
    (bar2_start + 0.5, 67, 100),  # A (Dm7)
    (bar2_start + 0.5, 69, 100),  # C (Dm7)
    (bar2_start + 0.5, 58, 100),  # D (Dm7)
    (bar2_start + 1.0, 65, 100),  # E (F7) on beat 4
    (bar2_start + 1.0, 67, 100),  # A (F7)
    (bar2_start + 1.0, 69, 100),  # C (F7)
    (bar2_start + 1.0, 62, 100),  # F (F7)
    (bar2_start + 2.5, 65, 100),  # E (A7) on beat 2
    (bar2_start + 2.5, 67, 100),  # A (A7)
    (bar2_start + 2.5, 69, 100),  # C (A7)
    (bar2_start + 2.5, 71, 100),  # G (A7)
    (bar2_start + 3.0, 69, 100),  # C (C7) on beat 4
    (bar2_start + 3.0, 71, 100),  # E (C7)
    (bar2_start + 3.0, 74, 100),  # G (C7)
    (bar2_start + 3.0, 70, 100),  # Bb (C7)
    (bar2_start + 4.5, 65, 100),  # E (F7) on beat 2
    (bar2_start + 4.5, 67, 100),  # A (F7)
    (bar2_start + 4.5, 69, 100),  # C (F7)
    (bar2_start + 4.5, 62, 100),  # F (F7)
    (bar2_start + 5.0, 65, 100),  # E (A7) on beat 4
    (bar2_start + 5.0, 67, 100),  # A (A7)
    (bar2_start + 5.0, 69, 100),  # C (A7)
    (bar2_start + 5.0, 71, 100),  # G (A7)
]

for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1))

# Dante - Saxophone: One short motif, make it sing. Start it, leave it hanging.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D -> Eb -> F -> rest (space)
# Then come back with D -> C -> Bb -> rest
# Create a simple, haunting melody with space

sax_notes = [
    (bar2_start + 0.0, 62, 95),    # D (start of motif)
    (bar2_start + 0.25, 63, 90),   # Eb
    (bar2_start + 0.5, 65, 95),    # F
    (bar2_start + 0.75, 62, 90),   # D (return)
    (bar2_start + 1.0, 60, 90),    # C
    (bar2_start + 1.25, 59, 90),   # Bb
    (bar2_start + 1.5, 62, 90),    # D (end)
]

for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_jazz_intro.mid")
