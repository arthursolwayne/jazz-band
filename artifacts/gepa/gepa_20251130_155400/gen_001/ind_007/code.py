
import pretty_midi

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the time per bar in seconds (4/4 at 160 BPM)
BEAT_DURATION = 0.375
BAR_DURATION = 4 * BEAT_DURATION

# Function to convert time to seconds
def to_time(time_in_beats):
    return time_in_beats * BEAT_DURATION

# Define instruments
sax_program = pretty_midi.instrument_name_to_program("Tenor Saxophone")
piano_program = pretty_midi.instrument_name_to_program("Acoustic Piano")
bass_program = pretty_midi.instrument_name_to_program("Double Bass")
drum_program = pretty_midi.instrument_name_to_program("Acoustic Drum Kit")

# Create instrument tracks
sax = pretty_midi.Instrument(program=sax_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
drums = pretty_midi.Instrument(program=drum_program)

# Add instruments to the MIDI file
pm.instruments.append(sax)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(drums)

# Drum pattern for Bar 1 (only kick, snare, hihat)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Note numbers: Kick (36), Snare (38), Hihat (42)
for bar in range(1):
    time = to_time(0) + bar * BAR_DURATION
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time + beat * BEAT_DURATION, end=time + beat * BEAT_DURATION + 0.05)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time + beat * BEAT_DURATION, end=time + beat * BEAT_DURATION + 0.05)
        drums.notes.append(note)
    # Hihat on every eighth
    for beat in range(0, 4):
        for eighth in [0, 1]:
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + beat * BEAT_DURATION + eighth * BEAT_DURATION / 2,
                                    end=time + beat * BEAT_DURATION + eighth * BEAT_DURATION / 2 + 0.025)
            drums.notes.append(note)

# Saxophone motif (Bar 2-4)
# Motif: Fm7 -> Bb -> Ab -> Fm7 (as a melodic idea, not a chord)
# Fm7: F, Ab, Bb, Db (used as melody pitches)
# Notes in time: start on beat 1 of bar 2

sax_notes = [
    # Bar 2
    (to_time(4 + 0), 64),  # F4 (64)
    (to_time(4 + 1), 71),  # Bb4 (71)
    (to_time(4 + 2), 69),  # Ab4 (69)
    # Bar 3
    (to_time(8 + 0), 64),  # F4
    (to_time(8 + 1), 69),  # Ab4
    (to_time(8 + 2), 71),  # Bb4
    # Bar 4
    (to_time(12 + 0), 64),  # F4
    (to_time(12 + 1), 69),  # Ab4
    (to_time(12 + 2), 71),  # Bb4
    (to_time(12 + 3), 0),   # Rest on 4
]

for start, pitch in sax_notes:
    if pitch != 0:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
        sax.notes.append(note)

# Bass line: chromatic walking bass in Fm (F, Gb, G, Ab, A, Bb, B, C)
# Bar 2: F -> Gb -> G -> Ab
# Bar 3: A -> Bb -> B -> C
# Bar 4: Db -> D -> Eb -> F (resolution to Fm)

bass_notes = [
    # Bar 2
    (to_time(4 + 0), 64),  # F3
    (to_time(4 + 1), 65),  # Gb3
    (to_time(4 + 2), 67),  # G3
    (to_time(4 + 3), 69),  # Ab3
    # Bar 3
    (to_time(8 + 0), 71),  # A3
    (to_time(8 + 1), 72),  # Bb3
    (to_time(8 + 2), 74),  # B3
    (to_time(8 + 3), 76),  # C4
    # Bar 4
    (to_time(12 + 0), 67),  # Db4
    (to_time(12 + 1), 69),  # D4
    (to_time(12 + 2), 71),  # Eb4
    (to_time(12 + 3), 64),  # F4
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano chords: Fm7 on beat 2 and 4 of each bar
# Fm7 = F, Ab, Bb, Db (chord)

def add_piano_chord(time, chord_notes):
    for pitch in chord_notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Chord: Fm7 = F, Ab, Bb, Db
Fm7 = [53, 56, 58, 60]  # F3, Ab3, Bb3, Db4

# Bar 2: beat 2
add_piano_chord(to_time(4 + 1), Fm7)
# Bar 2: beat 4
add_piano_chord(to_time(4 + 3), Fm7)
# Bar 3: beat 2
add_piano_chord(to_time(8 + 1), Fm7)
# Bar 3: beat 4
add_piano_chord(to_time(8 + 3), Fm7)
# Bar 4: beat 2
add_piano_chord(to_time(12 + 1), Fm7)
# Bar 4: beat 4
add_piano_chord(to_time(12 + 3), Fm7)

# Write MIDI file
pm.write("dante_intro.mid")
