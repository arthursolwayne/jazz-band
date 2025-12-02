
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define note durations and bar timing
beats_per_bar = 4
beat = 60.0 / tempo  # in seconds
bar_duration = beat * beats_per_bar  # 6 seconds per bar

# Instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Define Dm scale: D, Eb, F, G, Ab, Bb, C
# We'll use Dm7 for harmony

# Helper function to make a note
def make_note(note_number, start, end, velocity):
    return Note(note_number, start, end, velocity)

# --- BAR 1: Drums Only (Question) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = bar_duration

# Kick
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar1_start + 0.0, bar1_start + 0.1, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar1_start + 1.5, bar1_start + 1.6, 80))

# Snare
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar1_start + 0.75, bar1_start + 0.85, 90))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar1_start + 1.25, bar1_start + 1.35, 90))

# Hi-hat
for i in range(8):
    drums.notes.append(make_note(pretty_midi.note_name_to_number('G#4'), bar1_start + i * 0.375, bar1_start + i * 0.375 + 0.1, 70))

# --- BAR 2: Full Ensemble (Development of the Question) ---
bar2_start = bar1_end
bar2_end = bar1_end + bar_duration

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    ('F3', 0.0),  # Dm root
    ('Eb3', 0.375),  # chromatic
    ('E3', 0.75),   # chromatic
    ('F3', 1.125),  # Dm root
    ('G3', 1.5),    # Dm 5
    ('Ab3', 1.875), # chromatic
    ('A3', 2.25),   # chromatic
    ('Bb3', 2.625), # Dm 7
    ('C4', 3.0),    # Dm 9
]

for note, time in bass_notes:
    start = bar2_start + time
    end = start + 0.25
    bass.notes.append(make_note(pretty_midi.note_name_to_number(note), start, end, 75))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, Ab, C)
    ('D3', 0.0, 0.25, 70),
    ('F3', 0.0, 0.25, 70),
    ('Ab3', 0.0, 0.25, 70),
    ('C4', 0.0, 0.25, 70),

    # Bar 2: Bb7 (Bb, D, F, Ab)
    ('Bb3', 1.5, 1.75, 70),
    ('D4', 1.5, 1.75, 70),
    ('F4', 1.5, 1.75, 70),
    ('Ab4', 1.5, 1.75, 70),
]

for note, start, end, vel in piano_notes:
    piano.notes.append(make_note(pretty_midi.note_name_to_number(note), start + bar2_start, end + bar2_start, vel))

# Drums (same as bar1)
for i in range(8):
    drums.notes.append(make_note(pretty_midi.note_name_to_number('G#4'), bar2_start + i * 0.375, bar2_start + i * 0.375 + 0.1, 70))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar2_start + 0.0, bar2_start + 0.1, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar2_start + 1.5, bar2_start + 1.6, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar2_start + 0.75, bar2_start + 0.85, 90))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar2_start + 1.25, bar2_start + 1.35, 90))

# --- BAR 3: Tenor Sax Melody (Answer Begins) ---
bar3_start = bar2_end
bar3_end = bar3_start + bar_duration

# Tenor Sax: Sparse, emotional, expressive
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Motif: D -> Eb -> G -> rest -> C -> Ab -> F -> rest

tenor = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program('Tenor Saxophone'))

tenor_notes = [
    ('D4', 0.0, 0.25, 95),
    ('Eb4', 0.375, 0.625, 80),
    ('G4', 0.75, 1.0, 100),
    ('C4', 1.5, 1.75, 90),
    ('Ab4', 1.875, 2.125, 85),
    ('F4', 2.25, 2.5, 95),
]

for note, start, end, vel in tenor_notes:
    tenor.notes.append(make_note(pretty_midi.note_name_to_number(note), bar3_start + start, bar3_start + end, vel))

# Drums (same as bar1)
for i in range(8):
    drums.notes.append(make_note(pretty_midi.note_name_to_number('G#4'), bar3_start + i * 0.375, bar3_start + i * 0.375 + 0.1, 70))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar3_start + 0.0, bar3_start + 0.1, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar3_start + 1.5, bar3_start + 1.6, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar3_start + 0.75, bar3_start + 0.85, 90))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar3_start + 1.25, bar3_start + 1.35, 90))

# --- BAR 4: Full Ensemble (Answer Completes) ---
bar4_start = bar3_end
bar4_end = bar4_start + bar_duration

# Bass: resolves with a chromatic run to D
bass_notes = [
    ('F3', 0.0),  # Dm
    ('Eb3', 0.375),  # chromatic
    ('E3', 0.75),   # chromatic
    ('F3', 1.125),  # Dm
    ('G3', 1.5),    # Dm 5
    ('Ab3', 1.875), # chromatic
    ('A3', 2.25),   # chromatic
    ('Bb3', 2.625), # Dm 7
    ('D3', 3.0),    # D
]

for note, time in bass_notes:
    start = bar4_start + time
    end = start + 0.25
    bass.notes.append(make_note(pretty_midi.note_name_to_number(note), start, end, 75))

# Piano: Dm7 on 2 and 4
piano_notes = [
    # Bar 4: Dm7 (D, F, Ab, C)
    ('D3', 0.0, 0.25, 70),
    ('F3', 0.0, 0.25, 70),
    ('Ab3', 0.0, 0.25, 70),
    ('C4', 0.0, 0.25, 70),

    # Bar 4: Dm7
    ('D3', 1.5, 1.75, 70),
    ('F3', 1.5, 1.75, 70),
    ('Ab3', 1.5, 1.75, 70),
    ('C4', 1.5, 1.75, 70),
]

for note, start, end, vel in piano_notes:
    piano.notes.append(make_note(pretty_midi.note_name_to_number(note), start + bar4_start, end + bar4_start, vel))

# Drums (same as bar1)
for i in range(8):
    drums.notes.append(make_note(pretty_midi.note_name_to_number('G#4'), bar4_start + i * 0.375, bar4_start + i * 0.375 + 0.1, 70))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar4_start + 0.0, bar4_start + 0.1, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('C3'), bar4_start + 1.5, bar4_start + 1.6, 80))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar4_start + 0.75, bar4_start + 0.85, 90))
drums.notes.append(make_note(pretty_midi.note_name_to_number('D3'), bar4_start + 1.25, bar4_start + 1.35, 90))

# Add instruments to the MIDI file
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(tenor)

# Write to MIDI file
pm.write('cellar_intro.mid')
print("MIDI file generated: cellar_intro.mid")
