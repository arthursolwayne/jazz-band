
import pretty_midi

# Initialize MIDI object with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds per beat
beat = 0.375  # since 160 BPM = 60 / 160 = 0.375 sec per beat
bar_length = 1.5  # 4 beats per bar

# --- Bar 1: Drums only, build tension ---
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(8):
    start = i * 0.1875  # 8 eighth notes per bar
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

# --- Bar 2: Bass enters with a walking line in D minor, chromatic approaches ---
# D Dorian: D, E, F, G, A, B, C
# Walking bass line in D minor: D - F - G - B♭ (chromatic) - A - B - C - D

bass_notes = [
    (0, 2),  # D (2)
    (0.375, 5),  # F (5)
    (0.75, 7),  # G (7)
    (1.125, 10),  # B♭ (10)
    (1.5, 2),  # D
    (1.875, 5),  # F
    (2.25, 7),  # G
    (2.625, 10),  # B♭
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.375))

# --- Bar 2: Piano enters with 7th chords, comp on 2 and 4 (in 4/4 time) ---
# D7 chord: D, F#, A, C
# D7 on beat 2 and 4

piano_notes = [
    # Beat 2 (0.375)
    (0.375, 2),  # D
    (0.375, 6),  # F#
    (0.375, 10),  # A
    (0.375, 12),  # C
    
    # Beat 4 (1.125)
    (1.125, 2),  # D
    (1.125, 6),  # F#
    (1.125, 10),  # A
    (1.125, 12),  # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.1875))

# --- Bar 2: Drums continue the same pattern ---
# Copy the same hihat and snare/kick pattern as in bar 1
for i in range(8):
    start = 1.5 + i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=2.625, end=3.0))

# --- Bar 3: Saxophone enters with the motif ---
# Simple, haunting melody in D minor
# D - F - G - B♭
# D, F, G, B♭

sax_notes = [
    (1.5, 2),  # D
    (1.875, 5),  # F
    (2.25, 7),  # G
    (2.625, 10),  # B♭
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# --- Bar 4: Everyone plays together, sax continues the motif, bass walks, piano comps, drums fill the space ---
# Bass continues with the same walking line
bass_notes = [
    (3.0, 2),  # D
    (3.375, 5),  # F
    (3.75, 7),  # G
    (4.125, 10),  # B♭
    (4.5, 2),  # D
    (4.875, 5),  # F
    (5.25, 7),  # G
    (5.625, 10),  # B♭
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=start, end=start + 0.375))

# Piano continues comping on 2 and 4 (in this bar, beats 2 and 4 are 3.375 and 4.125)
piano_notes = [
    (3.375, 2),  # D
    (3.375, 6),  # F#
    (3.375, 10),  # A
    (3.375, 12),  # C
    (4.125, 2),  # D
    (4.125, 6),  # F#
    (4.125, 10),  # A
    (4.125, 12),  # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.1875))

# Drums continue with the same pattern
for i in range(8):
    start = 3.0 + i * 0.1875
    end = start + 0.1875
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=start, end=end))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=4.125, end=4.5))

# Saxophone continues the motif and resolves on the last beat
sax_notes = [
    (4.5, 2),  # D
    (4.875, 5),  # F
    (5.25, 7),  # G
    (5.625, 10),  # B♭
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=pitch, start=start, end=start + 0.375))

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
