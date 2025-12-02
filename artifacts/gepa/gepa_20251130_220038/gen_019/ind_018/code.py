
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (MIDI note numbers)
kick = 36
snare = 38
hi_hat = 42

# D major scale: D (D4=62), E (E4=64), F# (F#4=66), G (G4=67), A (A4=69), B (B4=71), C# (C#5=73)

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(0, 6):
    time = i * 0.375
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.375)
        drums.notes.append(note)
    elif i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.375)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line in D major, chromatic approaches
bass_notes = [62, 64, 66, 67, 69, 71, 73, 72, 70, 68, 67, 66, 64, 62]  # D, E, F#, G, A, B, C#, C, B, A, G, F#, E, D
for i, note in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# D7 = D, F#, A, C
# G7 = G, B, D, F
# A7 = A, C#, E, G
piano_notes = [
    # Bar 2: D7 on beat 2, G7 on beat 4
    (62, 1.5 + 0.375 * 1), (66, 1.5 + 0.375 * 1), (69, 1.5 + 0.375 * 1), (72, 1.5 + 0.375 * 1),  # D7 (beat 2)
    (67, 1.5 + 0.375 * 3), (71, 1.5 + 0.375 * 3), (62, 1.5 + 0.375 * 3), (65, 1.5 + 0.375 * 3),  # G7 (beat 4)
]

for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: Your motif (D, F#, G, A) — start it, leave it hanging
sax_notes = [
    (62, 1.5), (66, 1.5 + 0.375), (67, 1.5 + 0.75), (69, 1.5 + 1.125),
    # Return on the last beat of the bar
    (62, 1.5 + 1.5)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line continuation (typical walking line)
bass_notes = [62, 64, 66, 67, 69, 71, 73, 72, 70, 68, 67, 66, 64, 62]
for i, note in enumerate(bass_notes):
    time = 3.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano comp: A7 on beat 2, D7 on beat 4
piano_notes = [
    (69, 3.0 + 0.375 * 1), (72, 3.0 + 0.375 * 1), (64, 3.0 + 0.375 * 1), (67, 3.0 + 0.375 * 1),  # A7 (beat 2)
    (62, 3.0 + 0.375 * 3), (66, 3.0 + 0.375 * 3), (69, 3.0 + 0.375 * 3), (72, 3.0 + 0.375 * 3),  # D7 (beat 4)
]

for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: Motif variation — start again with a slight chromatic twist
sax_notes = [
    (62, 3.0), (66, 3.0 + 0.375), (67, 3.0 + 0.75), (69, 3.0 + 1.125),
    (67, 3.0 + 1.5)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line continuation
bass_notes = [62, 64, 66, 67, 69, 71, 73, 72, 70, 68, 67, 66, 64, 62]
for i, note in enumerate(bass_notes):
    time = 4.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Piano comp: D7 on beat 2, G7 on beat 4
piano_notes = [
    (62, 4.5 + 0.375 * 1), (66, 4.5 + 0.375 * 1), (69, 4.5 + 0.375 * 1), (72, 4.5 + 0.375 * 1),  # D7 (beat 2)
    (67, 4.5 + 0.375 * 3), (71, 4.5 + 0.375 * 3), (62, 4.5 + 0.375 * 3), (65, 4.5 + 0.375 * 3),  # G7 (beat 4)
]

for pitch, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note_obj)

# Sax: Finish the motif — return to D, but with a chromatic twist
sax_notes = [
    (62, 4.5), (66, 4.5 + 0.375), (67, 4.5 + 0.75), (69, 4.5 + 1.125),
    (62, 4.5 + 1.5)
]
for pitch, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
