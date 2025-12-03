
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = []
pm.time_signature_changes.append(pretty_midi.TimeSignature(4, 4, 0.0))
pm.tempo_changes = []
pm.tempo_changes.append(pretty_midi.TempoChange(160.0, 0.0))

# Define instruments
drums = Instrument(program=Program(0), is_drum=True, name="Drums")
bass = Instrument(program=Program(33), name="Bass")
piano = Instrument(program=Program(0), name="Piano")
sax = Instrument(program=Program(64), name="Saxophone")

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)

# Time per bar (1.5s), beat is 0.375s
bar_duration = 1.5
beat_duration = 0.375
time = 0.0

### DRUMS (Little Ray)
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(time, bar_duration):
    # Kick on 1 and 3
    for i in [0, 2]:
        drums.notes.append(Note(36, 100, time + i * beat_duration, time + i * beat_duration + 0.1))
    # Snare on 2 and 4
    for i in [1, 3]:
        drums.notes.append(Note(38, 100, time + i * beat_duration, time + i * beat_duration + 0.1))
    # Hihat on every eighth
    for i in range(8):
        drums.notes.append(Note(42, 80, time + i * beat_duration / 2, time + i * beat_duration / 2 + 0.05))

# Bar 1 (only drums)
add_drums(time, bar_duration)
time += bar_duration

### BASS (Marcus)
# Bar 2: Walking line with chromatic approaches, D2-G2 (MIDI 38-43)
def add_bass(time, bar_duration):
    # Bass line: D2 (38), Eb2 (39), F2 (41), G2 (43)
    # Start on D2, walk down to Eb2 with chromatic approach, then to F2, then G2
    notes = [
        (38, 0.0),
        (39, 0.375),    # chromatic approach to Eb2
        (41, 0.75),     # F2
        (43, 1.125)     # G2
    ]
    for pitch, offset in notes:
        bass.notes.append(Note(pitch, 70, time + offset, time + offset + 0.1))

# Bar 2
add_bass(time, bar_duration)
time += bar_duration

### PIANO (Diane)
# Bar 2: Open voicings, different chord each bar, resolve on the last
def add_piano(time):
    # Bar 2: Dm7 (D, F, A, C)
    piano.notes.append(Note(62, 90, time, time + 0.1))  # D
    piano.notes.append(Note(66, 90, time, time + 0.1))  # F
    piano.notes.append(Note(71, 90, time, time + 0.1))  # A
    piano.notes.append(Note(67, 90, time, time + 0.1))  # C

    # Bar 3: G7 (G, B, D, F)
    piano.notes.append(Note(67, 90, time + beat_duration, time + beat_duration + 0.1))  # G
    piano.notes.append(Note(71, 90, time + beat_duration, time + beat_duration + 0.1))  # B
    piano.notes.append(Note(62, 90, time + beat_duration, time + beat_duration + 0.1))  # D
    piano.notes.append(Note(66, 90, time + beat_duration, time + beat_duration + 0.1))  # F

    # Bar 4: Bm7 (B, D#, F#, A)
    piano.notes.append(Note(73, 90, time + 2 * beat_duration, time + 2 * beat_duration + 0.1))  # B
    piano.notes.append(Note(62, 90, time + 2 * beat_duration, time + 2 * beat_duration + 0.1))  # D#
    piano.notes.append(Note(69, 90, time + 2 * beat_duration, time + 2 * beat_duration + 0.1))  # F#
    piano.notes.append(Note(71, 90, time + 2 * beat_duration, time + 2 * beat_duration + 0.1))  # A

# Bar 2-4 (piano only comp on 2 and 4)
add_piano(time)
time += bar_duration

### SAX (You)
# Bar 2: Start the motif, leave it hanging
def add_sax(time):
    # Motif: D (62), E (64), D (62) — haunting, incomplete
    sax.notes.append(Note(62, 100, time, time + 0.25))  # D
    sax.notes.append(Note(64, 100, time + 0.375, time + 0.625))  # E
    sax.notes.append(Note(62, 100, time + 0.75, time + 1.0))  # D

# Bar 2
add_sax(time)
time += bar_duration

# Save the MIDI file
pm.write('jazz_intro_wayne_shorter.mid')
