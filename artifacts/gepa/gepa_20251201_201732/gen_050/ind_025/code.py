
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key signature (F minor)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F minor is key number 5

# Define the time per bar (in seconds)
bar_duration = 1.5  # 160 BPM => 60/160 = 0.375 per beat, 4 beats per bar = 1.5s

# Function to add a note
def add_note(instrument, pitch, start, duration, velocity=100):
    note = pretty_midi.Note(velocity, pitch, start, start + duration)
    instrument.notes.append(note)

# Create instruments
bass_program = pretty_midi.programs.Program(33)  # Electric Bass
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

piano_program = pretty_midi.programs.Program(0)  # Acoustic Piano
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

drums_program = pretty_midi.programs.Program(9)  # Acoustic Drums
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

sax_program = pretty_midi.programs.Program(62)  # Alto Sax (Tenor is similar)
sax = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax)

# BAR 1: Little Ray on drums — just a breath, a heartbeat
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = {
    'kick': [0, 2],  # Beats 1 and 3
    'snare': [1, 3],  # Beats 2 and 4
    'hihat': [0, 1, 2, 3],  # Every eighth
}

# Map drum notes to MIDI numbers
drum_map = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Add drum hits in bar 1
for beat in range(4):
    for drum in drum_notes:
        if beat in drum_notes[drum]:
            add_note(drums, drum_map[drum], start=beat * 0.375, duration=0.15)

# BAR 2: Diane on piano — open voicings, different chords each bar
# Bar 2: Fm7 → Ab7 → Bb7 → Cm7 (resolve on Cm7)
chord_pitches = {
    0: [7, 10, 12, 14],  # Fm7 (F, Ab, C, Eb)
    1: [10, 12, 14, 17],  # Ab7 (Ab, C, Eb, G)
    2: [11, 14, 16, 19],  # Bb7 (Bb, D, F, Ab)
    3: [8, 12, 15, 17]    # Cm7 (C, Eb, G, Bb)
}

# Add piano chords on 2 and 4
for bar in range(1, 4):
    for chord_idx, pitches in enumerate(chord_pitches):
        if (bar == 1 and chord_idx == 0) or (bar == 2 and chord_idx == 1) or (bar == 3 and chord_idx == 2):
            start = bar * 1.5 + (chord_idx * 0.75)
            duration = 0.75
            for pitch in pitches:
                add_note(piano, pitch, start, duration, velocity=90)

# BAR 2: Marcus on bass — walking line (Fm7 chord: F, Ab, C, Eb)
# Roots and fifths with chromatic approaches
bass_line = [53, 55, 57, 52, 53, 55, 52, 53]  # F, Ab, C, Eb, F, Ab, F, F
for i, pitch in enumerate(bass_line):
    add_note(bass, pitch, i * 0.375, 0.375, velocity=70)

# BAR 2-4: Dante on tenor sax — one short motif, make it sing
# Start with a motif: F, Ab, Bb, C
# Leave it hanging, then return with F, Ab, Bb, F (resolve)
sax_notes = [
    (53, 0.0),     # F
    (55, 0.375),   # Ab
    (57, 0.75),    # Bb
    (58, 1.125),   # C
    (53, 1.5),     # Return to F
    (55, 1.875),   # Ab
    (57, 2.25),    # Bb
    (53, 2.625)    # F (resolve)
]

for pitch, start in sax_notes:
    add_note(sax, pitch, start, 0.375, velocity=100)

# SAVE MIDI FILE
pm.write("dante_intro.mid")
