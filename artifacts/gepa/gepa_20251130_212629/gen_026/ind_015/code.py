
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Define the key (D Major)
KEY = 'D'
KEY_NOTE = pretty_midi.note_number_from_name('D4')  # D4 is the tonic

# Define instruments
instrument_drums = pretty_midi.Instrument(program=10)
instrument_piano = pretty_midi.Instrument(program=0)
instrument_bass = pretty_midi.Instrument(program=33)
instrument_sax = pretty_midi.Instrument(program=64)

pm.instruments = [instrument_drums, instrument_piano, instrument_bass, instrument_sax]

# Time settings
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = 4 * BEAT  # seconds per bar
TOTAL_TIME = 4 * BAR  # 4 bars

# Time for each event in seconds
time = 0.0

# Bar 1: Little Ray (Drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(time, bar_length):
    # Kick on 1 and 3
    kick_notes = [pretty_midi.note_number_from_name('C2'), pretty_midi.note_number_from_name('C2')]
    kick_times = [time + (bar_length / 4), time + (bar_length / 4) * 3]
    for note, t in zip(kick_notes, kick_times):
        instrument_drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.05))

    # Snare on 2 and 4
    snare_notes = [pretty_midi.note_number_from_name('G2'), pretty_midi.note_number_from_name('G2')]
    snare_times = [time + (bar_length / 4) * 2, time + (bar_length / 4) * 4]
    for note, t in zip(snare_notes, snare_times):
        instrument_drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=t, end=t + 0.05))

    # Hi-hat on every eighth
    hihat_notes = [pretty_midi.note_number_from_name('C6')] * 8
    hihat_times = [time + (bar_length / 8) * i for i in range(8)]
    for note, t in zip(hihat_notes, hihat_times):
        instrument_drums.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=t, end=t + 0.03))

# Bar 1
add_drums(time, BAR)
time += BAR

# Bar 2: All in. Sax takes the melody
# Melody: A short, questioning motif — one phrase that ends on a suspended note
# Dm7 -> G7 -> Cmaj7 -> Dmaj7 -> Dm7
# D (root), Bm7, G7, Cmaj7, Dmaj7
# Melody: D - B - A - G (suspended), with rests and space

# Define melody notes (D4, B3, A3, G3) with durations and rests
melody = [
    (pretty_midi.note_number_from_name('D4'), 0.5),  # D4, quarter note
    (pretty_midi.note_number_from_name('B3'), 0.25), # B3, eighth note
    (pretty_midi.note_number_from_name('A3'), 0.25), # A3, eighth note
    (None, 0.5),                                    # rest, quarter note
    (pretty_midi.note_number_from_name('G3'), 0.25), # G3, eighth note
    (None, 0.25)                                    # rest, eighth note
]

# Add melody to sax
melody_time = time
for note, duration in melody:
    if note:
        instrument_sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=melody_time, end=melody_time + duration))
    melody_time += duration

# Bar 2: Diane (Piano) — 7th chords comp on 2 and 4
# Dmin7 on 2, G7 on 4
def add_piano(time, bar_length):
    # Dmin7 (D, F, A, C)
    # Play on beat 2
    dmin7_notes = [pretty_midi.note_number_from_name('D4'), pretty_midi.note_number_from_name('F4'),
                   pretty_midi.note_number_from_name('A4'), pretty_midi.note_number_from_name('C5')]
    dmin7_time = time + (bar_length / 4) * 2
    for note in dmin7_notes:
        instrument_piano.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=dmin7_time, end=dmin7_time + 0.25))

    # G7 (G, B, D, F)
    # Play on beat 4
    g7_notes = [pretty_midi.note_number_from_name('G4'), pretty_midi.note_number_from_name('B4'),
                pretty_midi.note_number_from_name('D5'), pretty_midi.note_number_from_name('F5')]
    g7_time = time + (bar_length / 4) * 4
    for note in g7_notes:
        instrument_piano.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=g7_time, end=g7_time + 0.25))

# Bar 2
add_piano(time, BAR)
time += BAR

# Bar 3: Marcus (Bass) — walking line, chromatic approach to D
# D - Eb - E - F - G - Ab - A - Bb - B - C - D
# Walking line from D4 to D5 with chromatic approach
def add_bass(time, bar_length):
    # D4 -> Eb4 -> E4 -> F4 -> G4 -> Ab4 -> A4 -> Bb4 -> B4 -> C5 -> D5
    bass_notes = [
        pretty_midi.note_number_from_name('D4'),
        pretty_midi.note_number_from_name('Eb4'),
        pretty_midi.note_number_from_name('E4'),
        pretty_midi.note_number_from_name('F4'),
        pretty_midi.note_number_from_name('G4'),
        pretty_midi.note_number_from_name('Ab4'),
        pretty_midi.note_number_from_name('A4'),
        pretty_midi.note_number_from_name('Bb4'),
        pretty_midi.note_number_from_name('B4'),
        pretty_midi.note_number_from_name('C5'),
        pretty_midi.note_number_from_name('D5'),
    ]
    # Bass plays quarter note every beat
    for i, note in enumerate(bass_notes):
        start_time = time + (bar_length / 4) * i
        end_time = start_time + 0.25
        instrument_bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=end_time))

# Bar 3
add_bass(time, BAR)
time += BAR

# Bar 4: Diane (Piano) — Cmaj7 on 2, Dmaj7 on 4
def add_piano_bar4(time, bar_length):
    # Cmaj7 (C, E, G, B)
    cmaj7_notes = [pretty_midi.note_number_from_name('C5'), pretty_midi.note_number_from_name('E5'),
                   pretty_midi.note_number_from_name('G5'), pretty_midi.note_number_from_name('B5')]
    cmaj7_time = time + (bar_length / 4) * 2
    for note in cmaj7_notes:
        instrument_piano.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=cmaj7_time, end=cmaj7_time + 0.25))

    # Dmaj7 (D, F#, A, C#)
    dmaj7_notes = [pretty_midi.note_number_from_name('D5'), pretty_midi.note_number_from_name('F#5'),
                   pretty_midi.note_number_from_name('A5'), pretty_midi.note_number_from_name('C#6')]
    dmaj7_time = time + (bar_length / 4) * 4
    for note in dmaj7_notes:
        instrument_piano.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=dmaj7_time, end=dmaj7_time + 0.25))

# Bar 4
add_piano_bar4(time, BAR)
time += BAR

# Add the drums for bar 4 — same pattern
add_drums(time - BAR, BAR)

# Save the MIDI file
pm.write("dante_intro.mid")
