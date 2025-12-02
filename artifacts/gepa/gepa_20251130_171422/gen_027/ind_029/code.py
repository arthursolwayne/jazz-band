
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note numbers
D4 = 62
E4 = 64
F4 = 65
G4 = 67
A4 = 69
B4 = 71
C5 = 72

# Define drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(1, 5):
    time = (beat - 1) * 0.375  # 0.375s per beat
    if beat % 2 == 1:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
    for eighth in [0, 0.1875]:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time + eighth, end=time + eighth + 0.0625))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: D4 -> F4 -> G4 -> A4 (motif)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=D4, start=1.5, end=1.5 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=F4, start=1.875, end=1.875 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=G4, start=2.25, end=2.25 + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=A4, start=2.625, end=2.625 + 0.375))

# Bass: Walking line in D minor (D4, Eb4, F4, G4, A4, Bb4, C5, D5)
bass_notes = [D4, E4, F4, G4, A4, B4, C5, D5]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.125
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=D4, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=F4, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=A4, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=C5, start=1.875, end=2.25))

# Bar 3: D7 again, but with a chromatic passing tone
piano.notes.append(pretty_midi.Note(velocity=90, pitch=D4, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=F4, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=A4, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=C5, start=3.0, end=3.375))
piano.notes.append(pretty_midi.Note(velocity=70, pitch=E4, start=3.125, end=3.25))  # Chromatic passing tone

# Bar 4: D7 again (same as Bar 2), with a little push
piano.notes.append(pretty_midi.Note(velocity=90, pitch=D4, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=F4, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=A4, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=C5, start=3.75, end=4.125))

# Drums continue in Bar 2-4
for bar in range(2, 5):
    for beat in range(1, 5):
        time = 1.5 + (bar - 2) * 1.5 + (beat - 1) * 0.375  # 1.5s per bar
        if beat % 2 == 1:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125))
        for eighth in [0, 0.1875]:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time + eighth, end=time + eighth + 0.0625))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
