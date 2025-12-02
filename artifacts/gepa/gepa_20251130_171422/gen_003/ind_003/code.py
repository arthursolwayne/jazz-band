
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160
time_signature = (4, 4)
duration = 6.0  # 4 bars at 160 BPM = 6 seconds

# MIDI settings
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)
midi.time_signature_changes = [pretty_midi.TimeSignature(time_signature[0], time_signature[1], 0)]

# Create instruments
drums = Instrument(program=10, is_drum=True, name="Drums")
bass = Instrument(program=33, name="Bass")
piano = Instrument(program=0, name="Piano")
sax = Instrument(program=64, name="Saxophone")

# Function to convert time in seconds to MIDI ticks
def seconds_to_ticks(seconds):
    return int(seconds * midi.resolution * tempo / 60)

def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# ---------------------------
# DRUMS - Little Ray
# ---------------------------
# Kick on 1 and 3
kick = 36
snare = 38
hihat = 42

# Bar 1
bar_start = 0
bar_end = 1.5
add_note(drums, kick, bar_start, bar_start + 0.2)
add_note(drums, hihat, bar_start, bar_start + 0.2)
add_note(drums, kick, bar_start + 0.75, bar_start + 0.75 + 0.2)
add_note(drums, hihat, bar_start + 0.75, bar_start + 0.75 + 0.2)

# Bars 2-4
for bar in range(1, 4):
    bar_start = bar * 1.5
    add_note(drums, kick, bar_start, bar_start + 0.2)
    add_note(drums, hihat, bar_start, bar_start + 0.2)
    add_note(drums, kick, bar_start + 0.75, bar_start + 0.75 + 0.2)
    add_note(drums, hihat, bar_start + 0.75, bar_start + 0.75 + 0.2)
    add_note(drums, snare, bar_start + 1.0, bar_start + 1.0 + 0.2)
    add_note(drums, hihat, bar_start + 1.0, bar_start + 1.0 + 0.2)

# ---------------------------
# BASS - Marcus
# ---------------------------
# Fm7: F, Ab, C, Eb
# Walking line with chromatic approach, starting on Ab
# Bar 1: Ab -> F -> Eb -> C
# Bar 2: F -> Eb -> D -> C
# Bar 3: C -> B -> Ab -> F
# Bar 4: Ab -> G -> F -> Eb

note_lengths = 0.25  # quarter note
bar_start = 0

# Bar 1
add_note(bass, 8, bar_start, bar_start + note_lengths)
add_note(bass, 5, bar_start + note_lengths, bar_start + 2 * note_lengths)
add_note(bass, 3, bar_start + 2 * note_lengths, bar_start + 3 * note_lengths)
add_note(bass, 0, bar_start + 3 * note_lengths, bar_start + 4 * note_lengths)

# Bar 2
add_note(bass, 5, bar_start + 4 * note_lengths, bar_start + 5 * note_lengths)
add_note(bass, 3, bar_start + 5 * note_lengths, bar_start + 6 * note_lengths)
add_note(bass, 2, bar_start + 6 * note_lengths, bar_start + 7 * note_lengths)
add_note(bass, 0, bar_start + 7 * note_lengths, bar_start + 8 * note_lengths)

# Bar 3
add_note(bass, 0, bar_start + 8 * note_lengths, bar_start + 9 * note_lengths)
add_note(bass, -1, bar_start + 9 * note_lengths, bar_start + 10 * note_lengths)
add_note(bass, 8, bar_start + 10 * note_lengths, bar_start + 11 * note_lengths)
add_note(bass, 5, bar_start + 11 * note_lengths, bar_start + 12 * note_lengths)

# Bar 4
add_note(bass, 8, bar_start + 12 * note_lengths, bar_start + 13 * note_lengths)
add_note(bass, 7, bar_start + 13 * note_lengths, bar_start + 14 * note_lengths)
add_note(bass, 5, bar_start + 14 * note_lengths, bar_start + 15 * note_lengths)
add_note(bass, 3, bar_start + 15 * note_lengths, bar_start + 16 * note_lengths)

# ---------------------------
# PIANO - Diane
# ---------------------------
# 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
# Bb7 (Bb, D, F, Ab) on beat 4

# Bar 1
bar_start = 0
add_note(piano, 8, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 11, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 12, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 10, bar_start + 0.5, bar_start + 0.75)

# Bar 2
bar_start = 1.5
add_note(piano, 10, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 13, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 12, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 8, bar_start + 0.5, bar_start + 0.75)

# Bar 3
bar_start = 3.0
add_note(piano, 8, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 11, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 12, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 10, bar_start + 0.5, bar_start + 0.75)

# Bar 4
bar_start = 4.5
add_note(piano, 10, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 13, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 12, bar_start + 0.5, bar_start + 0.75)
add_note(piano, 8, bar_start + 0.5, bar_start + 0.75)

# ---------------------------
# SAX - Dante
# ---------------------------
# Short, emotional motif: F, Eb, D, C
# Start on beat 1, leave it hanging on Eb, come back on beat 3 to finish

# Bar 1
bar_start = 0
add_note(sax, 5, bar_start, bar_start + 0.5)
add_note(sax, 3, bar_start + 0.5, bar_start + 1.0)
add_note(sax, 2, bar_start + 1.0, bar_start + 1.5)

# Bar 3 - finish the motif
bar_start = 3.0
add_note(sax, 5, bar_start, bar_start + 0.5)
add_note(sax, 3, bar_start + 0.5, bar_start + 1.0)
add_note(sax, 2, bar_start + 1.0, bar_start + 1.5)

# ---------------------------
# Add instruments to MIDI
# ---------------------------
midi.instruments = [drums, bass, piano, sax]

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file generated: dante_intro.mid")
