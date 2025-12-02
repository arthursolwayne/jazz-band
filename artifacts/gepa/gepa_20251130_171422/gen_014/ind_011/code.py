
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument

# Constants
BPM = 160
BAR_LENGTH = 6.0  # seconds
BEAT_LENGTH = BAR_LENGTH / 4  # 1.5 seconds per beat
SAMPLE_RATE = 44100
D_NOTE = 62  # MIDI note for D4 (D in the 4th octave)

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax is program 64
midi.instruments.append(instrument)

# Time in seconds
time = 0.0

# Bar 1: Little Ray alone (drum fill)
# We'll just note this in comments, actual drum tracks would be added elsewhere
print("Bar 1: Snare on 2 and 4, hihat on every eighth. Kick on 1 and 3.")

# Bar 2: Diane enters with 7th chords, comp on 2 and 4
# Diane on piano, 7th chords on beats 2 and 4
# We'll represent her chords in MIDI (D7 on beat 2, F#7 on beat 4)

diane_notes = [
    (D_NOTE + 11, 2.0, time + 0.75),  # D7 on beat 2
    (D_NOTE + 5, 2.0, time + 0.75),   # F#7 on beat 2
    (D_NOTE + 11, 2.0, time + 1.5),   # D7 on beat 4
    (D_NOTE + 5, 2.0, time + 1.5),    # F#7 on beat 4
]

for note, duration, start_time in diane_notes:
    instrument.notes.append(Note(note, start_time, duration))

# Bar 2-4: Marcus on bass, walking line, chromatic approaches
# Bass line: D, Eb, E, F, G, F#, G#, A, Bb, B, C, B, C#, D
# Each note is a 16th note, so lasting 0.09375 seconds
bass_line = [
    D_NOTE - 24,  # D2
    D_NOTE - 23,  # Eb2
    D_NOTE - 22,  # E2
    D_NOTE - 21,  # F2
    D_NOTE - 20,  # G2
    D_NOTE - 19,  # F#2
    D_NOTE - 18,  # G#2
    D_NOTE - 17,  # A2
    D_NOTE - 16,  # Bb2
    D_NOTE - 15,  # B2
    D_NOTE - 14,  # C3
    D_NOTE - 15,  # B2
    D_NOTE - 13,  # C#3
    D_NOTE - 12,  # D3
]

for note in bass_line:
    duration = 0.09375
    instrument.notes.append(Note(note, time, duration))
    time += duration

# Bar 2: Your melody starts — a whisper, one short motif

# You: Tenor Sax, melody starts with a D4, then G4, then Bb4 — a major 7th chord
# Then you leave it hanging for a beat before resolving

melody = [
    (D_NOTE, 0.5, 0.0),     # D4 for 0.5 seconds (beat 1)
    (D_NOTE + 7, 0.5, 0.5), # G4 for 0.5 seconds (beat 2)
    (D_NOTE + 8, 0.5, 1.0), # A4 for 0.5 seconds (beat 3)
    (D_NOTE + 10, 0.5, 1.5),# Bb4 for 0.5 seconds (beat 4)
]

for note, duration, start_time in melody:
    instrument.notes.append(Note(note, start_time, duration))

# Bar 3: You come back, finish the motif
# You continue with a descending line, then resolve on D5

melody_continuation = [
    (D_NOTE + 12, 0.5, 2.0),  # C5
    (D_NOTE + 11, 0.5, 2.5),  # B4
    (D_NOTE + 10, 0.5, 3.0),  # A4
    (D_NOTE + 9, 0.5, 3.5),   # G4
    (D_NOTE + 7, 0.5, 4.0),   # F4
    (D_NOTE + 5, 0.5, 4.5),   # D4
    (D_NOTE + 12, 0.5, 5.0),  # C5
    (D_NOTE + 12, 0.5, 5.5),  # C5
]

for note, duration, start_time in melody_continuation:
    instrument.notes.append(Note(note, start_time, duration))

# Bar 4: You end with a soft D5, leaving it open — a question or a memory

instrument.notes.append(Note(D_NOTE + 12, 0.5, 6.0))  # D5 at the end

# Save the MIDI file
midi.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
