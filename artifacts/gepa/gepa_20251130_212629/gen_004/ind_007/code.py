
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (kick=36, snare=38, hihat=42)
kick = 36
snare = 38
hihat = 42

# Time signatures: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar_length = 1.5  # 4/4 at 160 BPM

# Bar 1: Drums
# Time duration of a beat = 0.375 seconds
# 8 notes in the bar (1/8 notes)
for note_num in range(8):
    time = note_num * 0.375
    if note_num % 2 == 0:  # even indices: 0, 2, 4, 6 = beat 1, 3
        drum_note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.375)
        drums.notes.append(drum_note)
    elif note_num % 2 == 1:  # odd indices: 1, 3, 5, 7 = beat 2, 4
        drum_note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.375)
        drums.notes.append(drum_note)
    # Hihat on every 8th note
    hihat_note = pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.375)
    drums.notes.append(hihat_note)

# Bar 2: Full Quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
# Dm7 = D, F, A, C
# Bass line: D -> C -> B -> A -> G -> F -> E -> D
bass_notes = [62, 60, 61, 60, 59, 58, 57, 60]  # D, C, B, A, G, F, E, D
for i, note in enumerate(bass_notes):
    start_time = 1.5 + i * 0.375
    duration = 0.375
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb
# We'll play chords on beats 2 and 4 of bar 2 and bar 3
# Bar 2: Dm7 on beat 2, G7 on beat 4
# Bar 3: Cm7 on beat 2, F7 on beat 4

# Bar 2: Dm7 on beat 2 (start_time = 1.5 + 0.75 = 2.25)
chord_notes = [62, 65, 67, 60]  # D, F, A, C
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=2.25, end=2.25 + 0.375)
    piano.notes.append(piano_note)

# Bar 2: G7 on beat 4 (start_time = 1.5 + 1.5 = 3.0)
chord_notes = [67, 71, 69, 65]  # G, B, D, F
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=3.0, end=3.0 + 0.375)
    piano.notes.append(piano_note)

# Bar 3: Cm7 on beat 2 (start_time = 3.0 + 0.75 = 3.75)
chord_notes = [60, 63, 67, 69]  # C, Eb, G, Bb
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=3.75, end=3.75 + 0.375)
    piano.notes.append(piano_note)

# Bar 3: F7 on beat 4 (start_time = 3.0 + 1.5 = 4.5)
chord_notes = [65, 69, 67, 63]  # F, A, C, Eb
for note in chord_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=4.5, end=4.5 + 0.375)
    piano.notes.append(piano_note)

# Sax: Your motif — short, emotional, Dm scale with a twist
# Dm scale: D, Eb, F, G, A, Bb, C
# Your motif: D, F, G, A — a question, a memory, a moment
# Play it on beats 1 and 3 of bar 2

# Bar 2: D, F, G, A on beats 1 and 3
# Beat 1: D (62)
# Beat 3: F (65), G (67), A (69) — all at once, like a memory

# Beat 1 (start_time = 1.5)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(sax_note)

# Beat 3 (start_time = 1.5 + 1.5 = 3.0)
sax_note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.375)
sax.notes.append(sax_note)

# Bar 3: Let’s leave it hanging. No sax for a moment. Let the silence speak.
# Bar 4: Return — answer the question with a cry, a resolution — D, C, Bb, A

# Bar 4: D (62), C (60), Bb (61), A (67)
# Play on beats 1 and 3

# Beat 1 (start_time = 3.0 + 1.5 = 4.5)
sax_note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.375)
sax.notes.append(sax_note)

# Beat 3 (start_time = 4.5 + 1.5 = 6.0)
sax_note = pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.0 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=61, start=6.0, end=6.0 + 0.375)
sax.notes.append(sax_note)
sax_note = pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.0 + 0.375)
sax.notes.append(sax_note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
