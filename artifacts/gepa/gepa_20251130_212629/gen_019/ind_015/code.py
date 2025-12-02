
import pretty_midi
from pretty_midi import Note, NoteEvent, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS)
piano = Instrument(program=Program.PIANO)
sax = Instrument(program=Program.SAXOPHONE)

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Define the time per bar (160 BPM = 6/160 = 0.0375 minutes per beat)
# 4/4 time, so one bar = 4 beats = 4 * 0.0375 * 60 = 9 seconds per bar? No, that's wrong.
# Wait, 160 BPM = 160 beats per minute, so one beat = 60 / 160 = 0.375 seconds.
# 4 bars = 4 * 4 = 16 beats = 16 * 0.375 = 6 seconds (as specified).

# Each bar is 1.5 seconds
BAR_DURATION = 1.5
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds per beat

# Time (in seconds) for each note
time = 0.0

# --- DRUMS (Little Ray) - Bar 1: Syncopated, tension-filled ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'Kick': [0, 3],  # Beats 1 and 3
    'Snare': [1, 2],  # Beats 2 and 4
    'Hi-Hat': [0, 1, 2, 3, 4, 5, 6, 7],  # Eighth notes
}

for beat in drum_notes['Hi-Hat']:
    note = Note(velocity=100, pitch=42, start=time + beat * BEAT_DURATION, end=time + beat * BEAT_DURATION + 0.05)
    drums.notes.append(note)

for beat in drum_notes['Kick']:
    note = Note(velocity=100, pitch=36, start=time + beat * BEAT_DURATION, end=time + beat * BEAT_DURATION + 0.1)
    drums.notes.append(note)

for beat in drum_notes['Snare']:
    note = Note(velocity=100, pitch=38, start=time + beat * BEAT_DURATION, end=time + beat * BEAT_DURATION + 0.1)
    drums.notes.append(note)

time += BAR_DURATION  # Move to Bar 2

# --- BASS (Marcus) - Walking line in Dm, chromatic approaches ---
# Dm7: D, F, A, C
# Chromatic approach to D on beat 1
# Walking line: D, C#, D, F, E, F, G, A, G, A, Bb, B, A, Bb, C, D

bass_notes = [
    (0.0, 2, 100),     # D
    (0.375, 21, 100),  # C#
    (0.75, 2, 100),    # D
    (1.125, 5, 100),   # F
    (1.5, 4, 100),     # E
    (1.875, 5, 100),   # F
    (2.25, 7, 100),    # G
    (2.625, 9, 100),   # A
    (3.0, 7, 100),     # G
    (3.375, 9, 100),   # A
    (3.75, 10, 100),   # Bb
    (4.125, 11, 100),  # B
    (4.5, 9, 100),     # A
    (4.875, 10, 100),  # Bb
    (5.25, 0, 100),    # C
    (5.625, 2, 100),   # D
]

for start, pitch, velocity in bass_notes:
    note = Note(velocity=velocity, pitch=pitch, start=time + start, end=time + start + 0.05)
    bass.notes.append(note)

time += BAR_DURATION  # Move to Bar 3

# --- PIANO (Diane) - 7th chords, comp on 2 and 4, dark and aggressive ---
# Dm7: D, F, A, C
# Comping on 2 and 4 with 7th chords, but with tension (augmented 5ths, etc.)

# Use 1/2 note chords
# Bar 2: Dm7 on beat 2
# Bar 3: G7#5 on beat 4
# Bar 4: Cm7 on beat 2, B7 on beat 4

# Dm7: D, F, A, C
# G7#5: G, B, D, F# (augmented 5th)
# Cm7: C, Eb, G, Bb
# B7: B, D#, F#, A

note_events = [
    (time + 0.75, 2, 100, 0.3),   # Dm7 on beat 2
    (time + 0.75, 5, 100, 0.3),   # F
    (time + 0.75, 9, 100, 0.3),   # A
    (time + 0.75, 0, 100, 0.3),   # C

    (time + 2.25, 7, 100, 0.3),   # G7#5 on beat 4
    (time + 2.25, 11, 100, 0.3),  # B
    (time + 2.25, 2, 100, 0.3),   # D
    (time + 2.25, 6, 100, 0.3),   # F#

    (time + 3.75, 0, 100, 0.3),   # Cm7 on beat 2 (Bar 4)
    (time + 3.75, 3, 100, 0.3),   # Eb
    (time + 3.75, 9, 100, 0.3),   # G
    (time + 3.75, 10, 100, 0.3),  # Bb

    (time + 5.25, 11, 100, 0.3),  # B7 on beat 4
    (time + 5.25, 2, 100, 0.3),   # D#
    (time + 5.25, 6, 100, 0.3),   # F#
    (time + 5.25, 9, 100, 0.3),   # A
]

for start, pitch, velocity, duration in note_events:
    note = Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

time += BAR_DURATION  # Move to Bar 4

# --- SAX (You) - Short, singing motif, ends on a question ---
# Motif: D - F - A - (C?) — leave it hanging on A
# Note durations: quarter, quarter, quarter, eighth

sax_notes = [
    (time, 2, 100, 0.375),   # D
    (time + 0.375, 5, 100, 0.375),  # F
    (time + 0.75, 9, 100, 0.375),   # A
    (time + 1.125, 9, 100, 0.1875)  # A (short, hanging)
]

for start, pitch, velocity, duration in sax_notes:
    note = Note(velocity=velocity, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')

print("MIDI file created: 'dante_intro.mid'")
