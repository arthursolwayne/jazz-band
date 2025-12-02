
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.tempo = 160

# Define the key: F major
key = 'F'

# Create instruments
sax_instrument = Instrument(program=64, name='Tenor Saxophone')
bass_instrument = Instrument(program=33, name='Double Bass')
piano_instrument = Instrument(program=0, name='Acoustic Piano')
drum_instrument = Instrument(program=0, name='Drums')

pm.instruments.append(sax_instrument)
pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drum_instrument)

# Define time in seconds per beat (160 BPM = 60/160 = 0.375 seconds per beat)
beat = 0.375
bar_length = 4 * beat  # 1.5 seconds per bar
total_duration = 4 * bar_length  # 6 seconds for 4 bars

# Define F major scale: F, G, A, Bb, B, C, D
note_numbers = {
    'F': 65,
    'G': 67,
    'A': 69,
    'Bb': 70,
    'B': 71,
    'C': 72,
    'D': 74
}

# Define saxophone motif (starts on beat 0 of bar 1, ends on beat 3 of bar 1)
# Motif: F (1/2 beat), rest (1/2 beat), Bb (1/4 beat), rest (1/4 beat)
# This creates a breathy, questioning opening — space, tension, promise
sax_notes = [
    Note(note_number=note_numbers['F'], start=0.0, end=beat * 0.5, velocity=90),
    Note(note_number=note_numbers['Bb'], start=beat * 1.5, end=beat * 1.75, velocity=90)
]

sax_instrument.notes.extend(sax_notes)

# Define bass line (walking, chromatic)
# Bar 1: F (beat 1) -> G (beat 2) -> Ab (beat 3) -> A (beat 4)
# Bar 2: Bb (beat 1) -> B (beat 2) -> C (beat 3) -> D (beat 4)
# Bar 3: F (beat 1) -> G (beat 2) -> Ab (beat 3) -> A (beat 4)
# Bar 4: B (beat 1) -> C (beat 2) -> D (beat 3) -> F (beat 4)
bass_notes = [
    # Bar 1
    Note(note_number=note_numbers['F'], start=beat * 0, end=beat * 0.25, velocity=70),
    Note(note_number=note_numbers['G'], start=beat * 1, end=beat * 1.25, velocity=70),
    Note(note_number=note_numbers['Ab'], start=beat * 2, end=beat * 2.25, velocity=70),
    Note(note_number=note_numbers['A'], start=beat * 3, end=beat * 3.25, velocity=70),

    # Bar 2
    Note(note_number=note_numbers['Bb'], start=beat * 4, end=beat * 4.25, velocity=70),
    Note(note_number=note_numbers['B'], start=beat * 5, end=beat * 5.25, velocity=70),
    Note(note_number=note_numbers['C'], start=beat * 6, end=beat * 6.25, velocity=70),
    Note(note_number=note_numbers['D'], start=beat * 7, end=beat * 7.25, velocity=70),

    # Bar 3
    Note(note_number=note_numbers['F'], start=beat * 8, end=beat * 8.25, velocity=70),
    Note(note_number=note_numbers['G'], start=beat * 9, end=beat * 9.25, velocity=70),
    Note(note_number=note_numbers['Ab'], start=beat * 10, end=beat * 10.25, velocity=70),
    Note(note_number=note_numbers['A'], start=beat * 11, end=beat * 11.25, velocity=70),

    # Bar 4
    Note(note_number=note_numbers['B'], start=beat * 12, end=beat * 12.25, velocity=70),
    Note(note_number=note_numbers['C'], start=beat * 13, end=beat * 13.25, velocity=70),
    Note(note_number=note_numbers['D'], start=beat * 14, end=beat * 14.25, velocity=70),
    Note(note_number=note_numbers['F'], start=beat * 15, end=beat * 15.25, velocity=70)
]

bass_instrument.notes.extend(bass_notes)

# Define piano chords: 7th chords, comp on beat 2 and 4
# Bar 1: F7 (F, A, C, Eb) on beat 2
# Bar 2: Bb7 (Bb, D, F, Ab) on beat 4
# Bar 3: F7 on beat 2
# Bar 4: Bb7 on beat 4
piano_notes = [
    # Bar 1 - F7 on beat 2
    Note(note_number=note_numbers['F'], start=beat * 2, end=beat * 2.25, velocity=90),
    Note(note_number=note_numbers['A'], start=beat * 2, end=beat * 2.25, velocity=90),
    Note(note_number=note_numbers['C'], start=beat * 2, end=beat * 2.25, velocity=90),
    Note(note_number=note_numbers['Eb'], start=beat * 2, end=beat * 2.25, velocity=90),

    # Bar 2 - Bb7 on beat 4
    Note(note_number=note_numbers['Bb'], start=beat * 4, end=beat * 4.25, velocity=90),
    Note(note_number=note_numbers['D'], start=beat * 4, end=beat * 4.25, velocity=90),
    Note(note_number=note_numbers['F'], start=beat * 4, end=beat * 4.25, velocity=90),
    Note(note_number=note_numbers['Ab'], start=beat * 4, end=beat * 4.25, velocity=90),

    # Bar 3 - F7 on beat 2
    Note(note_number=note_numbers['F'], start=beat * 8, end=beat * 8.25, velocity=90),
    Note(note_number=note_numbers['A'], start=beat * 8, end=beat * 8.25, velocity=90),
    Note(note_number=note_numbers['C'], start=beat * 8, end=beat * 8.25, velocity=90),
    Note(note_number=note_numbers['Eb'], start=beat * 8, end=beat * 8.25, velocity=90),

    # Bar 4 - Bb7 on beat 4
    Note(note_number=note_numbers['Bb'], start=beat * 12, end=beat * 12.25, velocity=90),
    Note(note_number=note_numbers['D'], start=beat * 12, end=beat * 12.25, velocity=90),
    Note(note_number=note_numbers['F'], start=beat * 12, end=beat * 12.25, velocity=90),
    Note(note_number=note_numbers['Ab'], start=beat * 12, end=beat * 12.25, velocity=90)
]

piano_instrument.notes.extend(piano_notes)

# Define drums:
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every 8th
# Bar 1:
# Kick: 0, 2
# Snare: 1, 3
# Hihat: 0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625
# Bar 2: same
# Bar 3: same
# Bar 4: same

def make_drums():
    drum_notes = []
    for bar in range(4):
        for beat in range(4):
            # Kick on 1 & 3
            if beat == 0 or beat == 2:
                kick = Note(note_number=36, start=beat + bar * 4, end=beat + bar * 4 + 0.1, velocity=100)
                drum_notes.append(kick)
            # Snare on 2 & 4
            if beat == 1 or beat == 3:
                snare = Note(note_number=38, start=beat + bar * 4, end=beat + bar * 4 + 0.1, velocity=100)
                drum_notes.append(snare)
            # Hihat on every 8th
            for eighth in range(2):
                hihat = Note(note_number=42, start=(beat * 2 + eighth) + bar * 4, end=(beat * 2 + eighth) + bar * 4 + 0.05, velocity=80)
                drum_notes.append(hihat)
    return drum_notes

drum_notes = make_drums()
drum_instrument.notes.extend(drum_notes)

# Save the MIDI file
pm.write("wayne_intro.mid")
print("MIDI file created: 'wayne_intro.mid'")
