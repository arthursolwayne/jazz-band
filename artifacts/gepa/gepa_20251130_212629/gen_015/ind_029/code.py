
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
track = pretty_midi.Instrument(program=64)  # Tenor sax (program 64)
pm.instruments.append(track)

# Definitions
F = 69  # MIDI note number for F4
bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat (160 BPM)
quarter = beat_length
eighth = beat_length / 2
sixteenth = beat_length / 4

# Create a list to store notes for each instrument
notes = {
    'tenor': [],
    'bass': [],
    'piano': [],
    'drums': []
}

# Bar 1: Little Ray on drums (snare and hihat only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_drums = [
    # Kick on 1 and 3
    (36, 0.0),  # Kick on beat 1
    (36, 1.125),  # Kick on beat 3
    # Snare on 2 and 4
    (38, 0.375),  # Snare on beat 2
    (38, 1.5),    # Snare on beat 4
    # Hihat on every eighth
    (42, 0.0), (42, 0.1875), (42, 0.375), (42, 0.5625),
    (42, 0.75), (42, 0.9375), (42, 1.125), (42, 1.3125)
]
for note, time in bar1_drums:
    notes['drums'].append(Note(note, time, duration=0.125))

# Bar 2: Everyone in
# Tenor sax
# Start with a short motif: F (69), D (62), Bb (60), rest
# Then come back with F, Bb, F, rest — leave it hanging
tenor_notes = [
    Note(F, 0.0, duration=0.375),  # F4 on beat 1
    Note(62, 0.375, duration=0.25),  # D4 on beat 2
    Note(60, 0.625, duration=0.25),  # Bb4 on beat 3
    Note(F, 0.875, duration=0.125),  # F4 on beat 3.5
    Note(60, 1.0, duration=0.25),  # Bb4 on beat 4
    Note(F, 1.25, duration=0.125),  # F4 on beat 4.5
    Note(60, 1.375, duration=0.125),  # Bb4 on beat 4.75
]
for note in tenor_notes:
    notes['tenor'].append(note)

# Bass: Walking line, chromatic, no repeated notes
# F (69), Gb (68), G (67), Ab (66), A (65), Bb (64), B (63), C (60)
# Then repeat starting from Gb (68)
bass_notes = [
    Note(69, 0.0, duration=0.25),  # F4 on beat 1
    Note(68, 0.25, duration=0.25),  # Gb4 on beat 2
    Note(67, 0.5, duration=0.25),  # G4 on beat 3
    Note(66, 0.75, duration=0.25),  # Ab4 on beat 4
    Note(65, 1.0, duration=0.25),  # A4 on beat 5 (next bar)
    Note(64, 1.25, duration=0.25),  # Bb4 on beat 6
    Note(63, 1.5, duration=0.25),  # B4 on beat 7
    Note(60, 1.75, duration=0.25),  # C4 on beat 8 (end of bar 2)
]
for note in bass_notes:
    notes['bass'].append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 (F, A, C, Eb) on beat 2 and 4
piano_notes = [
    Note(69, 0.375, duration=0.25),  # F4 on beat 2
    Note(64, 0.375, duration=0.25),  # A4 on beat 2
    Note(60, 0.375, duration=0.25),  # C4 on beat 2
    Note(62, 0.375, duration=0.25),  # Eb4 on beat 2
    Note(69, 1.5, duration=0.25),  # F4 on beat 4
    Note(64, 1.5, duration=0.25),  # A4 on beat 4
    Note(60, 1.5, duration=0.25),  # C4 on beat 4
    Note(62, 1.5, duration=0.25),  # Eb4 on beat 4
]
for note in piano_notes:
    notes['piano'].append(note)

# Add notes to instruments
for note in notes['tenor']:
    track.notes.append(note)

# Create bass instrument
bass = Instrument(program=33)
for note in notes['bass']:
    bass.notes.append(note)
pm.instruments.append(bass)

# Create piano instrument
piano = Instrument(program=0)
for note in notes['piano']:
    piano.notes.append(note)
pm.instruments.append(piano)

# Create drum instrument
drums = Instrument(program=10)
for note in notes['drums']:
    drums.notes.append(note)
pm.instruments.append(drums)

# Save the MIDI file
pm.write("dante_intro.mid")
