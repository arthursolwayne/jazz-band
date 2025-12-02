
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key and time signature
key = 'F major'
time_signature = (4, 4)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Constants
BEAT = 1.5  # 6 seconds for 4 bars at 160 BPM
BAR_DURATION = 1.5
NOTE_DURATION = 0.375  # One beat = 0.375s at 160 BPM
REST = 0.0

# Define the notes in F major
F_MAJOR = [65, 67, 69, 71, 72, 74, 76]  # F, G, A, Bb, B, C, D

# Drum pattern
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def create_drums():
    bar = 0
    for beat in [0, 1, 2, 3]:
        time = beat * NOTE_DURATION
        if beat == 0 or beat == 2:  # Kick
            note = pretty_midi.Note(velocity=100, pitch=35, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        if beat == 1 or beat == 3:  # Snare
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + NOTE_DURATION)
            drums.notes.append(note)
        for eighth in [0, 1]:
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * NOTE_DURATION / 2,
                                    end=time + eighth * NOTE_DURATION / 2 + NOTE_DURATION / 2)
            drums.notes.append(note)

# Bass line: walking line, chromatic approaches
def create_bass():
    # Bar 1: chromatic approach to F
    notes = [64, 65, 69, 67, 65]  # C#, F, A, G, F
    for i, pitch in enumerate(notes):
        time = i * NOTE_DURATION
        note = pretty_midi.Note(velocity=60, pitch=pitch, start=time, end=time + NOTE_DURATION)
        bass.notes.append(note)

    # Bar 2: F, G, A, Bb
    notes = [65, 67, 69, 71]
    for i, pitch in enumerate(notes):
        time = i * NOTE_DURATION + BAR_DURATION
        note = pretty_midi.Note(velocity=60, pitch=pitch, start=time, end=time + NOTE_DURATION)
        bass.notes.append(note)

    # Bar 3: Bb, B, C, D
    notes = [71, 72, 74, 76]
    for i, pitch in enumerate(notes):
        time = i * NOTE_DURATION + 2 * BAR_DURATION
        note = pretty_midi.Note(velocity=60, pitch=pitch, start=time, end=time + NOTE_DURATION)
        bass.notes.append(note)

    # Bar 4: F, G, A, Bb
    notes = [65, 67, 69, 71]
    for i, pitch in enumerate(notes):
        time = i * NOTE_DURATION + 3 * BAR_DURATION
        note = pretty_midi.Note(velocity=60, pitch=pitch, start=time, end=time + NOTE_DURATION)
        bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
def create_piano():
    # Bar 1: Rest
    pass

    # Bar 2: F7 on beat 2
    chord_notes = [65, 67, 69, 72]
    time = 1 * NOTE_DURATION + BAR_DURATION
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + NOTE_DURATION)
        piano.notes.append(note)

    # Bar 3: G7 on beat 2
    chord_notes = [67, 69, 71, 74]
    time = 1 * NOTE_DURATION + 2 * BAR_DURATION
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + NOTE_DURATION)
        piano.notes.append(note)

    # Bar 4: A7 on beat 2
    chord_notes = [69, 71, 72, 76]
    time = 1 * NOTE_DURATION + 3 * BAR_DURATION
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + NOTE_DURATION)
        piano.notes.append(note)

# Sax: sparse, expressive motif
def create_sax():
    # Bar 1: Rest
    pass

    # Bar 2: Start the motif
    note = pretty_midi.Note(velocity=100, pitch=69, start=0 * NOTE_DURATION + BAR_DURATION,
                            end=0 * NOTE_DURATION + BAR_DURATION + NOTE_DURATION)
    sax.notes.append(note)

    # Bar 3: Continue the motif
    note = pretty_midi.Note(velocity=100, pitch=71, start=1 * NOTE_DURATION + BAR_DURATION,
                            end=1 * NOTE_DURATION + BAR_DURATION + NOTE_DURATION)
    sax.notes.append(note)

    # Bar 4: Finish the motif
    note = pretty_midi.Note(velocity=100, pitch=69, start=2 * NOTE_DURATION + BAR_DURATION,
                            end=2 * NOTE_DURATION + BAR_DURATION + NOTE_DURATION)
    sax.notes.append(note)

# Generate the MIDI content
create_drums()
create_bass()
create_piano()
create_sax()

# Save the MIDI file
midi.write('jazz_intro.mid')
print("MIDI file created: jazz_intro.mid")
