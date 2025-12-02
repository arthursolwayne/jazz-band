
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define the time in seconds per beat
beat = 60.0 / tempo  # 0.375 seconds per beat

# Define the key: F major
key = 'F'

# Bar duration in seconds
bar_duration = 4 * beat  # 1.5 seconds

# Define instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define MIDI note ranges
# Bass (D2 to G2)
bass_notes = {
    'D2': 38,
    'Eb2': 39,
    'E2': 40,
    'F2': 41,
    'G2': 43
}

# Piano: open voicings, F major, F7, E7, D7
piano_chords = [
    [65, 69, 72, 76],  # Fmaj7 (F, A, C, E)
    [65, 69, 72, 76],  # Repeat same chord for tension
    [64, 68, 72, 76],  # E7 (E, G#, B, D)
    [62, 66, 72, 76],  # D7 (D, F#, A, C#)
]

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': 36,    # MIDI note for kick
    'snare': 38,   # MIDI note for snare
    'hihat': 42,   # MIDI note for hihat
    'fill': 37     # MIDI note for drum fill (optional)
}

# Sax: short motif, F, A, C, Eb, with rests and dynamics
sax_notes = [
    # Bar 1: Empty (drums only)
    (),
    # Bar 2: F (65)
    (65, 0.5, 100),  # note, duration, velocity
    # Bar 3: A (69)
    (69, 0.5, 100),
    # Bar 4: C (72) and Eb (74)
    (72, 0.25, 100),
    (74, 0.25, 80)
]

#------------- BASS LINES -----------------
# Bar 1: Rest
# Bar 2: D2
# Bar 3: F2
# Bar 4: G2 with chromatic approach to E
bass_notes_time = []

# Bar 2: D2
note = pretty_midi.Note(velocity=70, pitch=bass_notes['D2'], start=beat, end=beat * 2)
bass.notes.append(note)

# Bar 3: F2
note = pretty_midi.Note(velocity=70, pitch=bass_notes['F2'], start=beat * 2, end=beat * 3)
bass.notes.append(note)

# Bar 4: G2 and chromatic approach to E
note = pretty_midi.Note(velocity=70, pitch=bass_notes['G2'], start=beat * 3, end=beat * 4)
bass.notes.append(note)

#------------- PIANO LINES -----------------
# Bar 1: Rest
# Bar 2: Fmaj7
# Bar 3: Fmaj7
# Bar 4: E7 -> D7

for bar in range(4):
    start_time = beat * bar
    if bar == 0:
        continue  # No chord on bar 1
    if bar == 1 or bar == 2:
        chord = piano_chords[0]  # Fmaj7
    elif bar == 3:
        chord = piano_chords[3]  # D7
    else:
        chord = piano_chords[1]  # Fmaj7 again

    for note in chord:
        pitch = note
        # Comp on 2 and 4
        if bar % 2 == 0:
            continue
        note_obj = pretty_midi.Note(velocity=80, pitch=pitch, start=start_time, end=start_time + beat / 2)
        piano.notes.append(note_obj)

#------------- DRUMS -----------------
# Bar 1: Kick on 1 and 3, hihat on every eighth
# Bar 2: Kick on 1 and 3, hihat on every eighth
# Bar 3: Kick on 1 and 3, hihat on every eighth
# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth, fill on 4

for bar in range(4):
    start_time = beat * bar

    # Kick on 1 and 3
    kick_time = start_time
    kick_note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=kick_time, end=kick_time + 0.1)
    drums.notes.append(kick_note)

    if bar != 3:  # No kick on 3 of bar 4
        kick_time = start_time + beat * 2
        kick_note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=kick_time, end=kick_time + 0.1)
        drums.notes.append(kick_note)

    # Snare on 2 and 4 (only on bar 4)
    if bar == 3:
        snare_time1 = start_time + beat
        snare_note1 = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=snare_time1, end=snare_time1 + 0.1)
        drums.notes.append(snare_note1)

        snare_time2 = start_time + beat * 3
        snare_note2 = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=snare_time2, end=snare_time2 + 0.1)
        drums.notes.append(snare_note2)

    # Hihat on every eighth
    for i in range(8):
        time = start_time + (beat / 8) * i
        hihat_note = pretty_midi.Note(velocity=70, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
        drums.notes.append(hihat_note)

#------------- SAX -----------------
for note_info in sax_notes:
    if not note_info:
        continue
    pitch, duration, velocity = note_info
    start_time = 0
    if sax_notes.index(note_info) == 0:
        start_time = 0  # Bar 2, beat 1
    elif sax_notes.index(note_info) == 1:
        start_time = beat  # Bar 3, beat 1
    elif sax_notes.index(note_info) == 2:
        start_time = beat * 2  # Bar 4, beat 1
    elif sax_notes.index(note_info) == 3:
        start_time = beat * 3  # Bar 4, beat 3
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=start_time + duration)
    sax.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro_wayne.mid")
