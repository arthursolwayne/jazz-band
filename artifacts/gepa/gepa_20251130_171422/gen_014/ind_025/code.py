
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
quarter_note_duration = 60.0 / tempo  # seconds per quarter note

# Create a MIDI file
pm = pretty_midi.PrettyMIDI()

# Define the time for each bar (4/4)
bar_duration = quarter_note_duration * 4  # 4 quarters per bar
total_duration = bar_duration * 4  # 4 bars

# Create a time grid in seconds
time_points = []
for i in range(4):
    for j in range(4):  # Each bar has 4 quarter notes
        time_points.append((i + 1) * quarter_note_duration * j)

# Create instruments
drums = Instrument(program=49, is_drum=True)
piano = Instrument(program=0)
bass = Instrument(program=33)
sax = Instrument(program=64)

pm.instruments.append(drums)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(sax)

# --- DRUMS: Bar 1: Little Ray plays on 1 and 3, snare on 2 and 4, hihat on every 8th ---
for t in time_points[:4]:  # First 4 quarter notes of bar 1
    # Kick on 1 and 3
    if t == 0 or t == 2 * quarter_note_duration:
        drums.notes.append(Note(36, 100, t, t + 0.1))
    # Snare on 2 and 4
    if t == 1 * quarter_note_duration or t == 3 * quarter_note_duration:
        drums.notes.append(Note(38, 100, t, t + 0.1))
    # Hihat on every 8th
    for k in range(2):
        if t == k * quarter_note_duration / 2:
            drums.notes.append(Note(42, 90, t, t + 0.05))

# --- PIANO: Comp on 2 and 4 (chords) ---
# Bar 1: No piano (drums only)
# Bar 2: Dm7 (D F A C)
# Bar 3: Dm7 (D F A C)
# Bar 4: Gm7 (G Bb D F) - a chromatic movement down

# Bar 2, beat 2
piano.notes.append(Note(62, 80, 2 * quarter_note_duration, 2 * quarter_note_duration + 0.1))  # F
piano.notes.append(Note(67, 80, 2 * quarter_note_duration, 2 * quarter_note_duration + 0.1))  # A
piano.notes.append(Note(69, 80, 2 * quarter_note_duration, 2 * quarter_note_duration + 0.1))  # C
piano.notes.append(Note(64, 80, 2 * quarter_note_duration, 2 * quarter_note_duration + 0.1))  # D

# Bar 3, beat 2
piano.notes.append(Note(62, 80, 6 * quarter_note_duration, 6 * quarter_note_duration + 0.1))  # F
piano.notes.append(Note(67, 80, 6 * quarter_note_duration, 6 * quarter_note_duration + 0.1))  # A
piano.notes.append(Note(69, 80, 6 * quarter_note_duration, 6 * quarter_note_duration + 0.1))  # C
piano.notes.append(Note(64, 80, 6 * quarter_note_duration, 6 * quarter_note_duration + 0.1))  # D

# Bar 4, beat 2
piano.notes.append(Note(67, 80, 10 * quarter_note_duration, 10 * quarter_note_duration + 0.1))  # Bb
piano.notes.append(Note(69, 80, 10 * quarter_note_duration, 10 * quarter_note_duration + 0.1))  # D
piano.notes.append(Note(65, 80, 10 * quarter_note_duration, 10 * quarter_note_duration + 0.1))  # G
piano.notes.append(Note(62, 80, 10 * quarter_note_duration, 10 * quarter_note_duration + 0.1))  # F

# --- BASS: Walking line with chromatic approaches ---
# Bar 1: D → C → B → A (approaching Dm7)
# Bar 2: C → B → A → G (walking up)
# Bar 3: G → F → E → D (chromatic up)
# Bar 4: D → C → B → A (back to D)

bass_notes = [
    (64, 0),  # D
    (60, 0.25),  # C
    (59, 0.5),  # B
    (67, 0.75),  # A (chromatic approach to Dm7)

    (60, 1),  # C
    (59, 1.25),  # B
    (67, 1.5),  # A
    (69, 1.75),  # G

    (69, 2),  # G
    (67, 2.25),  # F
    (65, 2.5),  # E
    (64, 2.75),  # D

    (64, 3),  # D
    (60, 3.25),  # C
    (59, 3.5),  # B
    (67, 3.75),  # A
]

for note, time in bass_notes:
    bass.notes.append(Note(note, 60, time * quarter_note_duration, time * quarter_note_duration + 0.2))

# --- SAX: Your motif — a short, melodic phrase — starts on bar 2, beat 1
# Dm7 chord: D, F, A, C
# Your motif: D (64), F (67), A (69), C (71) — play D, F, A, C in sequence across bars 2–4 with space

sax_notes = [
    (64, 1.0),  # D
    (67, 1.5),  # F
    (69, 2.0),  # A
    (71, 2.5),  # C
]

for note, time in sax_notes:
    sax.notes.append(Note(note, 100, time * quarter_note_duration, time * quarter_note_duration + 0.2))

# Set the tempo and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=tempo, time=0.0)]

# Save the MIDI file
pm.write('dante_russo_intro.mid')
print("MIDI file created: 'dante_russo_intro.mid'")
