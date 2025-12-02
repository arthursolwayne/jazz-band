
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F major (key_number=17)
key = 17

# Create instruments
instrument_sax = Instrument(program=Program.SAXOPHONE_TENOR, is_drum=False)
instrument_piano = Instrument(program=Program.PIANO, is_drum=False)
instrument_bass = Instrument(program=Program.BASS_FRETLESS, is_drum=False)
instrument_drums = Instrument(program=Program.DRUMS, is_drum=True)

# Add instruments to the MIDI file
pm.instruments.append(instrument_sax)
pm.instruments.append(instrument_piano)
pm.instruments.append(instrument_bass)
pm.instruments.append(instrument_drums)

# Quarter note duration (60 / 160 = 0.375 seconds)
note_duration = 0.375

# Temporal markers: 4 bars at 160 BPM
bar_length = 4 * note_duration  # 4 beats in a bar

# ---------------------------
# 1. DRUMS: Little Ray
# ---------------------------

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# 8 beats per bar: 1, 2, 3, 4, 5, 6, 7, 8

# Kick
kick_notes = [0, 0, 0, 0, 0, 0, 0, 0]
kick_notes[0] = 36  # Kick
kick_notes[2] = 36  # Kick

# Snare
snare_notes = [0, 0, 0, 0, 0, 0, 0, 0]
snare_notes[1] = 38  # Snare
snare_notes[3] = 38

# Hi-hat on every eighth
hihat_notes = [42] * 8  # 42 = closed hi-hat

# Add drum notes
for i, pitch in enumerate(kick_notes):
    if pitch != 0:
        note = Note(pitch, i * note_duration, i * note_duration + note_duration)
        instrument_drums.notes.append(note)

for i, pitch in enumerate(snare_notes):
    if pitch != 0:
        note = Note(pitch, i * note_duration, i * note_duration + note_duration)
        instrument_drums.notes.append(note)

for i, pitch in enumerate(hihat_notes):
    note = Note(pitch, i * note_duration, i * note_duration + note_duration / 2)
    instrument_drums.notes.append(note)

# ---------------------------
# 2. BASS: Marcus
# ---------------------------

# Walking line in F major: F, G, A, Bb, C, D, E, F
bass_notes = [78, 82, 87, 88, 92, 97, 101, 78]  # MIDI numbers for F, G, A, Bb, C, D, E, F

# Add bass line (on beats 1, 2, 3, 4)
for i, pitch in enumerate(bass_notes):
    if i % 2 == 0:
        note = Note(pitch, i * note_duration, i * note_duration + note_duration)
        instrument_bass.notes.append(note)

# ---------------------------
# 3. PIANO: Diane
# ---------------------------

# Open voicings with chromatic tension, resolving on 4th beat of each bar.
# Bar 1: F7 (F, A, C, E)
# Bar 2: Gm7 (G, Bb, D, F)
# Bar 3: Am7 (A, C, E, G)
# Bar 4: Bb7 (Bb, D, F, A)

# Bar 1: F7
piano_notes_bar1 = [78, 92, 97, 103]  # F, A, C, E
# Play on beats 2 and 4
for i, pitch in enumerate(piano_notes_bar1):
    note = Note(pitch, (i + 1) * note_duration, (i + 1) * note_duration + note_duration)
    instrument_piano.notes.append(note)

# Bar 2: Gm7
piano_notes_bar2 = [82, 88, 97, 92]  # G, Bb, D, F
# Play on beats 2 and 4
for i, pitch in enumerate(piano_notes_bar2):
    note = Note(pitch, (i + 1) * note_duration, (i + 1) * note_duration + note_duration)
    instrument_piano.notes.append(note)

# Bar 3: Am7
piano_notes_bar3 = [87, 97, 103, 92]  # A, C, E, G
# Play on beats 2 and 4
for i, pitch in enumerate(piano_notes_bar3):
    note = Note(pitch, (i + 1) * note_duration, (i + 1) * note_duration + note_duration)
    instrument_piano.notes.append(note)

# Bar 4: Bb7
piano_notes_bar4 = [88, 97, 103, 108]  # Bb, D, F, A
# Play on beats 2 and 4
for i, pitch in enumerate(piano_notes_bar4):
    note = Note(pitch, (i + 1) * note_duration, (i + 1) * note_duration + note_duration)
    instrument_piano.notes.append(note)

# ---------------------------
# 4. SAX: Dante - Your motif
# ---------------------------

# Tenor saxophone motif: F, Bb, C, F
# Start on beat 1, with a rest on beat 2, then F again on beat 3, and a resolution on beat 4
sax_notes = [78, 88, 92, 78]  # F, Bb, C, F

# Play on beats 1 and 3
for i in range(len(sax_notes)):
    if i % 2 == 0:
        note = Note(sax_notes[i], i * note_duration, i * note_duration + note_duration)
        instrument_sax.notes.append(note)

# Add a slight delay on the last note to make it "hang"
note = Note(78, 3 * note_duration, 3 * note_duration + note_duration * 1.5)
instrument_sax.notes.append(note)

# ---------------------------
# Save the MIDI file
# ---------------------------

pm.write('dante_intro.mid')
print("MIDI file generated: dante_intro.mid")
