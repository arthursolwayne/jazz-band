
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar (160 BPM, 4/4 time)
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * BAR_DURATION
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for eighth in range(8):
        note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=start + eighth * BEAT_DURATION / 2, end=start + eighth * BEAT_DURATION / 2 + 0.05)
        drums.notes.append(note)

# Bar 2-4: Full Quartet (1.5 - 6.0s)
# Let's set up a melody in F minor (F, G, Ab, Bb, C, Db, D) but with a twist
# We'll use a simple motif that makes an impression

# Bass line: walking in Fm (F, C, G, Bb, F, Ab, D, Bb)
bass_notes = [78, 67, 77, 71, 78, 76, 74, 71]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + i * BEAT_DURATION
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano chords: Open voicings
# Fm7 (F, Ab, C, Eb), Bbm7 (Bb, Db, F, Ab), Am7 (A, C, E, G), Dm7 (D, F, A, C)
chords = [
    [78, 76, 72, 70],  # Fm7
    [71, 69, 78, 76],  # Bbm7
    [77, 72, 76, 79],  # Am7
    [74, 72, 77, 76],  # Dm7
]
for i, chord in enumerate(chords):
    start = 1.5 + i * BAR_DURATION
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
        piano.notes.append(note)

# Sax melody: Short, singable motif (F, G, Ab, F)
sax_notes = [78, 79, 76, 78]
for i, pitch in enumerate(sax_notes):
    start = 1.5 + i * BEAT_DURATION
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * BAR_DURATION
    # Kick on 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for eighth in range(8):
        note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=start + eighth * BEAT_DURATION / 2, end=start + eighth * BEAT_DURATION / 2 + 0.05)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
