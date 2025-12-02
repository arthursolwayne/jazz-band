
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.resolution = 480  # 480 ticks per quarter note
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define time per bar (160 BPM = 60 / 160 = 0.375 seconds per beat; 4/4 = 4 beats)
time_per_beat = 0.375
time_per_bar = time_per_beat * 4  # 1.5 seconds per bar

# --------------------------
# DRUMS: Little Ray
# --------------------------

drums = pretty_midi.Instrument(program=0)  # Drums

# Kick on 1 and 3
kick_notes = [pretty_midi.note_number_to_midi(36)]  # C1
kick_times = [0, time_per_beat * 2]  # Bar 1: beat 1, beat 3

# Snare on 2 and 4
snare_notes = [pretty_midi.note_number_to_midi(38)]  # D1
snare_times = [time_per_beat * 1, time_per_beat * 3]  # Bar 1: beat 2, beat 4

# Hi-hat on every eighth note
hihat_notes = [pretty_midi.note_number_to_midi(42)]  # F#1
hihat_times = []
for bar in range(1):
    for beat in range(4):
        for eighth in range(2):
            time = time_per_beat * (beat + eighth / 2)
            hihat_times.append(time)

# Add notes to drum instrument
for note, time in zip(kick_notes, kick_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

for note, time in zip(snare_notes, snare_times):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05))

for note, time in zip(hihat_notes, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.05))

pm.instruments.append(drums)

# --------------------------
# BASS: Marcus
# --------------------------

bass = pretty_midi.Instrument(program=33)  # Acoustic Bass

# Walking bass line in Dm: Dm7 = D, F, A, C
# Roots: D2 (D), F2 (F), A2 (A), C3 (C)
# Chromatic approaches on upbeats

bass_notes = [
    pretty_midi.note_number_to_midi(50),  # D2
    pretty_midi.note_number_to_midi(51),  # Eb2 (chromatic approach)
    pretty_midi.note_number_to_midi(53),  # F2
    pretty_midi.note_number_to_midi(55),  # G2 (chromatic)
    pretty_midi.note_number_to_midi(57),  # A2
    pretty_midi.note_number_to_midi(58),  # Bb2 (chromatic)
    pretty_midi.note_number_to_midi(60),  # B2 (chromatic)
    pretty_midi.note_number_to_midi(62),  # C3
]

bass_times = [time_per_beat * i for i in range(8)]

for note, time in zip(bass_notes, bass_times):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

pm.instruments.append(bass)

# --------------------------
# PIANO: Diane
# --------------------------

piano = pretty_midi.Instrument(program=0)  # Acoustic Piano

# Bar 1: Dm7 (open voicing)
# D - F - A - C
# Root: D3 (62), F: 65, A: 69, C: 60
# Open voicing: D3, F4, A4, C5
chords = [
    # Bar 1: Dm7
    [pretty_midi.note_number_to_midi(62), pretty_midi.note_number_to_midi(65), pretty_midi.note_number_to_midi(69), pretty_midi.note_number_to_midi(72)],
    
    # Bar 2: G7 (no 3, but with C#)
    [pretty_midi.note_number_to_midi(67), pretty_midi.note_number_to_midi(71), pretty_midi.note_number_to_midi(76), pretty_midi.note_number_to_midi(79)],

    # Bar 3: Cm7
    [pretty_midi.note_number_to_midi(60), pretty_midi.note_number_to_midi(63), pretty_midi.note_number_to_midi(67), pretty_midi.note_number_to_midi(72)],

    # Bar 4: Dm7 (resolve)
    [pretty_midi.note_number_to_midi(62), pretty_midi.note_number_to_midi(65), pretty_midi.note_number_to_midi(69), pretty_midi.note_number_to_midi(72)],
]

# Play chords on beats 2 and 4 (for comping)
for bar, chord in enumerate(chords):
    for note in chord:
        start_time = (bar + 1) * time_per_beat * 1.5  # 1.5 seconds = 2 beats
        duration = 0.5
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Add a final resolution chord at the end to give closure
resolution = [pretty_midi.note_number_to_midi(62), pretty_midi.note_number_to_midi(65), pretty_midi.note_number_to_midi(69), pretty_midi.note_number_to_midi(72)]
for note in resolution:
    start_time = time_per_bar * 4 - 0.25  # 0.25 seconds before end
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + 0.25))

pm.instruments.append(piano)

# --------------------------
# SAXOPHONE: You (Dante Russo)
# --------------------------

sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone

# Motif: Start with a lyrical, sparse phrase
# Dm7 - G7 - Cm7 - Dm7
# Motif: D4 - F4 - A4 - C5 - F4 - D4 (melodic, simple, emotional)

motif = [
    (pretty_midi.note_number_to_midi(62), 0.0),       # D4
    (pretty_midi.note_number_to_midi(65), 0.25),      # F4
    (pretty_midi.note_number_to_midi(69), 0.5),       # A4
    (pretty_midi.note_number_to_midi(72), 0.75),      # C5
    (pretty_midi.note_number_to_midi(65), 1.0),       # F4
    (pretty_midi.note_number_to_midi(62), 1.25),      # D4
]

# Repeat motif once, then leave it hanging on a D4
for i, (note, time) in enumerate(motif):
    start_time = time
    duration = 0.25
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Final D4 to hang on the last chord
sax.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.25))

pm.instruments.append(sax)

# Save the MIDI file
pm.write('dante_intro.mid')
