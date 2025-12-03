
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define the key: D minor (D, F, G)
# Root: D, 3rd: F, 5th: G

# Define the time per beat and per bar
beats_per_bar = 4
bars = 4
beat_duration = 60.0 / tempo  # seconds per beat
bar_duration = beat_duration * beats_per_bar  # seconds per bar

# Define note durations
quarter_note = beat_duration
eighth_note = beat_duration / 2

# ---------------------------
# 1. DRUMS - Little Ray
# ---------------------------

drums_program = Program(0, 0)  # 0 is percussion
drums = Instrument(program=drums_program, is_drum=True)

# Kick on 1 and 3
for bar in range(bars):
    kick_beat = bar * beats_per_bar + 0
    kick_time = kick_beat * beat_duration
    kick_note = Note(36, 100, kick_time, kick_time + quarter_note)
    drums.notes.append(kick_note)

    kick_beat = bar * beats_per_bar + 2
    kick_time = kick_beat * beat_duration
    kick_note = Note(36, 100, kick_time, kick_time + quarter_note)
    drums.notes.append(kick_note)

# Snare on 2 and 4
for bar in range(bars):
    snare_beat = bar * beats_per_bar + 1
    snare_time = snare_beat * beat_duration
    snare_note = Note(38, 100, snare_time, snare_time + quarter_note)
    drums.notes.append(snare_note)

    snare_beat = bar * beats_per_bar + 3
    snare_time = snare_beat * beat_duration
    snare_note = Note(38, 100, snare_time, snare_time + quarter_note)
    drums.notes.append(snare_note)

# Hi-hat on every eighth note
start = 0
for bar in range(bars):
    for beat in range(4):
        for i in range(2):
            hihat_time = (bar * 4 + beat) * beat_duration + i * eighth_note
            hihat_note = Note(42, 80, hihat_time, hihat_time + eighth_note)
            drums.notes.append(hihat_note)

pm.instruments.append(drums)

# ---------------------------
# 2. BASS - Marcus
# ---------------------------

bass_program = Program(33, 0)  # Double Bass
bass = Instrument(program=bass_program)

# Walking bass line: D2, F2, G2, A2, etc. Roots and fifths with chromatic approaches
# Each bar has 4 notes (quarter notes)
# We'll use D2 (MIDI 38), F2 (MIDI 41), G2 (MIDI 43), A2 (MIDI 45), etc.

# Bar 1
bass_notes = [38, 41, 43, 45]
for i, note in enumerate(bass_notes):
    start = i * beat_duration
    bass_note = Note(note, 70, start, start + quarter_note)
    bass.notes.append(bass_note)

# Bar 2: D2 -> F2 -> G2 -> Ab2
bass_notes = [38, 41, 43, 44]
for i, note in enumerate(bass_notes):
    start = (1 * 4 + i) * beat_duration
    bass_note = Note(note, 70, start, start + quarter_note)
    bass.notes.append(bass_note)

# Bar 3: D2 -> F2 -> G2 -> A2
bass_notes = [38, 41, 43, 45]
for i, note in enumerate(bass_notes):
    start = (2 * 4 + i) * beat_duration
    bass_note = Note(note, 70, start, start + quarter_note)
    bass.notes.append(bass_note)

# Bar 4: D2 -> F2 -> G2 -> A2
bass_notes = [38, 41, 43, 45]
for i, note in enumerate(bass_notes):
    start = (3 * 4 + i) * beat_duration
    bass_note = Note(note, 70, start, start + quarter_note)
    bass.notes.append(bass_note)

pm.instruments.append(bass)

# ---------------------------
# 3. PIANO - Diane
# ---------------------------

piano_program = Program(0, 0)  # Acoustic Grand Piano
piano = Instrument(program=piano_program)

# Bar 1: Dm7 (D, F, A, C)
# Open voicing: C (MIDI 60), A (MIDI 69), F (MIDI 53), D (MIDI 62)
note_start = 0
note_duration = quarter_note
chord = [60, 69, 53, 62]
for note in chord:
    piano_note = Note(note, 90, note_start, note_start + note_duration)
    piano.notes.append(piano_note)

# Bar 2: D7 (D, F, A, C#)
# Resolve to C#
note_start = 1 * beat_duration
note_duration = quarter_note
chord = [60, 69, 53, 64]
for note in chord:
    piano_note = Note(note, 90, note_start, note_start + note_duration)
    piano.notes.append(piano_note)

# Bar 3: Dm7 (resolve back to Dm)
note_start = 2 * beat_duration
note_duration = quarter_note
chord = [60, 69, 53, 62]
for note in chord:
    piano_note = Note(note, 90, note_start, note_start + note_duration)
    piano.notes.append(piano_note)

# Bar 4: G7 (Dm -> G7 for V7/I)
note_start = 3 * beat_duration
note_duration = quarter_note
chord = [67, 76, 62, 67]  # G7: G, B, D, F
for note in chord:
    piano_note = Note(note, 90, note_start, note_start + note_duration)
    piano.notes.append(piano_note)

pm.instruments.append(piano)

# ---------------------------
# 4. SAX - You
# ---------------------------

sax_program = Program(64, 0)  # Tenor Saxophone
sax = Instrument(program=sax_program)

# Sax line: simple, haunting motif
# Bar 1: Rest
pass

# Bar 2: Start of motif
note_start = 1 * beat_duration
note_duration = eighth_note
sax_note = Note(64, 95, note_start, note_start + note_duration)  # E4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(62, 95, note_start, note_start + note_duration)  # D4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(64, 95, note_start, note_start + note_duration)  # E4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(65, 95, note_start, note_start + note_duration)  # F4
sax.notes.append(sax_note)

# Rest of bar 2
note_start += note_duration
rest_time = note_start
rest_end = rest_time + (bar_duration - note_start)
sax_note = Note(-1, 0, rest_time, rest_end)
sax.notes.append(sax_note)

# Bar 3: Rest
pass

# Bar 4: Return to motif
note_start = 3 * beat_duration
note_duration = eighth_note
sax_note = Note(64, 95, note_start, note_start + note_duration)  # E4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(62, 95, note_start, note_start + note_duration)  # D4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(64, 95, note_start, note_start + note_duration)  # E4
sax.notes.append(sax_note)

note_start += note_duration
sax_note = Note(65, 95, note_start, note_start + note_duration)  # F4
sax.notes.append(sax_note)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
