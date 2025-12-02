
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor
key = 'Fm'

# Initialize instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Add instruments to the piece
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define time per beat (in seconds)
tempo = 160  # BPM
time_per_beat = 60 / tempo  # 0.375 seconds per beat
bar_length = 4 * time_per_beat  # 1.5 seconds per bar

# --- BAR 1: DRUMS ONLY (Little Ray) ---
# Kicks on 1 and 3, snares on 2 and 4, hihat on every eighth

bar_start = 0.0
drum_notes = {
    'Kick': 36, 'Snare': 38, 'HiHat': 42
}

# Kick on 1 and 3
kick_times = [bar_start + time_per_beat * i for i in [0, 2]]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['Kick'], start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar_start + time_per_beat * i for i in [1, 3]]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['Snare'], start=t, end=t + 0.1)
    drums.notes.append(note)

# Hi-hat on every eighth note
for i in range(8):
    hihat_time = bar_start + time_per_beat * (i / 2)
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['HiHat'], start=hihat_time, end=hihat_time + 0.05)
    drums.notes.append(note)

# --- BAR 2: BASS, PIANO, SAX (Marcus, Diane, You) ---

bar_start = bar_length

# BASS: Walking line in F minor (F - G - D - E)
# F2 (38), G2 (40), D2 (34), E2 (36)
bass_notes = [38, 40, 34, 36]
for i, pitch in enumerate(bass_notes):
    start_time = bar_start + time_per_beat * i
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + time_per_beat)
    bass.notes.append(note)

# PIANO: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Open voicings: F (72), Ab (70), C (72), Eb (69) → F, Eb, Ab, C
piano_notes = [72, 69, 70, 72]
for i, pitch in enumerate(piano_notes):
    start_time = bar_start + time_per_beat * (i % 2)  # Comp on 2 and 4
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start_time, end=start_time + 0.5)
    piano.notes.append(note)

# SAX: Your motif — a simple, haunting phrase
# Motif: F (65), Ab (67), E (69), D (67) → F, Ab, E, D
# Start on beat 2 (1.0), finish on beat 4 (3.0)

# First note (F, beat 2)
note = pretty_midi.Note(velocity=100, pitch=65, start=bar_start + time_per_beat * 1, end=bar_start + time_per_beat * 1 + 0.5)
sax.notes.append(note)

# Second note (Ab, beat 2.5)
note = pretty_midi.Note(velocity=100, pitch=67, start=bar_start + time_per_beat * 2.5, end=bar_start + time_per_beat * 2.5 + 0.5)
sax.notes.append(note)

# Third note (E, beat 3)
note = pretty_midi.Note(velocity=100, pitch=69, start=bar_start + time_per_beat * 3, end=bar_start + time_per_beat * 3 + 0.5)
sax.notes.append(note)

# Fourth note (D, beat 3.5)
note = pretty_midi.Note(velocity=100, pitch=67, start=bar_start + time_per_beat * 3.5, end=bar_start + time_per_beat * 3.5 + 0.5)
sax.notes.append(note)

# --- BAR 3: BASS, PIANO, SAX (Marcus, Diane, You) ---

bar_start += bar_length

# BASS: Walking line in F minor (Ab - Bb - F - G)
# Ab2 (36), Bb2 (37), F2 (38), G2 (40)
bass_notes = [36, 37, 38, 40]
for i, pitch in enumerate(bass_notes):
    start_time = bar_start + time_per_beat * i
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + time_per_beat)
    bass.notes.append(note)

# PIANO: Open voicings
# Bar 3: Bm7b5 (B, D, F, Ab)
# Open voicings: B (71), F (69), Ab (67), D (65)
piano_notes = [71, 69, 67, 65]
for i, pitch in enumerate(piano_notes):
    start_time = bar_start + time_per_beat * (i % 2)  # Comp on 2 and 4
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start_time, end=start_time + 0.5)
    piano.notes.append(note)

# SAX: Motif repeat (but leave it hanging)
# Play first two notes again, leave it unresolved

# First note (F, beat 2)
note = pretty_midi.Note(velocity=100, pitch=65, start=bar_start + time_per_beat * 1, end=bar_start + time_per_beat * 1 + 0.5)
sax.notes.append(note)

# Second note (Ab, beat 2.5)
note = pretty_midi.Note(velocity=100, pitch=67, start=bar_start + time_per_beat * 2.5, end=bar_start + time_per_beat * 2.5 + 0.5)
sax.notes.append(note)

# --- BAR 4: BASS, PIANO, SAX (Marcus, Diane, You) ---

bar_start += bar_length

# BASS: Walking line in F minor (Bb - C - Ab - Bb)
# Bb2 (37), C2 (40), Ab2 (36), Bb2 (37)
bass_notes = [37, 40, 36, 37]
for i, pitch in enumerate(bass_notes):
    start_time = bar_start + time_per_beat * i
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + time_per_beat)
    bass.notes.append(note)

# PIANO: Open voicings
# Bar 4: Fm7 (F, Ab, C, Eb)
# Open voicings: F (72), Eb (69), Ab (70), C (72)
piano_notes = [72, 69, 70, 72]
for i, pitch in enumerate(piano_notes):
    start_time = bar_start + time_per_beat * (i % 2)  # Comp on 2 and 4
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=start_time, end=start_time + 0.5)
    piano.notes.append(note)

# SAX: Finish the motif
# Continue from where you left off (Ab, beat 2.5)
note = pretty_midi.Note(velocity=100, pitch=69, start=bar_start + time_per_beat * 3, end=bar_start + time_per_beat * 3 + 0.5)
sax.notes.append(note)

# Save the MIDI file
pm.write("whispers_in_fm.mid")

print("MIDI file saved as 'whispers_in_fm.mid'")
