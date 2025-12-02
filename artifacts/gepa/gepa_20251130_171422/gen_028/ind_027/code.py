
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
tempo = 160  # BPM
time_signature = (4, 4)

# Define a note class for easy creation
class Note:
    def __init__(self, note_name, start, duration, velocity=100, instrument=None):
        self.note_name = note_name
        self.start = start
        self.duration = duration
        self.velocity = velocity
        self.instrument = instrument

    def add_to_midi(self, pm, channel=None):
        if self.instrument:
            pm.instruments[self.instrument].notes.append(self.note)
        else:
            if not pm.instruments:
                pm.instruments.append(pretty_midi.Instrument())
            pm.instruments[0].notes.append(self.note)

# Create instruments
pm.instruments = [
    pretty_midi.Instrument(program=41, is_drum=False),  # Sax (Tenor)
    pretty_midi.Instrument(program=33, is_drum=False),  # Piano
    pretty_midi.Instrument(program=32, is_drum=False),  # Bass
    pretty_midi.Instrument(program=0, is_drum=True)     # Drums
]

# Define note values in Dm key (D, F, G, A, Bb, C, Eb)
note_map = {
    'D': 62,
    'F': 64,
    'G': 67,
    'A': 69,
    'Bb': 70,
    'C': 60,
    'Eb': 63
}

# Time in seconds per beat
beat_length = 60.0 / tempo  # 0.375 seconds per beat
bar_length = beat_length * 4  # 1.5 seconds per bar
total_length = bar_length * 4  # 6 seconds

# --- DRUMS (Little Ray) ---
def add_drums(pm):
    drum_instrument = pm.instruments[3]
    time = 0.0

    # Bar 1: Build tension with hihat and snare
    drum_notes = [
        # Bar 1: 0.0 - 1.5
        Note('kick', 0.0, 0.1, 80, 3),
        Note('snare', 0.5, 0.1, 100, 3),
        Note('hihat', 0.1, 0.7, 80, 3),
        Note('hihat', 0.8, 0.7, 80, 3),
        Note('hihat', 1.5, 0.1, 80, 3)  # End of Bar 1
    ]

    # Bar 2: Full rhythm with variation
    drum_notes += [
        Note('kick', 1.5, 0.1, 80, 3),
        Note('snare', 2.0, 0.1, 100, 3),
        Note('hihat', 1.6, 0.7, 80, 3),
        Note('hihat', 2.0, 0.4, 80, 3),
        Note('hihat', 2.4, 0.4, 80, 3),
        Note('hihat', 2.8, 0.4, 80, 3)
    ]

    # Bar 3: Introduce space
    drum_notes += [
        Note('kick', 3.0, 0.1, 80, 3),
        Note('snare', 3.5, 0.1, 100, 3),
        Note('hihat', 3.1, 0.6, 80, 3),
        Note('hihat', 3.7, 0.4, 80, 3)
    ]

    # Bar 4: Resolve with a strong snare and kick
    drum_notes += [
        Note('kick', 4.5, 0.1, 80, 3),
        Note('snare', 5.0, 0.1, 100, 3),
        Note('hihat', 4.6, 0.7, 80, 3),
        Note('hihat', 5.3, 0.7, 80, 3)
    ]

    # Convert note names to MIDI note numbers
    for note in drum_notes:
        if note.note_name == 'kick':
            note.note = 36  # MIDI note for kick
        elif note.note_name == 'snare':
            note.note = 38  # MIDI note for snare
        elif note.note_name == 'hihat':
            note.note = 42  # MIDI note for hihat

        note.add_to_midi(pm, 3)

# --- BASS (Marcus) ---
def add_bass(pm):
    bass_instrument = pm.instruments[2]
    note_values = [note_map['D'], note_map['F'], note_map['G'], note_map['A'], note_map['Bb'], note_map['C'], note_map['Eb']]

    # Walking line in Dm with chromatic approach
    notes = [
        Note('F', 0.0, 0.375, 90, 2),  # Bar 1
        Note('F#', 0.375, 0.375, 90, 2),
        Note('G', 0.75, 0.375, 90, 2),
        Note('A', 1.125, 0.375, 90, 2),

        Note('Bb', 1.5, 0.375, 90, 2),  # Bar 2
        Note('B', 1.875, 0.375, 90, 2),
        Note('C', 2.25, 0.375, 90, 2),
        Note('C#', 2.625, 0.375, 90, 2),

        Note('D', 3.0, 0.375, 90, 2),  # Bar 3
        Note('Eb', 3.375, 0.375, 90, 2),
        Note('F', 3.75, 0.375, 90, 2),
        Note('F#', 4.125, 0.375, 90, 2),

        Note('G', 4.5, 0.375, 90, 2),  # Bar 4
        Note('A', 4.875, 0.375, 90, 2),
        Note('Bb', 5.25, 0.375, 90, 2),
        Note('C', 5.625, 0.375, 90, 2)
    ]

    for note in notes:
        note.add_to_midi(pm, 2)

# --- PIANO (Diane) ---
def add_piano(pm):
    piano_instrument = pm.instruments[1]
    time = 0.0

    # Bar 1: Rest
    pass

    # Bar 2: Comp on 2 and 4
    # Dm7 = D, F, A, C
    # D7 = D, F, A, C#
    # F7 = F, A, C, E
    # G7 = G, Bb, D, F
    # A7 = A, C, E, G
    # Bb7 = Bb, D, F, Ab
    # C7 = C, E, G, Bb

    # Bar 2: Dm7 on beat 2, F7 on beat 4
    notes = [
        Note('D', 1.5, 0.25, 90, 1),  # Dm7 on beat 2
        Note('F', 1.5, 0.25, 90, 1),
        Note('A', 1.5, 0.25, 90, 1),
        Note('C', 1.5, 0.25, 90, 1),
        Note('F', 2.0, 0.25, 90, 1),  # F7 on beat 4
        Note('A', 2.0, 0.25, 90, 1),
        Note('C', 2.0, 0.25, 90, 1),
        Note('E', 2.0, 0.25, 90, 1)
    ]

    # Bar 3: G7 on beat 2, A7 on beat 4
    notes += [
        Note('G', 3.0, 0.25, 80, 1),
        Note('Bb', 3.0, 0.25, 80, 1),
        Note('D', 3.0, 0.25, 80, 1),
        Note('F', 3.0, 0.25, 80, 1),
        Note('A', 3.5, 0.25, 80, 1),
        Note('C', 3.5, 0.25, 80, 1),
        Note('E', 3.5, 0.25, 80, 1),
        Note('G', 3.5, 0.25, 80, 1)
    ]

    # Bar 4: Bb7 on beat 2, C7 on beat 4
    notes += [
        Note('Bb', 4.5, 0.25, 80, 1),
        Note('D', 4.5, 0.25, 80, 1),
        Note('F', 4.5, 0.25, 80, 1),
        Note('Ab', 4.5, 0.25, 80, 1),
        Note('C', 5.0, 0.25, 80, 1),
        Note('E', 5.0, 0.25, 80, 1),
        Note('G', 5.0, 0.25, 80, 1),
        Note('Bb', 5.0, 0.25, 80, 1)
    ]

    for note in notes:
        note.add_to_midi(pm, 1)

# --- SAX (You) ---
def add_sax(pm):
    sax_instrument = pm.instruments[0]
    time = 0.0

    # Bar 1: Rest
    pass

    # Bar 2: Start the motif
    # Motif: D -> F -> A -> Bb (Dm scale, but with emotion)
    notes = [
        Note('D', 1.5, 0.375, 100, 0),  # Start on beat 2
        Note('F', 1.875, 0.375, 100, 0),
        Note('A', 2.25, 0.375, 100, 0),
        Note('Bb', 2.625, 0.375, 100, 0)
    ]

    # Bar 3: Rest, leave it hanging
    pass

    # Bar 4: Return and finish the motif
    notes += [
        Note('D', 4.5, 0.375, 100, 0),
        Note('F', 4.875, 0.375, 100, 0),
        Note('A', 5.25, 0.375, 100, 0),
        Note('Bb', 5.625, 0.375, 100, 0)
    ]

    for note in notes:
        note.add_to_midi(pm, 0)

# Run all functions
add_drums(pm)
add_bass(pm)
add_piano(pm)
add_sax(pm)

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' has been saved.")
