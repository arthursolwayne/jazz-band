
import pretty_midi
from pretty_midi import Note, Instrument, MetaMessage
import numpy as np

# Constants
BPM = 160
TEMPO = 60 * 1000 / BPM  # microseconds per beat
TIME_SIGNATURE = (4, 4)
KEY = 'D'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=TEMPO)
pm.time_signature_changes.append(pretty_midi.TimeSignature(numerator=4, denominator=4, time=0))
pm.key_signatures.append(pretty_midi.KeySignature(key_number=2, time=0))  # D major

# Track for each instrument
bass_track = Instrument(program=33)  # Bass
piano_track = Instrument(program=0)  # Piano
drums_track = Instrument(program=0)  # Drums
sax_track = Instrument(program=64)  # Tenor Sax

pm.instruments.append(bass_track)
pm.instruments.append(piano_track)
pm.instruments.append(drums_track)
pm.instruments.append(sax_track)

# Time per beat in seconds
beat_time = TEMPO / 1_000_000  # Convert microseconds to seconds

# Time per bar
bar_time = beat_time * 4

# Helper to make notes
def make_note(note_number, start, duration, velocity=100):
    return Note(note_number, start, duration, velocity)

# 4 bars = 6 seconds
# Bar 1: Drums only
# Bar 2-4: Full band, sax takes the melody

# BAR 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beat 1
drums_track.notes.append(make_note(36, 0, beat_time, 80))  # Kick
# Snare on beat 2
drums_track.notes.append(make_note(38, beat_time, beat_time, 80))  # Snare
# Hihat on every eighth
for i in range(8):
    drums_track.notes.append(make_note(42, i * beat_time / 2, beat_time / 2, 60))  # Hihat

# Kick on beat 3
drums_track.notes.append(make_note(36, 3 * beat_time, beat_time, 80))  # Kick
# Snare on beat 4
drums_track.notes.append(make_note(38, 4 * beat_time, beat_time, 80))  # Snare
# Hihat on every eighth
for i in range(8):
    drums_track.notes.append(make_note(42, (3 * beat_time) + i * beat_time / 2, beat_time / 2, 60))  # Hihat

# BAR 2: Sax melody, piano, bass
# Key is D major: D, E, F#, G, A, B, C#
# Simple motif for sax: D4, F#4, A4, D5
# Let the first note hang

sax_notes = [
    make_note(62, 4 * beat_time, beat_time * 0.5, 100),  # D4
    make_note(67, 4 * beat_time + beat_time * 0.5, beat_time * 1.5, 100),  # F#4
    make_note(69, 4 * beat_time + beat_time * 2.0, beat_time * 1.0, 100),  # A4
    make_note(72, 4 * beat_time + beat_time * 3.0, beat_time * 0.5, 100),  # D5
]

for note in sax_notes:
    sax_track.notes.append(note)

# Bass: Walking line in D major, roots and fifths with chromatic approaches
# D2 -> E2 -> F#2 -> G2 -> A2 -> B2 -> C#3 -> D3

bass_notes = [
    make_note(38, 4 * beat_time, beat_time, 80),  # D2
    make_note(40, 5 * beat_time, beat_time, 80),  # E2
    make_note(39, 6 * beat_time, beat_time, 80),  # F#2 (chromatic approach)
    make_note(43, 7 * beat_time, beat_time, 80),  # G2
    make_note(45, 8 * beat_time, beat_time, 80),  # A2
    make_note(47, 9 * beat_time, beat_time, 80),  # B2
    make_note(48, 10 * beat_time, beat_time, 80),  # C#3 (chromatic approach)
    make_note(50, 11 * beat_time, beat_time, 80),  # D3
]

for note in bass_notes:
    bass_track.notes.append(note)

# Piano: Open voicings, resolve on last chord (bar 2: D major, bar 3: G major, bar 4: A minor)

# Bar 2: Dmaj7 (D4, F#4, A4, C#4)
piano_notes = [
    make_note(62, 4 * beat_time, beat_time * 0.5, 100),  # D4
    make_note(67, 4 * beat_time, beat_time * 0.5, 100),  # F#4
    make_note(69, 4 * beat_time, beat_time * 0.5, 100),  # A4
    make_note(65, 4 * beat_time, beat_time * 0.5, 100),  # C#4
]

# Bar 3: Gmaj7 (G4, B4, D5, F#4)
piano_notes += [
    make_note(67, 5 * beat_time, beat_time * 0.5, 100),  # G4
    make_note(71, 5 * beat_time, beat_time * 0.5, 100),  # B4
    make_note(72, 5 * beat_time, beat_time * 0.5, 100),  # D5
    make_note(67, 5 * beat_time, beat_time * 0.5, 100),  # F#4
]

# Bar 4: Am7 (A4, C#4, E4, G4)
piano_notes += [
    make_note(69, 6 * beat_time, beat_time * 0.5, 100),  # A4
    make_note(65, 6 * beat_time, beat_time * 0.5, 100),  # C#4
    make_note(67, 6 * beat_time, beat_time * 0.5, 100),  # E4
    make_note(67, 6 * beat_time, beat_time * 0.5, 100),  # G4
]

for note in piano_notes:
    piano_track.notes.append(note)

# BAR 3 and 4: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# BAR 2 (note: Bar 2-4 is the full band, so starting from bar 2 which is 4*beat_time)

# For Bar 2 (already done), Bar 3, and Bar 4, repeat the same pattern
for bar in range(2, 4):
    start = bar * 4 * beat_time
    # Kick on 1 and 3
    drums_track.notes.append(make_note(36, start, beat_time, 80))  # Kick
    drums_track.notes.append(make_note(36, start + 3 * beat_time, beat_time, 80))  # Kick
    # Snare on 2 and 4
    drums_track.notes.append(make_note(38, start + beat_time, beat_time, 80))  # Snare
    drums_track.notes.append(make_note(38, start + 4 * beat_time, beat_time, 80))  # Snare
    # Hihat on every eighth
    for i in range(8):
        drums_track.notes.append(make_note(42, start + i * beat_time / 2, beat_time / 2, 60))  # Hihat

# Write the MIDI file
pm.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been generated.")
