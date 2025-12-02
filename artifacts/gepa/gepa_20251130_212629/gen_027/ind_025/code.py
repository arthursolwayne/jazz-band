
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set the tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# --- INSTRUMENTS ---
# Create the instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)    # Bass
piano = pretty_midi.Instrument(program=0)   # Piano
sax = pretty_midi.Instrument(program=64)    # Tenor Sax

pm.instruments = [drums, bass, piano, sax]

# --- BAR 1: DRUMS (LITTLE RAY) ---
# Bar 1: 6 seconds, 4/4 time, 160 BPM => 4 beats per bar = 1.5 seconds per beat

# Beat = 0.375 seconds
beat = 0.375

# Bar 1: Drums only — space, tension, subtle syncopation
# Kick on 1 and 3, snare on 2 and 4, but leave some space

drum_notes = [
    (pretty_midi.note_number_to_name(36), beat * 0.0),  # Kick on beat 1
    (pretty_midi.note_number_to_name(38), beat * 1.0),  # Snare on beat 2
    (pretty_midi.note_number_to_name(36), beat * 2.0),  # Kick on beat 3
    (pretty_midi.note_number_to_name(38), beat * 3.0),  # Snare on beat 4
]

# Add a fill in the middle of the bar to add tension
drum_notes.append((pretty_midi.note_number_to_name(40), beat * 1.5))  # Hi-hat or splash

# Add notes to the drum instrument
for note_name, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.2)
    drums.notes.append(note)

# --- BAR 2–4: BASS, PIANO, SAX ---
# Start at 1.5 seconds (end of bar 1)

# --- BASS LINE (Marcus) ---
# F major key: F, Gm7, Am7, D7
# Walking line with chromatic approaches

bass_notes = [
    # Bar 2 (F7)
    (pretty_midi.note_number_to_name(71), 1.5),  # F
    (pretty_midi.note_number_to_name(70), 1.75),  # E (chromatic approach)
    (pretty_midi.note_number_to_name(71), 2.0),   # F
    (pretty_midi.note_number_to_name(72), 2.25),  # G

    # Bar 3 (Gm7)
    (pretty_midi.note_number_to_name(72), 2.5),   # G
    (pretty_midi.note_number_to_name(71), 2.75),  # F
    (pretty_midi.note_number_to_name(70), 3.0),   # E
    (pretty_midi.note_number_to_name(69), 3.25),  # D

    # Bar 4 (Am7)
    (pretty_midi.note_number_to_name(69), 3.5),   # A
    (pretty_midi.note_number_to_name(70), 3.75),  # Bb
    (pretty_midi.note_number_to_name(69), 4.0),   # A
    (pretty_midi.note_number_to_name(71), 4.25),  # B
]

# Add the bass notes
for note_name, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.25)
    bass.notes.append(note)

# --- PIANO LINE (Diane) ---
# Comp on 2 and 4

piano_notes = [
    # Bar 2 (F7)
    (pretty_midi.note_number_to_name(71), 1.75),  # F7 chord: F, A, C, E
    (pretty_midi.note_number_to_name(74), 1.75),
    (pretty_midi.note_number_to_name(76), 1.75),
    (pretty_midi.note_number_to_name(78), 1.75),

    # Bar 3 (Gm7)
    (pretty_midi.note_number_to_name(72), 2.75),  # Gm7: G, Bb, D, F
    (pretty_midi.note_number_to_name(71), 2.75),
    (pretty_midi.note_number_to_name(69), 2.75),
    (pretty_midi.note_number_to_name(72), 2.75),

    # Bar 4 (Am7)
    (pretty_midi.note_number_to_name(69), 3.75),  # Am7: A, C, E, G
    (pretty_midi.note_number_to_name(71), 3.75),
    (pretty_midi.note_number_to_name(74), 3.75),
    (pretty_midi.note_number_to_name(76), 3.75),
]

# Add piano notes
for note_name, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.1)
    piano.notes.append(note)

# --- SAX LINE (You, Dante) ---
# Short motif — ends in a question

dante_notes = [
    # Bar 2 (F)
    (pretty_midi.note_number_to_name(71), 1.5),    # F
    (pretty_midi.note_number_to_name(72), 1.75),   # G
    (pretty_midi.note_number_to_name(71), 2.0),    # F

    # Bar 3 (G)
    (pretty_midi.note_number_to_name(72), 2.5),    # G
    (pretty_midi.note_number_to_name(74), 2.75),   # A
    (pretty_midi.note_number_to_name(72), 3.0),    # G

    # Bar 4 (A)
    (pretty_midi.note_number_to_name(69), 3.5),    # A
    (pretty_midi.note_number_to_name(71), 3.75),   # B
    (pretty_midi.note_number_to_name(69), 4.0)     # A
]

# Add sax notes
for note_name, time in dante_notes:
    note = pretty_midi.Note(velocity=100, pitch=pretty_midi.note_name_to_number(note_name), start=time, end=time + 0.25)
    sax.notes.append(note)

# --- SAVE THE MIDI FILE ---
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
