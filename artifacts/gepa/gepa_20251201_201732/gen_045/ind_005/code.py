
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set key signature to F major
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F major

# ----------------------------
# Define instruments
# ----------------------------

# 1. Drums (Little Ray) - 9
drums = pretty_midi.Instrument(program=9)
pm.instruments.append(drums)

# 2. Bass (Marcus) - 33 (Acoustic Bass)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# 3. Piano (Diane) - 0 (Acoustic Piano)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# 4. Tenor Sax (You) - 67 (Soprano Sax, close enough)
sax = pretty_midi.Instrument(program=67)
pm.instruments.append(sax)

# ----------------------------
# Bar 1: Drums only — 16th-note ride cymbal, with a fill
# ----------------------------

# Define the ride pattern
ride_pattern = [9, 42]  # 9 = hi-hat, 42 = ride cymbal
bar_length = 6.0 / 4  # 6 seconds for 4 bars, so 1.5s per bar
note_duration = bar_length / 4  # 0.375s per 16th note

for i in range(0, 4):  # 4 beats per bar
    for j in range(0, 4):  # 4 16th notes per beat
        note = pretty_midi.Note(velocity=100, pitch=ride_pattern[i % 2], start=i * 0.25 + j * note_duration, end=i * 0.25 + j * note_duration + note_duration)
        drums.notes.append(note)

# ----------------------------
# Bar 2: All instruments — Diane, Marcus, and you
# ----------------------------

# Diane: Open voicings (chords)
# Bar 2: F7
diane_chord = [65, 72, 76, 80]  # F7 (F, A, C, E♭)
for pitch in diane_chord:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=1.5, end=2.25)
    piano.notes.append(note)

# Bar 3: C7 (V7 of F)
diane_chord = [72, 79, 84, 87]  # C7
for pitch in diane_chord:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=2.25, end=3.0)
    piano.notes.append(note)

# Bar 4: Gm7 (ii chord)
diane_chord = [71, 76, 81, 87]  # Gm7
for pitch in diane_chord:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=3.0, end=3.75)
    piano.notes.append(note)

# Marcus: Walking bass line (F major with chromatic approaches)
bass_notes = [
    65,  # F (root)
    67,  # G (chromatic approach)
    69,  # A (3rd)
    72,  # C (5th)
    71,  # B (chromatic approach)
    72,  # C (5th)
    69,  # A (3rd)
    67,  # G (chromatic approach)
    65,  # F (root)
    67,  # G (chromatic approach)
    72,  # C (5th)
    74,  # D (chromatic approach)
    72,  # C (5th)
    71,  # B (chromatic approach)
    72,  # C (5th)
    69,  # A (3rd)
]

for i, note in enumerate(bass_notes):
    start = i * 0.375 + 1.5
    end = start + 0.375
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    bass.notes.append(bass_note)

# You (sax): Motif — starts with a question, builds tension, resolves with a touch of mystery
# Motif: F (65), E♭ (64), G (67), F (65) — a simple question with a chromatic approach to the 3rd
sax_notes = [
    65,  # F
    64,  # E♭ (chromatic)
    67,  # G (3rd)
    65,  # F (resolve)
    67,  # G (half-step up)
    69,  # A (3rd again)
    67,  # G (half-step)
    69  # A (resolve)
]

sax_start = 1.5
sax_duration = 0.375

for i, note in enumerate(sax_notes):
    start = sax_start + i * sax_duration
    end = start + sax_duration
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    sax.notes.append(sax_note)

# ----------------------------
# Save the MIDI file
# ----------------------------
pm.write("dante_shorter_intro.mid")

print("MIDI file generated: 'dante_shorter_intro.mid'")
