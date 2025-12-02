
# Jazz Intro Generator - 4-Bar Composition in F Major at 160 BPM
# For Dante Russo and The Cellar, with Wayne Shorter in the back

import pretty_midi
from pretty_midi import Note, Instrument

# Constants
BPM = 160
BEATS_PER_BAR = 4
BARS = 4
TEMPO = BPM
TIME_SIGNATURE = (4, 4)
NOTE_DURATION = 0.375  # Seconds per beat
PITCHES = {
    'C': 60,
    'D': 62,
    'E': 64,
    'F': 65,
    'G': 67,
    'A': 69,
    'B': 71,
    'Bb': 66,
    'Ab': 68,
    'Db': 61,
    'Gb': 68,
    'Eb': 65,
    'F#': 66,
    'G#': 69,
    'A#': 71
}

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(*TIME_SIGNATURE, 0)]
midi.instruments = []

# Create instruments
bass = Instrument(program=33, is_drum=False, name='Bass')
piano = Instrument(program=0, is_drum=False, name='Piano')
sax = Instrument(program=64, is_drum=False, name='Saxophone')
drums = Instrument(program=0, is_drum=True, name='Drums')

# Add instruments to MIDI
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)
midi.instruments.append(drums)

# Bar 1: Drums only — build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(note, time, duration):
    note = Note(note, time, duration)
    drums.notes.append(note)

# Bar 1
time = 0.0
for beat in range(4):
    if beat == 0 or beat == 2:
        add_drums(pretty_midi.note_number_from_name('C3'), time, 0.375)  # Kick
    if beat == 1 or beat == 3:
        add_drums(pretty_midi.note_number_from_name('C5'), time, 0.375)  # Snare
    add_drums(pretty_midi.note_number_from_name('C6'), time, 0.1875)  # Hihat
    add_drums(pretty_midi.note_number_from_name('C6'), time + 0.1875, 0.1875)
    time += 0.375

# Bar 2: Everyone enters
# Bass: Walking line in F major, chromatic approaches
# Piano: 7th chords, comp on 2 and 4
# Sax: Melody — one clear motif, leave it hanging
# Drums: Same pattern, but with subtle variation on the 3rd beat

# Bass line (walking in F)
def add_bass(note, time, duration):
    note = Note(note, time, duration)
    bass.notes.append(note)

# Bass: F - G - A - Bb - C - D - Eb - F
bass_notes = [65, 67, 69, 68, 60, 62, 64, 65]
for i, note in enumerate(bass_notes):
    add_bass(note, i * 0.375, 0.375)

# Piano: 7th chords on 2 and 4
def add_piano(note, time, duration):
    note = Note(note, time, duration)
    piano.notes.append(note)

# F7 on beat 2, A7 on beat 4
add_piano(65, 0.75, 0.375)  # F
add_piano(67, 0.75, 0.375)  # A
add_piano(69, 0.75, 0.375)  # C
add_piano(68, 0.75, 0.375)  # Bb

add_piano(67, 1.5, 0.375)  # A
add_piano(69, 1.5, 0.375)  # C
add_piano(71, 1.5, 0.375)  # E
add_piano(68, 1.5, 0.375)  # G

# Sax: Melody — one motif, leave it hanging
def add_sax(note, time, duration):
    note = Note(note, time, duration)
    sax.notes.append(note)

# Motif: F - G - A - Eb (sings, then hangs on the Eb)
add_sax(65, 0.0, 0.375)
add_sax(67, 0.375, 0.375)
add_sax(69, 0.75, 0.375)
add_sax(64, 1.125, 0.375)  # Hang on the Eb

# Bar 3: Repeat the motif with slight variation (maybe a grace note)
add_sax(65, 1.5, 0.1875)  # Grace note
add_sax(65, 1.6875, 0.375)
add_sax(69, 2.0625, 0.375)
add_sax(64, 2.4375, 0.375)

# Bar 4: End with a rest, open-ended
# Sax: No note, let the idea linger
# Drums: Same pattern, but with a subtle fill on the last beat

# Drums — Bar 3 & 4
for beat in range(4):
    time = 1.5 + beat * 0.375
    if beat == 0 or beat == 2:
        add_drums(pretty_midi.note_number_from_name('C3'), time, 0.375)  # Kick
    if beat == 1 or beat == 3:
        add_drums(pretty_midi.note_number_from_name('C5'), time, 0.375)  # Snare
    add_drums(pretty_midi.note_number_from_name('C6'), time, 0.1875)  # Hihat
    add_drums(pretty_midi.note_number_from_name('C6'), time + 0.1875, 0.1875)
    if beat == 3:
        add_drums(pretty_midi.note_number_from_name('F4'), time, 0.375)  # Fill

# Save the file
midi.write("dante_intro.mid")

print("Intro composed and saved as 'dante_intro.mid'")
print("It's the kind of intro that makes Wayne Shorter lean forward.")
print("Now go play it. Make it sing.")
