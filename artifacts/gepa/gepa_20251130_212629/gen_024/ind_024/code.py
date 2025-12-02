
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)             # Saxophone
bass = pretty_midi.Instrument(program=33)            # Double Bass
piano = pretty_midi.Instrument(program=0)            # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Time signatures and note duration in seconds (1/4 = 0.75 sec at 160 BPM)
note_length = 0.75  # 1/4 note
half_note = note_length * 2
quarter_note = note_length
eighth_note = note_length / 2
sixteenth_note = note_length / 4

# ---- BAR 1: Little Ray (Drums) ----
# Kick on beat 1, 2, 3, 4
drums.notes.append(pretty_midi.Note(
    velocity=100, pitch=36, start=0.0, end=0.75))
drums.notes.append(pretty_midi.Note(
    velocity=100, pitch=36, start=1.5, end=2.25))
drums.notes.append(pretty_midi.Note(
    velocity=100, pitch=36, start=3.0, end=3.75))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(
    velocity=90, pitch=38, start=1.5, end=2.25))
drums.notes.append(pretty_midi.Note(
    velocity=90, pitch=38, start=3.0, end=3.75))

# Hihat on every 8th note
for i in range(0, 4):
    drums.notes.append(pretty_midi.Note(
        velocity=80, pitch=42, start=i * 0.75, end=i * 0.75 + 0.25))

# ---- BAR 2: Full Quartet ----
# Bass: Walking bass line in Dm
# Dm7: D F A C
# Walking bass: D → F → A → C → D (chromatic chromatic)
bass_notes = [
    (0.0, 2), (0.75, 5), (1.5, 7), (2.25, 10),
    (3.0, 2)  # Repeat for the next bar
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=80, pitch=pitch, start=start, end=start + 0.75))

# Piano: Comping with Dm7 chords
# Dm7: D F A C
piano_notes = [
    (0.0, 5), (0.0, 7), (0.0, 10), (0.0, 12),  # Dm7
    (1.5, 5), (1.5, 7), (1.5, 10), (1.5, 12),  # Dm7
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=pitch, start=start, end=start + 0.75))

# Sax: Melodic motif in Dm
# Simple Dm scale: D, F, G, A, C
sax_notes = [
    (0.0, 2), (0.75, 5), (1.5, 7), (2.25, 10)
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(
        velocity=100, pitch=pitch, start=start, end=start + 0.75))

# ---- BAR 3: Little Ray + Bass + Piano ----
# Drums same as Bar 1, but shift to 3.0s
for note in drums.notes:
    note.start += 3.0
    note.end += 3.0

# Bass: Walk again
bass_notes = [
    (3.0, 2), (3.75, 5), (4.5, 7), (5.25, 10)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(
        velocity=80, pitch=pitch, start=start, end=start + 0.75))

# Piano: Comping again on Dm7 for Bar 3
piano_notes = [
    (3.0, 5), (3.0, 7), (3.0, 10), (3.0, 12),
    (4.5, 5), (4.5, 7), (4.5, 10), (4.5, 12)
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(
        velocity=80, pitch=pitch, start=start, end=start + 0.75))

# ---- BAR 4: Full Quartet (same as Bar 2) ----
# Copy sax and piano notes from Bar 2 to Bar 4
for note in sax.notes:
    if note.start < 3.0:
        new_note = pretty_midi.Note(
            pitch=note.pitch, velocity=note.velocity,
            start=note.start + 3.0, end=note.end + 3.0)
        sax.notes.append(new_note)

for note in piano.notes:
    if note.start < 3.0:
        new_note = pretty_midi.Note(
            pitch=note.pitch, velocity=note.velocity,
            start=note.start + 3.0, end=note.end + 3.0)
        piano.notes.append(new_note)

# Save the MIDI file
midi.write("dm_jazz_quartet.mid")
