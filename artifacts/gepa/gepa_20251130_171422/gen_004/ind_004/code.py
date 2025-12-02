
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Upright bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note values
D4 = 62  # D4
E4 = 64  # E4
F4 = 65  # F4
G4 = 67  # G4
A4 = 69  # A4
B4 = 71  # B4
C5 = 72  # C5
D5 = 74  # D5

# Define drum note values
kick = 36
snare = 38
hihat = 42

# Time in seconds per beat: 60 / 160 = 0.375 sec per beat
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar

# Bar 1: Little Ray (Drums only)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat_num in range(4):
    time = beat_num * beat
    # Kick on 1 and 3
    if beat_num == 0 or beat_num == 2:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat_num == 1 or beat_num == 3:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for eighth in range(2):
        hihat_time = time + eighth * beat / 2
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(note)

# Bar 2: Full quartet starts
# Bass line: walking line, chromatic approach to D
# D4 -> C#4 -> D4 -> E4 -> F4 -> E4 -> D4 -> C#4
bass_notes = [
    (D4, 0.0), (61, 0.375), (D4, 0.75), (E4, 1.125),
    (F4, 1.5), (E4, 1.875), (D4, 2.25), (61, 2.625)
]
for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# D7 = D4, F4, A4, C5
# G7 = G4, B4, D5, F5 (7th chord with flat 9)
piano_notes = []
# Bar 2 (1.5s): D7 on beat 2
piano_notes.extend([
    (D4, 1.5), (F4, 1.5), (A4, 1.5), (C5, 1.5),
    (D4, 1.75), (F4, 1.75), (A4, 1.75), (C5, 1.75)
])
# Bar 3 (3.0s): G7 on beat 2
piano_notes.extend([
    (G4, 3.0), (B4, 3.0), (D5, 3.0), (F5, 3.0),
    (G4, 3.25), (B4, 3.25), (D5, 3.25), (F5, 3.25)
])
# Bar 4 (4.5s): D7 on beat 2
piano_notes.extend([
    (D4, 4.5), (F4, 4.5), (A4, 4.5), (C5, 4.5),
    (D4, 4.75), (F4, 4.75), (A4, 4.75), (C5, 4.75)
])
# Add piano notes
for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Tenor motif — a short, singing phrase
# D4 -> E4 -> F4 -> D4 (Motif), then repeat with variation
sax_notes = [
    (D4, 1.5), (E4, 1.75), (F4, 2.0), (D4, 2.25),
    (E4, 2.5), (F4, 2.75), (A4, 3.0), (D5, 3.25),
    (D4, 3.5), (E4, 3.75), (F4, 4.0), (D4, 4.25)
]
for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
