
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # 480 ticks per quarter note
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Constants
BPM = 160
BARS = 4
QUARTER_NOTES = 4
TICKS_PER_QUARTER = pm.resolution
TICKS_PER_BAR = TICKS_PER_QUARTER * QUARTER_NOTES
TICKS_PER_BAR = int(TICKS_PER_BAR)

# --- BAR 1: DRUMS ONLY (Building tension) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
quarter = TICKS_PER_QUARTER

# Hihat on every eighth (2 per beat)
for i in range(0, TICKS_PER_BAR, quarter // 2):
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=i, end=i + quarter // 2))  # Hihat

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=quarter))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2*quarter, end=3*quarter))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=quarter, end=2*quarter))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3*quarter, end=4*quarter))

# --- BAR 2: INTRO TO THE MELODY (Tenor Sax) ---
# Melody: Dm7 – D, F, Ab, Bb
# Introduce a motif: D, F, Bb, Ab
# Start on D (D4 = 62), F (F4 = 65), Bb (Bb4 = 67), Ab (Ab4 = 66)

# Each note is 1/4 note
note_duration = quarter

# Melody in Bar 2
melody_notes = [
    (62, 0),   # D4
    (65, 1),   # F4
    (67, 2),   # Bb4
    (66, 3),   # Ab4
]

for pitch, beat in melody_notes:
    start = beat * quarter
    end = start + note_duration
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# --- BAR 3: RHYTHM SECTION JOIN IN (Marcus on bass, Diane on piano) ---

# Marcus on bass (walking line in Dm7: D, F, Ab, Bb, D, F, Ab, Bb)
bass_line = [62, 65, 67, 66, 62, 65, 67, 66]
for i, pitch in enumerate(bass_line):
    start = i * (quarter / 2)  # 16th note
    end = start + (quarter / 2)
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Diane on piano (comping on 2 and 4)
# Dm7 = D, F, Ab, Bb
# Root on 2 and 4, 7th chord
piano_notes = [
    (66, 1),   # Bb4 (7th of Dm7) on beat 2
    (66, 3),   # Bb4 on beat 4
]

for pitch, beat in piano_notes:
    start = beat * quarter
    end = start + note_duration
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# --- BAR 4: CONTINUE THE MELODY, BUT LEAVE IT HANGING ---
# Tenor sax continues the motif, but ends on Ab, not resolving
# This leaves the listener in anticipation

sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3 * quarter, end=4 * quarter))

# --- End of piece ---
pm.write('jazz_intro_in_dm.mid')

print("MIDI file 'jazz_intro_in_dm.mid' has been created.")
