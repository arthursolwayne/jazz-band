
import pretty_midi
from pretty_midi import Note, Instrument

# Constants
BPM = 160
TIME_SIGNATURE = (4, 4)
TEMPO = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * TEMPO  # seconds per bar
NOTE_DURATION = TEMPO / 4  # quarter note in seconds

# MIDI note numbers (D4 = 62)
D4 = 62
F_SHARP4 = 66
B4 = 71
C5 = 60
D5 = 62
F5 = 65
G5 = 67
A5 = 69

# Time stamps (in seconds)
bar_1 = 0.0
bar_2 = BAR_DURATION
bar_3 = 2 * BAR_DURATION
bar_4 = 3 * BAR_DURATION

# Create a MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Create instruments
bass = Instrument(program=33)  # Acoustic Bass
piano = Instrument(program=0)  # Acoustic Grand Piano
drums = Instrument(program=0, is_drum=True)
sax = Instrument(program=64)  # Tenor Saxophone

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# BAR 1: DRUMS ONLY — The setup
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (bar_1, 35),  # Kick on beat 1
    (bar_1 + TEMPO/2, 42),  # Snare on beat 2
    (bar_1 + TEMPO, 35),  # Kick on beat 3
    (bar_1 + 3*TEMPO/2, 42),  # Snare on beat 4
]
for time, note in drum_notes:
    n = Note(velocity=100, start=time, end=time + 0.05)
    drums.notes.append(n)

# BAR 2: EVERYONE JOIN — SAX TAKES THE MELODY
# Sax: short motif — D4 -> F#4 -> B4 -> rest — then D5 -> F5 -> G5 -> A5
sax_notes = [
    Note(velocity=100, start=bar_2, end=bar_2 + NOTE_DURATION, pitch=D4),
    Note(velocity=100, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=F_SHARP4),
    Note(velocity=100, start=bar_2 + 2*NOTE_DURATION, end=bar_2 + 3*NOTE_DURATION, pitch=B4),
    Note(velocity=100, start=bar_3, end=bar_3 + NOTE_DURATION, pitch=D5),
    Note(velocity=100, start=bar_3 + NOTE_DURATION, end=bar_3 + 2*NOTE_DURATION, pitch=F5),
    Note(velocity=100, start=bar_3 + 2*NOTE_DURATION, end=bar_3 + 3*NOTE_DURATION, pitch=G5),
    Note(velocity=100, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=A5)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    Note(velocity=80, start=bar_2, end=bar_2 + NOTE_DURATION, pitch=C5),
    Note(velocity=80, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=D5),
    Note(velocity=80, start=bar_2 + 2*NOTE_DURATION, end=bar_2 + 3*NOTE_DURATION, pitch=F5),
    Note(velocity=80, start=bar_2 + 3*NOTE_DURATION, end=bar_2 + 4*NOTE_DURATION, pitch=G5),
    Note(velocity=80, start=bar_3, end=bar_3 + NOTE_DURATION, pitch=A5),
    Note(velocity=80, start=bar_3 + NOTE_DURATION, end=bar_3 + 2*NOTE_DURATION, pitch=B4),
    Note(velocity=80, start=bar_3 + 2*NOTE_DURATION, end=bar_3 + 3*NOTE_DURATION, pitch=D5),
    Note(velocity=80, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=F5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C) on beat 2 (bar_2 + NOTE_DURATION)
    Note(velocity=90, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=D4),
    Note(velocity=90, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=F_SHARP4),
    Note(velocity=90, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=A4),
    Note(velocity=90, start=bar_2 + NOTE_DURATION, end=bar_2 + 2*NOTE_DURATION, pitch=C5),

    # Bar 3: G7 (G B D F) on beat 4 (bar_3 + 3*NOTE_DURATION)
    Note(velocity=90, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=G4),
    Note(velocity=90, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=B4),
    Note(velocity=90, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=D5),
    Note(velocity=90, start=bar_3 + 3*NOTE_DURATION, end=bar_3 + 4*NOTE_DURATION, pitch=F5),
]
piano.notes.extend(piano_notes)

# BAR 4: DRUMS AGAIN — Keep the energy up with hihat and snare
drum_notes = [
    (bar_4, 35),  # Kick on beat 1
    (bar_4 + TEMPO/2, 42),  # Snare on beat 2
    (bar_4 + TEMPO, 35),  # Kick on beat 3
    (bar_4 + 3*TEMPO/2, 42),  # Snare on beat 4
]
for time, note in drum_notes:
    n = Note(velocity=100, start=time, end=time + 0.05)
    drums.notes.append(n)

# Save the MIDI file
pm.time_signature = TIME_SIGNATURE
pm.write("jazz_intro.mid")

print("MIDI file 'jazz_intro.mid' has been created.")
