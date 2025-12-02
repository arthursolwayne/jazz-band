
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
BEAT_DURATION = 60.0 / BPM  # 0.375 seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # 1.5 seconds per bar
TOTAL_DURATION = 4 * BAR_DURATION  # 6 seconds

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)
track = pretty_midi.Track(program=0)  # Default instrument is acoustic grand piano
midi.instruments.append(track)

# Helper function to convert beat to time in seconds
def beat_to_time(beat):
    return beat * BEAT_DURATION

# Function to add a note
def add_note(instrument, note_number, start_time, duration, velocity=100):
    note = Note(note_number, start_time, duration, velocity)
    instrument.notes.append(note)

# ---------------------------
# 1. Drums: Bar 1 Only
# ---------------------------

drum_program = pretty_midi.Instrument(program=128)  # Drums
midi.instruments.append(drum_program)

# Kick on 1 and 3 (beat 0 and 2)
add_note(drum_program, 36, beat_to_time(0), BEAT_DURATION / 2)
add_note(drum_program, 36, beat_to_time(2), BEAT_DURATION / 2)

# Snare on 2 and 4 (beat 1 and 3)
add_note(drum_program, 38, beat_to_time(1), BEAT_DURATION / 2)
add_note(drum_program, 38, beat_to_time(3), BEAT_DURATION / 2)

# Hi-hat on every eighth note (0.1875s intervals)
for i in range(8):
    add_note(drum_program, 42, beat_to_time(i * 0.125), BEAT_DURATION / 8)

# ---------------------------
# 2. Bass: Bars 2-4
# ---------------------------

bass_program = pretty_midi.Instrument(program=33)  # Acoustic Bass
midi.instruments.append(bass_program)

# Bass line: walking line with chromatic approaches, no repeated notes
# Bar 2
add_note(bass_program, 62, beat_to_time(4), BEAT_DURATION)  # F#3
add_note(bass_program, 63, beat_to_time(5), BEAT_DURATION)  # G3
add_note(bass_program, 61, beat_to_time(6), BEAT_DURATION)  # F3
add_note(bass_program, 60, beat_to_time(7), BEAT_DURATION)  # E3

# Bar 3
add_note(bass_program, 60, beat_to_time(8), BEAT_DURATION)  # E3
add_note(bass_program, 61, beat_to_time(9), BEAT_DURATION)  # F3
add_note(bass_program, 62, beat_to_time(10), BEAT_DURATION)  # F#3
add_note(bass_program, 64, beat_to_time(11), BEAT_DURATION)  # G#3

# Bar 4
add_note(bass_program, 64, beat_to_time(12), BEAT_DURATION)  # G#3
add_note(bass_program, 63, beat_to_time(13), BEAT_DURATION)  # G3
add_note(bass_program, 62, beat_to_time(14), BEAT_DURATION)  # F#3
add_note(bass_program, 60, beat_to_time(15), BEAT_DURATION)  # E3

# ---------------------------
# 3. Piano: Bars 2-4 (7th chords, sparse comping)
# ---------------------------

piano_program = pretty_midi.Instrument(program=0)  # Acoustic Grand Piano
midi.instruments.append(piano_program)

# 7th chords on beats 2 and 4
# Bar 2
add_note(piano_program, 67, beat_to_time(5), 0.1875)  # B3 (D7 chord: D, F#, A, C)
add_note(piano_program, 69, beat_to_time(5), 0.1875)  # D4
add_note(piano_program, 71, beat_to_time(5), 0.1875)  # F#4
add_note(piano_program, 72, beat_to_time(5), 0.1875)  # G4

# Bar 3
add_note(piano_program, 67, beat_to_time(9), 0.1875)  # B3 (D7 chord again)
add_note(piano_program, 69, beat_to_time(9), 0.1875)  # D4
add_note(piano_program, 71, beat_to_time(9), 0.1875)  # F#4
add_note(piano_program, 72, beat_to_time(9), 0.1875)  # G4

# Bar 4
add_note(piano_program, 67, beat_to_time(13), 0.1875)  # B3 (D7 chord)
add_note(piano_program, 69, beat_to_time(13), 0.1875)  # D4
add_note(piano_program, 71, beat_to_time(13), 0.1875)  # F#4
add_note(piano_program, 72, beat_to_time(13), 0.1875)  # G4

# ---------------------------
# 4. Tenor Sax: Bars 2-4 (unique, singable motif)
# ---------------------------

sax_program = pretty_midi.Instrument(program=64)  # Tenor Saxophone
midi.instruments.append(sax_program)

# Motif: G4 (beat 4), A4 (beat 4 + 0.1875), D5 (beat 4 + 0.5625), G4 (beat 5)
# This is a short, singable phrase with space and resolution
add_note(sax_program, 71, beat_to_time(4), 0.1875)  # G4
add_note(sax_program, 72, beat_to_time(4.1875), 0.1875)  # A4
add_note(sax_program, 76, beat_to_time(4.5625), 0.1875)  # D5
add_note(sax_program, 71, beat_to_time(5), 0.1875)  # G4

# Space (rest) until beat 6
add_note(sax_program, 71, beat_to_time(6), 0.1875)  # G4 (resolution)
add_note(sax_program, 72, beat_to_time(6.1875), 0.1875)  # A4
add_note(sax_program, 76, beat_to_time(6.5625), 0.1875)  # D5
add_note(sax_program, 71, beat_to_time(7), 0.1875)  # G4 (resolution again)

# Final resolution in bar 4
add_note(sax_program, 71, beat_to_time(12), 0.1875)  # G4
add_note(sax_program, 72, beat_to_time(12.1875), 0.1875)  # A4
add_note(sax_program, 76, beat_to_time(12.5625), 0.1875)  # D5
add_note(sax_program, 71, beat_to_time(13), 0.1875)  # G4 (resolution, full stop)

# ---------------------------
# Save the MIDI file
# ---------------------------

midi.write('dante_russo_intro.mid')
print("MIDI file saved as 'dante_russo_intro.mid'")
