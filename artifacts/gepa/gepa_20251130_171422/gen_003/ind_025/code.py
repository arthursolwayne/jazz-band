
import numpy as np
import pretty_midi
from pretty_midi import Instrument, Note

# Constants
BPM = 160
TEMPO = BPM * 60 / 4  # seconds per bar
BEAT_DURATION = TEMPO / 4  # seconds per beat
BAR_DURATION = TEMPO  # 6 seconds per 4 bars

# Key: D minor (D Dorian for a modal, open feel)
KEY = 'D'
MODE = 'Dorian'

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]
midi.tempos = [pretty_midi.TempoChange(tempo=BPM, time=0)]

# Create instruments
drums = Instrument(program=0, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

# List of tracks
tracks = [drums, bass, piano, sax]
midi.instruments = tracks

# Time counter
time = 0.0

# --- DRUMS (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth ---
# 4 bars = 16 beats = 32 eighth notes
for beat in range(16):
    time = beat * BEAT_DURATION
    if beat % 4 == 0 or beat % 4 == 2:  # Kick on 1 and 3 of each bar
        Note(number=36, start=time, end=time + 0.1).add_to_instrument(drums)
    if beat % 4 == 1 or beat % 4 == 3:  # Snare on 2 and 4
        Note(number=38, start=time, end=time + 0.1).add_to_instrument(drums)
    # Hi-hat on every eighth
    Note(number=42, start=time, end=time + 0.05).add_to_instrument(drums)

# --- BASS (Marcus): Walking line, chromatic approach, never repeats the same note ---
# D Dorian scale: D, E, F, G, A, B, C
# Walking bass line in 4 bars (16 beats), starting on D
bass_notes = [49, 51, 50, 52, 53, 55, 54, 56, 57, 59, 58, 60, 61, 62, 63, 60]  # D Dorian walking line
for i, note_num in enumerate(bass_notes):
    start_time = i * BEAT_DURATION
    end_time = start_time + 0.25
    Note(number=note_num, start=start_time, end=end_time).add_to_instrument(bass)

# --- PIANO (Diane): 7th chords, comp on 2 and 4 ---
# Chords for D Dorian: Dm7, E7, Fmaj7, Gm7, Am7, B7, Cmaj7
# Comp on beats 2 and 4 of each bar
chords = [
    (49, 52, 56, 59),  # Dm7 (D, F, A, C)
    (52, 55, 59, 62),  # E7 (E, G#, B, D)
    (51, 55, 59, 62),  # Fmaj7 (F, A, C, E)
    (50, 53, 57, 60),  # Gm7 (G, Bb, D, F)
    (53, 56, 60, 63),  # Am7 (A, C, E, G)
    (55, 58, 62, 65),  # B7 (B, D#, F#, A)
    (51, 55, 59, 62),  # Fmaj7 (repeated for open feel)
    (52, 55, 59, 62),  # E7 (repeated)
]

# Distribute chords on beats 2 and 4 of each bar
for bar in range(4):
    for beat in [1, 3]:  # 2 and 4
        time = (bar * 4 + beat) * BEAT_DURATION
        chord_notes = chords[bar * 2 + beat - 1]  # select chord
        for note_num in chord_notes:
            Note(number=note_num, start=time, end=time + 0.25).add_to_instrument(piano)

# --- SAX (You): Motif in the first bar, then a return in bar 2-3, leaving it hanging ---
# Motif: D - F - G - A (Dorian scale, simple and emotional)
# Bar 1: D (beat 1), F (beat 2), G (beat 3), A (beat 4)
# Bar 2: D (beat 1), F (beat 2), G (beat 3), rest (beat 4) — leave it hanging
# Bar 3: return on beat 1, then rest the rest
# Bar 4: return on beat 1, end on A (beat 4) — unresolved

sax_notes = [
    (49, 0.0, 0.5),   # D on beat 1
    (51, 1.5, 2.0),   # F on beat 2
    (52, 3.0, 3.5),   # G on beat 3
    (53, 4.5, 5.0),   # A on beat 4

    (49, 6.0, 6.5),   # D on beat 1 (bar 2)
    (51, 7.5, 8.0),   # F on beat 2 (bar 2)
    (52, 9.0, 9.5),   # G on beat 3 (bar 2)

    (49, 12.0, 12.5), # D on beat 1 (bar 3)
    (53, 13.5, 14.0), # A on beat 2 (bar 3)
]

for note_num, start, end in sax_notes:
    Note(number=note_num, start=start, end=end).add_to_instrument(sax)

# Save the MIDI file
midi.save("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
