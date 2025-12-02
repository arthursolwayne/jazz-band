
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Program numbers for the instruments
DRUMS_PROGRAM = 0  # Acoustic Drums
BASS_PROGRAM = 33  # Electric Bass
PIANO_PROGRAM = 0  # Acoustic Grand Piano
SAX_PROGRAM = 64   # Tenor Saxophone

# Create instruments
drums = Instrument(program=DRUMS_PROGRAM, is_drum=True)
bass = Instrument(program=BASS_PROGRAM)
piano = Instrument(program=PIANO_PROGRAM)
sax = Instrument(program=SAX_PROGRAM)

# Define the tempo (160 BPM)
tempo = 160
beat = 60.0 / tempo  # seconds per beat
bar_length = 4 * beat  # seconds per bar

# Helper function: add note
def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# -----------------------------
# BAR 1: Drums only
# -----------------------------
# Kick on 1 and 3
add_note(drums, 36, 0.0, 0.25)
add_note(drums, 36, 1.5, 1.75)
# Snare on 2 and 4
add_note(drums, 38, 0.75, 0.95)
add_note(drums, 38, 2.25, 2.45)
# Hihats on every eighth
hihat_pitches = [42] * 8  # 8 eighth notes per bar
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for time in hihat_times:
    add_note(drums, 42, time, time + 0.15)

# -----------------------------
# BAR 2: Full Band Enters
# -----------------------------
# Bass: walking line in F major
# Notes: F, E, D, C, Bb, A, G, Ab
bass_notes = [71, 70, 69, 67, 65, 64, 62, 60]
bass_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for pitch, time in zip(bass_notes, bass_times):
    add_note(bass, pitch, time, time + 0.25)

# Piano: 7th chords on 2 and 4, F7
# F7 = F, A, C, E♭
piano_notes = [71, 74, 76, 70]
for time in [0.75, 2.25]:
    for note in piano_notes:
        add_note(piano, note, time, time + 0.25)

# Sax: Motif - F (71), A (74), pause, F (71)
add_note(sax, 71, 0.0, 0.375)  # F
add_note(sax, 74, 0.75, 1.125)  # A
add_note(sax, 71, 1.5, 1.875)  # F

# -----------------------------
# BAR 3: Continue Bass and Piano
# -----------------------------
# Bass: walking line again, but chromatic (F, E, D#, C#, B, A#, G#, G)
bass_notes = [71, 70, 69, 67, 65, 64, 62, 60]
bass_times = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for pitch, time in zip(bass_notes, bass_times):
    add_note(bass, pitch, time, time + 0.25)

# Piano: 7th chords again
for time in [3.75, 5.25]:
    for note in piano_notes:
        add_note(piano, note, time, time + 0.25)

# -----------------------------
# BAR 4: Sax motif returns, leaves it open
# -----------------------------
add_note(sax, 71, 3.0, 3.375)  # F
add_note(sax, 74, 3.75, 4.125)  # A
add_note(sax, 71, 4.5, 4.875)  # F

# -----------------------------
# Add instruments to the PrettyMIDI object
# -----------------------------
pm.instruments = [drums, bass, piano, sax]

# Save to MIDI file
pm.write("jazz_intro_wayne_shorter.mid")
