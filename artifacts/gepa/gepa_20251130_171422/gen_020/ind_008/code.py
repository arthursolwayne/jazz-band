
import pretty_midi

# Initialize the MIDI file with 160 BPM (6.0 seconds for 4 bars)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Set up the time grid (160 BPM = 0.375 seconds per beat, 1.5 seconds per bar)
beat = 0.375
bar = 1.5

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth note

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(0, 8):
    start = i * beat
    end = start + beat
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Melody on saxophone: Fm7 -> Bb -> Ab -> G -> Fm7

# Saxophone melody (Fm7 -> Bb -> Ab -> G -> Fm7)
# Fm7: F, Ab, Bb, Db
# Bb: Bb
# Ab: Ab
# G: G
# Fm7: F, Ab, Bb, Db

note_duration = 0.75  # 3/4 note, gives space for the rest to play

# F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + note_duration))
# Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5 + note_duration, end=1.5 + note_duration * 2))
# Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5 + note_duration * 2, end=1.5 + note_duration * 3))
# G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5 + note_duration * 3, end=1.5 + note_duration * 4))
# F (end of bar)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5 + note_duration * 4, end=3.0))

# Bass: Chromatic walk - F, Gb, G, Ab
bass_notes = [71, 70, 72, 68]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=1.5, end=1.5 + beat))

# Piano: 7th chords on the offbeats
# Fm7 on beat 2 (offbeat 1), Bb7 on beat 3 (offbeat 2), Ab7 on beat 4 (offbeat 3)
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Ab7: Ab, C, Db, F

# Fm7 at 1.75s (beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.125))

# Bb7 at 2.25s (beat 3)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625))

# Ab7 at 2.75s (beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Melody: Bb -> Ab -> G -> Fm7 (same as in bar 2, but shifted)
# Bass: Chromatic walk - G, Ab, A, Bb
# Piano: 7th chords on the offbeats

# Saxophone melody (Fm7 -> Bb -> Ab -> G -> Fm7)
# Fm7: F, Ab, Bb, Db
# Bb: Bb
# Ab: Ab
# G: G
# Fm7: F, Ab, Bb, Db

# F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + note_duration))
# Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.0 + note_duration, end=3.0 + note_duration * 2))
# Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0 + note_duration * 2, end=3.0 + note_duration * 3))
# G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0 + note_duration * 3, end=3.0 + note_duration * 4))
# F (end of bar)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0 + note_duration * 4, end=4.5))

# Bass: Chromatic walk - G, Ab, A, Bb
bass_notes = [72, 68, 74, 71]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=3.0, end=3.0 + beat))

# Piano: 7th chords on the offbeats
# Fm7 on beat 2 (offbeat 1), Bb7 on beat 3 (offbeat 2), Ab7 on beat 4 (offbeat 3)
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Ab7: Ab, C, Db, F

# Fm7 at 3.75s (beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125))

# Bb7 at 4.25s (beat 3)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.625))

# Ab7 at 4.75s (beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Melody: Fm7 -> Bb -> Ab -> G -> Fm7 (repeat of the opening motif, slightly different timing)
# Bass: Chromatic walk - Bb, B, C, C#
# Piano: 7th chords on the offbeats

# Saxophone melody (Fm7 -> Bb -> Ab -> G -> Fm7)
# Fm7: F, Ab, Bb, Db
# Bb: Bb
# Ab: Ab
# G: G
# Fm7: F, Ab, Bb, Db

# F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + note_duration))
# Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.5 + note_duration, end=4.5 + note_duration * 2))
# Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5 + note_duration * 2, end=4.5 + note_duration * 3))
# G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5 + note_duration * 3, end=4.5 + note_duration * 4))
# F (end of bar)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5 + note_duration * 4, end=6.0))

# Bass: Chromatic walk - Bb, B, C, C#
bass_notes = [71, 72, 74, 75]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=4.5, end=4.5 + beat))

# Piano: 7th chords on the offbeats
# Fm7 on beat 2 (offbeat 1), Bb7 on beat 3 (offbeat 2), Ab7 on beat 4 (offbeat 3)
# Fm7: F, Ab, Bb, Db
# Bb7: Bb, D, F, Ab
# Ab7: Ab, C, Db, F

# Fm7 at 5.25s (beat 2)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625))

# Bb7 at 5.75s (beat 3)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.125))

# Ab7 at 6.25s (beat 4)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=6.25, end=6.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=6.25, end=6.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=6.25, end=6.625))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=6.25, end=6.625))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
