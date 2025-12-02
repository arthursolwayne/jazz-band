
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 1.5
beat_length = 0.375

# --- Bar 1: Little Ray alone (0.0 - 1.5s)
# Setup with tension and space. Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# Dynamic variation to create a question, a breath before the storm.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=1.125, end=1.5))

# Hihat on every eighth
for i in range(8):
    start = i * beat_length
    end = start + beat_length
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=drum_notes['hihat'], start=start, end=end))

# --- Bars 2-4: Full quartet (1.5 - 6.0s)
# Saxophone motif: start with a short phrase that feels incomplete, leave it hanging.
# Bass: Walking line in Fm, chromatic approaches, never the same note twice.
# Piano: 7th chords, comp on 2 and 4, stay out of the way but keep the motion.
# Drums: Continue the rhythm, fill the bar with energy.

# Time for bars 2-4 (1.5 - 6.0s)
start_time = 1.5

# Saxophone motif: Fm7 -> Bb -> Eb -> Ab — a descending line with tension.
# First bar (Bar 2): Fm7 -> Bb (half note) -> Eb (eighth note) -> Ab (eighth note)
# Leave it hanging on Ab, not resolving immediately.

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=start_time, end=start_time + 1.0),   # F (Fm7)
    pretty_midi.Note(velocity=95, pitch=80, start=start_time + 1.0, end=start_time + 1.125), # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=start_time + 1.125, end=start_time + 1.25), # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=start_time + 1.25, end=start_time + 1.5), # Ab (hangs)
]

sax.notes.extend(sax_notes)

# Bass: Walking line in Fm, chromatic approaches
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C -> D -> Eb -> E -> F
# Use open strings when possible, unrelenting motion

bass_notes = [
    pretty_midi.Note(velocity=70, pitch=70, start=start_time, end=start_time + 0.375),    # F
    pretty_midi.Note(velocity=70, pitch=69, start=start_time + 0.375, end=start_time + 0.75), # Gb
    pretty_midi.Note(velocity=70, pitch=71, start=start_time + 0.75, end=start_time + 1.125), # G
    pretty_midi.Note(velocity=70, pitch=72, start=start_time + 1.125, end=start_time + 1.5), # Ab

    pretty_midi.Note(velocity=70, pitch=74, start=start_time + 1.5, end=start_time + 1.875), # A
    pretty_midi.Note(velocity=70, pitch=75, start=start_time + 1.875, end=start_time + 2.25), # Bb
    pretty_midi.Note(velocity=70, pitch=77, start=start_time + 2.25, end=start_time + 2.625), # B
    pretty_midi.Note(velocity=70, pitch=79, start=start_time + 2.625, end=start_time + 3.0), # C

    pretty_midi.Note(velocity=70, pitch=81, start=start_time + 3.0, end=start_time + 3.375), # D
    pretty_midi.Note(velocity=70, pitch=83, start=start_time + 3.375, end=start_time + 3.75), # Eb
    pretty_midi.Note(velocity=70, pitch=84, start=start_time + 3.75, end=start_time + 4.125), # E
    pretty_midi.Note(velocity=70, pitch=87, start=start_time + 4.125, end=start_time + 4.5), # F
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on beat 2 and 4 (base 60 velocity)
# Fm7 (F, Ab, C, Eb) | Bb7 (Bb, D, F, Ab) | Eb7 (Eb, G, Bb, Db) | Ab7 (Ab, C, Eb, G)

piano_notes = []

# Bar 2: Fm7 on beat 2
piano_notes.append(pretty_midi.Note(velocity=60, pitch=87, start=start_time + 0.75, end=start_time + 1.125))  # F
piano_notes.append(pretty_midi.Note(velocity=60, pitch=71, start=start_time + 0.75, end=start_time + 1.125))  # Ab
piano_notes.append(pretty_midi.Note(velocity=60, pitch=76, start=start_time + 0.75, end=start_time + 1.125))  # C
piano_notes.append(pretty_midi.Note(velocity=60, pitch=76, start=start_time + 0.75, end=start_time + 1.125))  # Eb (D#)

# Bar 3: Bb7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=60, pitch=80, start=start_time + 2.625, end=start_time + 3.0))  # Bb
piano_notes.append(pretty_midi.Note(velocity=60, pitch=74, start=start_time + 2.625, end=start_time + 3.0))  # D
piano_notes.append(pretty_midi.Note(velocity=60, pitch=87, start=start_time + 2.625, end=start_time + 3.0))  # F
piano_notes.append(pretty_midi.Note(velocity=60, pitch=71, start=start_time + 2.625, end=start_time + 3.0))  # Ab

# Bar 4: Eb7 on beat 2
piano_notes.append(pretty_midi.Note(velocity=60, pitch=76, start=start_time + 3.75, end=start_time + 4.125))  # Eb
piano_notes.append(pretty_midi.Note(velocity=60, pitch=81, start=start_time + 3.75, end=start_time + 4.125))  # G
piano_notes.append(pretty_midi.Note(velocity=60, pitch=80, start=start_time + 3.75, end=start_time + 4.125))  # Bb
piano_notes.append(pretty_midi.Note(velocity=60, pitch=79, start=start_time + 3.75, end=start_time + 4.125))  # Db

# Bar 4: Ab7 on beat 4
piano_notes.append(pretty_midi.Note(velocity=60, pitch=71, start=start_time + 4.875, end=start_time + 5.25))  # Ab
piano_notes.append(pretty_midi.Note(velocity=60, pitch=79, start=start_time + 4.875, end=start_time + 5.25))  # C
piano_notes.append(pretty_midi.Note(velocity=60, pitch=76, start=start_time + 4.875, end=start_time + 5.25))  # Eb
piano_notes.append(pretty_midi.Note(velocity=60, pitch=81, start=start_time + 4.875, end=start_time + 5.25))  # G

piano.notes.extend(piano_notes)

# Drums continue for full 4 bars, same pattern as bar 1
for i in range(4):
    bar_start = start_time + i * bar_length
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=bar_start, end=bar_start + beat_length))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['kick'], start=bar_start + 0.75, end=bar_start + 1.125))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=bar_start + beat_length, end=bar_start + 0.75 + beat_length))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=bar_start + 1.125, end=bar_start + 1.5 + beat_length))
    
    # Hihat on every eighth
    for j in range(8):
        hit_start = bar_start + j * beat_length
        hit_end = hit_start + beat_length
        drums.notes.append(pretty_midi.Note(velocity=60, pitch=drum_notes['hihat'], start=hit_start, end=hit_end))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro_Fm.mid")
