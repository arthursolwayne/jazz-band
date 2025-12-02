
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Dm (D minor)
key = 'Dm'

# Define the tempo: 160 BPM
tempo = 160

# Define note durations in terms of beats (1 beat = 60 / tempo seconds)
beat_duration = 60.0 / tempo

# Define bar duration (4/4 time)
bar_duration = 4 * beat_duration

# Define the time for each bar (seconds)
bar_times = [0.0, bar_duration, 2 * bar_duration, 3 * bar_duration, 4 * bar_duration]

# --- Define instruments ---
# Drums: Little Ray
drums = Instrument(program=Program.DRUMS, is_drum=True)
pm.instruments.append(drums)

# Bass: Marcus
bass = Instrument(program=Program.BASS, name="Marcus")
pm.instruments.append(bass)

# Piano: Diane
piano = Instrument(program=Program.PIANO, name="Diane")
pm.instruments.append(piano)

# Sax: Dante
sax = Instrument(program=Program.SAXOPHONE, name="Dante")
pm.instruments.append(sax)

# --- DRUMS - Little Ray ---
# Kick on 1 and 3
drum_kick = 35  # MIDI note for kick
drum_snare = 38  # MIDI note for snare
drum_hihat = 42  # MIDI note for closed hihat

# Bar 1: Kick on 1 and 3, hihat on every 8th
for i in range(0, 4):
    time = bar_times[0] + (i * beat_duration / 2)
    note = Note(drum_hihat, time, beat_duration / 2)
    drums.notes.append(note)

# Kick on 1 and 3
for i in [0, 2]:
    time = bar_times[0] + (i * beat_duration)
    note = Note(drum_kick, time, beat_duration / 2)
    drums.notes.append(note)

# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    time = bar_times[1] + (i * beat_duration / 2)
    note = Note(drum_hihat, time, beat_duration / 2)
    drums.notes.append(note)

for i in [0, 2]:
    time = bar_times[1] + (i * beat_duration)
    note = Note(drum_kick, time, beat_duration / 2)
    drums.notes.append(note)

for i in [1, 3]:
    time = bar_times[1] + (i * beat_duration)
    note = Note(drum_snare, time, beat_duration / 2)
    drums.notes.append(note)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    time = bar_times[2] + (i * beat_duration / 2)
    note = Note(drum_hihat, time, beat_duration / 2)
    drums.notes.append(note)

for i in [0, 2]:
    time = bar_times[2] + (i * beat_duration)
    note = Note(drum_kick, time, beat_duration / 2)
    drums.notes.append(note)

for i in [1, 3]:
    time = bar_times[2] + (i * beat_duration)
    note = Note(drum_snare, time, beat_duration / 2)
    drums.notes.append(note)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for i in range(0, 4):
    time = bar_times[3] + (i * beat_duration / 2)
    note = Note(drum_hihat, time, beat_duration / 2)
    drums.notes.append(note)

for i in [0, 2]:
    time = bar_times[3] + (i * beat_duration)
    note = Note(drum_kick, time, beat_duration / 2)
    drums.notes.append(note)

for i in [1, 3]:
    time = bar_times[3] + (i * beat_duration)
    note = Note(drum_snare, time, beat_duration / 2)
    drums.notes.append(note)

# --- BASS - Marcus ---
# Bass line: walking line in D minor, chromatic approaches, no repeated notes

# Dm: D, F, A, C (notes in 12-TET)
# D = 62, F = 65, A = 69, C = 60

# Bar 1: F, C, A, D (chromatic approach on F)
bass_notes = [65, 60, 69, 62]
for i, note in enumerate(bass_notes):
    time = bar_times[0] + (i * beat_duration)
    bass_note = Note(note, time, beat_duration)
    bass.notes.append(bass_note)

# Bar 2: D, C, B, A (chromatic approach on D)
bass_notes = [62, 60, 61, 69]
for i, note in enumerate(bass_notes):
    time = bar_times[1] + (i * beat_duration)
    bass_note = Note(note, time, beat_duration)
    bass.notes.append(bass_note)

# Bar 3: A, G, F#, F (chromatic approach on A)
bass_notes = [69, 67, 66, 65]
for i, note in enumerate(bass_notes):
    time = bar_times[2] + (i * beat_duration)
    bass_note = Note(note, time, beat_duration)
    bass.notes.append(bass_note)

# Bar 4: F, E, D, C (chromatic approach on F)
bass_notes = [65, 64, 62, 60]
for i, note in enumerate(bass_notes):
    time = bar_times[3] + (i * beat_duration)
    bass_note = Note(note, time, beat_duration)
    bass.notes.append(bass_note)

# --- PIANO - Diane ---
# Diane: 7th chords, comp on 2 and 4

# Dm7 = D, F, A, C
# F7 = F, A, C, E
# A7 = A, C, E, G
# C7 = C, E, G, B

# Bar 1: Dm7 on 2 and 4
for i in [1, 3]:
    time = bar_times[0] + (i * beat_duration)
    for note in [62, 65, 69, 60]:
        piano_note = Note(note, time, beat_duration / 2)
        piano.notes.append(piano_note)

# Bar 2: F7 on 2 and 4
for i in [1, 3]:
    time = bar_times[1] + (i * beat_duration)
    for note in [65, 69, 60, 64]:
        piano_note = Note(note, time, beat_duration / 2)
        piano.notes.append(piano_note)

# Bar 3: A7 on 2 and 4
for i in [1, 3]:
    time = bar_times[2] + (i * beat_duration)
    for note in [69, 60, 64, 67]:
        piano_note = Note(note, time, beat_duration / 2)
        piano.notes.append(piano_note)

# Bar 4: C7 on 2 and 4
for i in [1, 3]:
    time = bar_times[3] + (i * beat_duration)
    for note in [60, 64, 67, 71]:
        piano_note = Note(note, time, beat_duration / 2)
        piano.notes.append(piano_note)

# --- SAX - Dante ---
# Dante: Tenor sax, short motif, make it sing
# Dm scale notes: D (62), E (64), F (65), G (67), A (69), Bb (66), C (60)
# Motif: D -> F -> E -> rest (suspense), then back to C -> D -> G -> rest (resolution)

# Bar 1: Start with the motif
# D -> F -> E -> rest
notes = [62, 65, 64, 62]  # last is rest
for i, note in enumerate(notes):
    if note == 62:
        time = bar_times[0] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 65:
        time = bar_times[0] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 64:
        time = bar_times[0] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 62:
        # Rest (no note)
        pass

# Bar 2: Rest
# Just a rest
# No notes

# Bar 3: Resolve the motif: C -> D -> G -> rest
notes = [60, 62, 67, 62]
for i, note in enumerate(notes):
    if note == 60:
        time = bar_times[2] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 62:
        time = bar_times[2] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 67:
        time = bar_times[2] + (i * beat_duration)
        sax_note = Note(note, time, beat_duration)
        sax.notes.append(sax_note)
    elif note == 62:
        # Rest
        pass

# Bar 4: Nothing — leave it hanging, let the silence speak
# No notes from sax here

# Save to MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
