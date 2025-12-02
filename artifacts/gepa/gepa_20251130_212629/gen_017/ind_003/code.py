
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor (Fm)
# The key signature for Fm is one flat (Bb)
pm.key_signature = pretty_midi.KeySignature(key_signature=pretty_midi.KeySignature.F_MINOR)

# Create instruments
drums = pretty_midi.Instrument(program=10)  # Drums
bass = pretty_midi.Instrument(program=33)   # Electric Bass
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano
sax = pretty_midi.Instrument(program=69)   # Tenor Saxophone

pm.instruments = [drums, bass, piano, sax]

# Define the tempo and time resolution
tempo = 160.0  # BPM
time_per_beat = 60.0 / tempo
time_per_bar = time_per_beat * 4
time_per_eighth = time_per_beat / 2

# Define the note durations in seconds
sixteenth = time_per_beat / 4
eighth = time_per_beat / 2
quarter = time_per_beat
half = time_per_beat * 2

# ---------------------------
# DRUMS - Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: open space, just hihat
# Bars 2-4: full kit

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375))  # Hihat (closed)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))  # Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0))    # Hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0))

# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))  # Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0))

# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375))  # Kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.75))  # Snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.75))    # Hihat

# ---------------------------
# BASS - Marcus
# Walking line in Fm: F, Gb, Ab, A, Bb, B, C, Db
# Bars 1-4

# Bar 1: F -> Gb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=0.375))  # F (3rd octave)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=0.375, end=0.75))  # Gb

# Bar 2: Ab -> A
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=0.75, end=1.125))  # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.125, end=1.5))   # A

# Bar 3: Bb -> B
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25))  # B

# Bar 4: C -> Db
bass.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))  # C
bass.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0))   # Db

# ---------------------------
# PIANO - Diane
# 7th chords on 2 and 4 in Fm
# F7 (F, Ab, Bb, C), Bb7 (Bb, Db, Eb, F)

# Bar 1: nothing, space
# Bar 2: F7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0))  # Ab
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0))  # C

# Bar 3: nothing
# Bar 4: Bb7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0))  # F

# ---------------------------
# SAX - You
# Motif: F -> Ab -> Bb -> C (sixteenth notes)
# Start on beat 1, leave it hanging, return on beat 4

# Bar 1: F, Ab (on beat 1 and 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=0.375))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=0.375, end=0.75))  # Ab

# Bar 4: Bb, C (on beat 1 and 2)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75))  # C

# Save the MIDI file
pm.write("dante_intro.mid")
