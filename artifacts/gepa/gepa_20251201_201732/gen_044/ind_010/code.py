
import pretty_midi

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375  # 0.375s per beat at 160 BPM
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125))
        for eighth in [0.0, 0.1875]:  # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=time + eighth, end=time + eighth + 0.0625))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - Dm7 -> G7 -> Cm7 -> F7
# Start the motif, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D (from Dm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25))  # G (from G7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.75))  # C (from Cm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25))  # F (from F7)

# Bass - Walking line in Dm: D2 -> F2 -> G2 -> A2 -> Bb2 -> C2 -> D2 -> Eb2
bass_notes = [38, 41, 43, 45, 46, 48, 38, 49]  # D2, F2, G2, A2, Bb2, C2, D2, Eb2
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano - Open voicings
# Dm7 (bar 2) = D, F, A, C (root, 3rd, 5th, 7th)
# G7 (bar 3) = G, B, D, F (root, 3rd, 5th, b7)
# Cm7 (bar 4) = C, Eb, G, Bb (root, b3, 5th, b7)
# F7 (bar 5) = F, A, C, Eb (root, 3rd, 5th, b7)

# Bar 2 (1.5 - 1.875s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.875))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875))  # C

# Bar 3 (1.875 - 2.25s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.25))  # B
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25))  # F

# Bar 4 (2.25 - 2.625s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.625))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625))  # Eb
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625))  # G
piano.notes.append(pretty_midi.Note(velocity=85, pitch=70, start=2.25, end=2.625))  # Bb

# Bar 5 (2.625 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=65, start=2.625, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=71, start=2.625, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=85, pitch=64, start=2.625, end=3.0))  # Eb

# Bar 3: Drums (1.875 - 3.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 1.875 + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125))
        for eighth in [0.0, 0.1875]:  # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=time + eighth, end=time + eighth + 0.0625))

# Bar 4: Drums (3.0 - 4.5s)
# Same pattern as bar 1, just shifted
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=kick, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=snare, start=time, end=time + 0.125))
        for eighth in [0.0, 0.1875]:  # Hihat on every eighth
            drums.notes.append(pretty_midi.Note(velocity=85, pitch=hihat, start=time + eighth, end=time + eighth + 0.0625))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
