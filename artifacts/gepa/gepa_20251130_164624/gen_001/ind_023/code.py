
import pretty_midi

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0)]  # F Major
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Fretless Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Time per bar in seconds
tempo = 160
seconds_per_bar = 60.0 / tempo * 4

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
time = 0
for bar in range(1):
    for beat in range(4):
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(
                velocity=90,
                pitch=36,
                start=time + beat * (seconds_per_bar / 4),
                end=time + beat * (seconds_per_bar / 4) + 0.1
            )
            drums.notes.append(note)
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(
                velocity=90,
                pitch=38,
                start=time + beat * (seconds_per_bar / 4),
                end=time + beat * (seconds_per_bar / 4) + 0.1
            )
            drums.notes.append(note)
        # Hihat on every eighth note
        for eighth in range(2):
            note = pretty_midi.Note(
                velocity=90,
                pitch=42,
                start=time + (beat * 2 + eighth) * (seconds_per_bar / 8),
                end=time + (beat * 2 + eighth) * (seconds_per_bar / 8) + 0.05
            )
            drums.notes.append(note)
    time += seconds_per_bar

# Bars 2-4: All instruments
bar_start = time
bar_duration = seconds_per_bar
bass_notes = []
piano_notes = []
sax_notes = []

# Bass line: F major scale, chromatic walking line with no repeated notes
# F, G, A, Bb, B, C, D, E, F (chromatic variation)
bass_line = [71, 72, 74, 73, 75, 76, 78, 77, 71]  # F, G, A, Bb, B, C, D, E, F
for i in range(3):  # 3 bars
    for beat in range(4):
        note = pretty_midi.Note(
            velocity=80,
            pitch=bass_line[i * 4 + beat],
            start=bar_start + beat * (bar_duration / 4),
            end=bar_start + beat * (bar_duration / 4) + 0.25
        )
        bass.notes.append(note)

# Piano: 7th chords on beats 2 and 4
# Chord progression: F7, Bb7, C7, F7 (for 3 bars)
chords = [
    [71, 74, 76, 78],  # F7
    [73, 76, 78, 80],  # Bb7
    [76, 78, 80, 82],  # C7
    [71, 74, 76, 78],  # F7
]
for i in range(3):  # 3 bars
    for beat in range(4):
        if beat == 1 or beat == 3:
            chord = chords[i]
            for pitch in chord:
                note = pretty_midi.Note(
                    velocity=90,
                    pitch=pitch,
                    start=bar_start + beat * (bar_duration / 4),
                    end=bar_start + beat * (bar_duration / 4) + 0.25
                )
                piano.notes.append(note)

# Sax melody: concise, unique motif
# F, Ab, Bb, F (with a descending chromatic line)
sax_line = [
    (71, 0.5),
    (76, 0.5),
    (73, 0.5),
    (71, 0.5),
    (70, 0.5),
    (69, 0.5),
    (71, 1.0)
]
for i, (pitch, duration) in enumerate(sax_line):
    start = bar_start + i * 0.5
    note = pretty_midi.Note(
        velocity=100,
        pitch=pitch,
        start=start,
        end=start + duration
    )
    sax.notes.append(note)

pm.write('jazz_intro.mid')
