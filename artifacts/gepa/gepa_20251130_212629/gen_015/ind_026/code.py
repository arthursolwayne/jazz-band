
import pretty_midi
import numpy as np

# Initialize the MIDI file with tempo and time signature
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI Note Definitions
# Drums
kick = 36
snare = 38
hihat = 42
# Saxophone in Dm (Dm7): D, F, A, C
# D = 62, F = 65, A = 69, C = 60
# Bass notes: walking line in Dm
# Piano chords: Dm7 (D, F, A, C) with some chromatic passing tones

# Bar 1: Drums only (0.0 to 1.5 seconds)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:
    for beat in [0, 2]:  # Kick on 1 and 3
        note = pretty_midi.Note(velocity=np.random.randint(80, 100), pitch=kick, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        note = pretty_midi.Note(velocity=np.random.randint(90, 110), pitch=snare, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.08)
        drums.notes.append(note)
    for beat in range(4):  # Hi-hat on every eighth
        note = pretty_midi.Note(velocity=np.random.randint(60, 75), pitch=hihat, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 to 6.0 seconds)

# Bass line: Walking line in Dm, chromatic passing tones
bass_notes = [
    # Bar 2: D -> C -> B -> A (chromatic down from D)
    62, 60, 59, 69,
    # Bar 3: A -> G -> F -> D (chromatic down from A)
    69, 67, 65, 62,
    # Bar 4: D -> F -> E -> D (chromatic up from D)
    62, 65, 64, 62
]

for i, note in enumerate(bass_notes):
    duration = 0.375
    start = 1.5 + i * 0.375
    velocity = np.random.randint(60, 80)
    bass_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano chords: Dm7 in bar 2, Dm7 with chromatic passing in bar 3, Dm7 again in bar 4
# Comp on 2 and 4
chords = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 65, 69, 60),
    # Bar 3: Dm7 with F# (chromatic passing)
    (62, 66, 69, 60),
    # Bar 4: Dm7
    (62, 65, 69, 60)
]

for bar_idx, (root, seventh, fifth, third) in enumerate(chords):
    for beat in [1, 3]:  # Comp on 2 and 4
        start = 1.5 + bar_idx * 1.5 + beat * 0.375
        for pitch in [root, seventh, fifth, third]:
            note = pretty_midi.Note(velocity=np.random.randint(90, 110), pitch=pitch, start=start, end=start + 0.08)
            piano.notes.append(note)

# Saxophone melody: Simple, haunting, one motif that leaves space
# Motif: D -> F -> A (2nd bar) then resolves on C (4th bar), with silence in between
note_durations = [0.375, 0.375, 0.375, 0.375]
melody_notes = [62, 65, 69, 60]

for i, note in enumerate(melody_notes):
    start = 1.5 + i * 0.375
    velocity = np.random.randint(90, 110)
    sax_note = pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + note_durations[i])
    sax.notes.append(sax_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
