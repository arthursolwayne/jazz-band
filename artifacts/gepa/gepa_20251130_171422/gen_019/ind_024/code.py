
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum notes: kick=36, snare=38, hihat=42
drum_kick = 36
drum_snare = 38
drum_hihat = 42

# Time in seconds per bar
bar_length = 1.5  # 160 BPM, 4/4 time
note_length = 0.375  # 1/4 note in seconds (160 BPM)

# =================
# BAR 1: DRUMS ONLY (0.0 - 1.5s)
# Little Ray sets the mood with space and precision

# Kick on 1 and 3 (beats 0 and 2 of the bar)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_kick, start=0.75, end=1.125))

# Snare on 2 and 4 (beats 1 and 3 of the bar)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_snare, start=1.125, end=1.5))

# Hi-hat on every eighth note
for i in range(8):
    start = i * note_length
    end = start + note_length
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_hihat, start=start, end=end))

# =================
# BAR 2: FULL QUARTET (1.5 - 3.0s)
# Saxophone enters with a short, emotional motif in D.

# D major scale: D E F# G A B C#
# Motif: D - F# - G - B (ascending minor third, then major third)

# D (C4 in MIDI) at beat 0.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))

# F# (E4 in MIDI) at beat 0.75
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))

# G (F#4 in MIDI) at beat 1.5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))

# Bass: Chromatic walk under the melody (D - C - B - A - G - F# - E - D)
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + i * note_length
    end = start + note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Angry, aggressive comping on 7th chords on the offbeats
# Use D7 (D F# A C) on beats 2 and 4
# Offbeats: 0.75, 1.5, 2.25, 3.0

# Beat 0.75 (bar 2, beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))  # C

# Beat 1.5 (bar 2, beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0))  # C

# =================
# BAR 3: FULL QUARTET (3.0 - 4.5s)
# Repeat the motif with a slight variation or resolution

# D (C4 in MIDI) at beat 0.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375))

# F# (E4 in MIDI) at beat 0.75
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75))

# G (F#4 in MIDI) at beat 1.5
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125))

# Bass: Repeat the chromatic motion
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
for i, pitch in enumerate(bass_notes):
    start = 3.0 + i * note_length
    end = start + note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Repeat the 7th chords on offbeats
# Beat 0.75 (bar 3, beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125))  # C

# Beat 1.5 (bar 3, beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5))  # C

# =================
# BAR 4: FULL QUARTET (4.5 - 6.0s)
# Finish the motif, leave it hanging. Saxophone ends with a sustained note.

# D (C4 in MIDI) at beat 0.0
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0))  # Sustained D

# Bass: Repeat the chromatic motion
bass_notes = [62, 61, 60, 59, 58, 57, 56, 62]
for i, pitch in enumerate(bass_notes):
    start = 4.5 + i * note_length
    end = start + note_length
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# Piano: Repeat the 7th chords on offbeats
# Beat 0.75 (bar 4, beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625))  # C

# Beat 1.5 (bar 4, beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0))  # C

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
