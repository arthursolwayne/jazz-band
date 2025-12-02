
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.key_signature_changes = [pretty_midi.KeySignature(-3, 0)]  # Fm (F minor)

# Define BPM and time in seconds per beat
BPM = 160
seconds_per_beat = 60.0 / BPM  # 0.375 seconds per beat
bar_length = seconds_per_beat * 4  # 1.5 seconds per bar

# Create instruments
drums = Instrument(program=Program(0), is_drum=True)
bass = Instrument(program=Program(33))
piano = Instrument(program=Program(0))
saxophone = Instrument(program=Program(64))

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, saxophone]

# Helper functions
def add_note(instrument, note, start, end, velocity):
    note_obj = Note(note, start, end, velocity)
    instrument.notes.append(note_obj)

# Bar 1: Drums - Little Ray sets the tone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Use dynamic contrast and space

# Kick
add_note(drums, 36, 0.0, 0.1, 80)
add_note(drums, 36, 1.5, 1.6, 80)

# Snare
add_note(drums, 38, 0.75, 0.85, 85)
add_note(drums, 38, 1.25, 1.35, 85)

# Hihat (every eighth)
hihat_velocity = 60
for i in range(8):
    add_note(drums, 42, i * 0.375, i * 0.375 + 0.1, hihat_velocity)

# Bar 2-4: Bring in the full quartet

# Bass: Marcus - walking, chromatic, no repetition
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Chromatic walking: F, Gb, G, Ab, A, Bb, B, C, Db, etc.
# Start at F, walk chromatically for 3 bars (12 notes)

bass_notes = [65, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]  # F, Gb, G, Ab, A, Bb, B, C, Db, D, Eb, E
for i, note in enumerate(bass_notes):
    start = i * seconds_per_beat
    end = start + 0.1
    add_note(bass, note, start, end, 90)

# Piano: Diane - 7th chords on beats 2 and 4, comp on 2 and 4
# Fm7 = F, Ab, Bb, C
# Fm7 on beat 2 of bar 2, and 4 of bar 2
# Fm7 on beat 2 of bar 3, and 4 of bar 3

# Bar 2
add_note(piano, 65, 0.75, 0.75 + 0.1, 85)  # F
add_note(piano, 67, 0.75, 0.75 + 0.1, 85)  # Ab
add_note(piano, 68, 0.75, 0.75 + 0.1, 85)  # Bb
add_note(piano, 72, 0.75, 0.75 + 0.1, 85)  # C

add_note(piano, 65, 1.5, 1.5 + 0.1, 85)  # F
add_note(piano, 67, 1.5, 1.5 + 0.1, 85)  # Ab
add_note(piano, 68, 1.5, 1.5 + 0.1, 85)  # Bb
add_note(piano, 72, 1.5, 1.5 + 0.1, 85)  # C

# Bar 3
add_note(piano, 65, 2.25, 2.25 + 0.1, 85)  # F
add_note(piano, 67, 2.25, 2.25 + 0.1, 85)  # Ab
add_note(piano, 68, 2.25, 2.25 + 0.1, 85)  # Bb
add_note(piano, 72, 2.25, 2.25 + 0.1, 85)  # C

add_note(piano, 65, 3.0, 3.0 + 0.1, 85)  # F
add_note(piano, 67, 3.0, 3.0 + 0.1, 85)  # Ab
add_note(piano, 68, 3.0, 3.0 + 0.1, 85)  # Bb
add_note(piano, 72, 3.0, 3.0 + 0.1, 85)  # C

# Saxophone: You - short, singable motif. Start it, leave it hanging, come back
# Fmi7 - F, Ab, Bb, C
# Melody: F (beat 1), Ab (beat 2), rest (beat 3), Bb (beat 4), F (beat 1 next bar), Ab (beat 2), rest (beat 3), C (beat 4)

# Bar 2 - Start of melody
add_note(saxophone, 65, 0.0, 0.15, 90)  # F
add_note(saxophone, 67, 0.75, 0.9, 90)  # Ab
add_note(saxophone, 68, 3.0, 3.15, 90)  # Bb
add_note(saxophone, 65, 3.75, 3.9, 90)  # F
add_note(saxophone, 67, 4.5, 4.65, 90)  # Ab
add_note(saxophone, 68, 5.25, 5.4, 90)  # Bb
add_note(saxophone, 72, 5.75, 5.9, 90)  # C

# Add dynamic subtlety (velocity variation):
# 90, 85, 80, 90, 85, 80, 90
# Not fully implemented in this script but implied by velocity changes

# Write to file
midi.write("fm_intro.mid")
print("MIDI file 'fm_intro.mid' has been written.")
