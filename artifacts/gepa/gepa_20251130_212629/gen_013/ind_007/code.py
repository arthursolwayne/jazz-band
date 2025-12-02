
import pretty_midi
import numpy as np

# Setup
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
program = pretty_midi.instrument_name_to_program('Electric Piano')
piano = pretty_midi.Instrument(program=program)
program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=program)
program = pretty_midi.instrument_name_to_program('Drum Kit')
drums = pretty_midi.Instrument(program=program)
program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=program)

# Time per bar in seconds
time_per_bar = 1.5  # 160 BPM, 4/4 time

# --- DRUMS (Little Ray) - Bar 1 (0.0 to 1.5s) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [36]  # C1
snare_notes = [38]  # D1
hihat_notes = [42]  # G1

# Bar 1 (0.0 to 1.5s)
for beat in [0, 1, 2, 3]:  # 4 beats in a bar
    time = beat * 0.375
    if beat == 0 or beat == 2:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time, end=time + 0.2)
        drums.notes.append(note)
    if beat == 1 or beat == 3:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=120, pitch=snare_notes[0], start=time, end=time + 0.2)
        drums.notes.append(note)
    # Hihat on every eighth note (4 per bar)
    for eighth in [0, 1, 2, 3]:
        hihat_time = time + eighth * 0.1875
        note = pretty_midi.Note(velocity=80, pitch=hihat_notes[0], start=hihat_time, end=hihat_time + 0.1)
        drums.notes.append(note)

# --- BASS (Marcus) - Bar 2 (1.5 to 3.0s) ---
# Walking bass line in Fm (F, Gb, Ab, A, Bb, B, C, Db)
# Chromatic movement, no repeated notes
bass_notes = [71, 70, 68, 69, 67, 68, 69, 71]  # F (71), Gb (70), Ab (68), A (69), Bb (67), B (68), C (69), Db (71)
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    bass.notes.append(note_obj)

# --- PIANO (Diane) - Bars 2-4 (1.5 to 4.5s) ---
# 7th chords on 2 and 4 of each bar
# Comp on 2 and 4 with dynamic phrasing
# F7 (F, A, C, Eb)
# Bb7 (Bb, D, F, Ab)
# Eb7 (Eb, G, Bb, Db)
# Ab7 (Ab, C, Eb, Gb)

def add_piano_chord(chord_notes, start_time):
    for note in chord_notes:
        note_obj = pretty_midi.Note(velocity=np.random.randint(60, 100), pitch=note, start=start_time, end=start_time + 0.3)
        piano.notes.append(note_obj)

# Bar 2: F7 on beat 2
add_piano_chord([71, 74, 76, 70], 1.5 + 0.375)
# Bar 2: Bb7 on beat 4
add_piano_chord([70, 73, 76, 68], 1.5 + 0.75)

# Bar 3: Eb7 on beat 2
add_piano_chord([68, 71, 73, 67], 3.0 + 0.375)
# Bar 3: Ab7 on beat 4
add_piano_chord([67, 71, 68, 66], 3.0 + 0.75)

# Bar 4: F7 on beat 2
add_piano_chord([71, 74, 76, 70], 4.5 + 0.375)
# Bar 4: Bb7 on beat 4
add_piano_chord([70, 73, 76, 68], 4.5 + 0.75)

# --- SAX (You) - Bar 4 (3.0 to 4.5s) ---
# Concise, emotional motif in Fm: F, Ab, Bb, C – but with a twist
sax_notes = [
    71,  # F
    68,  # Ab
    67,  # Bb
    69,  # C
    68,  # Ab
    67,  # Bb
]

for i, note in enumerate(sax_notes):
    start = 3.0 + i * 0.375
    end = start + 0.25
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(note_obj)

# Add instruments to MIDI
midi.instruments.append(piano)
midi.instruments.append(bass)
midi.instruments.append(drums)
midi.instruments.append(sax)

# Save the MIDI file
midi.save("wayne_shorter_intro.mid")
print("MIDI file created: 'wayne_shorter_intro.mid'")
