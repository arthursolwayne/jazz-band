
import pretty_midi
import numpy as np

# Create a new MIDI file with tempo 160 BPM (160 beats per minute)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers for D major scale
D_MAJOR = [50, 52, 53, 55, 57, 59, 60]  # D, E, F#, G, A, B, C#
D_MINOR = [50, 52, 53, 55, 57, 58, 60]  # D, E, F#, G, A, Bb, C#

# Drums: kick=36, snare=38, hihat=42
DRUMS = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
bar_duration = 1.5  # in seconds per bar

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * bar_duration + beat * (bar_duration / 4)
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(
                velocity=int(80 + np.random.randint(10)), 
                pitch=DRUMS['kick'], 
                start=time, 
                end=time + 0.1
            )
            drums.notes.append(note)
        elif beat == 1 or beat == 3:
            note = pretty_midi.Note(
                velocity=int(80 + np.random.randint(10)), 
                pitch=DRUMS['snare'], 
                start=time, 
                end=time + 0.1
            )
            drums.notes.append(note)
        # Hihat on every eighth
        for eighth in [0, 0.5]:
            note = pretty_midi.Note(
                velocity=60, 
                pitch=DRUMS['hihat'], 
                start=time + eighth, 
                end=time + eighth + 0.05
            )
            drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
start_time = 1.5

# Bass: Walking line, chromatic approaches, no same note twice
# D minor scale: [50, 52, 53, 55, 57, 58, 60]
bass_notes = [52, 53, 55, 57, 58, 50, 52, 53]
for i, note in enumerate(bass_notes):
    time = start_time + i * (bar_duration / 4)
    note_obj = pretty_midi.Note(
        velocity=70 + np.random.randint(10), 
        pitch=note,
        start=time,
        end=time + 0.25
    )
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4, emotional and tense
# Chords: Dm7, G7, Cm7, F7
chords = [
    [50, 53, 57, 58],  # Dm7
    [55, 57, 59, 62],  # G7
    [60, 63, 65, 67],  # Cm7
    [57, 60, 62, 64],  # F7
]
for i, chord in enumerate(chords):
    time = start_time + i * (bar_duration / 4)
    for note in chord:
        note_obj = pretty_midi.Note(
            velocity=90 + np.random.randint(10), 
            pitch=note,
            start=time,
            end=time + 0.25
        )
        piano.notes.append(note_obj)

# Sax: One short motif, haunting and simple
# Melody: D, F#, Bb, A, G, D
sax_notes = [50, 53, 58, 57, 55, 50]
for i, note in enumerate(sax_notes):
    time = start_time + i * (bar_duration / 4)
    note_obj = pretty_midi.Note(
        velocity=95 + np.random.randint(5), 
        pitch=note,
        start=time,
        end=time + 0.25
    )
    sax.notes.append(note_obj)

# Bar 3: Full ensemble (3.0 - 4.5s)
start_time = 3.0

# Bass: Walking line, chromatic approaches
bass_notes = [52, 53, 55, 57, 58, 50, 52, 53]
for i, note in enumerate(bass_notes):
    time = start_time + i * (bar_duration / 4)
    note_obj = pretty_midi.Note(
        velocity=70 + np.random.randint(10), 
        pitch=note,
        start=time,
        end=time + 0.25
    )
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
chords = [
    [55, 57, 59, 62],  # G7
    [60, 63, 65, 67],  # Cm7
    [57, 60, 62, 64],  # F7
    [50, 53, 57, 58],  # Dm7
]
for i, chord in enumerate(chords):
    time = start_time + i * (bar_duration / 4)
    for note in chord:
        note_obj = pretty_midi.Note(
            velocity=90 + np.random.randint(10), 
            pitch=note,
            start=time,
            end=time + 0.25
        )
        piano.notes.append(note_obj)

# Sax: Melody continuation
sax_notes = [50, 53, 55, 60, 57, 55]
for i, note in enumerate(sax_notes):
    time = start_time + i * (bar_duration / 4)
    note_obj = pretty_midi.Note(
        velocity=95 + np.random.randint(5), 
        pitch=note,
        start=time,
        end=time + 0.25
    )
    sax.notes.append(note_obj)

# Bar 4: Full ensemble (4.5 - 6.0s)
start_time = 4.5

# Bass: Walking line, chromatic approaches
bass_notes = [52, 53, 55, 57, 58, 50, 52, 53]
for i, note in enumerate(bass_notes):
    time = start_time + i * (bar_duration / 4)
    note_obj = pretty_midi.Note(
        velocity=70 + np.random.randint(10), 
        pitch=note,
        start=time,
        end=time + 0.25
    )
    bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
chords = [
    [57, 60, 62, 64],  # F7
    [50, 53, 57, 58],  # Dm7
    [55, 57, 59, 62],  # G7
    [60, 63, 65, 67],  # Cm7
]
for i, chord in enumerate(chords):
    time = start_time + i * (bar_duration / 4)
    for note in chord:
        note_obj = pretty_midi.Note(
            velocity=90 + np.random.randint(10), 
            pitch=note,
            start=time,
            end=time + 0.25
        )
        piano.notes.append(note_obj)

# Sax: Final motif — leave it hanging
sax_notes = [57, 55, 53, 50]
for i, note in enumerate(sax_notes):
    time = start_time + i * (bar_duration / 4)
    if i == len(sax_notes) - 1:
        end_time = time + 0.1
    else:
        end_time = time + 0.25
    note_obj = pretty_midi.Note(
        velocity=95 + np.random.randint(5), 
        pitch=note,
        start=time,
        end=end_time
    )
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
