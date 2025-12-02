
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(1, 0.0)]  # F major

# Define instruments
# Tenor Sax (program 64)
sax_part = pretty_midi.Instrument(program=64)
pm.instruments.append(sax_part)

# Bass (program 33)
bass_part = pretty_midi.Instrument(program=33)
pm.instruments.append(bass_part)

# Piano (program 0)
piano_part = pretty_midi.Instrument(program=0)
pm.instruments.append(piano_part)

# Drums (program 128)
drums_part = pretty_midi.Instrument(program=128)
pm.instruments.append(drums_part)

# Time in seconds per bar (160 BPM, 4/4)
bar_length = 60.0 / 160.0 * 4  # 6 seconds per 4 bars

# Define the timing for each bar
bar_start = 0.0
bar_end = bar_length

# -------------------
# Bar 1: Drums only (set the scene)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# 160 BPM = 0.375 sec per beat
# Bar = 4 beats = 1.5 seconds

# Kick on beat 1 (0.0) and beat 3 (1.125)
drums_part.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.1))
drums_part.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.1))

# Snare on beat 2 (0.75) and beat 4 (1.5)
drums_part.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.75 + 0.1))
drums_part.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.5 + 0.1))

# Hi-Hat on every eighth note (0.0, 0.375, 0.75, 1.125, 1.5, ...)
for i in range(8):
    start = bar_start + i * 0.375
    end = start + 0.05
    drums_part.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# -------------------
# Bar 2-4: Full ensemble

# Tenor Sax: A short, singable motif (your moment)
# F major scale: F, G, A, Bb, C, D, Eb
# Let's craft a motif that starts on F, moves to Bb, and ends on A — creates a question

# Bar 2
# Note durations: 0.25, 0.5, 0.25, 0.5, 0.5
# F (0.25), Bb (0.5), A (0.25), Bb (0.5), G (0.5)
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 1.5, end=bar_start + 1.5 + 0.25))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.75, end=bar_start + 1.75 + 0.5))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=bar_start + 2.25, end=bar_start + 2.25 + 0.25))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 2.5, end=bar_start + 2.5 + 0.5))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 3.0, end=bar_start + 3.0 + 0.5))

# Bar 3: Continue the motif with a variation
# C, Bb, A, G, F (slower, descending with unique durations)
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 3.5, end=bar_start + 3.5 + 0.5))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 4.0, end=bar_start + 4.0 + 0.25))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=bar_start + 4.25, end=bar_start + 4.25 + 0.25))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 4.5, end=bar_start + 4.5 + 0.25))
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 4.75, end=bar_start + 4.75 + 0.25))

# Bar 4: Resolution — ends on A (70) with a lingering note
sax_part.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=bar_start + 5.0, end=bar_start + 5.0 + 0.75))  # 0.75 sec hold

# -------------------
# Bass: Walking line, chromatic approaches, never the same note twice
# Starts on F, then Ab, Bb, B, etc. — chromatic walks

# Bar 2
# F (0.25), Ab (0.25), Bb (0.25), B (0.25)
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=bar_start + 1.5, end=bar_start + 1.5 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bar_start + 1.75, end=bar_start + 1.75 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bar_start + 2.0, end=bar_start + 2.0 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=bar_start + 2.25, end=bar_start + 2.25 + 0.25))

# Bar 3
# C (0.25), Db (0.25), D (0.25), Eb (0.25)
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar_start + 2.5, end=bar_start + 2.5 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=bar_start + 2.75, end=bar_start + 2.75 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar_start + 3.0, end=bar_start + 3.0 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=bar_start + 3.25, end=bar_start + 3.25 + 0.25))

# Bar 4
# F (0.25), G (0.25), Ab (0.25), A (0.25)
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=48, start=bar_start + 3.5, end=bar_start + 3.5 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=bar_start + 3.75, end=bar_start + 3.75 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=bar_start + 4.0, end=bar_start + 4.0 + 0.25))
bass_part.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=bar_start + 4.25, end=bar_start + 4.25 + 0.25))

# -------------------
# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 on beat 2 (0.75)
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 1.75, end=bar_start + 1.75 + 0.25))  # F
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.75, end=bar_start + 1.75 + 0.25))  # A
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 1.75, end=bar_start + 1.75 + 0.25))  # C
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 1.75, end=bar_start + 1.75 + 0.25))  # Bb

# Bar 4: F7 on beat 2 (0.75) again
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 4.75, end=bar_start + 4.75 + 0.25))  # F
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 4.75, end=bar_start + 4.75 + 0.25))  # A
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 4.75, end=bar_start + 4.75 + 0.25))  # C
piano_part.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 4.75, end=bar_start + 4.75 + 0.25))  # Bb

# -------------------
# Write MIDI file
pm.write("wayne_intro.mid")

print("MIDI file 'wayne_intro.mid' has been created.")
