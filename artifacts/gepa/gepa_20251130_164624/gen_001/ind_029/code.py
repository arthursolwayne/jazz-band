
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key (D major)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]  # D major (key number 2)

# Define the time per bar: 160 BPM, 4/4 time
# 60 seconds / 160 beats = 0.375 seconds per beat.
# 4 bars = 6 seconds total.

# Define bar divisions (6 seconds total)
bar_duration = 1.5  # 1.5 seconds per bar
beat_duration = 0.375  # 0.375 seconds per beat

# Create instruments
drum_instrument = Instrument(program=0, is_drum=True)
piano_instrument = Instrument(program=0)
bass_instrument = Instrument(program=33)
sax_instrument = Instrument(program=64)

pm.instruments = [drum_instrument, piano_instrument, bass_instrument, sax_instrument]

# -----------------------------
# Bar 1: Only Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Bar 1 starts at 0.0 seconds
# -----------------------------

# Kick on 1 and 3 (beats 0 and 2 in bar)
drum_instrument.notes.append(Note(36, 100, 0.0, 0.375))  # Kick on 1
drum_instrument.notes.append(Note(36, 100, 0.75, 0.375))  # Kick on 3

# Snare on 2 and 4
drum_instrument.notes.append(Note(38, 100, 0.375, 0.375))  # Snare on 2
drum_instrument.notes.append(Note(38, 100, 1.125, 0.375))  # Snare on 4

# Hi-hat on every eighth note (total 8 notes per bar)
for i in range(8):
    start = i * 0.375
    drum_instrument.notes.append(Note(42, 100, start, 0.375))

# -----------------------------
# Bar 2: Full Quartet
# Start at 1.5 seconds
# -----------------------------

# Bass line (walking line, chromatic approaches, no repeated notes)
# D major key: D, E, F#, G, A, B, C#, D
# Bass line in 4/4, walking on each beat with chromatic passing tones
# Chord root on beat 1: D7 (D F# A C#)

# Bass notes (in beats, relative to start time: 1.5)
bass_notes = [
    Note(62, 90, 1.5, 0.375),  # D
    Note(63, 90, 1.875, 0.375),  # E
    Note(61, 90, 2.25, 0.375),  # C# (chromatic passing)
    Note(63, 90, 2.625, 0.375),  # E
    Note(65, 90, 2.999, 0.375),  # G
    Note(67, 90, 3.375, 0.375),  # B
    Note(66, 90, 3.75, 0.375),  # A
    Note(65, 90, 4.125, 0.375),  # G
]

bass_instrument.notes.extend(bass_notes)

# Piano comping on beats 2 and 4 with 7th chords
# D7: D, F#, A, C#
# Chord on beat 2 (start time 1.875)
piano_notes = [
    Note(62, 100, 1.875, 0.375),  # D
    Note(67, 100, 1.875, 0.375),  # F#
    Note(69, 100, 1.875, 0.375),  # A
    Note(71, 100, 1.875, 0.375),  # C#

    # Chord on beat 4 (start time 2.625)
    Note(62, 100, 2.625, 0.375),  # D
    Note(67, 100, 2.625, 0.375),  # F#
    Note(69, 100, 2.625, 0.375),  # A
    Note(71, 100, 2.625, 0.375),  # C#
]

piano_instrument.notes.extend(piano_notes)

# Drums for bar 2 (same pattern as bar 1)
# Kick on 1 and 3
drum_instrument.notes.append(Note(36, 100, 1.5, 0.375))
drum_instrument.notes.append(Note(36, 100, 1.875, 0.375))

# Snare on 2 and 4
drum_instrument.notes.append(Note(38, 100, 1.875, 0.375))
drum_instrument.notes.append(Note(38, 100, 2.625, 0.375))

# Hi-hat on every eighth note (starts at 1.5)
for i in range(8):
    start = 1.5 + i * 0.375
    drum_instrument.notes.append(Note(42, 100, start, 0.375))

# -----------------------------
# Saxophone Motif (Bar 2-3)
# Start at 1.5
# Motif: D -> F# -> rest -> A
# Rhythmic durations: D on beat 1 (0.375), F# on beat 2 (0.25), rest on beat 3 (0.5), A on beat 4 (0.5)
# -----------------------------

sax_notes = [
    Note(62, 110, 1.5, 0.375),  # D
    Note(67, 105, 1.875, 0.25),  # F#
    Note(69, 110, 2.125, 0.5),  # A (starts on beat 3.5, ends on beat 4)
]

# Additional note to close the bar (but rest from F# to A)
# Wait, original instruction says to leave a rest in the melody, so a space between F# and A
# So the saxophone rests from beat 2.25 (end of F#) to beat 2.625 (start of A)
# That's a rest of 0.375 seconds

sax_instrument.notes.extend(sax_notes)

# -----------------------------
# Bar 3 (same as bar 2 for drums and bass, but saxophone motif continues)
# But we only need to go up to 4 bars, and the sax motif is complete in bar 2-3
# So saxophone motif ends with the A on beat 4 (start time 2.625)
# Bar 4: Continue full quartet
# -----------------------------

# Bar 3 is already covered by saxophone motif (starts on beat 1 of bar 2, ends on beat 4 of bar 2)
# No sax in bar 3, but bass and drums continue

# Bar 4: Full quartet, but saxophone leaves a rest — we don't add any saxophone notes
# So saxophone is silent in bar 4

# Write the MIDI file
pm.write('dante_intro.mid')
