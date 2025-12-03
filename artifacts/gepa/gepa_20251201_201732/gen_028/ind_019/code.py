
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define key: F minor
key = 'F minor'

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create tracks
bass_track = pretty_midi.Instrument(program=bass_program)
piano_track = pretty_midi.Instrument(program=piano_program)
drums_track = pretty_midi.Instrument(program=drums_program)
sax_track = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass_track, piano_track, drums_track, sax_track]

# Constants
BPM = 160
BPM_TO_SECONDS = 60.0 / BPM
BEAT_DURATION = BPM_TO_SECONDS
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
NOTE_DURATION = BEAT_DURATION / 4  # quarter note

# Function to create a note event
def note_on(note_number, time, duration, velocity=100):
    return pretty_midi.Note(velocity, note_number, time, time + duration)

# Function to create a rest
def rest(time, duration):
    return pretty_midi.Note(0, 0, time, time + duration)

# Drums: Bar 1 only, kick on 1&3, snare on 2&4, hihat every eighth
drum_notes = {
    'kick': [0, 2, 3, 5],  # kick on 1,3
    'snare': [1, 3, 4, 6],  # snare on 2,4
    'hihat': list(range(0, 8)),  # every eighth
}

# Bar 1 - Drums
for note in drum_notes['hihat']:
    time = (note * NOTE_DURATION)
    drums_track.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + NOTE_DURATION))
for note in drum_notes['kick']:
    time = (note * NOTE_DURATION)
    drums_track.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + NOTE_DURATION))
for note in drum_notes['snare']:
    time = (note * NOTE_DURATION)
    drums_track.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + NOTE_DURATION))

# Bar 2-4 - Everyone in

# Bass: Walking line in F minor (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# Bar 2: Fm -> Bb -> Ab -> D
bass_notes = [
    (38, 0),  # F2
    (42, 1),  # Ab2
    (43, 2),  # Bb2
    (40, 3),  # D2
    (41, 4),  # Eb2 (chromatic approach)
    (38, 5),  # F2
    (42, 6),  # Ab2
    (43, 7),  # Bb2
    (40, 8),  # D2
    (41, 9),  # Eb2
    (38, 10), # F2
    (42, 11), # Ab2
    (43, 12), # Bb2
    (40, 13), # D2
    (41, 14), # Eb2
    (38, 15), # F2
]

for note_num, time in zip(bass_notes, np.arange(0, BAR_DURATION * 3, NOTE_DURATION)):
    bass_track.notes.append(note_on(note_num, time, NOTE_DURATION, velocity=70))

# Piano: Open voicings, resolve on the last chord of each bar
# Bar 2: Fm7 (F A C Eb)
piano_notes = [
    (53, 0), # F4
    (60, 0), # A4
    (64, 0), # C5
    (62, 0), # Eb5
]
for note in piano_notes:
    piano_track.notes.append(note_on(note[0], note[1], BAR_DURATION, velocity=90))

# Bar 3: Bb7 (Bb D F A)
piano_notes = [
    (57, BAR_DURATION), # Bb4
    (62, BAR_DURATION), # D5
    (64, BAR_DURATION), # F5
    (69, BAR_DURATION), # A5
]
for note in piano_notes:
    piano_track.notes.append(note_on(note[0], note[1], BAR_DURATION, velocity=90))

# Bar 4: Ab7 (Ab C Eb G)
piano_notes = [
    (54, 2*BAR_DURATION), # Ab4
    (64, 2*BAR_DURATION), # C5
    (62, 2*BAR_DURATION), # Eb5
    (67, 2*BAR_DURATION), # G5
]
for note in piano_notes:
    piano_track.notes.append(note_on(note[0], note[1], BAR_DURATION, velocity=90))

# Sax: Melody - a short motif, singable, with rests, unique
# Start on G (G4, 71)
sax_notes = [
    (71, 0), # G4
    (69, 1), # F4
    (67, 2), # Eb4 (rest for 1 beat)
    (71, 3), # G4
    (72, 4), # A4
    (69, 5), # F4
    (67, 6), # Eb4
    (69, 7), # F4
    (71, 8), # G4
    (69, 9), # F4
    (67, 10), # Eb4
    (69, 11), # F4
    (71, 12), # G4
    (72, 13), # A4
    (69, 14), # F4
    (67, 15), # Eb4
]

for note_num, time in sax_notes:
    sax_track.notes.append(note_on(note_num, time, NOTE_DURATION, velocity=100))

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
