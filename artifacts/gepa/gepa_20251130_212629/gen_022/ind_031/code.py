
import pretty_midi

# Create a PrettyMIDI object with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66, is_drum=False)       # Saxophone
bass = pretty_midi.Instrument(program=33, is_drum=False)      # Bass
piano = pretty_midi.Instrument(program=0, is_drum=False)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)       # Drums

# Add instruments to the MIDI file
midi.instruments = [drums, sax, bass, piano]

# Define the time per bar at 160 BPM
time_per_bar = 60 / 160 * 4  # 1.5 seconds per bar

# Bar 1: Drums only
# Kick on 1 & 3, snare on 2 & 4, hihat on all 8th notes
def add_drums(start_time):
    kick_notes = [36] * 2  # 1 & 3
    snare_notes = [38] * 2  # 2 & 4
    hihat_notes = [42] * 4  # every 8th note

    # Kick on 1 & 3
    for i, note in enumerate(kick_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time + i * 0.75, end=start_time + i * 0.75 + 0.25)
        drums.notes.append(note_obj)

    # Snare on 2 & 4
    for i, note in enumerate(snare_notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time + i * 0.75 + 0.5, end=start_time + i * 0.75 + 0.75)
        drums.notes.append(note_obj)

    # Hihat on every 8th note
    for i, note in enumerate(hihat_notes):
        note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start_time + i * 0.25, end=start_time + i * 0.25 + 0.1)
        drums.notes.append(note_obj)

# Bar 1: Drums only
add_drums(0.0)

# Bar 2: Full quartet
def add_sax(start_time):
    # Dm scale: D, Eb, F, G, Ab, Bb, C
    # A simple melodic motif in Dm
    # D - F - Eb - G
    notes = [62, 64, 63, 67]  # D, F, Eb, G
    durations = [0.5, 0.5, 0.5, 0.5]
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time + i * 0.5, end=start_time + i * 0.5 + durations[i])
        sax.notes.append(note_obj)

def add_bass(start_time):
    # Bass line walking through Dm
    # F - Eb - D - C - Bb - Ab - G - F
    notes = [64, 63, 62, 60, 59, 57, 67, 64]
    durations = [0.375] * 8
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start_time + i * 0.375, end=start_time + i * 0.375 + durations[i])
        bass.notes.append(note_obj)

def add_piano(start_time):
    # Comping with Dm7 and Gm7 chords
    # Dm7: D, F, A, C
    # Gm7: G, Bb, D, F
    # Play on off-beats
    chords = [[62, 64, 69, 67], [71, 69, 62, 64]]
    for i, chord in enumerate(chords):
        for note in chord:
            note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start_time + i * 0.75 + 0.25, end=start_time + i * 0.75 + 0.5)
            piano.notes.append(note_obj)

# Bar 2
add_drums(1.5)
add_sax(1.5)
add_bass(1.5)
add_piano(1.5)

# Bar 3: Full quartet with slight variation
def add_sax_var(start_time):
    # D - G - E - F
    notes = [62, 67, 64, 64]
    durations = [0.5, 0.5, 0.5, 0.5]
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time + i * 0.5, end=start_time + i * 0.5 + durations[i])
        sax.notes.append(note_obj)

def add_bass_var(start_time):
    # Walk through the same line but with slight syncopation
    notes = [64, 63, 62, 60, 59, 57, 67, 64]
    durations = [0.375] * 8
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start_time + i * 0.375, end=start_time + i * 0.375 + durations[i])
        bass.notes.append(note_obj)

def add_piano_var(start_time):
    # Dm7 again, on off-beats
    chords = [[62, 64, 69, 67], [71, 69, 62, 64]]
    for i, chord in enumerate(chords):
        for note in chord:
            note_obj = pretty_midi.Note(velocity=70, pitch=note, start=start_time + i * 0.75 + 0.25, end=start_time + i * 0.75 + 0.5)
            piano.notes.append(note_obj)

# Bar 3
add_drums(3.0)
add_sax_var(3.0)
add_bass_var(3.0)
add_piano_var(3.0)

# Bar 4: Full quartet, resolution
def add_sax_res(start_time):
    # D - C - Bb - Ab
    notes = [62, 60, 59, 57]
    durations = [0.5, 0.5, 0.5, 0.5]
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=100, pitch=note, start=start_time + i * 0.5, end=start_time + i * 0.5 + durations[i])
        sax.notes.append(note_obj)

def add_bass_res(start_time):
    # Walk back to D
    notes = [64, 63, 62, 60, 59, 57, 67, 62]
    durations = [0.375] * 8
    for i, note in enumerate(notes):
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start_time + i * 0.375, end=start_time + i * 0.375 + durations[i])
        bass.notes.append(note_obj)

def add_piano_res(start_time):
    # Dm7 again, with slightly more emphasis
    chords = [[62, 64, 69, 67], [71, 69, 62, 64]]
    for i, chord in enumerate(chords):
        for note in chord:
            note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start_time + i * 0.75 + 0.25, end=start_time + i * 0.75 + 0.5)
            piano.notes.append(note_obj)

# Bar 4
add_drums(4.5)
add_sax_res(4.5)
add_bass_res(4.5)
add_piano_res(4.5)

# Save the MIDI file
midi.write("dm_quartet.mid")
