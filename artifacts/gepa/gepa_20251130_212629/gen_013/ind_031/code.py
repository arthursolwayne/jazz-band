
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the tempo (BPM) and time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Define the key (D major)
key = 'D'

# Define the instruments
bass_program = Program(instrument=33)  # Electric Bass
piano_program = Program(instrument=0)  # Acoustic Piano
drums_program = Program(instrument=10) # Acoustic Drum Set
sax_program = Program(instrument=62)   # Tenor Saxophone

# Create instrument tracks
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define the note durations (in seconds)
beat = 0.375  # 160 BPM = 60/160 = 0.375 seconds per beat
bar = beat * 4
quarter = beat
eighth = beat / 2
sixteenth = beat / 4

# BAR 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (Note(name='C2', start=0, end=beat, velocity=100)),  # Kick on beat 1
    (Note(name='C2', start=beat * 2, end=beat * 3, velocity=100)),  # Kick on beat 3
    (Note(name='F2', start=beat, end=beat * 2, velocity=90)),  # Snare on beat 2
    (Note(name='F2', start=beat * 3, end=beat * 4, velocity=90)),  # Snare on beat 4
    (Note(name='B1', start=0, end=bar, velocity=60, note_type='hihat')),  # Hihat on every eighth
]

for note in drum_notes:
    if 'hihat' in note.name:
        note.pitch = 48  # Hihat pitch (typically around middle C)
    else:
        note.pitch = pretty_midi.note_name_to_number(note.name)
    note = Note(note.pitch, note.start, note.end, note.velocity)
    drums.notes.append(note)

# BAR 2-4: Full ensemble
# Time starts at bar = 1.5 seconds

# Bass line (chromatic walking line, no repeated notes)
bass_line = [
    'D2', 'Eb2', 'F2', 'Gb2',  # Bar 2
    'G2', 'Ab2', 'A2', 'Bb2',  # Bar 3
    'B2', 'C3', 'Db3', 'D3'    # Bar 4
]

for note_name in bass_line:
    note = Note(pretty_midi.note_name_to_number(note_name), 
                start=bar + (bass_line.index(note_name) * beat),
                end=bar + (bass_line.index(note_name) + 1) * beat,
                velocity=80)
    bass.notes.append(note)

# Piano (7th chords, comp on 2 and 4)
piano_notes = []

# Bar 2: C7 (D is the key, but C7 is a ii chord) on beat 2
piano_notes.append(Note(pretty_midi.note_name_to_number('C4'), bar + beat, bar + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('E4'), bar + beat, bar + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('G4'), bar + beat, bar + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('B4'), bar + beat, bar + beat + eighth, velocity=90))

# Bar 3: G7 (V chord) on beat 2
piano_notes.append(Note(pretty_midi.note_name_to_number('G4'), bar * 2 + beat, bar * 2 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('B4'), bar * 2 + beat, bar * 2 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('D5'), bar * 2 + beat, bar * 2 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('F5'), bar * 2 + beat, bar * 2 + beat + eighth, velocity=90))

# Bar 4: D7 (I chord) on beat 2
piano_notes.append(Note(pretty_midi.note_name_to_number('D4'), bar * 3 + beat, bar * 3 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('F4'), bar * 3 + beat, bar * 3 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('A4'), bar * 3 + beat, bar * 3 + beat + eighth, velocity=90))
piano_notes.append(Note(pretty_midi.note_name_to_number('C5'), bar * 3 + beat, bar * 3 + beat + eighth, velocity=90))

for note in piano_notes:
    piano.notes.append(note)

# Drums continue in bars 2-4 with same pattern
drum_notes = [
    (Note(name='C2', start=bar, end=bar + beat, velocity=100)),  # Kick on beat 1
    (Note(name='C2', start=bar + beat * 2, end=bar + beat * 3, velocity=100)),  # Kick on beat 3
    (Note(name='F2', start=bar + beat, end=bar + beat * 2, velocity=90)),  # Snare on beat 2
    (Note(name='F2', start=bar + beat * 3, end=bar + beat * 4, velocity=90)),  # Snare on beat 4
    (Note(name='B1', start=bar, end=bar * 2, velocity=60, note_type='hihat')),  # Hihat on every eighth
    (Note(name='B1', start=bar * 2, end=bar * 3, velocity=60, note_type='hihat')),  # Hihat on every eighth
    (Note(name='B1', start=bar * 3, end=bar * 4, velocity=60, note_type='hihat')),  # Hihat on every eighth
]

for note in drum_notes:
    if 'hihat' in note.name:
        note.pitch = 48  # Hihat pitch (typically around middle C)
    else:
        note.pitch = pretty_midi.note_name_to_number(note.name)
    note = Note(note.pitch, note.start, note.end, note.velocity)
    drums.notes.append(note)

# Saxophone: Four-bar motif
# Start with a short motif, leave it hanging, come back and finish it
# D (D4), F# (F#4), A (A4), then leave it hanging on G#
sax_notes = [
    Note(pretty_midi.note_name_to_number('D4'), bar, bar + eighth, velocity=100),
    Note(pretty_midi.note_name_to_number('F#4'), bar + eighth, bar + quarter, velocity=100),
    Note(pretty_midi.note_name_to_number('A4'), bar + quarter, bar + quarter + eighth, velocity=100),
    Note(pretty_midi.note_name_to_number('G#4'), bar + quarter + eighth, bar + quarter + sixteenth * 2, velocity=80),
    # Re-enter on beat 3
    Note(pretty_midi.note_name_to_number('D4'), bar + beat * 2, bar + beat * 2 + eighth, velocity=100),
    Note(pretty_midi.note_name_to_number('F#4'), bar + beat * 2 + eighth, bar + beat * 2 + quarter, velocity=100),
    Note(pretty_midi.note_name_to_number('A4'), bar + beat * 2 + quarter, bar + beat * 2 + quarter + eighth, velocity=100),
    Note(pretty_midi.note_name_to_number('G#4'), bar + beat * 2 + quarter + eighth, bar + beat * 2 + quarter + sixteenth * 2, velocity=80),
    # End with resolution on D
    Note(pretty_midi.note_name_to_number('D4'), bar + beat * 3 + eighth, bar + beat * 3 + quarter, velocity=100),
    Note(pretty_midi.note_name_to_number('F#4'), bar + beat * 3 + quarter, bar + beat * 3 + quarter + eighth, velocity=100),
    Note(pretty_midi.note_name_to_number('A4'), bar + beat * 3 + quarter + eighth, bar + beat * 3 + quarter + sixteenth * 2, velocity=100),
]

for note in sax_notes:
    sax.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file 'dante_russo_intro.mid' has been created.")
