
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per beat (160 BPM = 60/160 = 0.375 seconds per beat)
BEAT = 0.375
BAR = 4 * BEAT  # 1.5 seconds per bar

# Function to add a note
def add_note(instrument, pitch, start_time, duration=BEAT):
    note = Note(pitch=pitch, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# Define instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.ACOUSTIC_GRAND_PIANO)
sax = Instrument(program=Program.TENOR_SAXOPHONE)

pm.instruments.extend([drums, bass, piano, sax])

# BAR 1: Silence (build anticipation)
# Drums only on the hihat — subtle, building tension
add_note(drums, pretty_midi.note_number_to_name(42), 0, duration=BAR)  # Hihat on every eighth

# BAR 2: Bass enters with a chromatic walking line
# 16 notes over the bar (each 0.09375 seconds apart)
for i in range(16):
    note_number = 50 + i % 12  # Chromatic pattern, starting at C (50) in D minor:
    time = BEAT * 2 + i * 0.09375
    add_note(bass, note_number, time, duration=0.09375)

# BAR 2: Piano enters with comping on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4, with 7th chord voicings:
add_note(piano, 62, BEAT * 2 + BEAT * 0.5, duration=0.25)  # D (62)
add_note(piano, 65, BEAT * 2 + BEAT * 0.5, duration=0.25)  # F (65)
add_note(piano, 67, BEAT * 2 + BEAT * 0.5, duration=0.25)  # A (67)
add_note(piano, 71, BEAT * 2 + BEAT * 0.5, duration=0.25)  # C (71)

# BAR 3: Saxophone enters with a searching motif (searching for resolution)
sax_notes = [
    (62, 0.0),     # D (start of bar)
    (65, 0.5),     # F
    (67, 1.0),     # A
    (62, 1.5),     # D
    (65, 2.0),     # F
    (67, 2.5),     # A
    (62, 3.0),     # D (end of bar)
]
for pitch, offset in sax_notes:
    add_note(sax, pitch, BEAT * 2 + offset, duration=0.5)

# BAR 3: Drums continue — kick on 1 and 3, snare on 2 and 4
add_note(drums, pretty_midi.note_number_to_name(36), BEAT * 2, duration=0.125)  # Kick
add_note(drums, pretty_midi.note_number_to_name(21), BEAT * 2 + BEAT * 1, duration=0.125)  # Snare
add_note(drums, pretty_midi.note_number_to_name(36), BEAT * 2 + BEAT * 2, duration=0.125)  # Kick
add_note(drums, pretty_midi.note_number_to_name(21), BEAT * 2 + BEAT * 3, duration=0.125)  # Snare
add_note(drums, pretty_midi.note_number_to_name(42), BEAT * 2, duration=BAR)  # Hihat every 8th

# BAR 4: Piano continues with comping, slight variation
add_note(piano, 62, BEAT * 3 + BEAT * 0.5, duration=0.25)  # D (62)
add_note(piano, 65, BEAT * 3 + BEAT * 0.5, duration=0.25)  # F (65)
add_note(piano, 67, BEAT * 3 + BEAT * 0.5, duration=0.25)  # A (67)
add_note(piano, 72, BEAT * 3 + BEAT * 0.5, duration=0.25)  # C# (72) — a twist

# BAR 4: Sax repeats motif, ends on a question
for pitch, offset in sax_notes:
    add_note(sax, pitch, BEAT * 3 + offset, duration=0.5)

# Save to MIDI file
pm.write("dante_intro.mid")
