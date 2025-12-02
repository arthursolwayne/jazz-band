
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures and key
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
key_signature = pretty_midi.KeySignature(key_number=1, time=0)  # F major
midi.time_signature_changes = [time_signature]
midi.key_signature_changes = [key_signature]

# Define note durations (in seconds)
beat = 0.375  # 160 BPM, 4/4 time, 1 beat = 0.375 seconds
bar_length = 1.5  # 4 beats per bar
note_lengths = {
    'quarter': beat,
    'eighth': beat / 2,
    'sixteenth': beat / 4
}

# Define instrument programs
drum_program = Program(0, 0)  # Drums
bass_program = Program(33, 0)  # Double Bass
piano_program = Program(0, 0)  # Acoustic Piano
sax_program = Program(64, 0)  # Tenor Saxophone

# Create instruments
drum_inst = Instrument(program=drum_program)
bass_inst = Instrument(program=bass_program)
piano_inst = Instrument(program=piano_program)
sax_inst = Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [drum_inst, bass_inst, piano_inst, sax_inst]

# Define MIDI note numbers
F3 = 71  # F3
Bb3 = 73  # Bb3
C4 = 72  # C4
F4 = 79  # F4
G4 = 80  # G4
A4 = 81  # A4
B4 = 82  # B4
C5 = 84  # C5
D5 = 86  # D5
E5 = 87  # E5
F5 = 88  # F5
G5 = 89  # G5
A5 = 91  # A5
B5 = 93  # B5
C6 = 96  # C6

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def create_drums():
    # Bar 1
    notes = [
        Note(60, 0, beat, 0),  # Kick on 1
        Note(62, beat, beat, 0),  # Snare on 2
        Note(42, beat * 1.5, beat, 0),  # Kick on 3
        Note(62, beat * 2, beat, 0),  # Snare on 4
    ]

    # Add hihat on every eighth
    for i in range(0, 4):
        Note(46, beat * i, beat, 0)  # Hihat on every eighth

    for note in notes:
        drum_inst.notes.append(note)

    # Bar 2, 3, 4: same pattern
    for bar in range(1, 4):
        for note in notes:
            note.start += bar * bar_length
            drum_inst.notes.append(note)

# Bass: Walking line, chromatic approaches, no repeated notes
def create_bass():
    # Bars 2-4 (start at bar 1, 1.5 seconds)
    # Start at bar 1 (time = 1.5)
    # F major scale: F, G, A, Bb, C, D, E
    # Walking bass line with chromatic approaches
    # F3 -> G -> Ab -> A -> Bb -> C -> Db -> D -> Eb -> E -> F -> G -> Ab -> A -> Bb -> C

    pattern = [
        F3,  # F3
        G4,  # G4
        A4,  # A4
        Bb4,  # Bb4
        C5,  # C5
        Db5,  # Db5
        D5,  # D5
        Eb5,  # Eb5
        E5,  # E5
        F5,  # F5
        G5,  # G5
        Ab5,  # Ab5
        A5,  # A5
        Bb5,  # Bb5
        C6,  # C6
    ]

    # Add notes with quarter note duration
    for i, note_number in enumerate(pattern):
        start_time = bar_length + i * note_lengths['quarter']
        note = Note(note_number, start_time, note_lengths['quarter'], 0)
        bass_inst.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
def create_piano():
    # Bars 2-4 (start at 1.5 seconds)
    # F7, Bb7, C7, F7 chords
    # Comp on 2 and 4 (beat 2 and beat 4 of each bar)

    chord_notes = {
        # Bar 2: F7 (F, A, C, Eb)
        2: [F3, A3, C4, Eb4],
        # Bar 3: Bb7 (Bb, D, F, Ab)
        3: [Bb3, D4, F4, Ab4],
        # Bar 4: C7 (C, E, G, Bb)
        4: [C4, E4, G4, Bb4]
    }

    for bar, notes in chord_notes.items():
        time = bar_length * (bar - 1) + beat * 2  # on 2nd beat
        for note in notes:
            note_obj = Note(note, time, note_lengths['quarter'], 0)
            piano_inst.notes.append(note)

        time = bar_length * (bar - 1) + beat * 4  # on 4th beat
        for note in notes:
            note_obj = Note(note, time, note_lengths['quarter'], 0)
            piano_inst.notes.append(note)

# Sax: One short motif (2-3 notes), start it, leave it hanging, return to finish it
# Motif: F4 (start), G4 (hanging), then back to F4 (resolve)
def create_sax():
    # Bar 2: start motif
    Note(F4, bar_length, note_lengths['quarter'], 0)
    Note(G4, bar_length + note_lengths['quarter'], note_lengths['eighth'], 0)

    # Bar 3: leave it hanging, resolve in bar 4
    Note(F4, bar_length * 2 + note_lengths['quarter'], note_lengths['quarter'], 0)

# Generate all parts
create_drums()
create_bass()
create_piano()
create_sax()

# Save the MIDI file
midi.write('wayne_shorter_intro.mid')
print("MIDI file 'wayne_shorter_intro.mid' has been created.")
