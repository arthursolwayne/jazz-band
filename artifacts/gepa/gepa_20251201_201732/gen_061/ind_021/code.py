
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)

# Set up time signature
pm.time_signature_changes.append(pretty_midi.TimeSignature(numerator=4, denominator=4, time=0))

# Define note durations and note values
BAR_DURATION = 6.0  # 6 seconds for 4 bars
BPM = 160
BEAT_DURATION = 60.0 / BPM  # 0.375 seconds per beat
NOTE_DURATION = 0.375  # quarter note

# Define the key of D Major
D_MAJOR_SCALE = [2, 4, 5, 7, 9, 11, 12]  # D, E, F#, G, A, B, C#

# MIDI note numbers for D Major scale (starting at D2 = 38)
D2 = 38
D_MAJOR_NOTES = [38, 40, 42, 43, 45, 47, 49]

# Define the chords for Diane (piano)
# Chord progressions will be Dmaj7 -> G7 -> A7 -> Dmaj7
# Chord voicings: open, spaced, resolving on the last
CHORDS = {
    0: [38, 42, 45, 47],  # Dmaj7 (D, F#, A, C#)
    1: [43, 47, 50, 52],  # G7 (G, B, D, F)
    2: [45, 49, 52, 54],  # A7 (A, C#, E, G)
    3: [38, 42, 45, 47]   # Dmaj7 again
}

# Define the walking bass line for Marcus
# Walking bass: D2 -> E2 -> F#2 -> G2 -> A2 -> B2 -> C#3 -> D3
BASS_LINE = [38, 40, 42, 43, 45, 47, 49, 50]

# Define drum pattern for Little Ray
# Kick on 1 & 3, snare on 2 & 4, hihat on all 8ths
DRUM_PATTERNS = {
    'kick': [0, 0, 1, 0, 0, 0, 1, 0],  # 1 and 3
    'snare': [0, 1, 0, 1, 0, 0, 0, 0],  # 2 and 4
    'hihat': [1, 1, 1, 1, 1, 1, 1, 1]   # every 8th
}

# Define the saxophone motif: a short, singing phrase with space
# Notes: D (38), F# (42), B (47), D (38)
# Start on beat 1, rest on beat 2, play on beat 3, end on beat 4
SAX_MOTIF = [38, 42, 47, 38]
SAX_TIMINGS = [0.0, 1.5, 3.0, 4.5]  # in seconds

# Create instrument tracks
# Drums (program 36 - Acoustic Drum Kit)
drum_program = pretty_midi.Instrument(program=36)
pm.instruments.append(drum_program)

# Bass (program 33 - Double Bass)
bass_program = pretty_midi.Instrument(program=33)
pm.instruments.append(bass_program)

# Piano (program 0 - Acoustic Grand Piano)
piano_program = pretty_midi.Instrument(program=0)
pm.instruments.append(piano_program)

# Sax (program 64 - Alto Sax, but works for tenor)
sax_program = pretty_midi.Instrument(program=64)
pm.instruments.append(sax_program)

# Add drum hits
for i in range(8):
    time = i * BEAT_DURATION
    if DRUM_PATTERNS['kick'][i]:
        drum_program.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1))
    if DRUM_PATTERNS['snare'][i]:
        drum_program.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1))
    if DRUM_PATTERNS['hihat'][i]:
        drum_program.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=time, end=time + 0.1))

# Add bass line
for i, note in enumerate(BASS_LINE):
    time = i * BEAT_DURATION
    bass_program.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + NOTE_DURATION))

# Add piano chords
for bar, notes in enumerate(CHORDS):
    for note in notes:
        start = bar * BEAT_DURATION * 2
        duration = NOTE_DURATION
        piano_program.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add saxophone motif
for i, note in enumerate(SAX_MOTIF):
    start = SAX_TIMINGS[i]
    duration = NOTE_DURATION
    sax_program.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' generated.")
