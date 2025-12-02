
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
pm.instruments.append(instrument)

# Add drums
drums = pretty_midi.Instrument(program=0)  # Drums
pm.instruments.append(drums)

# Add piano
piano = pretty_midi.Instrument(program=0)  # Piano
pm.instruments.append(piano)

# Add bass
bass = pretty_midi.Instrument(program=33)  # Bass
pm.instruments.append(bass)

# Define note values and time
BPM = 160
beats_per_bar = 4
notes_per_beat = 4  # quarter note = 1 beat
note_length = 1 / notes_per_beat  # 0.25

# Time per bar in seconds
time_per_bar = (60.0 / BPM) * beats_per_bar

# Time for each beat
time_per_beat = time_per_bar / beats_per_bar

# Define note pitches (Dm scale: D, Eb, F, G, Ab, Bb, C)
# Root: D = 62
# Notes: D (62), Eb (63), F (65), G (67), Ab (68), Bb (70), C (72)
# Minor 7th chord: Dm7 = D, F, Ab, C (62, 65, 68, 72)

# Define chromatic bass line
bass_notes = [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]  # Start from D and walk chromatically

# Define saxophone motif (melodic, starts on bar 2, ends with a question)
sax_notes = [65, 67, 69, 70]  # F, G, A, Bb — ends on Bb, not resolving

# Define drum pattern: kick on 1&3, snare on 2&4, hihat on every 8th
# Note: 8th notes in 4/4 = 2 per beat, so 8 per bar

# Bar 1: Only drums
def create_drum_pattern(pm, start_time, bar_length):
    # Kick on 1 and 3
    for i in range(0, 2):
        kick_time = start_time + (i * 2) * (time_per_beat / 2)
        kick = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick)

    # Snare on 2 and 4
    for i in range(0, 2):
        snare_time = start_time + (i * 2 + 1) * (time_per_beat / 2)
        snare = pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.1)
        drums.notes.append(snare)

    # Hi-hat on every 8th note
    for i in range(0, 8):
        hihat_time = start_time + i * (time_per_beat / 2)
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=hihat_time, end=hihat_time + 0.1)
        drums.notes.append(hihat)

# Bar 1
create_drum_pattern(pm, 0, time_per_bar)

# Bar 2–4: Full quartet

# Bass line (chromatic, walking)
def create_bass_line(pm, start_time, notes, time_per_beat):
    for i, pitch in enumerate(notes):
        note_start = start_time + i * time_per_beat
        note_end = note_start + time_per_beat
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=note_start, end=note_end)
        bass.notes.append(note)

# Bass: 12 notes to walk chromatically
bass_start = time_per_bar
create_bass_line(pm, bass_start, bass_notes[0:12], time_per_beat)

# Piano: 7th chords on 2 and 4
def create_piano_chords(pm, start_time, time_per_beat, chord_notes):
    # Beat 2
    beat_2 = start_time + time_per_beat
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=beat_2, end=beat_2 + time_per_beat)
        piano.notes.append(note)

    # Beat 4
    beat_4 = start_time + 3 * time_per_beat
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=beat_4, end=beat_4 + time_per_beat)
        piano.notes.append(note)

piano_notes = [62, 65, 68, 72]  # Dm7: D, F, Ab, C
create_piano_chords(pm, bass_start, time_per_beat, piano_notes)

# Saxophone motif: starts on bar 2, 4 notes
def create_sax_melody(pm, start_time, notes, time_per_beat):
    for i, pitch in enumerate(notes):
        note_start = start_time + i * time_per_beat
        note_end = note_start + time_per_beat
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=note_start, end=note_end)
        instrument.notes.append(note)

sax_start = bass_start
create_sax_melody(pm, sax_start, sax_notes, time_per_beat)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file created: dante_intro.mid")
