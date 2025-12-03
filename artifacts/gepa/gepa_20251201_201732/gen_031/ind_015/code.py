
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
BEAT_DURATION = 60 / BPM  # seconds per beat
BAR_DURATION = 1.5  # seconds per bar (4/4 time)
SAMPLE_RATE = 44100

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI()

# Define key: F major
F_MAJOR_SCALE = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
sax = Instrument(program=sax_program)
drums = Instrument(program=drums_program)

# Add instruments to the MIDI
midi.instruments = [bass, piano, sax, drums]

# --- DRUMS: Little Ray ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# Time signature: 4/4, tempo: 160 BPM

def add_drums(instrument, start_time, duration):
    time = start_time
    for bar in range(4):
        # 4 beats per bar
        for beat in range(4):
            # Kick on 1 and 3
            if beat == 0 or beat == 2:
                note = Note(36, time, duration)
                instrument.notes.append(note)
            # Snare on 2 and 4
            if beat == 1 or beat == 3:
                note = Note(38, time, duration)
                instrument.notes.append(note)
            # Hi-hat every 8th
            for eighth in range(2):
                note = Note(42, time, duration)
                instrument.notes.append(note)
                time += duration / 2
            time += duration

    # Add fills on last bar
    # Quick fill at the end of bar 4
    for i in range(4):
        note = Note(38, time + (i * 0.375), 0.125)
        instrument.notes.append(note)
        note = Note(42, time + (i * 0.375), 0.125)
        instrument.notes.append(note)

add_drums(drums, 0, BEAT_DURATION / 2)

# --- BASS: Marcus ---
# Roots and fifths with chromatic approaches, walking line
# F, C, G, C
# Time: 0.0s - 6.0s

def add_bass(instrument, start_time, duration, notes, velocities):
    for i, note in enumerate(notes):
        time = start_time + i * duration
        velocity = velocities[i % len(velocities)]
        instrument.notes.append(Note(note, time, duration, velocity))

# Bass notes: F (65), C (69), G (67), C (69)
# With chromatic passing tone on G (67)
bass_notes = [65, 66, 67, 69, 69, 67, 66, 65]
bass_velocities = [60, 70, 80, 90, 90, 80, 70, 60]  # dynamic variation
add_bass(bass, 0, BEAT_DURATION / 2, bass_notes, bass_velocities)

# --- PIANO: Diane ---
# Open voicings, different chord each bar
# Comp on 2 and 4

def add_piano(instrument, start_time, duration, chords, velocities):
    for i, chord in enumerate(chords):
        time = start_time + i * duration
        # Chord: root, third, fifth, seventh (open voicing)
        for note in chord:
            instrument.notes.append(Note(note, time, duration, velocities[i % len(velocities)]))

# Chords: Fmaj7, Bbmaj7, Dm7, Am7
# Chord voicings in open positions
# Fmaj7: F (65), A (69), C (72), E (74)
# Bbmaj7: Bb (62), D (67), F (69), A (72)
# Dm7: D (67), F (69), A (72), C (74)
# Am7: A (69), C (72), E (74), G (76)

piano_chords = [
    [65, 69, 72, 74],  # Fmaj7
    [62, 67, 69, 72],  # Bbmaj7
    [67, 69, 72, 74],  # Dm7
    [69, 72, 74, 76],  # Am7
]
piano_velocities = [95, 90, 85, 80]  # Comp on 2 and 4 (only 2nd and 4th bars)
add_piano(piano, 1.0, BEAT_DURATION / 2, piano_chords[1:], piano_velocities)

# --- SAX: Dante ---
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F, Ab, Bb (F minor motif, but open-ended)

def add_sax(instrument, start_time, duration, notes, velocities):
    for i, note in enumerate(notes):
        time = start_time + i * duration
        instrument.notes.append(Note(note, time, duration, velocities[i % len(velocities)]))

# Sax motif: F (65), Ab (67), Bb (67), F (65) — then wait
# Want it to feel like a question, not a statement
sax_notes = [65, 67, 67, 65]
sax_velocities = [90, 85, 80, 75]
add_sax(sax, 0, BEAT_DURATION / 2, sax_notes, sax_velocities)

# Save the MIDI
# midi.write disabled
print("MIDI file saved as 'dante_intro.mid'")
