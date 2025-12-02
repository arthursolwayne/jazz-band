
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Setup
tempo = 160  # BPM
time_signature = (4, 4)
beat_duration = 60.0 / tempo  # 0.375 seconds per beat
bar_duration = beat_duration * 4  # 1.5 seconds per bar

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Instrumetns
# Drums
drum_program = Program(program=0, is_drum=True)
drum_instrument = Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# Bass
bass_program = Program(program=33)
bass_instrument = Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Piano
piano_program = Program(program=0)
piano_instrument = Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Saxophone
sax_program = Program(program=64)
sax_instrument = Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Time in seconds
time = 0.0

# ---------------------------
# 🥁 DRUMS: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 (0.0 - 1.5 sec)
for beat in [0, 2]:  # Beats 1 and 3
    kick = Note(velocity=100, pitch=36, start=time + beat * beat_duration, end=time + beat * beat_duration + 0.1)
    drum_instrument.notes.append(kick)
for beat in [1, 3]:  # Beats 2 and 4
    snare = Note(velocity=100, pitch=38, start=time + beat * beat_duration, end=time + beat * beat_duration + 0.1)
    drum_instrument.notes.append(snare)
for eighth in range(8):
    hihat = Note(velocity=80, pitch=42, start=time + eighth * beat_duration / 2, end=time + eighth * beat_duration / 2 + 0.05)
    drum_instrument.notes.append(hihat)

# ---------------------------
# 🎸 BASS: Walking line with chromatic tension
# F minor: F, Gb, Ab, Bb, B, Db, Eb, F
# Walking bass line: F, Gb, Ab, Bb (bar 1)
# To be continued into bar 2

bass_notes = [
    Note(pitch=53, start=time, end=time + beat_duration),
    Note(pitch=54, start=time + beat_duration, end=time + 2 * beat_duration),
    Note(pitch=51, start=time + 2 * beat_duration, end=time + 3 * beat_duration),
    Note(pitch=50, start=time + 3 * beat_duration, end=time + 4 * beat_duration),
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# ---------------------------
# 🤖 PIANO: 7th chords on 2 and 4
# F7 = F, A, C, Eb
# 2nd beat: A7 = A, C, E, G
# 4th beat: D7 = D, F#, A, C
# These are 7th chords on each 2nd and 4th beat of the bar

for beat in [1, 3]:
    start_time = time + beat * beat_duration
    end_time = start_time + 0.25  # Short duration for comping
    # F7 (F, A, C, Eb)
    if beat == 1:
        chord_notes = [53, 58, 60, 63]
    elif beat == 3:
        chord_notes = [60, 64, 67, 69]

    for pitch in chord_notes:
        note = Note(pitch=pitch, start=start_time, end=end_time, velocity=90)
        piano_instrument.notes.append(note)

# ---------------------------
# 🎵 SAX: Motif in 4 bars
# Bar 1: 1 note, then rest
# Bar 2: continuation of the motif
# Bar 3: build tension
# Bar 4: resolve with an open-ended phrase

# Fm: F, Ab, Bb, Db, Eb, F
# Motif
# Bar 1: F (beat 1)
# Bar 2: Ab (beat 2)
# Bar 3: Bb (beat 3)
# Bar 4: Db (beat 4) — leave it hanging

# Bar 1: F
sax_notes = [
    Note(pitch=53, start=time, end=time + beat_duration),
    # Bar 2: Ab
    Note(pitch=51, start=time + 2 * beat_duration, end=time + 2.5 * beat_duration),
    # Bar 3: Bb
    Note(pitch=50, start=time + 3 * beat_duration, end=time + 3.5 * beat_duration),
    # Bar 4: Db (leave hanging)
    Note(pitch=55, start=time + 4 * beat_duration, end=time + 4.5 * beat_duration),
]

for note in sax_notes:
    sax_instrument.notes.append(note)

# ---------------------------
# Write to file
pm.write('jazz_intro_f_minor.mid')
print("MIDI file written: jazz_intro_f_minor.mid")
