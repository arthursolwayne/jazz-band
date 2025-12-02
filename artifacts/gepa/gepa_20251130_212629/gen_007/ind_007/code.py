
import pretty_midi
from pretty_midi import Note, NoteContainer, Instrument

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: D major (key number is 2)
key = 'D'

# Set the tempo to 160 BPM
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)  # Acoustic Piano
drums_instrument = Instrument(program=0)  # Drums
sax_instrument = Instrument(program=64)  # Tenor Saxophone

# Add instruments to the PrettyMIDI object
pm.instruments = [bass_instrument, piano_instrument, drums_instrument, sax_instrument]

# Define bar length in seconds (160 BPM, 4/4 time => each beat = 0.375s, bar = 1.5s)
bar_length = 1.5

# Define time in seconds for each bar
bar_times = [0, 1.5, 3.0, 4.5, 6.0]

# Drum pattern: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Drums only
drum_notes = [
    Note(60, 0.0, 0.375),  # Kick on beat 1
    Note(62, 0.75, 0.375), # Snare on beat 2
    Note(60, 1.125, 0.375), # Kick on beat 3
    Note(62, 1.875, 0.375), # Snare on beat 4
]

# Add hi-hats (every eighth note)
for i in range(8):
    Note(42, i * 0.375, 0.125)

# Create NoteContainer for drums
drum_notes_container = NoteContainer(drum_notes)
drums_instrument.notes = drum_notes_container

# Bar 2-4: All instruments enter
# Define the saxophone motif (start of the melody)
sax_notes = [
    Note(62, 1.5, 0.375),  # D4 (start of melody)
    Note(64, 1.875, 0.375), # E4
    Note(67, 2.25, 0.375), # G4
    Note(65, 2.625, 0.375), # F#4
    Note(62, 3.0, 0.375),  # D4 (return)
    Note(64, 3.375, 0.375), # E4
    Note(67, 3.75, 0.375), # G4
    Note(65, 4.125, 0.375), # F#4
]

# Create NoteContainer for saxophone
sax_notes_container = NoteContainer(sax_notes)
sax_instrument.notes = sax_notes_container

# Bass line: Walking line in D major
# Chromatic approaches, no repeated notes, anchor the rhythm
bass_notes = [
    Note(45, 1.5, 0.375),  # D3
    Note(46, 1.875, 0.375), # E3
    Note(47, 2.25, 0.375), # F#3
    Note(49, 2.625, 0.375), # A3
    Note(48, 3.0, 0.375),  # G3
    Note(47, 3.375, 0.375), # F#3
    Note(45, 3.75, 0.375), # D3
    Note(43, 4.125, 0.375), # B2 (chromatic approach)
]

# Create NoteContainer for bass
bass_notes_container = NoteContainer(bass_notes)
bass_instrument.notes = bass_notes_container

# Piano: 7th chords on 2 and 4, comping
# D7 (2nd beat of bar 2), G7 (2nd beat of bar 3), C7 (2nd beat of bar 4)
piano_notes = [
    # Bar 2, beat 2: D7 = D, F#, A, C
    Note(62, 1.875, 0.125), # D4
    Note(67, 1.875, 0.125), # A4
    Note(64, 1.875, 0.125), # E4
    Note(69, 1.875, 0.125), # C5

    # Bar 3, beat 2: G7 = G, B, D, F#
    Note(67, 3.375, 0.125), # G4
    Note(71, 3.375, 0.125), # B4
    Note(69, 3.375, 0.125), # C5
    Note(72, 3.375, 0.125), # D5

    # Bar 4, beat 2: C7 = C, E, G, B
    Note(60, 4.875, 0.125), # C4
    Note(64, 4.875, 0.125), # E4
    Note(67, 4.875, 0.125), # G4
    Note(69, 4.875, 0.125), # B4
]

# Create NoteContainer for piano
piano_notes_container = NoteContainer(piano_notes)
piano_instrument.notes = piano_notes_container

# Add hi-hats in bars 2-4 too
for i in range(8):
    if i * 0.375 >= 1.5:
        Note(42, i * 0.375, 0.125)

# Write the MIDI file
pm.write("jazz_intro.mid")

print("MIDI file 'jazz_intro.mid' has been created.")
