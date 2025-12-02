
import pretty_midi
import numpy as np

# Create a PrettyMIDI object at 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature track
time_signature = pretty_midi.TimeSignatureTrack()
pm.time_signature_tracks.append(time_signature)

# Define the duration of the piece in seconds
bar_duration = 1.5  # 160 BPM, 4/4 time => 60 / 160 * 4 = 1.5s per bar
total_duration = 4 * bar_duration

# Create instrument tracks
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drums)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(sax)

# Define the key: F major
key = 'F'

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums():
    time = 0.0
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time + beat * 0.375, end=time + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time + beat * 0.375, end=time + beat * 0.375 + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for i in range(8):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + i * 0.125, end=time + i * 0.125 + 0.05)
        drums.notes.append(note)

add_drums()

# Bar 2-4: Everyone in (Marcus, Diane, You)

# Define F major scale
F_major = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, C, D, E, F#

# Bar 2: Diane (piano) — comping on 2 and 4 with 7th chords
def add_piano():
    time = 0.0
    # Chord: F7 on beat 2 (F, A, C, E♭)
    chords = [
        [65, 69, 72, 74],  # F7 on beat 2
        [65, 69, 72, 74],  # F7 on beat 4
    ]
    for idx, chord in enumerate(chords):
        start = time + (idx + 1) * 0.375
        for pitch in chord:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.5)
            piano.notes.append(note)

add_piano()

# Bar 2: Marcus (bass) — walking line with chromatic approach
def add_bass():
    time = 0.0
    # Walking line in F major, chromatic approach to G
    bass_line = [
        65,  # F
        66,  # F#
        67,  # G
        69,  # A
        72,  # C
        74,  # D
        76,  # E
        77,  # F#
        65   # F
    ]
    for i, pitch in enumerate(bass_line):
        start = time + i * 0.375
        note = pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=start + 0.25)
        bass.notes.append(note)

add_bass()

# Bar 2-4: You (tenor sax) — short motif, question-like, haunting
def add_sax():
    time = 0.0
    # Motif: F (65) -> G (67) -> F (65) -> rest
    # Then, return with a slight variation to end the phrase
    notes = [
        (65, 0.0, 0.5),     # F
        (67, 0.5, 0.75),    # G
        (65, 0.75, 1.0),    # F
        (65, 1.5, 1.75),    # F
        (67, 1.75, 2.0),    # G
        (66, 2.0, 2.25),    # F#
        (65, 2.25, 2.5),    # F
    ]
    for pitch, start, end in notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
        sax.notes.append(note)

add_sax()

# Write MIDI file
pm.write('dante_intro.mid')
print("MIDI file generated: 'dante_intro.mid'")
