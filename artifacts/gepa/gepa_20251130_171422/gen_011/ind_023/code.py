
import pretty_midi
from pretty_midi import Note, Instrument, TempoChange

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: D major (key number 2)
midi.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]

# Set the time in seconds per bar (160 BPM, 4/4 time)
time_per_bar = 60.0 / 160 * 4

# Create a new instrument for each player
sax_instrument = Instrument(program=64, is_drum=False, name='Tenor Saxophone')
bass_instrument = Instrument(program=33, is_drum=False, name='Bass')
piano_instrument = Instrument(program=0, is_drum=False, name='Piano')
drums_instrument = Instrument(program=0, is_drum=True, name='Drums')

# Add instruments to the MIDI file
midi.instruments.append(sax_instrument)
midi.instruments.append(bass_instrument)
midi.instruments.append(piano_instrument)
midi.instruments.append(drums_instrument)

# Define the start time (in seconds)
start_time = 0.0

# --- BAR 1: DRUMS (Little Ray) - 6.0 seconds total; 1.5 seconds per bar
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time per beat: 60 / 160 = 0.375 seconds
beat_time = 0.375

# Bar 1 - 0.0 to 1.5 seconds
# Kick on 1 and 3
kick1 = Note(36, 100, start_time, 0.1)
kick3 = Note(36, 100, start_time + 2 * beat_time, 0.1)
drums_instrument.notes.append(kick1)
drums_instrument.notes.append(kick3)

# Snare on 2 and 4
snare2 = Note(38, 100, start_time + beat_time, 0.1)
snare4 = Note(38, 100, start_time + 3 * beat_time, 0.1)
drums_instrument.notes.append(snare2)
drums_instrument.notes.append(snare4)

# Hi-hats on every eighth note
hihat_notes = [start_time + i * beat_time / 2 for i in range(8)]
for h in hihat_notes:
    hihat = Note(42, 80, h, 0.05)
    drums_instrument.notes.append(hihat)

# --- BAR 2: PIANO (Diane) - 7th chords, comp on 2 and 4

# Bar 2 starts at 1.5 seconds
bar2_start = 1.5

# 7th chords: D7 (D, F#, A, C)
# Root on 1, 7th on 2
# Diane plays on beat 2 and 4 (comping)

# Time of comping notes
comp_time_2 = bar2_start + beat_time
comp_time_4 = bar2_start + 3 * beat_time

# D7 chord: D, F#, A, C
d7_notes = [62, 67, 69, 64]
for note in d7_notes:
    piano_note = Note(note, 80, comp_time_2, 0.2)
    piano_instrument.notes.append(piano_note)

# Repeat on beat 4
for note in d7_notes:
    piano_note = Note(note, 80, comp_time_4, 0.2)
    piano_instrument.notes.append(piano_note)

# --- BAR 2: BASS (Marcus) - Walking line, chromatic approaches

# Bar 2 walking line: D -> Eb -> E -> F -> F# (chromatic approach to G)
# D = 62, Eb = 63, E = 64, F = 65, F# = 66

# Timing: 1, 2, 3, 4
bass_notes = [62, 63, 64, 65]
bass_times = [bar2_start + i * beat_time for i in range(4)]

for i, note in enumerate(bass_notes):
    bass_note = Note(note, 70, bass_times[i], 0.2)
    bass_instrument.notes.append(bass_note)

# Chromatic approach to G (F#)
bass_note = Note(66, 70, bass_times[3] + 0.05, 0.15)
bass_instrument.notes.append(bass_note)

# --- BAR 2: SAX (You) - Motif starts

# Sax motif: D (62), F# (67), A (69), G (67) -> question-like, lingering
# D -> F# -> A -> G

sax_notes = [62, 67, 69, 67]
sax_times = [bar2_start + 0.05, bar2_start + 0.2, bar2_start + 0.35, bar2_start + 0.5]
sax_durations = [0.1, 0.1, 0.1, 0.1]

for i, note in enumerate(sax_notes):
    sax = Note(note, 100, sax_times[i], sax_durations[i])
    sax_instrument.notes.append(sax)

# --- BAR 3: PIANO (Diane) - 7th chords, comp on 2 and 4

bar3_start = 3.0

# D7 again
comp_time_2 = bar3_start + beat_time
comp_time_4 = bar3_start + 3 * beat_time

for note in d7_notes:
    piano_note = Note(note, 80, comp_time_2, 0.2)
    piano_instrument.notes.append(piano_note)

for note in d7_notes:
    piano_note = Note(note, 80, comp_time_4, 0.2)
    piano_instrument.notes.append(piano_note)

# --- BAR 3: BASS (Marcus) - Walking line, chromatic approaches

bass_times = [bar3_start + i * beat_time for i in range(4)]
bass_notes = [67, 68, 69, 70]

for i, note in enumerate(bass_notes):
    bass_note = Note(note, 70, bass_times[i], 0.2)
    bass_instrument.notes.append(bass_note)

# Chromatic approach to A (G#)
bass_note = Note(70, 70, bass_times[3] + 0.05, 0.15)
bass_instrument.notes.append(bass_note)

# --- BAR 3: SAX (You) - Motif returns

sax_notes = [67, 69, 71, 69]
sax_times = [bar3_start + 0.05, bar3_start + 0.2, bar3_start + 0.35, bar3_start + 0.5]
for i, note in enumerate(sax_notes):
    sax = Note(note, 100, sax_times[i], 0.1)
    sax_instrument.notes.append(sax)

# --- BAR 4: PIANO (Diane) - 7th chords, comp on 2 and 4

bar4_start = 4.5

comp_time_2 = bar4_start + beat_time
comp_time_4 = bar4_start + 3 * beat_time

for note in d7_notes:
    piano_note = Note(note, 80, comp_time_2, 0.2)
    piano_instrument.notes.append(piano_note)

for note in d7_notes:
    piano_note = Note(note, 80, comp_time_4, 0.2)
    piano_instrument.notes.append(piano_note)

# --- BAR 4: BASS (Marcus) - Walking line, chromatic approaches

bass_times = [bar4_start + i * beat_time for i in range(4)]
bass_notes = [71, 72, 73, 74]

for i, note in enumerate(bass_notes):
    bass_note = Note(note, 70, bass_times[i], 0.2)
    bass_instrument.notes.append(bass_note)

# Chromatic approach to B (A#)
bass_note = Note(74, 70, bass_times[3] + 0.05, 0.15)
bass_instrument.notes.append(bass_note)

# --- BAR 4: SAX (You) - Motif concludes

sax_notes = [69, 71, 73, 71]
sax_times = [bar4_start + 0.05, bar4_start + 0.2, bar4_start + 0.35, bar4_start + 0.5]
for i, note in enumerate(sax_notes):
    sax = Note(note, 100, sax_times[i], 0.1)
    sax_instrument.notes.append(sax)

# Save the MIDI file
midi.write("jazz_intro_wayne.mid")
