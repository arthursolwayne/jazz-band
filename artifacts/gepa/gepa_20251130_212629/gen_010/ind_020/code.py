
import pretty_midi

# Initialize the MIDI file with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time per bar in seconds (160 BPM, 4/4 time)
BAR_DURATION = 1.5

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time points in bar 1 (0.0 to 1.5)
note_times = [0.0, 0.375, 0.75, 1.125, 1.5]

# Kick on 1 and 3 (0.0 and 0.75)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=0.80))

# Snare on 2 and 4 (0.375 and 1.125)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.40))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.15))

# Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125)
for t in note_times:
    if t != 1.5:  # Don't play on the last eighth
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=t, end=t + 0.05))

# BAR 2: Full quartet (1.5 - 3.0s)

# SAX: D (D4), E (E4), F# (F#4), D (D4) — short motif
# Start at 1.5s, end at 1.65s (leaving a pause)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.65))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.9))  # E4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.15))  # F#4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4))  # D4 again

# BASS: Walking line in D minor — D, Eb, F, G, A, Bb, C, D
# In 1.5 - 3.0s, each quarter note is 0.375s
bass_notes = [62, 63, 65, 67, 69, 70, 72, 62]
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.25))

# PIANO: 7th chords, comp on 2 and 4
# Bar 2: D7 on 2, D7 on 4
# D7 = D, F#, A, C
# Comp on 2 and 4 (1.875 and 3.0s)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=1.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=1.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=1.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=1.9))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.05))

# BAR 3: Full quartet (3.0 - 4.5s)

# SAX: Motif again, but with a variation (D, E, F#, D)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.15))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.4))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.65))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9))

# BASS: Walking line in D minor — D, Eb, F, G, A, Bb, C, D
bass_notes = [62, 63, 65, 67, 69, 70, 72, 62]
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.25))

# PIANO: 7th chords, comp on 2 and 4
# Bar 3: D7 on 2, D7 on 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.4))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.4))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.4))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.4))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.55))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.55))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.55))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.55))

# BAR 4: Full quartet (4.5 - 6.0s)

# SAX: Motif again, but resolved — D, E, F#, G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.65))  # D4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.9))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.15))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.2, end=5.35))  # G4

# BASS: Walking line in D minor — D, Eb, F, G, A, Bb, C, D
bass_notes = [62, 63, 65, 67, 69, 70, 72, 62]
for i, pitch in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.25))

# PIANO: 7th chords, comp on 2 and 4
# Bar 4: D7 on 2, D7 on 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=4.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=4.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=4.9))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=4.9))

piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.05))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.05))

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
