
import pretty_midi

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
instrument_sax = pretty_midi.Instrument(program=64)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_drums = pretty_midi.Instrument(program=128)

pm.instruments = [instrument_sax, instrument_piano, instrument_bass, instrument_drums]

# Define tempo and time in seconds per beat
tempo = 160  # BPM
seconds_per_beat = 60.0 / tempo  # 0.375 seconds per beat

# Define the four bars (each bar is 1.5 seconds)
bar_length = 4 * seconds_per_beat  # 4 beats per bar

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Just hihat and kick on 1
# Bar 2-4: Full rhythm

# Bar 1: Kick on 1, hihat on all eighths
kick_times = [0 * seconds_per_beat]  # Kick on 1
hihat_times = [i * 0.1875 for i in range(0, 4 * 2)]  # every eighth note in the bar

for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    instrument_drums.notes.append(note)

for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    instrument_drums.notes.append(note)

# Bar 2:
kick_times = [1 * seconds_per_beat, 3 * seconds_per_beat]
snare_times = [2 * seconds_per_beat, 4 * seconds_per_beat]
hihat_times = [i * 0.1875 for i in range(4, 8 * 2)]

for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    instrument_drums.notes.append(note)

for time in snare_times:
    note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
    instrument_drums.notes.append(note)

for time in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    instrument_drums.notes.append(note)

# Bar 3 and 4: Same as Bar 2
for i in range(2, 4):
    kick_times = [(i * 4 + 1) * seconds_per_beat, (i * 4 + 3) * seconds_per_beat]
    snare_times = [(i * 4 + 2) * seconds_per_beat, (i * 4 + 4) * seconds_per_beat]
    hihat_times = [j * 0.1875 for j in range((i * 4) * 2, (i * 4 + 4) * 2)]

    for time in kick_times:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        instrument_drums.notes.append(note)

    for time in snare_times:
        note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
        instrument_drums.notes.append(note)

    for time in hihat_times:
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
        instrument_drums.notes.append(note)

# --- PIANO: Diane ---
# 7th chords, comp on 2 and 4, in D minor
# Bar 1: No piano
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Dm7 (D, F, A, C)
# Bar 4: Dm7 (D, F, A, C)

def add_chord(chord_notes, time):
    for note in chord_notes:
        n = pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.2)
        instrument_piano.notes.append(n)

# Bar 2: Dm7
add_chord([62, 65, 67, 72], 1 * seconds_per_beat)

# Bar 3: Dm7
add_chord([62, 65, 67, 72], 2 * seconds_per_beat)

# Bar 4: Dm7
add_chord([62, 65, 67, 72], 3 * seconds_per_beat)

# --- BASS: Marcus ---
# Walking line, chromatic approaches, no repeated notes
# Starts in D minor, walking line in D Dorian or D Aeolian

bass_notes = [
    62,  # D (beat 1)
    64,  # Eb (beat 2)
    62,  # D (beat 3)
    67,  # A (beat 4)
    67,  # A (beat 1)
    72,  # C (beat 2)
    67,  # A (beat 3)
    62,  # D (beat 4)
    62,  # D (beat 1)
    64,  # Eb (beat 2)
    62,  # D (beat 3)
    67,  # A (beat 4)
]

for i, note in enumerate(bass_notes):
    time = i * seconds_per_beat  # Start on beat
    n = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.2)
    instrument_bass.notes.append(n)

# --- SAX: Dante ---
# The motif: a simple phrase in D minor, sparse, waiting to be answered
# In D minor: D, Eb, F, G, A, Bb, C
# Motif: D (beat 1) -> Eb (beat 2) -> F (beat 3) -> rest (beat 4)
# Then repeat on beat 5 (bar 2), but shift up a half-step?
# D -> Eb -> F -> rest (bar 2)
# Then return to D on beat 9 (bar 3), but end the phrase on C (beat 10, 11, 12)

def add_sax_note(pitch, time):
    n = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.2)
    instrument_sax.notes.append(n)

# Bar 1: D, Eb, F, rest
add_sax_note(62, 0 * seconds_per_beat)
add_sax_note(64, 1 * seconds_per_beat)
add_sax_note(65, 2 * seconds_per_beat)

# Bar 2: D, Eb, F, rest
add_sax_note(62, 4 * seconds_per_beat)
add_sax_note(64, 5 * seconds_per_beat)
add_sax_note(65, 6 * seconds_per_beat)

# Bar 3: D, Eb, F, rest
add_sax_note(62, 8 * seconds_per_beat)
add_sax_note(64, 9 * seconds_per_beat)
add_sax_note(65, 10 * seconds_per_beat)

# Optional: End with a haunting C on beat 11 (bridge into the next part)
add_sax_note(60, 11 * seconds_per_beat)

# Save the MIDI
pm.write("dante_intro.mid")
