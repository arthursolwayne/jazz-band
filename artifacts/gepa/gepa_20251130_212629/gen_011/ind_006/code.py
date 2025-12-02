
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar duration is 1.5 seconds (160 BPM, 4/4 time)
BAR_DURATION = 1.5
NOTE_DURATION = 0.375  # 1/4 note
EIGHTH_NOTE_DURATION = NOTE_DURATION / 2

# ------------------------------
# Bar 1: Little Ray on Drums (0.0 - 1.5s)
# ------------------------------
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=NOTE_DURATION))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=NOTE_DURATION * 2, end=NOTE_DURATION * 3))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=NOTE_DURATION, end=NOTE_DURATION * 2))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=NOTE_DURATION * 3, end=NOTE_DURATION * 4))

# Hi-hats on every eighth note
for i in range(0, 4):
    start = i * EIGHTH_NOTE_DURATION
    end = start + EIGHTH_NOTE_DURATION
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start, end=end))

# ------------------------------
# Bars 2–4: Full Quartet (1.5 - 6.0s)
# ------------------------------
BAR_START = 1.5

# ------------------------------ 
# Drums (Bars 2–4)
# ------------------------------
for bar in range(2, 5):
    start = BAR_START + (bar - 2) * BAR_DURATION

    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start, end=start + NOTE_DURATION))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=start + NOTE_DURATION * 2, end=start + NOTE_DURATION * 3))

    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + NOTE_DURATION, end=start + NOTE_DURATION * 2))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=start + NOTE_DURATION * 3, end=start + NOTE_DURATION * 4))

    # Hi-hats on every eighth
    for i in range(0, 4):
        start_eighth = start + i * EIGHTH_NOTE_DURATION
        end_eighth = start_eighth + EIGHTH_NOTE_DURATION
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start_eighth, end=end_eighth))

# ------------------------------
# Bass (Bars 2–4): Chromatic walking line
# ------------------------------
# F major key: F, G, A, Bb, C, D, E, F
# We'll walk chromatically from F to G (F to F# to G — a half-step approach to G)
# Then continue with a walking line of F, G, A, Bb, C, D, E, F

bass_notes = [
    # Bar 2 (F -> G chromatic)
    (F, 1.5), (F_Sharp, 1.5 + 0.375), (G, 1.5 + 0.75),
    
    # Bar 3 (Walking F scale)
    (F, 1.5 + 1.5), (G, 1.5 + 1.875), (A, 1.5 + 2.25), (Bb, 1.5 + 2.625),
    (C, 1.5 + 3.0), (D, 1.5 + 3.375), (E, 1.5 + 3.75), (F, 1.5 + 4.125),
    
    # Bar 4 (Walking F scale again)
    (F, 1.5 + 4.5), (G, 1.5 + 4.875), (A, 1.5 + 5.25), (Bb, 1.5 + 5.625),
    (C, 1.5 + 6.0), (D, 1.5 + 6.375), (E, 1.5 + 6.75), (F, 1.5 + 7.125)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + NOTE_DURATION))

# ------------------------------
# Piano (Bars 2–4): 7th chord comping on 2 and 4
# ------------------------------
# F7 = F, A, C, E (dominant 7th)
# Comp on 2 and 4 of each bar
# Bar 2: F7 on beat 2
# Bar 3: G7 on beat 2
# Bar 4: C7 on beat 2

def add_chord_notes(chord, bar, time_offset):
    start = BAR_START + (bar - 2) * BAR_DURATION + time_offset
    for pitch in chord:
        piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + NOTE_DURATION * 0.5))

# F7 on beat 2 of bar 2
F7 = [F, A, C, E]
add_chord_notes(F7, 2, NOTE_DURATION)

# G7 on beat 2 of bar 3
G7 = [G, B, D, F]
add_chord_notes(G7, 3, NOTE_DURATION)

# C7 on beat 2 of bar 4
C7 = [C, E, G, B]
add_chord_notes(C7, 4, NOTE_DURATION)

# ------------------------------
# Sax (Bars 2–4): Haunting motif
# ------------------------------
# Tenor Sax: F -> G -> E -> D -> F (motif)
# Start on beat 1 of bar 2, leave it hanging, return on beat 3

# Notes in MIDI values
F = 65
G = 67
E = 64
D = 62
A = 69

# First pass of motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=F, start=BAR_START, end=BAR_START + NOTE_DURATION))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=G, start=BAR_START + NOTE_DURATION, end=BAR_START + NOTE_DURATION * 2))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=E, start=BAR_START + NOTE_DURATION * 2, end=BAR_START + NOTE_DURATION * 3))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=D, start=BAR_START + NOTE_DURATION * 3, end=BAR_START + NOTE_DURATION * 4))

# Second pass of motif (return on beat 3 of bar 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=F, start=BAR_START + NOTE_DURATION * 2, end=BAR_START + NOTE_DURATION * 3))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=G, start=BAR_START + NOTE_DURATION * 3, end=BAR_START + NOTE_DURATION * 4))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=E, start=BAR_START + NOTE_DURATION * 4, end=BAR_START + NOTE_DURATION * 5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=D, start=BAR_START + NOTE_DURATION * 5, end=BAR_START + NOTE_DURATION * 6))

# ------------------------------
# Add instruments to MIDI
# ------------------------------
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
