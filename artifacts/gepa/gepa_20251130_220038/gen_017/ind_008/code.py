
import pretty_midi

# Create a new MIDI file with initial tempo of 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define note durations in seconds (based on 160 BPM = 0.375 sec per beat)
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar
half_note = 2 * beat
quarter_note = beat
eighth_note = beat / 2

# Drums: kick (36), snare (38), hihat (42)
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
time = 0.0
for i in range(4):
    # Kick on 1 and 3
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=drum_kick, start=time, end=time + beat)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=drum_snare, start=time, end=time + beat)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(2):
        note = pretty_midi.Note(velocity=90, pitch=drum_hihat, start=time + j * eighth_note, end=time + j * eighth_note + eighth_note)
        drums.notes.append(note)
    time += beat

# Bar 2: Full ensemble (1.5 - 3.0s)

# Drums: same pattern
time = 1.5
for i in range(4):
    if i % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=drum_kick, start=time, end=time + beat)
        drums.notes.append(note)
    if i % 2 == 1:
        note = pretty_midi.Note(velocity=100, pitch=drum_snare, start=time, end=time + beat)
        drums.notes.append(note)
    for j in range(2):
        note = pretty_midi.Note(velocity=90, pitch=drum_hihat, start=time + j * eighth_note, end=time + j * eighth_note + eighth_note)
        drums.notes.append(note)
    time += beat

# Bass: Walking line in Fm7 (F, Ab, Bb, D)
# Bar 2: F -> Ab -> Bb -> D
# Bar 3: D -> F -> Ab -> Bb
# Bar 4: Bb -> D -> F -> Ab

# Bar 2
bass_notes = [78, 75, 76, 79]  # F, Ab, Bb, D
time = 1.5
for note_pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_pitch, start=time, end=time + quarter_note)
    bass.notes.append(note)
    time += quarter_note

# Bar 3
bass_notes = [79, 78, 75, 76]  # D, F, Ab, Bb
time = 3.0
for note_pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_pitch, start=time, end=time + quarter_note)
    bass.notes.append(note)
    time += quarter_note

# Bar 4
bass_notes = [76, 79, 78, 75]  # Bb, D, F, Ab
time = 4.5
for note_pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_pitch, start=time, end=time + quarter_note)
    bass.notes.append(note)
    time += quarter_note

# Piano: 7th chords on 2 and 4 (comping)
# F7 on 2, Bb7 on 4
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: F7 (F, A, C, Eb)

# Bar 2
piano_notes = [78, 81, 79, 76]  # F, A, C, Eb
time = 2.0
for note_pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_pitch, start=time, end=time + half_note)
    piano.notes.append(note)

# Bar 3
piano_notes = [76, 79, 78, 75]  # Bb, D, F, Ab
time = 3.0
for note_pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_pitch, start=time, end=time + half_note)
    piano.notes.append(note)

# Bar 4
piano_notes = [78, 81, 79, 76]  # F, A, C, Eb
time = 4.0
for note_pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_pitch, start=time, end=time + half_note)
    piano.notes.append(note)

# Sax: 4-bar motif starting in bar 2
# Motif: F, Ab, Bb, C (in Fm7)
# Play the first note, leave it hanging, then come back to resolve

# Bar 2: Note on 1
note = pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.5 + eighth_note)
sax.notes.append(note)

# Bar 3: Note on 1 (Ab)
note = pretty_midi.Note(velocity=100, pitch=75, start=3.0, end=3.0 + eighth_note)
sax.notes.append(note)

# Bar 4: Note on 1 (Bb)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5 + eighth_note)
sax.notes.append(note)

# Bar 4: Resolution on 3 (C)
note = pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.25 + eighth_note)
sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.save('dante_intro.mid')
