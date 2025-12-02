
import pretty_midi

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
track_bass = pretty_midi.Instrument(program=33)  # Double Bass
track_piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
track_drums = pretty_midi.Instrument(program=10)  # Acoustic Drum Set
track_sax = pretty_midi.Instrument(program=64)  # Tenor Saxophone

# Constants
BPM = 160
BEAT_DURATION = 60.0 / BPM  # Seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
NOTES_PER_BAR = 4
MIDI_DURATION = BAR_DURATION  # Each bar is 6 seconds long

# Time in seconds for each bar
bar_start_times = [0, BAR_DURATION, 2 * BAR_DURATION, 3 * BAR_DURATION]

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = bar_start_times[0] + i * (BAR_DURATION / 4)
    # Kick
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15))
    # Snare
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + BAR_DURATION / 4, end=time + BAR_DURATION / 4 + 0.15))
    # Hihat
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.125, end=time + 0.25))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.25, end=time + 0.375))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.5))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.5, end=time + 0.625))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.625, end=time + 0.75))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 0.875))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.875, end=time + BAR_DURATION / 4))

# Bar 2: Marcus on bass (walking line in Dm, roots and fifths with chromatic approaches)
# Dm: D, F, A
# Bar 2: D -> F -> Eb -> A
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[1], end=bar_start_times[1] + 0.5)
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[1] + 0.5, end=bar_start_times[1] + 1.0)
note_eb = pretty_midi.Note(velocity=100, pitch=61, start=bar_start_times[1] + 1.0, end=bar_start_times[1] + 1.5)
note_a = pretty_midi.Note(velocity=100, pitch=67, start=bar_start_times[1] + 1.5, end=bar_start_times[1] + 2.0)
track_bass.notes.extend([note_d, note_f, note_eb, note_a])

# Bar 2: Diane on piano - Dm7 (D F A C), then F7 (F A C E), then Eb7 (Eb G Bb D), then A7 (A C E G)
# Open voicing, resolve on last note of bar
# Dm7: D, A, F, C
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[1], end=bar_start_times[1] + 0.75)
note_a = pretty_midi.Note(velocity=100, pitch=67, start=bar_start_times[1], end=bar_start_times[1] + 0.75)
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[1], end=bar_start_times[1] + 0.75)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=bar_start_times[1], end=bar_start_times[1] + 0.75)
track_piano.notes.extend([note_d, note_a, note_f, note_c])

# F7: F, C, A, E
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[1] + 0.75, end=bar_start_times[1] + 1.5)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=bar_start_times[1] + 0.75, end=bar_start_times[1] + 1.5)
note_a = pretty_midi.Note(velocity=100, pitch=67, start=bar_start_times[1] + 0.75, end=bar_start_times[1] + 1.5)
note_e = pretty_midi.Note(velocity=100, pitch=64 + 5, start=bar_start_times[1] + 0.75, end=bar_start_times[1] + 1.5)  # F7: F A C E
track_piano.notes.extend([note_f, note_c, note_a, note_e])

# Eb7: Eb, Bb, G, D
note_eb = pretty_midi.Note(velocity=100, pitch=61, start=bar_start_times[1] + 1.5, end=bar_start_times[1] + 2.25)
note_bb = pretty_midi.Note(velocity=100, pitch=58, start=bar_start_times[1] + 1.5, end=bar_start_times[1] + 2.25)
note_g = pretty_midi.Note(velocity=100, pitch=67 - 5, start=bar_start_times[1] + 1.5, end=bar_start_times[1] + 2.25)
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[1] + 1.5, end=bar_start_times[1] + 2.25)
track_piano.notes.extend([note_eb, note_bb, note_g, note_d])

# Bar 3: Marcus on bass - continue walking line
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[2], end=bar_start_times[2] + 0.5)
note_e = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[2] + 0.5, end=bar_start_times[2] + 1.0)
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[2] + 1.0, end=bar_start_times[2] + 1.5)
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[2] + 1.5, end=bar_start_times[2] + 2.0)
track_bass.notes.extend([note_f, note_e, note_d, note_f])

# Bar 3: Diane on piano - A7 (A C E G)
note_a = pretty_midi.Note(velocity=100, pitch=67, start=bar_start_times[2], end=bar_start_times[2] + 0.75)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=bar_start_times[2], end=bar_start_times[2] + 0.75)
note_e = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[2], end=bar_start_times[2] + 0.75)
note_g = pretty_midi.Note(velocity=100, pitch=67 - 5, start=bar_start_times[2], end=bar_start_times[2] + 0.75)
track_piano.notes.extend([note_a, note_c, note_e, note_g])

# Bar 4: Marcus on bass - resolve on D
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[3], end=bar_start_times[3] + 1.0)
track_bass.notes.append(note_d)

# Bar 4: Diane on piano - Dm7 (D F A C), resolve on last note
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[3], end=bar_start_times[3] + 0.75)
note_f = pretty_midi.Note(velocity=100, pitch=64, start=bar_start_times[3], end=bar_start_times[3] + 0.75)
note_a = pretty_midi.Note(velocity=100, pitch=67, start=bar_start_times[3], end=bar_start_times[3] + 0.75)
note_c = pretty_midi.Note(velocity=100, pitch=60, start=bar_start_times[3], end=bar_start_times[3] + 0.75)
track_piano.notes.extend([note_d, note_f, note_a, note_c])

# Bar 4: Little Ray on drums - same pattern as bar 1, but with emphasis on 3 and 4
for i in range(4):
    time = bar_start_times[3] + i * (BAR_DURATION / 4)
    # Kick
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.15))
    # Snare
    track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + BAR_DURATION / 4, end=time + BAR_DURATION / 4 + 0.15))
    # Hihat
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.125, end=time + 0.25))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.25, end=time + 0.375))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.375, end=time + 0.5))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.5, end=time + 0.625))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.625, end=time + 0.75))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.75, end=time + 0.875))
    track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + 0.875, end=time + BAR_DURATION / 4))

# Bar 4: You on sax - short motif: D, Eb, D, Bb (0.5s each)
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[3], end=bar_start_times[3] + 0.5)
note_eb = pretty_midi.Note(velocity=100, pitch=61, start=bar_start_times[3] + 0.5, end=bar_start_times[3] + 1.0)
note_d = pretty_midi.Note(velocity=100, pitch=62, start=bar_start_times[3] + 1.0, end=bar_start_times[3] + 1.5)
note_bb = pretty_midi.Note(velocity=100, pitch=58, start=bar_start_times[3] + 1.5, end=bar_start_times[3] + 2.0)
track_sax.notes.extend([note_d, note_eb, note_d, note_bb])

# Add tracks to MIDI
midi.instruments.append(track_bass)
midi.instruments.append(track_piano)
midi.instruments.append(track_drums)
midi.instruments.append(track_sax)

# Save the MIDI file
midi.write("dante_intro.mid")
