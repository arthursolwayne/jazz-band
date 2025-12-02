
import pretty_midi
from pretty_midi import Note, Instrument

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
tenor_sax = Instrument(program=64, is_drum=False, name='Tenor Sax')
bass = Instrument(program=33, is_drum=False, name='Bass')
piano = Instrument(program=0, is_drum=False, name='Piano')
drums = Instrument(program=0, is_drum=True, name='Drums')

pm.instruments.append(tenor_sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define the time in seconds for each beat (160 BPM = 0.375s per beat)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar

# Time markers for each bar
bar_times = [0, bar, bar * 2, bar * 3, bar * 4]

# -----------------------------
# DRUMS (Little Ray) - Bar 1: Solo
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0 - 1.5s
# -----------------------------
for i in range(8):
    time = i * beat / 2  # eighth notes
    if i % 2 == 0:  # kick on 1 and 3
        Note(36, 100, time, time + 0.15).add_to_instrument(drums)
    if i % 2 == 1:  # snare on 2 and 4
        Note(38, 100, time, time + 0.15).add_to_instrument(drums)
    if i % 2 == 0 or i == 3:  # hihat on every eighth
        Note(42, 70, time, time + 0.1).add_to_instrument(drums)

# -----------------------------
# BAR 2: Full ensemble enters
# Tenor sax (you) plays sparse, sparse motif
# Piano: 7th chords, comp on 2 and 4
# Bass: walking line, chromatic, no repeats
# -----------------------------

# TIME = bar * 1 = 1.5s

# Tenor sax (you) - sparse melody with rests and expressive dynamics
# Motif: Fm (F, Ab, Bb) - but not in root position, spaced out
# Notes: F (1st beat), Ab (3rd beat), Bb (4th beat), with rest on 2
# Velocity variation, variable durations
note_1 = Note(65, 80, 1.5, 1.5 + 0.4)  # F
note_2 = Note(68, 70, 1.5 + beat, 1.5 + beat + 0.2)  # Rest
note_3 = Note(67, 90, 1.5 + beat*2, 1.5 + beat*2 + 0.3)  # Ab
note_4 = Note(66, 85, 1.5 + beat*3, 1.5 + beat*3 + 0.25)  # Bb
note_1.add_to_instrument(tenor_sax)
note_2.add_to_instrument(tenor_sax)
note_3.add_to_instrument(tenor_sax)
note_4.add_to_instrument(tenor_sax)

# Bass (Marcus): Walking line, chromatic, no repeats
# Fm7: F, Ab, Bb, D, with chromatic passing tones
bass_notes = [
    Note(44, 60, 1.5, 1.5 + 0.25),  # F
    Note(45, 65, 1.5 + beat, 1.5 + beat + 0.25),  # Gb (chromatic)
    Note(43, 62, 1.5 + beat*2, 1.5 + beat*2 + 0.25),  # Eb (Ab)
    Note(46, 68, 1.5 + beat*3, 1.5 + beat*3 + 0.25),  # Bb
]
for note in bass_notes:
    note.add_to_instrument(bass)

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7 (F, Ab, Bb, D) on beat 2 and 4
# Velocity: medium to high, slightly aggressive
piano_notes_2 = [
    Note(65, 85, 1.5 + beat, 1.5 + beat + 0.2),
    Note(68, 80, 1.5 + beat, 1.5 + beat + 0.2),
    Note(66, 75, 1.5 + beat, 1.5 + beat + 0.2),
    Note(61, 90, 1.5 + beat, 1.5 + beat + 0.2),
]
for note in piano_notes_2:
    note.add_to_instrument(piano)

piano_notes_4 = [
    Note(65, 85, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(68, 80, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(66, 75, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(61, 90, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
]
for note in piano_notes_4:
    note.add_to_instrument(piano)

# -----------------------------
# BAR 3: Tenor sax continues with variation
# Piano: same comp, but now with a slight twist
# Bass: Chromatic walking, continues
# -----------------------------
# Tenor sax variation
note_5 = Note(67, 85, 1.5 + beat*2, 1.5 + beat*2 + 0.3)  # Ab again, higher velocity
note_5.add_to_instrument(tenor_sax)

note_6 = Note(66, 90, 1.5 + beat*3, 1.5 + beat*3 + 0.3)  # Bb again, but with more emotional weight
note_6.add_to_instrument(tenor_sax)

# Piano: same chords, but with a slightly altered rhythm
piano_notes_2_var = [
    Note(65, 85, 1.5 + beat, 1.5 + beat + 0.2),
    Note(68, 80, 1.5 + beat + 0.1, 1.5 + beat + 0.3),
    Note(66, 75, 1.5 + beat + 0.2, 1.5 + beat + 0.4),
    Note(61, 90, 1.5 + beat + 0.2, 1.5 + beat + 0.4),
]
for note in piano_notes_2_var:
    note.add_to_instrument(piano)

piano_notes_4_var = [
    Note(65, 85, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(68, 80, 1.5 + beat*3 + 0.1, 1.5 + beat*3 + 0.3),
    Note(66, 75, 1.5 + beat*3 + 0.2, 1.5 + beat*3 + 0.4),
    Note(61, 90, 1.5 + beat*3 + 0.2, 1.5 + beat*3 + 0.4),
]
for note in piano_notes_4_var:
    note.add_to_instrument(piano)

# Bass: continues with minor chromatic passing
note_7 = Note(45, 65, 1.5 + beat*2, 1.5 + beat*2 + 0.25)  # Gb
note_7.add_to_instrument(bass)

note_8 = Note(44, 60, 1.5 + beat*3, 1.5 + beat*3 + 0.25)  # F
note_8.add_to_instrument(bass)

# -----------------------------
# BAR 4: Tenor sax resolves the motif
# Piano: same comp
# Drum fills: Little Ray plays a fill
# -----------------------------
# Tenor sax resolution
note_9 = Note(65, 85, 1.5 + beat*2, 1.5 + beat*2 + 0.3)  # F again, but with a twist
note_9.add_to_instrument(tenor_sax)

note_10 = Note(64, 95, 1.5 + beat*3, 1.5 + beat*3 + 0.3)  # E flat (chromatic pull to F)
note_10.add_to_instrument(tenor_sax)

# Piano: same comp
piano_notes_2_final = [
    Note(65, 85, 1.5 + beat, 1.5 + beat + 0.2),
    Note(68, 80, 1.5 + beat, 1.5 + beat + 0.2),
    Note(66, 75, 1.5 + beat, 1.5 + beat + 0.2),
    Note(61, 90, 1.5 + beat, 1.5 + beat + 0.2),
]
for note in piano_notes_2_final:
    note.add_to_instrument(piano)

piano_notes_4_final = [
    Note(65, 85, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(68, 80, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(66, 75, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
    Note(61, 90, 1.5 + beat*3, 1.5 + beat*3 + 0.2),
]
for note in piano_notes_4_final:
    note.add_to_instrument(piano)

# Drums (fill on beat 4)
drum_fill = [
    Note(36, 100, 1.5 + beat*3, 1.5 + beat*3 + 0.15),  # Kick
    Note(38, 100, 1.5 + beat*3, 1.5 + beat*3 + 0.15),  # Snare
    Note(42, 70, 1.5 + beat*3, 1.5 + beat*3 + 0.05),  # Hihat
    Note(36, 100, 1.5 + beat*3 + 0.3, 1.5 + beat*3 + 0.45),  # Kick
    Note(38, 100, 1.5 + beat*3 + 0.3, 1.5 + beat*3 + 0.45),  # Snare
]
for note in drum_fill:
    note.add_to_instrument(drums)

# Save the MIDI file
pm.write("dante_russo_intro_Fm.mid")

print("MIDI file generated: 'dante_russo_intro_Fm.mid'")
