
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program("Acoustic Bass")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano")
drums_program = pretty_midi.instrument_name_to_program("Drum Kit")
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time in seconds per beat (60 / 160 = 0.375)
beat = 0.375
bar = beat * 4  # 1.5 seconds
bar_duration = 1.5

# ------- BAR 1: Little Ray (Drums) ------------------------
# Snare on 2 and 4, kick on 1 and 3
# Hihat on every eighth

# Kick on 1 and 3 of bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4 of bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625))

# Hihat on every eighth
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=t, end=t + 0.125))

# ------- BAR 2: Everyone comes in -------------------------

# Marcus (Bass): Walking line in D major
# D -> C# -> B -> A -> G -> F# -> E -> D -> C# -> B -> A -> G -> F# -> E -> D
# Chromatic approach to the root

note_values = [2, 1, 11, 10, 9, 8, 7, 2, 1, 11, 10, 9, 8, 7, 2]  # D is 2
note_values = [n + 12 for n in note_values]  # Transpose to D major

for i, note in enumerate(note_values):
    start = bar + i * beat
    end = start + beat
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane (Piano): 7th chords on 2 and 4, comping
# D7 on beat 2 and 4

# D7 = D, F#, A, C
# D is 2, F# is 6, A is 9, C is 0

# Bar 2, beat 2 (1.5 sec)
for pitch in [2, 6, 9, 0]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch + 12, start=1.5, end=1.875))

# Bar 2, beat 4 (3.0 sec)
for pitch in [2, 6, 9, 0]:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch + 12, start=3.0, end=3.375))

# ------- BAR 3: You (Tenor Sax) - Motif starts here -------------------------
# Short motif, rests, space, tension

# D (2) on beat 1, rest on beat 2, F# (6) on beat 3, rest on beat 4

# D (2) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=2 + 62, start=bar * 2, end=bar * 2 + beat))

# F# (6) on beat 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=6 + 62, start=bar * 2 + 2 * beat, end=bar * 2 + 3 * beat))

# Rest on beat 2 and 4

# ------- BAR 4: Motif returns, resolved or unresolved? -------------------------
# F# on beat 1, rest on beat 2, D on beat 3, rest on beat 4

# F# (6) on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=6 + 62, start=bar * 3, end=bar * 3 + beat))

# D (2) on beat 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=2 + 62, start=bar * 3 + 2 * beat, end=bar * 3 + 3 * beat))

# Save the MIDI file
pm.write("jazz_intro_d_major.mid")
