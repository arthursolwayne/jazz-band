
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [drums, bass, piano, sax]

# Define time in seconds
BPM = 160
beats_per_bar = 4
note_duration = 60.0 / BPM  # Duration of one beat in seconds
bar_length = note_duration * beats_per_bar  # 6 seconds per bar
total_length = bar_length * 4  # 24 seconds total

# --- BAR 1: DRUMS ONLY (0.0 - 6.0 seconds) ---
# Kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
for bar in range(1):
    bar_start = bar * bar_length
    kick_beats = [0, 2]  # Beats 1 and 3
    snare_beats = [1, 3]  # Beats 2 and 4
    hihat_beats = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]  # Every eighth note

    # Kicks
    for beat in kick_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=90, pitch=36, start=time, end=time + 0.1
        )
        drums.notes.append(drum_note)

    # Snares
    for beat in snare_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=85, pitch=38, start=time, end=time + 0.1
        )
        drums.notes.append(drum_note)

    # Hihats
    for beat in hihat_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=70, pitch=42, start=time, end=time + 0.05
        )
        drums.notes.append(drum_note)

# --- BAR 2: FULL BAND ENTRIES (6.0 - 12.0 seconds) ---

# Define the sax melody
# A short, haunting motif in Dm, with rest and space
# Dm scale: D, Eb, F, G, Ab, Bb, C
# Motif: D (beat 1), rest (beat 2), C (beat 3), rest (beat 4)
note_lengths = [note_duration, note_duration, note_duration, note_duration]

sax_notes = [
    (0, 62, 0.0, 0.5),  # D (beat 1: 0.0 - 0.5)
    (0, 0, 0.5, 1.0),   # Rest
    (0, 60, 1.0, 1.5),  # C (beat 3: 1.0 - 1.5)
    (0, 0, 1.5, 2.0),   # Rest
]

for note in sax_notes:
    start, pitch, start_time, end_time = note
    if pitch != 0:
        sax_note = pretty_midi.Note(
            velocity=100, pitch=pitch, start=start_time, end=end_time
        )
        sax.notes.append(sax_note)

# --- BASS (walking line in Dm) ---
# Simple walking line: D, Eb, F, G, Ab, Bb, C, D, etc.
# In root position, chromatic, moving down
# Bar 2: D, Eb, F, G
bass_notes = [
    (0, 62, 6.0, 6.5),  # D
    (0, 63, 6.5, 7.0),  # Eb
    (0, 64, 7.0, 7.5),  # F
    (0, 67, 7.5, 8.0),  # G
]

for note in bass_notes:
    start, pitch, start_time, end_time = note
    if pitch != 0:
        bass_note = pretty_midi.Note(
            velocity=70, pitch=pitch, start=start_time, end=end_time
        )
        bass.notes.append(bass_note)

# --- PIANO (7th chords, comp on 2 and 4) ---
# Dm7: D, F, Ab, C
# Play on beat 2 and 4 of bar 2
chord_notes = [(62, 64, 67, 69)]  # D, F, Ab, C

for i, chord in enumerate(chord_notes):
    bar_start = 6.0  # Start of bar 2
    beat = 1  # beat 2
    time = bar_start + beat * note_duration
    for pitch in chord:
        piano_note = pretty_midi.Note(
            velocity=80, pitch=pitch, start=time, end=time + 0.1
        )
        piano.notes.append(piano_note)

    beat = 3  # beat 4
    time = bar_start + beat * note_duration
    for pitch in chord:
        piano_note = pretty_midi.Note(
            velocity=80, pitch=pitch, start=time, end=time + 0.1
        )
        piano.notes.append(piano_note)

# --- BAR 3 and 4: CONTINUE THE motif and build momentum ---

# Bar 3: repeat the sax motif, but slightly shifted
for i in range(1, 3):  # bars 3 and 4
    bar_start = i * bar_length
    sax_notes = [
        (0, 62, bar_start + 0.0, bar_start + 0.5),
        (0, 0, bar_start + 0.5, bar_start + 1.0),
        (0, 60, bar_start + 1.0, bar_start + 1.5),
        (0, 0, bar_start + 1.5, bar_start + 2.0),
    ]

    for note in sax_notes:
        start, pitch, start_time, end_time = note
        if pitch != 0:
            sax_note = pretty_midi.Note(
                velocity=100, pitch=pitch, start=start_time, end=end_time
            )
            sax.notes.append(sax_note)

    # Drums continue the same pattern
    kick_beats = [0, 2]
    snare_beats = [1, 3]
    hihat_beats = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5]

    for beat in kick_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=90, pitch=36, start=time, end=time + 0.1
        )
        drums.notes.append(drum_note)

    for beat in snare_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=85, pitch=38, start=time, end=time + 0.1
        )
        drums.notes.append(drum_note)

    for beat in hihat_beats:
        time = bar_start + beat * note_duration
        drum_note = pretty_midi.Note(
            velocity=70, pitch=42, start=time, end=time + 0.05
        )
        drums.notes.append(drum_note)

# Save the MIDI
midi.write('dante_intro.mid')

print("MIDI file saved as 'dante_intro.mid'")
