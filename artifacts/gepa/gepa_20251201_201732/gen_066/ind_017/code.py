
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: D major
key = 'D major'

# Define the note durations in terms of MIDI ticks
# Assuming a resolution of 480 ticks per quarter note
ticks_per_quarter = 480
ticks_per_beat = ticks_per_quarter  # 4/4 time
ticks_per_eighth = ticks_per_beat // 2
ticks_per_sixteenth = ticks_per_beat // 4
ticks_per_bar = ticks_per_beat * 4  # 4 bars = 16 beats

# Create instruments
# Little Ray on drums
drums = Instrument(program=Program.DRUMS, is_drum=True)
midi.instruments.append(drums)

# Marcus on bass
bass = Instrument(program=Program.BASS_GUITAR, name='Marcus')
midi.instruments.append(bass)

# Diane on piano
piano = Instrument(program=Program.PIANO, name='Diane')
midi.instruments.append(piano)

# You on tenor sax
sax = Instrument(program=Program.SAXOPHONE, name='Dante')
midi.instruments.append(sax)

# BAR 1: LITTLE RAY ALONE
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar starts at time 0
bar_start = 0

# Kick on 1 and 3
kick1 = Note(36, 0, bar_start, bar_start + ticks_per_beat)
kick3 = Note(36, 0, bar_start + ticks_per_beat * 2, bar_start + ticks_per_beat * 2 + ticks_per_beat)
drums.notes.append(kick1)
drums.notes.append(kick3)

# Snare on 2 and 4
snare2 = Note(38, 0, bar_start + ticks_per_beat, bar_start + ticks_per_beat + ticks_per_beat)
snare4 = Note(38, 0, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 3 + ticks_per_beat)
drums.notes.append(snare2)
drums.notes.append(snare4)

# Hihat on every eighth
for i in range(8):
    hihat = Note(42, 0.5, bar_start + i * ticks_per_eighth, bar_start + i * ticks_per_eighth + ticks_per_eighth)
    drums.notes.append(hihat)

# BAR 2: EVERYONE IN
# Diane's chords: open voicings, different chord each bar, resolve on last
# Bar 2: Dmaj7 -> G7 -> Amin7 -> Dmaj7
# Convert to MIDI note numbers
# Dmaj7: D (62), F# (67), A (69), C# (71)
# G7: G (67), B (71), D (62), F (65)
# Amaj7: A (69), C# (71), E (74), G (67)
# Dmaj7 again: D (62), F# (67), A (69), C# (71)

# Diane plays on beat 2 and 4
bar_start = ticks_per_beat  # time of bar 2

# Dmaj7 on beat 2
chord = [62, 67, 69, 71]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat, bar_start + ticks_per_beat + ticks_per_beat)
    piano.notes.append(note_obj)

# G7 on beat 4
chord = [67, 71, 62, 65]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 3 + ticks_per_beat)
    piano.notes.append(note_obj)

# Marcus: walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches

# Bar 2 (D -> G -> A -> D)
# D (62), G (67), A (69), D (62)
# Each note played on beat 1, 2, 3, 4

bass_notes = [62, 67, 69, 62]
for i, note in enumerate(bass_notes):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Add chromatic approaches (lower by a half step before each root)
chromatic_approaches = [61, 66, 68, 61]
for i, note in enumerate(chromatic_approaches):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat / 2  # Half note (half beat)
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Your part: tenor sax, one short motif, make it sing
# Start with a phrase that leans on the tension, resolves with release
# D to F# to G to A to D: a simple but emotional motif
# Bar 2: Start the motif on beat 1
# D (62), F# (67), G (67+1=68?), A (69), D (62)
# Play it over bar 2 and bar 3, leave it hanging

# Bar 2, beat 1: D
note = Note(62, 1, bar_start, bar_start + ticks_per_beat)
sax.notes.append(note)

# Bar 2, beat 2: F#
note = Note(67, 1, bar_start + ticks_per_beat, bar_start + ticks_per_beat * 2)
sax.notes.append(note)

# Bar 2, beat 3: G
note = Note(68, 1, bar_start + ticks_per_beat * 2, bar_start + ticks_per_beat * 3)
sax.notes.append(note)

# Bar 2, beat 4: A
note = Note(69, 1, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 4)
sax.notes.append(note)

# BAR 3: Diane's chords: Bm7 -> E7 -> F#m7 -> Bm7
# Diane plays on beat 2 and 4
bar_start = ticks_per_beat * 2  # time of bar 3

# Bm7 on beat 2
chord = [64, 67, 71, 74]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat, bar_start + ticks_per_beat + ticks_per_beat)
    piano.notes.append(note_obj)

# E7 on beat 4
chord = [69, 74, 64, 67]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 3 + ticks_per_beat)
    piano.notes.append(note_obj)

# Marcus: walking bass line (B -> E -> F# -> B)
# B (64), E (74), F# (67), B (64)
# Each note played on beat 1, 2, 3, 4

bass_notes = [64, 74, 67, 64]
for i, note in enumerate(bass_notes):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Add chromatic approaches (lower by a half step before each root)
chromatic_approaches = [63, 73, 66, 63]
for i, note in enumerate(chromatic_approaches):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat / 2  # Half note (half beat)
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Your part: bar 3, continue the motif, but end on A (69), let it hang
# Bar 3, beat 1: D (62), but not played this bar
# Bar 3, beat 2: F# (67), but not played this bar
# Bar 3, beat 3: G (68), but not played this bar
# Bar 3, beat 4: A (69) — leave it hanging

note = Note(69, 1, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 4)
sax.notes.append(note)

# BAR 4: Diane's chords: C#m7 -> F#7 -> Gmaj7 -> C#m7
# Diane plays on beat 2 and 4
bar_start = ticks_per_beat * 3  # time of bar 4

# C#m7 on beat 2
chord = [65, 68, 72, 76]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat, bar_start + ticks_per_beat + ticks_per_beat)
    piano.notes.append(note_obj)

# F#7 on beat 4
chord = [68, 72, 65, 67]
for note in chord:
    note_obj = Note(note, 1, bar_start + ticks_per_beat * 3, bar_start + ticks_per_beat * 3 + ticks_per_beat)
    piano.notes.append(note_obj)

# Marcus: walking bass line (C# -> F# -> G -> C#)
# C# (65), F# (68), G (69), C# (65)
# Each note played on beat 1, 2, 3, 4

bass_notes = [65, 68, 69, 65]
for i, note in enumerate(bass_notes):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Add chromatic approaches (lower by a half step before each root)
chromatic_approaches = [64, 67, 68, 64]
for i, note in enumerate(chromatic_approaches):
    start = bar_start + i * ticks_per_beat
    duration = ticks_per_beat / 2  # Half note (half beat)
    note_obj = Note(note, 1, start, start + duration)
    bass.notes.append(note_obj)

# Your part: bar 4 — resolve the motif
note = Note(62, 1, bar_start, bar_start + ticks_per_beat)
sax.notes.append(note)

# Finally, save the MIDI file
# midi.write disabled
print("MIDI file written to 'dante_russo_intro.mid'")
