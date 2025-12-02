
import pretty_midi
from pretty_midi import PrettyMIDI, Instrument, Note

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Define the tempo: 160 BPM → 0.375 seconds per beat
beat = 0.375  # seconds

# Define note values
def note_to_midi(note_name):
    note_map = {
        'D3': 62,
        'E3': 64,
        'F3': 65,
        'G3': 67,
        'A3': 69,
        'B3': 71,
        'C4': 72,
        'D4': 74,
        'E4': 76,
        'F4': 77,
        'G4': 79,
        'A4': 81,
        'B4': 83,
        'C5': 84,
    }
    return note_map[note_name]

# --- Drums (Instrument 9) ---
drums = Instrument(program=9, is_drum=True)
pm.instruments.append(drums)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * beat
        if beat == 0 or beat == 2:  # Kick
            drums.notes.append(Note(velocity=100, pitch=36, start=time, end=time + 0.05))
        if beat == 1 or beat == 3:  # Snare
            drums.notes.append(Note(velocity=100, pitch=38, start=time, end=time + 0.05))
        # Hi-hats on every 8th
        for eighth in range(2):
            hihat_time = time + eighth * 0.1875
            drums.notes.append(Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.02))

# --- Bass (Instrument 33) ---
bass = Instrument(program=33)
pm.instruments.append(bass)

# Bar 2: Bass enters with a walking line (chromatic approach to 4ths)
# Bar 2: D3 -> F3 (chromatic up), G3 -> D4 (4th)
# Bar 3: D3 -> F3 (same), G3 -> F#4 (chromatic up)
# Bar 4: D3 -> F3, G3 -> E4 (4th)

bass_notes = [
    note_to_midi('D3'), note_to_midi('F3'), note_to_midi('G3'), note_to_midi('D4'),  # Bar 2
    note_to_midi('D3'), note_to_midi('F3'), note_to_midi('G3'), note_to_midi('F#4'), # Bar 3
    note_to_midi('D3'), note_to_midi('F3'), note_to_midi('G3'), note_to_midi('E4'),  # Bar 4
    note_to_midi('D3')  # Hold D3 at end
]

bass_times = [i * beat for i in range(4 * 4)]  # 16 notes total
for i, note in enumerate(bass_notes):
    start = bass_times[i]
    end = start + 0.25
    bass.notes.append(Note(velocity=100, pitch=note, start=start, end=end))

# --- Piano (Instrument 0) ---
piano = Instrument(program=0)
pm.instruments.append(piano)

# Bar 2: Comp on 2 and 4
piano_notes = [
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 2, beat 2
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 2, beat 4
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 3, beat 2
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 3, beat 4
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 4, beat 2
    note_to_midi('G3'), note_to_midi('D4'), note_to_midi('F4'), note_to_midi('A4'),  # Bar 4, beat 4
]

piano_times = [bar * 1.5 + beat * beat for bar in range(2, 5) for beat in [1, 3]]
for i, note in enumerate(piano_notes):
    start = piano_times[i]
    end = start + 0.25
    piano.notes.append(Note(velocity=100, pitch=note, start=start, end=end))

# --- Tenor Sax (Instrument 64) ---
sax = Instrument(program=64)
pm.instruments.append(sax)

# Bar 3 and 4: Tenor sax motif
# Bar 3: D4 -> E4 -> D4 -> F4 (melody)
# Bar 4: D3 -> E3 -> D3 -> F3 (lower register, same motif)
sax_notes = [
    note_to_midi('D4'), note_to_midi('E4'), note_to_midi('D4'), note_to_midi('F4'),  # Bar 3
    note_to_midi('D3'), note_to_midi('E3'), note_to_midi('D3'), note_to_midi('F3')   # Bar 4
]

sax_times = [bar * 1.5 for bar in range(2, 4)]  # Start on bar 3 and 4
for i, note in enumerate(sax_notes):
    start = sax_times[i // 4] + (i % 4) * beat
    end = start + 0.25
    sax.notes.append(Note(velocity=100, pitch=note, start=start, end=end))

# Save the MIDI file
pm.write('dante_intro.mid')

print("MIDI file 'dante_intro.mid' created successfully.")
