
import pretty_midi
from pretty_midi import Note, Instrument, PrettyMIDI

# Constants
TEMPO = 160  # BPM
TIME_SIGNATURE = (4, 4)
KEY = 'Fm'  # F minor
DURATION = 6.0  # 4 bars at 160 BPM = 6.0 seconds

# Create a PrettyMIDI object
pm = PrettyMIDI(initial_tempo=TEMPO, time_signature=(4, 4))

# Instrument Pitches
# Tenor Sax: C4 (60) to B5 (71)
# Bass: E2 (36) to G3 (47)
# Piano: C3 (48) to E5 (69)
# Drums: MIDI percussion (note numbers 36 to 47, 48 to 54, etc.)

# --- 1. Drums (Little Ray) ---
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drum_inst = Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_inst)

# Bar 1: 4/4, kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
# MIDI note numbers for kicks, snares, hihats
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: 6.0 seconds / 4 bars = 1.5 seconds per bar
bar_duration = 1.5
time = 0.0

# Bar 1: Kick on 1, snare on 2, hihat on every 8th
for i in range(0, 4):
    time = i * (bar_duration / 4)
    drum_inst.notes.append(Note(velocity=100, pitch=KICK, start=time, end=time + 0.125))
    drum_inst.notes.append(Note(velocity=100, pitch=SNARE, start=time + 0.5, end=time + 0.625))
    drum_inst.notes.append(Note(velocity=100, pitch=HIHAT, start=time, end=time + 0.125))
    drum_inst.notes.append(Note(velocity=100, pitch=HIHAT, start=time + 0.25, end=time + 0.375))
    drum_inst.notes.append(Note(velocity=100, pitch=HIHAT, start=time + 0.5, end=time + 0.625))
    drum_inst.notes.append(Note(velocity=100, pitch=HIHAT, start=time + 0.75, end=time + 0.875))

# --- 2. Tenor Sax (You) - Motif in F minor ---
tenor_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
tenor_inst = Instrument(program=tenor_program)
pm.instruments.append(tenor_inst)

# F minor scale: F, Gb, Ab, Bb, B, Db, Eb
F = 65
Gb = 66
Ab = 67
Bb = 68
B = 69
Db = 70
Eb = 71

# Tenor Sax Motif: F, Gb, Ab, rest, then F, Bb, B, Eb, rest
notes = [
    Note(velocity=100, pitch=F, start=1.5, end=1.75),
    Note(velocity=100, pitch=Gb, start=1.75, end=2.0),
    Note(velocity=100, pitch=Ab, start=2.0, end=2.25),
    Note(velocity=100, pitch=F, start=3.0, end=3.25),
    Note(velocity=100, pitch=Bb, start=3.25, end=3.5),
    Note(velocity=100, pitch=B, start=3.5, end=3.75),
    Note(velocity=100, pitch=Eb, start=3.75, end=4.0),
]

for note in notes:
    tenor_inst.notes.append(note)

# --- 3. Piano (Diane) - Comping on 2 and 4 (7th chords in Fm) ---
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano_inst = Instrument(program=piano_program)
pm.instruments.append(piano_inst)

# Fm7 = F, Ab, Bb, C
Fm7 = [65, 67, 68, 72]
# Comp on 2 and 4 of bars 2–4
comp_times = [
    1.75, 2.0,  # Bar 2: 2 and 4
    3.25, 3.5,  # Bar 3: 2 and 4
    4.5, 5.0,   # Bar 4: 2 and 4
]

for time in comp_times:
    for pitch in Fm7:
        piano_inst.notes.append(Note(velocity=90, pitch=pitch, start=time, end=time + 0.25))

# --- 4. Bass (Marcus) - Walking line in Fm (chromatic approach, no repetition) ---
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_inst = Instrument(program=bass_program)
pm.instruments.append(bass_inst)

# Walking line: F, Gb, Ab, Bb, B, C, Db, Eb
walking_line = [65, 66, 67, 68, 69, 72, 70, 71]
time = 1.5  # Bar 2

for i in range(len(walking_line)):
    pitch = walking_line[i]
    start = time + (i * 0.375)
    end = start + 0.25
    bass_inst.notes.append(Note(velocity=85, pitch=pitch, start=start, end=end))

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file written to 'dante_intro.mid'")
