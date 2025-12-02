
import pretty_midi

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define key and time
key = 'F'
time_signature = (4, 4)
bpm = 160
note_duration = 0.375  # 60 / 160 = 0.375 seconds per beat
bar_duration = 1.5  # 4 beats / 160 BPM = 1.5 sec per bar
total_duration = 6.0  # 4 bars * 1.5 sec per bar

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')

sax = pretty_midi.Instrument(program=sax_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
drums = pretty_midi.Instrument(program=drum_program)

pm.instruments.append(sax)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(drums)

# Define note values for F major
F_major = [65, 67, 69, 71, 72, 74, 76]  # F4, G4, A4, Bb4, B4, C5, D5

# Define the sax motif (questioning, open-ended, emotional)
# Motif: F4 - G4 - A4 (half note), then leave it hanging on G4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=0, end=1.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
]

# Add the motif to sax instrument
for note in sax_notes:
    sax.notes.append(note)

# Define piano chords (7th chords, comp on 2 and 4)
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: D7 (D, F#, A, C)
# Comp on beats 2 and 4

def add_piano_notes(bar_start, chord, velocity=100):
    # Chord structure: root, 3rd, 5th, 7th
    for note in chord:
        pretty_midi.Note(
            velocity=velocity,
            pitch=note,
            start=bar_start + 0.75,  # beat 2
            end=bar_start + 1.125
        )
        pretty_midi.Note(
            velocity=velocity,
            pitch=note,
            start=bar_start + 1.875,  # beat 4
            end=bar_start + 2.25
        )

# Bar 2: F7 = F, A, C, E
f7 = [65, 68, 69, 72]
add_piano_notes(1.5, f7, velocity=85)

# Bar 3: Bb7 = Bb, D, F, Ab
bb7 = [62, 67, 65, 69]
add_piano_notes(3.0, bb7, velocity=85)

# Bar 4: D7 = D, F#, A, C
d7 = [67, 71, 69, 72]
add_piano_notes(4.5, d7, velocity=85)

# Add piano to instrument
for note in piano.notes:
    piano.notes.append(note)

# Define bass line (walking line with chromatic approaches)

# Bar 1: Drums only
# Bar 2: F - G - Ab - A
# Bar 3: Bb - B - C - D
# Bar 4: D - E - F - G

def add_bass_notes(bar_start, notes, velocity=80):
    for i, note in enumerate(notes):
        pretty_midi.Note(
            velocity=velocity,
            pitch=note,
            start=bar_start + i * note_duration,
            end=bar_start + i * note_duration + note_duration
        )

# Bar 2
bar2_notes = [65, 67, 69, 71]  # F, G, A, B
add_bass_notes(1.5, bar2_notes)

# Bar 3
bar3_notes = [62, 63, 65, 67]  # Bb, B, C, D
add_bass_notes(3.0, bar3_notes)

# Bar 4
bar4_notes = [67, 69, 71, 72]  # D, E, F, G
add_bass_notes(4.5, bar4_notes)

# Add bass to instrument
for note in bass.notes:
    bass.notes.append(note)

# Define drum pattern (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)

def add_drums(bar_start):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.1)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.225)
    
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.85)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 1.975)
    
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1)

# Bar 1: Drums only
add_drums(0.0)

# Bar 2–4: Drums on
for bar in [1.5, 3.0, 4.5]:
    add_drums(bar)

# Add drums to instrument
for note in drums.notes:
    drums.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro_f_major.mid')
print("MIDI file 'jazz_intro_f_major.mid' has been created.")
