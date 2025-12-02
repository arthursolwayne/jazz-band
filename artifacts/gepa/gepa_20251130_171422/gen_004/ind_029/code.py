
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set key signature: D minor (1 flat)
pm.key_signature_changes = [pretty_midi.KeySignature(1, 0.0)]  # 1 = D minor

# Define beats and bar lengths
BPM = 160
BEAT_DURATION = 60.0 / BPM  # seconds per beat
BAR_DURATION = BEAT_DURATION * 4  # 4 beats per bar
BAR_1_DURATION = BAR_DURATION  # 6 seconds
BAR_2_4_DURATION = BAR_DURATION * 3  # 18 seconds

# Function to convert beat number to time in seconds
def beat_to_time(beat):
    return beat * BEAT_DURATION

# -----------------------------
# DRUMS (Instrument 0)
# -----------------------------
drums = pretty_midi.Instrument(program=10, is_drum=True)

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    # Kick on beat 1 and 3 (beats 0 and 2 in 0-based index)
    drums.notes.append(Note(36, 100, beat_to_time(beat), beat_to_time(beat) + 0.1))
    # Hihat on every eighth
    for eighth in [0, 0.5]:
        drums.notes.append(Note(42, 100, beat_to_time(beat) + eighth, beat_to_time(beat) + eighth + 0.05))

for beat in [1, 3]:
    # Snare on beat 2 and 4 (beats 1 and 3)
    drums.notes.append(Note(38, 100, beat_to_time(beat), beat_to_time(beat) + 0.1))
    # Hihat on every eighth
    for eighth in [0, 0.5]:
        drums.notes.append(Note(42, 100, beat_to_time(beat) + eighth, beat_to_time(beat) + eighth + 0.05))

pm.instruments.append(drums)

# -----------------------------
# BASS (Instrument 1)
# -----------------------------
bass = pretty_midi.Instrument(program=33)

# Bar 1-4: Walking bass line in Dm
# Dm scale: D, Eb, F, G, A, Bb, C
# Bass line: D, Eb, F, G, A, Bb, C, D
# Chromatic approach to each note
notes = [62, 63, 65, 67, 69, 70, 72, 62]  # D, Eb, F, G, A, Bb, C, D
rhythms = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]

for i, note in enumerate(notes):
    start_time = beat_to_time(i)
    end_time = start_time + rhythms[i]
    bass.notes.append(Note(note, 100, start_time, end_time))

pm.instruments.append(bass)

# -----------------------------
# PIANO (Instrument 2)
# -----------------------------
piano = pretty_midi.Instrument(program=0)

# Bar 1: Rest
# Bar 2-4: 7th chords on beat 2 and 4, comping with grace and tension
# Dm7 = D, F, A, C
# Bbm7 = Bb, Db, F, Ab
# Gm7 = G, Bb, D, F
# Am7 = A, C, E, G
# Chords on beat 2 and 4 of bars 2-4 (beats 6, 8, 10, 12)

chords = [
    [62, 65, 69, 72],  # Dm7 (bar 2, beat 2)
    [70, 72, 65, 69],  # Bbm7 (bar 2, beat 4)
    [67, 70, 62, 65],  # Gm7 (bar 3, beat 2)
    [69, 72, 67, 70],  # Am7 (bar 3, beat 4)
    [62, 65, 69, 72],  # Dm7 (bar 4, beat 2)
    [70, 72, 65, 69],  # Bbm7 (bar 4, beat 4)
]

for chord in chords:
    for note in chord:
        start = beat_to_time(beat=2 + (chords.index(chord) // 2) * 4)
        end = start + 0.25
        piano.notes.append(Note(note, 100, start, end))

pm.instruments.append(piano)

# -----------------------------
# SAX (Instrument 3)
# -----------------------------
sax = pretty_midi.Instrument(program=64)

# Bar 1: Rest
# Bar 2-4: Motif — 3 notes, ascending, with a delay on the last
# Notes: D (62), F (65), G (67) — D, F, G — Dm scale
# Phrasing: D (beat 2), F (beat 3), G (beat 4), repeat on beat 1 of next bar

# First motif
sax.notes.append(Note(62, 100, beat_to_time(2), beat_to_time(2) + 0.25))
sax.notes.append(Note(65, 100, beat_to_time(3), beat_to_time(3) + 0.25))
sax.notes.append(Note(67, 100, beat_to_time(4), beat_to_time(4) + 0.25))

# Repeat motif with slight variation on beat 1 of bar 3
sax.notes.append(Note(62, 100, beat_to_time(5), beat_to_time(5) + 0.25))
sax.notes.append(Note(65, 100, beat_to_time(6), beat_to_time(6) + 0.25))
sax.notes.append(Note(67, 100, beat_to_time(7), beat_to_time(7) + 0.25))

# Add a final return on beat 1 of bar 4
sax.notes.append(Note(62, 100, beat_to_time(8), beat_to_time(8) + 0.25))

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_russo_4bar_intro.mid")
