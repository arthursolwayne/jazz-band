
import pretty_midi
from pretty_midi import Note, Instrument
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key for the piece (Fm)
key = 'Fm'

# Time per bar (1.5 seconds)
bar_length = 1.5
beat_length = 0.375  # 160 BPM = 60/160 = 0.375 sec per beat

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

bass = Instrument(program=bass_program, is_drum=False)
piano = Instrument(program=piano_program, is_drum=False)
sax = Instrument(program=sax_program, is_drum=False)
drums = Instrument(program=drum_program, is_drum=True)

pm.instruments = [bass, piano, sax, drums]

# Define the Fm scale (F, Gb, Ab, Bb, B, Db, Eb)
# But since we're in Fm, we'll use the F minor scale (F, Gb, Ab, Bb, B, Db, Eb)

# Define root
root = pretty_midi.note_number_from_name('F3')

# Drums: Bar 1 - kick on 1 and 3, snare on 2 and 4, hihat every 8th
def create_drums():
    # Bar 1
    kick_times = [0, 2*beat_length]
    snare_times = [1*beat_length, 3*beat_length]
    hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
    # Bar 2-4: Add variation with fills
    kick_times.extend([3*beat_length, 5*beat_length])
    snare_times.extend([4*beat_length, 6*beat_length])
    hihat_times.extend([3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625])
    kick_times.extend([6*beat_length, 8*beat_length])
    snare_times.extend([7*beat_length, 9*beat_length])
    hihat_times.extend([6.0, 6.375, 6.75, 7.125, 7.5, 7.875, 8.25, 8.625])

    # Assign drum notes
    kick = Note(36, 100, 0, beat_length)
    snare = Note(38, 100, 0, beat_length)
    hihat = Note(42, 100, 0, beat_length)

    for t in kick_times:
        kick.time = t
        kick.start = t
        kick.end = t + 0.05
        drums.notes.append(kick.copy())

    for t in snare_times:
        snare.time = t
        snare.start = t
        snare.end = t + 0.05
        drums.notes.append(snare.copy())

    for t in hihat_times:
        hihat.time = t
        hihat.start = t
        hihat.end = t + 0.03
        drums.notes.append(hihat.copy())

create_drums()

# Bass line - walking with chromatic approaches
def create_bass_line():
    # Bar 1 (1-4)
    notes = [
        # Root (F3)
        Note(root, 80, 0, beat_length),
        # Chromatic approach to Gb (F#)
        Note(root + 1, 70, 1*beat_length, 2*beat_length),
        # Gb (F#)
        Note(root + 1, 80, 2*beat_length, 3*beat_length),
        # Chromatic approach to Ab
        Note(root + 2, 70, 3*beat_length, 4*beat_length),
        # Ab
        Note(root + 2, 80, 4*beat_length, 5*beat_length),
        # Chromatic approach to Bb
        Note(root + 3, 70, 5*beat_length, 6*beat_length),
        # Bb
        Note(root + 3, 80, 6*beat_length, 7*beat_length),
        # Chromatic approach to B (A#)
        Note(root + 4, 70, 7*beat_length, 8*beat_length),
        # B
        Note(root + 4, 80, 8*beat_length, 9*beat_length),
        # Chromatic approach to Db (C#)
        Note(root + 5, 70, 9*beat_length, 10*beat_length),
        # Db
        Note(root + 5, 80, 10*beat_length, 11*beat_length),
        # Chromatic approach to Eb
        Note(root + 6, 70, 11*beat_length, 12*beat_length),
        # Eb
        Note(root + 6, 80, 12*beat_length, 13*beat_length),
    ]
    for note in notes:
        bass.notes.append(note)

create_bass_line()

# Piano - comping on 2 and 4 with seventh chords
def create_piano():
    # Bar 1: Start with F7 (F, A, C, E)
    F7 = [root, root + 3, root - 1, root + 1]
    for n in F7:
        Note(n, 90, 1*beat_length, 1.5)
    piano.notes.append(Note(root, 90, 1*beat_length, 1.5))
    piano.notes.append(Note(root + 3, 90, 1*beat_length, 1.5))
    piano.notes.append(Note(root - 1, 90, 1*beat_length, 1.5))
    piano.notes.append(Note(root + 1, 90, 1*beat_length, 1.5))

    # Bar 2: Bb7 (Bb, D, F, Ab)
    Bb7 = [root + 3, root + 6, root, root + 2]
    for n in Bb7:
        Note(n, 90, 3*beat_length, 3.5)
    piano.notes.append(Note(root + 3, 90, 3*beat_length, 3.5))
    piano.notes.append(Note(root + 6, 90, 3*beat_length, 3.5))
    piano.notes.append(Note(root, 90, 3*beat_length, 3.5))
    piano.notes.append(Note(root + 2, 90, 3*beat_length, 3.5))

    # Bar 3: Eb7 (Eb, G, Bb, Db)
    Eb7 = [root + 6, root + 1, root + 3, root + 5]
    for n in Eb7:
        Note(n, 90, 5*beat_length, 5.5)
    piano.notes.append(Note(root + 6, 90, 5*beat_length, 5.5))
    piano.notes.append(Note(root + 1, 90, 5*beat_length, 5.5))
    piano.notes.append(Note(root + 3, 90, 5*beat_length, 5.5))
    piano.notes.append(Note(root + 5, 90, 5*beat_length, 5.5))

    # Bar 4: Ab7 (Ab, C, Eb, Gb)
    Ab7 = [root + 2, root + 5, root + 6, root + 3]
    for n in Ab7:
        Note(n, 90, 7*beat_length, 7.5)
    piano.notes.append(Note(root + 2, 90, 7*beat_length, 7.5))
    piano.notes.append(Note(root + 5, 90, 7*beat_length, 7.5))
    piano.notes.append(Note(root + 6, 90, 7*beat_length, 7.5))
    piano.notes.append(Note(root + 3, 90, 7*beat_length, 7.5))

create_piano()

# Sax line - concise, emotional, leaving space
def create_sax_line():
    # Bar 1: Start with a motif, leave it hanging
    # F3 (root)
    sax.notes.append(Note(root, 100, 0, 0.75))
    # F#3 (chromatic approach)
    sax.notes.append(Note(root + 1, 100, 1.5, 2.25))
    # Bb3 (Fm7 root movement)
    sax.notes.append(Note(root + 3, 100, 3.0, 3.75))
    # F3 (ending back to root)
    sax.notes.append(Note(root, 100, 4.5, 5.25))

create_sax_line()

# Save the MIDI file
pm.write("dante_russo_intro.mid")
