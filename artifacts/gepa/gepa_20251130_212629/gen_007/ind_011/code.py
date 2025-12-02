
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time settings
BPM = 160
BAR_DURATION = 6.0  # 4 bars total
BEAT_DURATION = BAR_DURATION / 4  # 1.5 seconds per bar
NOTE_DURATION = BEAT_DURATION / 2  # 0.75 seconds per note
TIME_RESOLUTION = 480  # MIDI ticks per beat (standard)
TIMESIG = (4, 4)

# Set time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define instruments
instrument_drums = pretty_midi.Instrument(program=10, is_drum=True)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_sax = pretty_midi.Instrument(program=64)

pm.instruments = [instrument_drums, instrument_bass, instrument_piano, instrument_sax]

# Define the key: D major
KEY = 'D'
KEY_SIGNATURE = pretty_midi.KeySignature(key_number=2)  # D major
pm.key_signature_changes = [KEY_SIGNATURE]

# Add the drums (tight and rhythmic)
# Bar 1: Just kick on 1 and 3, snare on 2 and 4
for bar in range(1):
    for beat in range(4):
        time = beat * BEAT_DURATION
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + NOTE_DURATION)
            instrument_drums.notes.append(note)
        elif beat == 1 or beat == 3:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + NOTE_DURATION)
            instrument_drums.notes.append(note)

# Bar 2-4: Add hihat on every eighth (tight, busy, fills the bar)
for bar in range(1, 4):
    for beat in range(4):
        for eighth in range(2):
            time = (beat * 2 + eighth) * (NOTE_DURATION / 2)
            note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + (NOTE_DURATION / 2))
            instrument_drums.notes.append(note)

# Bassline: Chromatic walking line, no repeated notes
# Bar 2-4: Bass enters on the second bar — walking line
bass_notes = [
    # Bar 2
    50, 51, 52, 53,
    # Bar 3
    54, 55, 56, 57,
    # Bar 4
    58, 59, 60, 61,
]
for i, pitch in enumerate(bass_notes):
    time = (i // 4 + 1) * BEAT_DURATION + (i % 4) * NOTE_DURATION
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + NOTE_DURATION)
    instrument_bass.notes.append(note)

# Piano: Sparse, impactful, 7th chords on 2 and 4
# Bar 2: Chord on beat 2
piano_notes = [
    # Bar 2, beat 2
    62, 67, 71, 75,  # D7 (D, F#, A, C#)
    # Bar 3, beat 2
    62, 67, 71, 75,  # D7
    # Bar 4, beat 1
    71, 76, 79, 82   # A7 (A, C#, E, G#)
]
for i, pitch in enumerate(piano_notes):
    time = (i // 4 + 1) * BEAT_DURATION + (i % 4) * NOTE_DURATION
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + NOTE_DURATION)
    instrument_piano.notes.append(note)

# Saxophone: Your moment — concise, expressive, memorable
# Bar 2: Start the motif
# Bar 3: Leave it hanging
# Bar 4: Return and finish it

sax_notes = [
    # Bar 2
    66,   # E
    69,   # G
    62,   # D (leave it hanging)
    # Bar 3
    66,   # E (return)
    71,   # A
    69,   # G
    66,   # E (finish it)
]
for i, pitch in enumerate(sax_notes):
    time = (i // 4 + 1) * BEAT_DURATION + (i % 4) * NOTE_DURATION
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + NOTE_DURATION)
    instrument_sax.notes.append(note)

# Write the MIDI file
pm.write("jazz_intro_wayne.mid")

print("MIDI file created: 'jazz_intro_wayne.mid'")
