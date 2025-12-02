
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Create instruments
drums = Instrument(program=Program.DRUMS)
bass = Instrument(program=Program.BASS, is_drum=False)
piano = Instrument(program=Program.PIANO, is_drum=False)
sax = Instrument(program=Program.SAXOPHONE, is_drum=False)

pm.instruments = [drums, bass, piano, sax]

# Define note durations and timing
BAR_DURATION = 1.5  # in seconds (160 BPM, 4/4 time)
BEAT_DURATION = 0.375  # seconds per beat
NOTE_DURATION = BEAT_DURATION * 0.5  # 8th note

# -----------------------------
# DRUMS (Little Ray)
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: same pattern
# -----------------------------
for bar in range(4):
    bar_start = bar * BAR_DURATION
    # Kick (Bass Drum 36)
    kick_times = [bar_start + BEAT_DURATION * i for i in [0, 2]]
    for t in kick_times:
        note = Note(velocity=100, start=t, end=t + NOTE_DURATION)
        drums.notes.append(note)
    # Snare (Snare Drum 38)
    snare_times = [bar_start + BEAT_DURATION * i for i in [1, 3]]
    for t in snare_times:
        note = Note(velocity=100, start=t, end=t + NOTE_DURATION)
        drums.notes.append(note)
    # Hihat (Hihat Closed 42)
    hihat_times = [bar_start + BEAT_DURATION * i for i in range(4)]
    for t in hihat_times:
        note = Note(velocity=90, start=t, end=t + NOTE_DURATION)
        drums.notes.append(note)

# -----------------------------
# BASS (Marcus)
# Walking line with chromatic approaches, F minor scale (F, Gb, G, Ab, A, Bb, B)
# Bar 1: F -> Gb -> G -> Ab
# Bar 2: A -> Bb -> B -> C
# Bar 3: Db -> D -> Eb -> E
# Bar 4: F -> Gb -> G -> Ab (repeat)
# -----------------------------
note_map = {
    'F': 78, 'Gb': 77, 'G': 79, 'Ab': 80,
    'A': 81, 'Bb': 82, 'B': 83, 'C': 84,
    'Db': 76, 'D': 85, 'Eb': 86, 'E': 87
}

for bar in range(4):
    bar_start = bar * BAR_DURATION
    # Bar 1: F -> Gb -> G -> Ab
    if bar == 0:
        notes = ['F', 'Gb', 'G', 'Ab']
    # Bar 2: A -> Bb -> B -> C
    elif bar == 1:
        notes = ['A', 'Bb', 'B', 'C']
    # Bar 3: Db -> D -> Eb -> E
    elif bar == 2:
        notes = ['Db', 'D', 'Eb', 'E']
    # Bar 4: F -> Gb -> G -> Ab
    else:
        notes = ['F', 'Gb', 'G', 'Ab']

    for i, note in enumerate(notes):
        time = bar_start + i * BEAT_DURATION
        pitch = note_map[note]
        velocity = 90
        note = Note(velocity=velocity, start=time, end=time + NOTE_DURATION)
        bass.notes.append(note)

# -----------------------------
# PIANO (Diane)
# Comp on 2 and 4 with 7th chords in F minor: F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab)
# Bar 1: F7 on beat 2, Bb7 on beat 4
# Bar 2: F7 on beat 2, Bb7 on beat 4
# Bar 3: F7 on beat 2, Bb7 on beat 4
# Bar 4: F7 on beat 2, Bb7 on beat 4
# -----------------------------
# F7 chord: F, A, C, Eb
# Bb7 chord: Bb, D, F, Ab
def add_piano_chord(chord, time):
    for pitch in chord:
        note = Note(velocity=95, start=time, end=time + NOTE_DURATION)
        piano.notes.append(note)

for bar in range(4):
    bar_start = bar * BAR_DURATION
    # F7 on beat 2
    add_piano_chord([78, 82, 84, 80], bar_start + BEAT_DURATION * 1)
    # Bb7 on beat 4
    add_piano_chord([82, 86, 78, 84], bar_start + BEAT_DURATION * 3)

# -----------------------------
# SAX (You)
# Melody: One short motif, F -> Eb -> D -> F
# Start on bar 2, leave it hanging, return on bar 4
# -----------------------------
# F (78), Eb (80), D (85), F (78)
# Bar 2: note on beat 1
# Bar 3: rest
# Bar 4: note on beat 1 and then resolution on beat 3

# Bar 2, beat 1: F
note = Note(velocity=105, start=BAR_DURATION * 1, end=BAR_DURATION * 1 + NOTE_DURATION)
sax.notes.append(note)

# Bar 4, beat 1: Eb
note = Note(velocity=105, start=BAR_DURATION * 3, end=BAR_DURATION * 3 + NOTE_DURATION)
sax.notes.append(note)

# Bar 4, beat 3: D
note = Note(velocity=105, start=BAR_DURATION * 3 + BEAT_DURATION * 2, end=BAR_DURATION * 3 + BEAT_DURATION * 2 + NOTE_DURATION)
sax.notes.append(note)

# Bar 4, beat 4: F
note = Note(velocity=105, start=BAR_DURATION * 3 + BEAT_DURATION * 3, end=BAR_DURATION * 3 + BEAT_DURATION * 3 + NOTE_DURATION)
sax.notes.append(note)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
