
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Instrument: Drums (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drum_program)

# Bar 1: 0.0 to 1.5s
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
def add_drums():
    beat = 0.375  # 160 BPM = 0.375s per beat
    for bar in range(1):
        for i in range(4):  # 4 beats per bar
            time = bar * 1.5 + i * beat
            if i == 0 or i == 2:  # Kick on 1 and 3
                note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.1)
                drums.notes.append(note)
            elif i == 1 or i == 3:  # Snare on 2 and 4
                note = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
                drums.notes.append(note)
            # Hi-hat on every eighth
            if i % 2 == 0:
                hihat = pretty_midi.Note(velocity=85, pitch=42, start=time, end=time + 0.05)
                drums.notes.append(hihat)

add_drums()

# Instrument: Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Walking bass line in D major
def add_bass():
    # Notes in D major: D, E, F#, G, A, B, C#
    # Bass line: D -> F# -> A -> C# -> D -> F# -> A -> C#
    bass_notes = [2, 4, 6, 8, 2, 4, 6, 8]  # MIDI: D (2), F# (4), A (6), C# (8)
    for i, note in enumerate(bass_notes):
        time = i * 0.375
        if time >= 1.5:
            time -= 1.5  # Only play from bar 2 to 4
        note_obj = pretty_midi.Note(velocity=80, pitch=note + 24, start=time, end=time + 0.375)
        bass.notes.append(note_obj)

add_bass()

# Instrument: Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = pretty_midi.Instrument(program=piano_program)

def add_piano():
    # Comp on 2 and 4 with 7th chords
    # D7 = D F# A C
    # G7 = G B D F
    # A7 = A C# E G
    # B7 = B D# F# A
    chords = {
        1: [2, 4, 6, 9],   # D7
        2: [7, 11, 12, 15], # G7
        3: [10, 14, 16, 19], # A7
        4: [11, 14, 16, 20]  # B7
    }

    for beat, chord in chords.items():
        time = (beat - 1) * 0.375 + 1.5  # Start on bar 2
        for pitch in chord:
            note = pretty_midi.Note(velocity=90, pitch=pitch + 24, start=time, end=time + 0.375)
            piano.notes.append(note)

add_piano()

# Instrument: Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

def add_sax():
    # Melody: D - F# - A - C# - (space) - D - F# - A - C#
    # Bar 1: No sax
    # Bar 2 (1.5s): D -> F# -> A -> C#
    # Bar 3 (2.0s): D -> F# -> A -> C#
    # Bar 4 (2.5s): D -> F# -> A -> C#

    notes = [2, 4, 6, 8]
    for i, note in enumerate(notes):
        time = 1.5 + i * 0.375
        note_obj = pretty_midi.Note(velocity=100, pitch=note + 62, start=time, end=time + 0.375)
        sax.notes.append(note_obj)

    # Add a space — leave the last note hanging
    # D at 3.0s (bar 3, beat 1)
    note_obj = pretty_midi.Note(velocity=100, pitch=2 + 62, start=3.0, end=3.375)
    sax.notes.append(note_obj)

add_sax()

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write('jazz_intro_d_major.mid')
