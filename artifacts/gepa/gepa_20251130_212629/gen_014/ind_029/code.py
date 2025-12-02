
import pretty_midi
import random

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to F minor
# Fm: F, Gb, Ab, Bb, C, Db, Eb
# Using MIDI note numbers for F minor scale
# F = 65, Gb = 66, Ab = 67, Bb = 68, C = 70, Db = 71, Eb = 72

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define time in seconds per bar
bpm = 160
note_duration = 60.0 / bpm / 4  # 4/4 time, per quarter note
bar_length = 4 * note_duration  # 4 bars = 4 * 6.0s = 24 seconds
start_time = 0.0

# --- DRUMS ---
# Bar 1: Little Ray alone. Snare on 2 and 4, kick on 1 and 3, hihat on every eighth.
# Bar 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, syncopation, velocity variation.

# Bar 1 (only drums)
for bar in range(1):
    for i in range(8):
        time = start_time + (i * note_duration / 2)
        if i % 2 == 0:  # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_duration / 2)
            drums.notes.append(note)
        else:  # Snare on 2 and 4
            note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + note_duration / 2)
            drums.notes.append(note)
        # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + note_duration / 2)
        drums.notes.append(note)

# Bar 2-4 (drums with syncopation and velocity variation)
for bar in range(2, 5):
    bar_start = start_time + bar * bar_length
    for i in range(8):
        time = bar_start + (i * note_duration / 2)
        # Kick on 1 and 3
        if i % 2 == 0:
            velocity = random.randint(90, 110)
            note = pretty_midi.Note(velocity=velocity, pitch=36, start=time, end=time + note_duration / 2)
            drums.notes.append(note)
        # Snare on 2 and 4
        else:
            velocity = random.randint(80, 100)
            note = pretty_midi.Note(velocity=velocity, pitch=38, start=time, end=time + note_duration / 2)
            drums.notes.append(note)
        # Hi-hat on every eighth, syncopated
        if i % 2 == 0:
            velocity = random.randint(70, 90)
            note = pretty_midi.Note(velocity=velocity, pitch=42, start=time, end=time + note_duration / 2)
            drums.notes.append(note)
        else:
            velocity = random.randint(60, 80)
            note = pretty_midi.Note(velocity=velocity, pitch=42, start=time, end=time + note_duration / 2)
            drums.notes.append(note)

# --- BASS ---
# Marcus: Walking line, chromatic approaches, never the same note twice.

# Bar 1: Fm7
# F (65), Ab (67), Bb (68), Db (71)
f_notes = [65, 67, 68, 71]
for i in range(4):
    time = start_time + i * note_duration
    note = pretty_midi.Note(velocity=100, pitch=f_notes[i % 4], start=time, end=time + note_duration)
    bass.notes.append(note)

# Bar 2: Chromatic approach to Bb
# F, Gb, Ab, Bb
for i in range(4):
    time = start_time + bar_length + i * note_duration
    note = pretty_midi.Note(velocity=100, pitch=65 + i, start=time, end=time + note_duration)
    bass.notes.append(note)

# Bar 3: Walking line, chromatic approach to F
# Bb, Ab, Gb, F
for i in range(4):
    time = start_time + 2 * bar_length + i * note_duration
    note = pretty_midi.Note(velocity=100, pitch=68 - i, start=time, end=time + note_duration)
    bass.notes.append(note)

# Bar 4: Chromatic approach to Ab
# F, Gb, Ab, Bb
for i in range(4):
    time = start_time + 3 * bar_length + i * note_duration
    note = pretty_midi.Note(velocity=100, pitch=65 + i, start=time, end=time + note_duration)
    bass.notes.append(note)

# --- PIANO ---
# Diane: 7th chords, comp on 2 and 4. Sharp and emotional.

# Bar 1: Fm7
# F, Ab, Bb, Db
for i in range(4):
    time = start_time + i * note_duration
    note = pretty_midi.Note(velocity=110, pitch=65, start=time, end=time + note_duration)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=67, start=time, end=time + note_duration)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=68, start=time, end=time + note_duration)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=110, pitch=71, start=time, end=time + note_duration)
    piano.notes.append(note)

# Bar 2: Bb7 (comp on 2 and 4)
for i in range(4):
    if i % 2 == 1:  # comp on 2 and 4
        time = start_time + bar_length + i * note_duration
        note = pretty_midi.Note(velocity=100, pitch=68, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + note_duration)
        piano.notes.append(note)

# Bar 3: Ab7 (comp on 2 and 4)
for i in range(4):
    if i % 2 == 1:
        time = start_time + 2 * bar_length + i * note_duration
        note = pretty_midi.Note(velocity=100, pitch=67, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=69, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=71, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=73, start=time, end=time + note_duration)
        piano.notes.append(note)

# Bar 4: Cm7 (comp on 2 and 4)
for i in range(4):
    if i % 2 == 1:
        time = start_time + 3 * bar_length + i * note_duration
        note = pretty_midi.Note(velocity=100, pitch=70, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=72, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=74, start=time, end=time + note_duration)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=76, start=time, end=time + note_duration)
        piano.notes.append(note)

# --- SAXOPHONE ---
# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 1: Start the motif
# F (65), Gb (66), Ab (67)
note = pretty_midi.Note(velocity=110, pitch=65, start=start_time, end=start_time + note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=start_time + note_duration, end=start_time + 2 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=start_time + 2 * note_duration, end=start_time + 3 * note_duration)
sax.notes.append(note)

# Bar 2: Silence (leave it hanging)
# No notes

# Bar 3: Come back and finish
note = pretty_midi.Note(velocity=110, pitch=65, start=start_time + 2 * bar_length, end=start_time + 2 * bar_length + note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=start_time + 2 * bar_length + note_duration, end=start_time + 2 * bar_length + 2 * note_duration)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=start_time + 2 * bar_length + 2 * note_duration, end=start_time + 2 * bar_length + 3 * note_duration)
sax.notes.append(note)

# Bar 4: End with a held note (Ab)
note = pretty_midi.Note(velocity=110, pitch=67, start=start_time + 3 * bar_length, end=start_time + 3 * bar_length + note_duration)
sax.notes.append(note)

# Save the MIDI file
midi.write("dante_russo_intro.mid")
print("MIDI file generated: 'dante_russo_intro.mid'")
