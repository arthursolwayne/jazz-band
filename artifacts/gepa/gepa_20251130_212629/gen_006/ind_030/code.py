
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Create instruments
bass_instrument = Instrument(program=33, is_drum=False)
piano_instrument = Instrument(program=0, is_drum=False)
tenor_sax_instrument = Instrument(program=64, is_drum=False)
drums_instrument = Instrument(program=0, is_drum=True)

pm.instruments = [bass_instrument, piano_instrument, tenor_sax_instrument, drums_instrument]

# Define timing
BPM = 160
beat = 60.0 / BPM  # seconds per beat
bar = beat * 4  # seconds per bar
note_duration = beat / 4  # quarter note duration

# Function to create a note
def create_note(note_number, start_time, duration):
    note = Note(velocity=100, pitch=note_number, start=start_time, end=start_time + duration)
    return note

# BAR 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on beat 1 and 3
drums_instrument.notes.append(create_note(36, 0.0, note_duration))  # Kick on beat 1
drums_instrument.notes.append(create_note(36, 2.0, note_duration))  # Kick on beat 3

# Snare on beat 2 and 4
drums_instrument.notes.append(create_note(38, 1.0, note_duration))  # Snare on beat 2
drums_instrument.notes.append(create_note(38, 3.0, note_duration))  # Snare on beat 4

# Hi-hats on every eighth
for i in range(0, 4):
    drums_instrument.notes.append(create_note(42, i * beat / 2, note_duration / 2))

# BAR 2: Everyone in

# Tenor sax: short motif (F - Bb - F - Eb) over 4 notes (quarter note each)
tenor_notes = [
    create_note(65, 4.0, note_duration),  # F
    create_note(67, 5.0, note_duration),  # Bb
    create_note(65, 6.0, note_duration),  # F
    create_note(62, 7.0, note_duration)   # Eb
]
tenor_sax_instrument.notes.extend(tenor_notes)

# Bass line (chromatic walking line, F -> Gb -> G -> Ab -> A -> Bb -> B -> C)
bass_notes = [
    create_note(64, 4.0, note_duration),  # F
    create_note(65, 5.0, note_duration),  # Gb
    create_note(66, 6.0, note_duration),  # G
    create_note(67, 7.0, note_duration)   # Ab
]
bass_instrument.notes.extend(bass_notes)

# Piano (7th chords, comp on 2 and 4)
# Bar starts at 4.0, chords on beat 2 and 4

# F7 (F, A, C, Eb) on beat 2 (5.0)
piano_notes = [
    create_note(65, 5.0, note_duration),  # F
    create_note(68, 5.0, note_duration),  # A
    create_note(69, 5.0, note_duration),  # Bb
    create_note(62, 5.0, note_duration),  # Eb
]

# Bb7 (Bb, D, F, Ab) on beat 4 (7.0)
piano_notes += [
    create_note(62, 7.0, note_duration),  # Bb
    create_note(65, 7.0, note_duration),  # D
    create_note(67, 7.0, note_duration),  # F
    create_note(69, 7.0, note_duration)   # Ab
]

piano_instrument.notes.extend(piano_notes)

# BAR 3: Tenor sax continues the motif, but ends on Bb
tenor_notes = [
    create_note(67, 8.0, note_duration),  # Bb
]
tenor_sax_instrument.notes.extend(tenor_notes)

# Bass line continues (A - Bb - B - C)
bass_notes = [
    create_note(69, 8.0, note_duration),  # A
    create_note(70, 9.0, note_duration),  # Bb
    create_note(71, 10.0, note_duration), # B
    create_note(72, 11.0, note_duration)  # C
]
bass_instrument.notes.extend(bass_notes)

# Piano (7th chords, comp on 2 and 4)

# F7 on beat 2 (9.0)
piano_notes = [
    create_note(65, 9.0, note_duration),  # F
    create_note(68, 9.0, note_duration),  # A
    create_note(69, 9.0, note_duration),  # Bb
    create_note(62, 9.0, note_duration),  # Eb
]

# Bb7 on beat 4 (11.0)
piano_notes += [
    create_note(62, 11.0, note_duration),  # Bb
    create_note(65, 11.0, note_duration),  # D
    create_note(67, 11.0, note_duration),  # F
    create_note(69, 11.0, note_duration)   # Ab
]

piano_instrument.notes.extend(piano_notes)

# BAR 4: Tenor sax resolves with a twist

# Tenor sax: Bb -> F -> D -> G (unexpected resolution)
tenor_notes = [
    create_note(67, 12.0, note_duration),  # Bb
    create_note(65, 13.0, note_duration),  # F
    create_note(62, 14.0, note_duration),  # D
    create_note(67, 15.0, note_duration)   # G
]
tenor_sax_instrument.notes.extend(tenor_notes)

# Bass line: C -> D -> Eb -> F
bass_notes = [
    create_note(72, 12.0, note_duration),  # C
    create_note(73, 13.0, note_duration),  # D
    create_note(74, 14.0, note_duration),  # Eb
    create_note(76, 15.0, note_duration)   # F
]
bass_instrument.notes.extend(bass_notes)

# Piano: F7 on beat 2 (13.0), C7 on beat 4 (15.0)
piano_notes = [
    create_note(65, 13.0, note_duration),  # F
    create_note(68, 13.0, note_duration),  # A
    create_note(69, 13.0, note_duration),  # Bb
    create_note(62, 13.0, note_duration),  # Eb
]

piano_notes += [
    create_note(72, 15.0, note_duration),  # C
    create_note(76, 15.0, note_duration),  # E
    create_note(77, 15.0, note_duration),  # G
    create_note(79, 15.0, note_duration)   # B
]

piano_instrument.notes.extend(piano_notes)

# Bar 4 Drums: Same as bar 1
# Kick on 1 and 3
drums_instrument.notes.append(create_note(36, 12.0, note_duration))  # Kick on beat 1 (bar 4)
drums_instrument.notes.append(create_note(36, 14.0, note_duration))  # Kick on beat 3

# Snare on beat 2 and 4
drums_instrument.notes.append(create_note(38, 13.0, note_duration))  # Snare on beat 2
drums_instrument.notes.append(create_note(38, 15.0, note_duration))  # Snare on beat 4

# Hi-hats on every eighth
for i in range(0, 4):
    drums_instrument.notes.append(create_note(42, 12.0 + i * beat / 2, note_duration / 2))

# Save the MIDI file
pm.write('jazz_intro.mid')
