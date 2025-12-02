
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

# Add instruments
sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define time in seconds per beat
tempo = 160
seconds_per_beat = 60 / tempo
bar_length = 4 * seconds_per_beat  # 4/4 time

# Create time stamps for 4 bars
bar_start = 0
bar_end = bar_length

# ============= DRUMS =============
# Bar 1: Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Kick on 1 and 3
for i in [0, 2]:
    kick_time = bar_start + i * seconds_per_beat
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=kick_time, end=kick_time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
for i in [1, 3]:
    snare_time = bar_start + i * seconds_per_beat
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=snare_time, end=snare_time + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth
for i in range(0, 4):
    hihat_time = bar_start + i * seconds_per_beat / 2
    note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(note)

# ============= BASS =============
# Chromatic walking line from F4 to Bb4 (chromatic up)
bass_notes = [77, 78, 79, 80, 81, 82, 83, 84]  # F4 to Bb4
note_duration = seconds_per_beat / 4  # 1/4 note = 1 beat

for i, note in enumerate(bass_notes):
    start_time = bar_start + i * note_duration
    end_time = start_time + note_duration
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=end_time)
    bass.notes.append(note_obj)

# ============= PIANO =============
# Comping on 2 and 4 with dominant 7th chords in F (F7)
# F7 = F, A, C, Eb
# Play on 2 and 4

notes = [77, 82, 87, 80]  # F, A, C, Eb

for i in [1, 3]:
    comp_time = bar_start + i * seconds_per_beat
    for note in notes:
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=comp_time, end=comp_time + 0.5)
        piano.notes.append(note_obj)

# ============= SAX =============
# Tenor Sax motif: F4 (77), A4 (81), C5 (84), rest, F5 (87), rest, F4 (77)
# Rhythmic spacing: quarter, eighth, eighth, rest, eighth, rest, eighth
# This creates a question, tension, and a hint of resolution

sax_notes = [
    (77, 0),      # F4 at bar_start (1/4 note)
    (81, 0.5),    # A4 on beat 2 (1/8 note)
    (84, 0.75),   # C5 on beat 2.5 (1/8 note)
    (77, 2.0),    # F4 on beat 4 (1/4 note)
    (87, 2.5),    # F5 on beat 4.5 (1/8 note)
]

for pitch, start_time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=bar_start + start_time, end=bar_start + start_time + 0.25)
    sax.notes.append(note_obj)

# Save the MIDI file
pm.write("wayne_intro.mid")
print("MIDI file 'wayne_intro.mid' saved.")
