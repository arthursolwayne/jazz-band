
import pretty_midi
import numpy as np

# Constants
TEMPO = 160  # BPM
TIME_SIGNATURE = (4, 4)
KEY = 'Dm7'  # D minor 7
NOTE_LENGTH = 0.25  # quarter note
BAR_DURATION = 1.5  # seconds per bar (160 BPM in 4/4 = 60 / 160 * 4 = 1.5)
TOTAL_DURATION = 6.0  # 4 bars
MIDI_FILE = 'jazz_intro.mid'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=TEMPO, time_signature_numerator=4, time_signature_denominator=4)

# Create instruments
drum_program = pretty_midi.programs[pretty_midi.instrument_name_to_program('Drums')]
bass_program = pretty_midi.programs[pretty_midi.instrument_name_to_program('Acoustic Bass')]
piano_program = pretty_midi.programs[pretty_midi.instrument_name_to_program('Electric Piano 1')]
sax_program = pretty_midi.programs[pretty_midi.instrument_name_to_program('Soprano Sax')]

drum_instrument = pretty_midi.Instrument(program=drum_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

# Time grid: 0.375s per beat (for 160 BPM), 4 beats per bar, 4 bars total
BEAT_DURATION = 60.0 / TEMPO  # 0.375s
BAR_DURATION = BEAT_DURATION * 4  # 1.5s
TIMES = [i * BEAT_DURATION for i in range(16)]  # 16 beats

# --------------------
# Drum Pattern (Little Ray)

# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for i in range(16):
    time = TIMES[i]

    if i % 4 == 0 or i % 4 == 2:  # Kick on 1 and 3
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + NOTE_LENGTH))
    if i % 4 == 1 or i % 4 == 3:  # Snare on 2 and 4
        drum_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + NOTE_LENGTH))
    if i % 2 == 0:  # Hihat on every eighth
        drum_instrument.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + NOTE_LENGTH / 2))

# --------------------
# Bass Line (Marcus)

# Chromatic approach line: D - C - Eb - F - D (Dm7)
# Each quarter note
note_map = {
    'D': 62,  # D4
    'C': 60,  # C4
    'Eb': 63, # Eb4
    'F': 65,  # F4
    'G': 67,  # G4
}

bass_notes = [note_map['D'], note_map['C'], note_map['Eb'], note_map['F'], note_map['D']]
for i in range(len(bass_notes)):
    time = TIMES[i]  # 0, 0.375, 0.75, 1.125, 1.5
    bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=bass_notes[i], start=time, end=time + NOTE_LENGTH))

# --------------------
# Piano (Diane) — sparse 7th chords: Dm7 on beat 2 and 4

# Dm7 = D, F, A, C
d7_notes = [62, 65, 69, 60]
for i in [1, 3]:  # beats 2 and 4
    time = TIMES[i]
    for pitch in d7_notes:
        piano_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + NOTE_LENGTH))

# --------------------
# Saxophone (You) — short, emotional motif: D - Eb - F - D (with space)

# Start on 1.5s, play 16th notes with dynamic contrast
sax_notes = [62, 63, 65, 62]  # D, Eb, F, D
for i, pitch in enumerate(sax_notes):
    time = 1.5 + i * 0.25  # start at bar 2 (1.5s), play every 0.25s
    velocity = 100 if i == 0 else 90  # start strong, then softer
    sax_instrument.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + 0.25))

# --------------------
# Save the MIDI file
pm.write(MIDI_FILE)
print(f"Generated MIDI file saved as '{MIDI_FILE}'")
