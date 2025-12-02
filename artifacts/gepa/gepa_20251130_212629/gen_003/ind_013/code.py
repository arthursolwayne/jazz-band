
import pretty_midi
import numpy as np

# Setup
tempo = 160  # BPM
time_signature = (4, 4)
key = 'Fm'  # F minor
duration_seconds = 6.0  # 4 bars at 160 BPM = 6 seconds
sample_rate = 44100

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define note values and durations
quarter_note = 60 / tempo  # seconds per quarter note
eighth_note = quarter_note / 2
sixteenth_note = quarter_note / 4

# Define instruments
saxophone_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')

# Create instruments
sax = pretty_midi.Instrument(program=saxophone_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define the key of F minor
# F minor scale: F, Gb, G, Ab, Bb, B, C, Db (no sharps, just flats)
# Scale degrees: 1 = F, 2 = Gb, 3 = G, 4 = Ab, 5 = Bb, 6 = B, 7 = C, 8 = Db

# Helper function to convert scale degree to note number
def scale_degree_to_note(scale_degree, root):
    scale_degrees = ['F', 'Gb', 'G', 'Ab', 'Bb', 'B', 'C', 'Db']
    return pretty_midi.note_number_to_name(pretty_midi.note_name_to_number(scale_degrees[scale_degree % 8]))

# Define saxophone motif in Fm
# Dante's motif: a simple, emotionally charged phrase that lingers — F, Ab, Bb, B (sad, slightly unresolved)
sax_notes = [pretty_midi.note_name_to_number('F4'),  # F4
             pretty_midi.note_name_to_number('Ab4'), # Ab4
             pretty_midi.note_name_to_number('Bb4'), # Bb4
             pretty_midi.note_name_to_number('B4')]  # B4 (unresolved)

sax_durations = [0.6, 0.6, 0.6, 0.6]  # each note played for 0.6 seconds
sax_times = [0.0, 1.5, 3.0, 4.5]  # bar 1, bar 2, bar 3, bar 4

for note, time, duration in zip(sax_notes, sax_times, sax_durations):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Drums: Little Ray — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: kick on 0.0, snare on 0.75, hihat on 0.0, 0.375, 0.75, 1.125
# Bar 2: kick on 1.5, snare on 2.25, hihat on 1.5, 1.875, 2.25, 2.625
# Bar 3: kick on 3.0, snare on 3.75, hihat on 3.0, 3.375, 3.75, 4.125
# Bar 4: kick on 4.5, snare on 5.25, hihat on 4.5, 4.875, 5.25, 5.625

# Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.5 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.5 + 0.1))

# Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.75 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.25 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.75 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.25 + 0.1))

# Hihat
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.375 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.75 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.125 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.5 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=1.875 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.25 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.625 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.0 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.375 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.75 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.125 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.5 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=4.875 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.25 + 0.1))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.625 + 0.1))

# Bass line: Marcus — dynamic, chromatic, walking line, no repeated notes
bass_notes = [
    pretty_midi.note_name_to_number('F3'),  # 1
    pretty_midi.note_name_to_number('Gb3'),  # 2
    pretty_midi.note_name_to_number('G3'),   # 3
    pretty_midi.note_name_to_number('Ab3'),  # 4
    pretty_midi.note_name_to_number('Bb3'),  # 5
    pretty_midi.note_name_to_number('B3'),   # 6
    pretty_midi.note_name_to_number('C3'),   # 7
    pretty_midi.note_name_to_number('Db3'),  # 8
    pretty_midi.note_name_to_number('F3'),   # 1
    pretty_midi.note_name_to_number('Gb3'),  # 2
    pretty_midi.note_name_to_number('G3'),   # 3
    pretty_midi.note_name_to_number('Ab3'),  # 4
    pretty_midi.note_name_to_number('Bb3'),  # 5
    pretty_midi.note_name_to_number('B3'),   # 6
    pretty_midi.note_name_to_number('C3'),   # 7
    pretty_midi.note_name_to_number('Db3'),  # 8
    pretty_midi.note_name_to_number('F3'),   # 1
    pretty_midi.note_name_to_number('Gb3'),  # 2
    pretty_midi.note_name_to_number('G3'),   # 3
    pretty_midi.note_name_to_number('Ab3'),  # 4
    pretty_midi.note_name_to_number('Bb3'),  # 5
    pretty_midi.note_name_to_number('B3'),   # 6
    pretty_midi.note_name_to_number('C3'),   # 7
    pretty_midi.note_name_to_number('Db3'),  # 8
]

bass_times = np.arange(0, 6, 0.375)  # 16 notes at 16th note interval
bass_durations = [0.375] * len(bass_notes)

for note, time, duration in zip(bass_notes, bass_times, bass_durations):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + duration))

# Piano: Diane — 7th chords, comp on 2 and 4
# Bars: 1 to 4
# Bar 1: Fm7 (F, Ab, Bb, C)
# Bar 2: Gbm7 (Gb, Bb, Db, Eb)
# Bar 3: Am7 (A, C, Eb, G)
# Bar 4: Bbm7 (Bb, Db, F, Ab)

# Bar 1: Fm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=pretty_midi.note_name_to_number('F4'), start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=pretty_midi.note_name_to_number('Ab4'), start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=pretty_midi.note_name_to_number('Bb4'), start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('C5'), start=0.0, end=0.75))

# Bar 2: Gbm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=pretty_midi.note_name_to_number('Gb4'), start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=pretty_midi.note_name_to_number('Bb4'), start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=pretty_midi.note_name_to_number('Db5'), start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Eb5'), start=1.5, end=2.25))

# Bar 3: Am7 (but in Fm, we're borrowing A as a passing chord)
piano.notes.append(pretty_midi.Note(velocity=95, pitch=pretty_midi.note_name_to_number('A4'), start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=pretty_midi.note_name_to_number('C5'), start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=pretty_midi.note_name_to_number('Eb5'), start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('G5'), start=3.0, end=3.75))

# Bar 4: Bbm7
piano.notes.append(pretty_midi.Note(velocity=95, pitch=pretty_midi.note_name_to_number('Bb4'), start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=pretty_midi.note_name_to_number('Db5'), start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=pretty_midi.note_name_to_number('F5'), start=4.5, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=pretty_midi.note_name_to_number('Ab5'), start=4.5, end=5.25))

# Save the MIDI file
pm.write('jazz_intro_in_Fm.mid')

print("MIDI file generated: jazz_intro_in_Fm.mid")
