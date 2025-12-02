
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instrument tracks
drums = pretty_midi.Instrument(program=10)  # Drums
sax = pretty_midi.Instrument(program=64)    # Tenor sax
bass = pretty_midi.Instrument(program=33)   # Electric bass
piano = pretty_midi.Instrument(program=0)   # Acoustic piano

# Define time in seconds
bar_length = 1.5  # 160 BPM = 60 / 160 * 4 = 1.5s per bar
beat_length = 0.375  # 60 / 160 = 0.375s per beat

# ----------------------
# Bar 1: Little Ray (Drums)
# ----------------------
# Kick on 1
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375))
# Snare on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))
# Hihat on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875))

pm.instruments.append(drums)

# ----------------------
# Bar 2: Full Band Enters
# ----------------------
# Tenor Sax (You) - 3-note phrase: F -> A -> Bb (but not quite resolved)
# Start on beat 2, leave it hanging
sax.notes.append(pretty_midi.Note(velocity=105, pitch=65, start=0.375, end=0.75))  # F (tenor sax)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=0.75, end=1.125)) # A
sax.notes.append(pretty_midi.Note(velocity=95, pitch=69, start=1.125, end=1.5))   # Bb

# Bass (Marcus) - Chromatic walking line (F -> G -> Ab -> A)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=0.0, end=0.375))   # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=0.375, end=0.75))   # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=50, start=0.75, end=1.125))   # Ab
bass.notes.append(pretty_midi.Note(velocity=80, pitch=51, start=1.125, end=1.5))    # A

# Piano (Diane) - 7th chords on beats 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=0.375, end=0.75))  # F7 (F, A, C, Eb)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=0.375, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=0.375, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=0.375, end=0.75))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875))  # F7 again on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875))

# ----------------------
# Bar 3 and 4: Empty for now (You finish the phrase in Bar 2, leave it hanging)
# ----------------------
# No more notes added here — just space, tension.

# Add instruments to the MIDI object
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)

# Save the MIDI file
pm.write("F_major_intro.mid")

print("MIDI file 'F_major_intro.mid' created successfully.")
