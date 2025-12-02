
import pretty_midi

# Create a MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Assign drum notes (Standard MIDI Percussion)
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar (160 BPM, 4/4)
BAR_DURATION = 1.5  # 60 / 160 * 4 = 1.5

# Bar 1: Little Ray (Drums) only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
for beat in range(4):
    time = beat * BAR_DURATION / 4
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    # Hi-hat on every 8th
    for eighth in range(2):
        hihat_time = time + eighth * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05))

# Bar 2: Full band (1.5s - 3.0s)
# Bass: Walking line in F minor
# F -> Gb -> G -> A -> Bb -> B -> C -> Db -> F (chromatic walk, no repeating notes)
bass_notes = [77, 76, 78, 80, 79, 81, 83, 82, 77]  # F, Gb, G, A, Bb, B, C, Db, F
bass_time = 1.5
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bass_time, end=bass_time + 0.25))
    bass_time += 0.25

# Piano: 7th chords on 2 and 4 (comping in F minor)
# F7 on bar 2, Bb7 on bar 4
piano_notes = [
    # Bar 2
    77, 80, 79, 82,  # F7 (F, A, Bb, D)
    # Bar 3 (rest)
    # Bar 4
    79, 82, 84, 87   # Bb7 (Bb, D, E, G)
]
piano_time = 1.5
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=piano_time, end=piano_time + 0.25))
    piano_time += 0.25

# Sax: Short motif in F minor (start, leave hanging, return)
# Motif: F, Ab, Bb, then return to F on beat 4
sax_notes = [
    # Bar 2
    77,  # F
    79,  # Ab
    80,  # Bb
    # Bar 3 (rest)
    # Bar 4
    77   # F
]
sax_time = 1.5
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=sax_time, end=sax_time + 0.25))
    sax_time += 0.25

# Bar 3: Drums continue (3.0s - 4.5s)
# Same pattern as bar 1
for beat in range(4):
    time = 3.0 + beat * BAR_DURATION / 4
    if beat % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1))
    else:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.1))
    for eighth in range(2):
        hihat_time = time + eighth * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=hihat_time, end=hihat_time + 0.05))

# Bar 4: Full band again (4.5s - 6.0s)
# Bass: Walking line again
bass_notes = [77, 76, 78, 80, 79, 81, 83, 82, 77]  # F, Gb, G, A, Bb, B, C, Db, F
bass_time = 4.5
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=bass_time, end=bass_time + 0.25))
    bass_time += 0.25

# Piano: 7th chords again
# F7 on bar 4
piano_notes = [
    77, 80, 79, 82  # F7
]
piano_time = 4.5
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=piano_time, end=piano_time + 0.25))
    piano_time += 0.25

# Sax: Follow-up to the motif (maybe chromatic motion or a resolution)
sax_notes = [
    79,  # Ab
    80,  # Bb
    82,  # Db
    77   # F
]
sax_time = 4.5
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=sax_time, end=sax_time + 0.25))
    sax_time += 0.25

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_introduction.mid")
