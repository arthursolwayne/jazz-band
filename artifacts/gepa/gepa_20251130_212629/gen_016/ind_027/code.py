
import pretty_midi
from pretty_midi import Note, NoteEvent, Instrument

# Setup
tempo = 160  # BPM
time_signature = (4, 4)
key = 'F minor'  # Fm

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
pm.instruments = []

# Time per beat
beat = 60.0 / tempo  # seconds per beat
bar_length = beat * 4  # 4 beats per bar
total_time = bar_length * 4  # 4 bars

# -------------------
# 1. Drums: Little Ray
# -------------------
drum_instrument = pretty_midi.Instrument(program=10, is_drum=True)
drum_instrument.name = "Drums - Little Ray"

# Bar 1: Snare on 2 and 4, hihat on all eighths, soft kick on 1
note_events = []
note_events.append(NoteEvent(note=38, time=0, velocity=60))  # Kick on 1
note_events.append(NoteEvent(note=42, time=beat*0.5, velocity=80))  # Hi-hat on 2
note_events.append(NoteEvent(note=38, time=beat*1, velocity=60))  # Kick on 3
note_events.append(NoteEvent(note=42, time=beat*1.5, velocity=40))  # Hi-hat on 4 (softer)
note_events.append(NoteEvent(note=42, time=beat*2, velocity=60))  # Hi-hat on 1 (next bar)

# Bar 2: Kick on 1, snare on 2, hihat on all eighths
note_events.append(NoteEvent(note=38, time=bar_length, velocity=60))  # Kick on 1
note_events.append(NoteEvent(note=42, time=bar_length + beat*0.5, velocity=80))  # Hi-hat
note_events.append(NoteEvent(note=46, time=bar_length + beat*1, velocity=70))  # Snare on 2
note_events.append(NoteEvent(note=38, time=bar_length + beat*1.5, velocity=60))  # Kick on 3
note_events.append(NoteEvent(note=42, time=bar_length + beat*2, velocity=60))  # Hi-hat on 4

# Bar 3: Kick on 1, snare on 2, hihat on all eighths
note_events.append(NoteEvent(note=38, time=bar_length*2, velocity=60))
note_events.append(NoteEvent(note=42, time=bar_length*2 + beat*0.5, velocity=80))
note_events.append(NoteEvent(note=46, time=bar_length*2 + beat*1, velocity=70))
note_events.append(NoteEvent(note=38, time=bar_length*2 + beat*1.5, velocity=60))
note_events.append(NoteEvent(note=42, time=bar_length*2 + beat*2, velocity=60))

# Bar 4: Kick on 1, snare on 2, hihat on all eighths, slower, more space
note_events.append(NoteEvent(note=38, time=bar_length*3, velocity=60))
note_events.append(NoteEvent(note=42, time=bar_length*3 + beat*0.5, velocity=80))
note_events.append(NoteEvent(note=46, time=bar_length*3 + beat*1, velocity=70))
note_events.append(NoteEvent(note=38, time=bar_length*3 + beat*1.5, velocity=60))
note_events.append(NoteEvent(note=42, time=bar_length*3 + beat*2, velocity=60))

drum_instrument.notes = note_events
pm.instruments.append(drum_instrument)

# -------------------
# 2. Bass: Marcus
# -------------------
bass_instrument = Instrument(program=33)
bass_instrument.name = "Bass - Marcus"

# Chromatic walking line, Fm key
notes = [64, 63, 62, 60, 61, 62, 63, 64,  # Fm: F, Eb, D, C, C#, D, Eb, F
         65, 64, 62, 63, 64, 65, 66, 65]  # Fm: F, F#, G, G#, A, Bb, B, A

note_events = []
time = 0
for i, note in enumerate(notes):
    note_obj = Note(note, 60, time + (i * beat / 4), time + (i * beat / 4) + (beat / 4))
    note_events.append(note_obj)

bass_instrument.notes = note_events
pm.instruments.append(bass_instrument)

# -------------------
# 3. Piano: Diane
# -------------------
piano_instrument = Instrument(program=0)
piano_instrument.name = "Piano - Diane"

# 7th chords on 2 and 4, Fm7 on beat 2, Bbm7 on beat 4
# Bar 2:
note_events = []
note_events.append(Note(64, 60, bar_length + beat*0.5, bar_length + beat*0.5 + 0.2))  # F
note_events.append(Note(67, 60, bar_length + beat*0.5, bar_length + beat*0.5 + 0.2))  # A
note_events.append(Note(69, 60, bar_length + beat*0.5, bar_length + beat*0.5 + 0.2))  # C
note_events.append(Note(71, 60, bar_length + beat*0.5, bar_length + beat*0.5 + 0.2))  # Eb

note_events.append(Note(60, 60, bar_length + beat*2, bar_length + beat*2 + 0.2))  # Bb
note_events.append(Note(63, 60, bar_length + beat*2, bar_length + beat*2 + 0.2))  # D
note_events.append(Note(65, 60, bar_length + beat*2, bar_length + beat*2 + 0.2))  # F
note_events.append(Note(67, 60, bar_length + beat*2, bar_length + beat*2 + 0.2))  # A

# Bar 3:
note_events.append(Note(64, 60, bar_length*2 + beat*0.5, bar_length*2 + beat*0.5 + 0.2))  # F
note_events.append(Note(67, 60, bar_length*2 + beat*0.5, bar_length*2 + beat*0.5 + 0.2))  # A
note_events.append(Note(69, 60, bar_length*2 + beat*0.5, bar_length*2 + beat*0.5 + 0.2))  # C
note_events.append(Note(71, 60, bar_length*2 + beat*0.5, bar_length*2 + beat*0.5 + 0.2))  # Eb

note_events.append(Note(60, 60, bar_length*2 + beat*2, bar_length*2 + beat*2 + 0.2))  # Bb
note_events.append(Note(63, 60, bar_length*2 + beat*2, bar_length*2 + beat*2 + 0.2))  # D
note_events.append(Note(65, 60, bar_length*2 + beat*2, bar_length*2 + beat*2 + 0.2))  # F
note_events.append(Note(67, 60, bar_length*2 + beat*2, bar_length*2 + beat*2 + 0.2))  # A

# Bar 4:
note_events.append(Note(64, 60, bar_length*3 + beat*0.5, bar_length*3 + beat*0.5 + 0.2))  # F
note_events.append(Note(67, 60, bar_length*3 + beat*0.5, bar_length*3 + beat*0.5 + 0.2))  # A
note_events.append(Note(69, 60, bar_length*3 + beat*0.5, bar_length*3 + beat*0.5 + 0.2))  # C
note_events.append(Note(71, 60, bar_length*3 + beat*0.5, bar_length*3 + beat*0.5 + 0.2))  # Eb

note_events.append(Note(60, 60, bar_length*3 + beat*2, bar_length*3 + beat*2 + 0.2))  # Bb
note_events.append(Note(63, 60, bar_length*3 + beat*2, bar_length*3 + beat*2 + 0.2))  # D
note_events.append(Note(65, 60, bar_length*3 + beat*2, bar_length*3 + beat*2 + 0.2))  # F
note_events.append(Note(67, 60, bar_length*3 + beat*2, bar_length*3 + beat*2 + 0.2))  # A

piano_instrument.notes = note_events
pm.instruments.append(piano_instrument)

# -------------------
# 4. Tenor Sax: You
# -------------------
sax_instrument = Instrument(program=64)
sax_instrument.name = "Tenor Sax - Dante"

# Short motif: F (64), rest, Ab (66), C (67), rest, F (64)
note_events = []

# Bar 4, beat 1: F (64)
note_events.append(Note(64, 80, bar_length*3, bar_length*3 + 0.3))

# Bar 4, beat 2: rest
# Bar 4, beat 3: Ab (66)
note_events.append(Note(66, 80, bar_length*3 + beat*1.5, bar_length*3 + beat*1.5 + 0.3))

# Bar 4, beat 4: C (67), then resolve to F (64)
note_events.append(Note(67, 80, bar_length*3 + beat*2, bar_length*3 + beat*2 + 0.2))
note_events.append(Note(64, 80, bar_length*3 + beat*2 + 0.3, bar_length*3 + beat*2 + 0.6))

sax_instrument.notes = note_events
pm.instruments.append(sax_instrument)

# Write to file
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' created with your 4-bar intro.")
