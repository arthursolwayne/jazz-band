
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define key and scale
key = 'D'  # D Major
scale_degrees = [0, 2, 4, 5, 7, 9, 11]  # D Major scale
scale_notes = [pretty_midi.note_number_to_name(62 + d) for d in scale_degrees]  # D4 = 62
scale_pitches = [62 + d for d in scale_degrees]  # D4 = 62

# Create instruments
instrument_drums = pretty_midi.Instrument(program=10, is_drum=True)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments.append(instrument_drums)
midi.instruments.append(instrument_piano)
midi.instruments.append(instrument_bass)
midi.instruments.append(instrument_sax)

# Set up time for each bar (6 seconds total, 4 bars)
bar_length = 1.5  # seconds per bar
time = 0.0

# ----------------------------
# Bar 1: Little Ray (Drums) alone — set the mood
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time signature: 4/4, 160 BPM → 0.375s per beat

# Kick on 1 and 3
kick_times = [0.0, 0.75]  # beats 1 and 3
kick_notes = [36]  # Kick drum is MIDI 36
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t * 0.375, end=(t + 0.01) * 0.375)
    instrument_drums.notes.append(note)

# Snare on 2 and 4
snare_times = [0.5, 1.5]
snare_notes = [38]  # Snare drum is MIDI 38
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t * 0.375, end=(t + 0.01) * 0.375)
    instrument_drums.notes.append(note)

# Hi-hat on every eighth note
hihat_notes = [42]  # Mid-hat is MIDI 42
for i in range(8):
    start = i * 0.375
    end = start + 0.01
    note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    instrument_drums.notes.append(note)

time += bar_length

# ----------------------------
# Bar 2: Diane (Piano) enters — open voicings, different chords each bar, resolve on the last

# Chord progression: Dmaj7 -> F#m7 -> Bm7 -> G7
# Dmaj7 = D, F#, A, C#
# F#m7 = F#, A, C, E
# Bm7 = B, D, F#, A
# G7 = G, B, D, F

# Bar 2: Dmaj7
# Open voicing: D (62), A (69), F# (66), C# (67)
d_notes = [62, 66, 67, 69]  # D, F#, C#, A
for note in d_notes:
    velocity = 100
    start = time
    end = time + 0.375
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=end)
    instrument_piano.notes.append(piano_note)
time += 0.375

# Bar 3: F#m7
# F# (65), A (69), C (60), E (64)
fsharp_notes = [60, 64, 65, 69]  # C, E, F#, A
for note in fsharp_notes:
    velocity = 100
    start = time
    end = time + 0.375
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=end)
    instrument_piano.notes.append(piano_note)
time += 0.375

# Bar 4: Bm7
# B (71), D (62), F# (66), A (69)
b_notes = [62, 66, 69, 71]  # D, F#, A, B
for note in b_notes:
    velocity = 100
    start = time
    end = time + 0.375
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=end)
    instrument_piano.notes.append(piano_note)
time += 0.375

# Bar 5: G7 (resolve)
# G (67), B (71), D (62), F (58)
g_notes = [58, 62, 67, 71]  # F, D, G, B
for note in g_notes:
    velocity = 100
    start = time
    end = time + 0.375
    piano_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=end)
    instrument_piano.notes.append(piano_note)
time += 0.375

# ----------------------------
# Bar 2: Marcus (Bass) enters — walking line, roots and fifths, chromatic approaches

# Walking line: D (62), F# (66), G (67), A (69), B (71), D (62), etc.
# Chromatic approach on F# (66) to G (67)
# Times: beat 1, 2, 3, 4

# Bar 2: D (62) on beat 1
note = pretty_midi.Note(velocity=100, pitch=62, start=time, end=time + 0.375)
instrument_bass.notes.append(note)
time += 0.375

# Bar 2: F# (66) on beat 2
note = pretty_midi.Note(velocity=100, pitch=66, start=time, end=time + 0.375)
instrument_bass.notes.append(note)
time += 0.375

# Bar 2: G (67) on beat 3
note = pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + 0.375)
instrument_bass.notes.append(note)
time += 0.375

# Bar 2: A (69) on beat 4
note = pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + 0.375)
instrument_bass.notes.append(note)
time += 0.375

# ----------------------------
# Bar 2: You (Tenor Sax) enter — short motif, leave it hanging, sing

# Motif: D (62) -> F# (66) -> B (71) -> D (62)
# Play on beat 3 and 4, leave it hanging on the last note

# Note 1: D (62) on beat 3
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
instrument_sax.notes.append(note)
time += 0.375

# Note 2: F# (66) on beat 4
note = pretty_midi.Note(velocity=110, pitch=66, start=time, end=time + 0.375)
instrument_sax.notes.append(note)
time += 0.375

# Note 3: B (71) — start at beat 4.5, end at beat 5.0
note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + 0.375)
instrument_sax.notes.append(note)
time += 0.375

# Note 4: D (62) — start at beat 5.0, end at beat 6.0 (rest of bar)
note = pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + 0.375)
instrument_sax.notes.append(note)

# ----------------------------
# Write to MIDI file
# midi.write disabled

print("MIDI file created: jazz_intro_d_maj.mid")
