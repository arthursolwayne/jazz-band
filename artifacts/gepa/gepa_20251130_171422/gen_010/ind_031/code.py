
import pretty_midi

# Initialize a PrettyMIDI object with 160 BPM (4/4 time)
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Add instruments
# 1. Drums (Little Ray)
drums = pretty_midi.Instrument(program=10, is_drum=True)
pm.instruments.append(drums)

# 2. Bass (Marcus)
bass = pretty_midi.Instrument(program=33)
pm.instruments.append(bass)

# 3. Piano (Diane)
piano = pretty_midi.Instrument(program=0)
pm.instruments.append(piano)

# 4. Tenor Sax (Dante)
tenor_sax = pretty_midi.Instrument(program=67)
pm.instruments.append(tenor_sax)

# Define time: 160 BPM, 4/4 time
# 4 bars = 6 seconds
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds
# 1 sixteenth note = 0.09375 seconds

# Bar 1: Little Ray (drums) — sparse, slow build
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar length: 1.5 seconds

# Bar 1: Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.09375))  # Kick on beat 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=0.84375)) # Kick on beat 3

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.46875)) # Snare on beat 2
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.21875)) # Snare on beat 4

# Hihat on every eighth
for i in range(8):
    hihat_start = i * 0.09375
    hihat_end = hihat_start + 0.09375
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=hihat_start, end=hihat_end))

# Bar 2: Tenor Sax enters with a short, emotional motif in Dm7 (D, F, Ab, C)
# Start at 1.5 seconds
note_lengths = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.125]  # 8 notes + 1 rest
note_pitches = [62, 65, 67, 72, 67, 72, 65, 62, 0]  # D, F, Ab, C (then back, then rest)
note_velocities = [100, 100, 100, 100, 100, 100, 100, 100, 0]  # All full, last one is a rest

for i in range(9):
    start = 1.5 + sum(note_lengths[:i])
    end = start + note_lengths[i]
    tenor_sax.notes.append(pretty_midi.Note(
        velocity=note_velocities[i],
        pitch=note_pitches[i],
        start=start,
        end=end
    ))

# Bar 3: Bass (Marcus) — walking line with chromatic passing tones
# Dm7 walking line: D, Eb, F, G, A, Bb, C, D
# Starts on beat 1 of bar 2 (1.5s)
bass_notes = [62, 63, 65, 67, 69, 70, 72, 62]
bass_lengths = [0.375] * 8
for i, pitch in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start, end=end))

# Bar 3: Diane (piano) — 7th chords, comp on 2 and 4
# Dm7: D, F, Ab, C
# Play on beats 2 and 4 of bar 2 (1.875s and 2.25s)
piano_notes = [62, 65, 67, 72]  # Dm7
for i, pitch in enumerate(piano_notes):
    start = 1.875 + i * 0.09375
    end = start + 0.09375
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Bar 4: Little Ray fills the bar with hihat and kick
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.09375))  # Kick on beat 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=3.84375)) # Kick on beat 3

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.46875)) # Snare on beat 2
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.21875)) # Snare on beat 4

# Hihat on every eighth
for i in range(8):
    hihat_start = 3.0 + i * 0.09375
    hihat_end = hihat_start + 0.09375
    drums.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=hihat_start, end=hihat_end))

# Write MIDI to file
pm.write("dante_intro.mid")
