
import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds per bar at 160 BPM
BAR_DURATION = 1.5
BEAT_DURATION = 0.375

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * BAR_DURATION
    # Kick on beats 0 and 2 (1 and 3)
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1))
    # Snare on beats 1 and 3 (2 and 4)
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1))
    # Hi-hat on every eighth note
    for eighth in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start + eighth * BEAT_DURATION / 2, end=start + eighth * BEAT_DURATION / 2 + 0.05))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# All instruments now play

## Marcus: Walking bass line in Dm
# Dm: D-F-A-C
# Walking line with chromatic approaches, no repeated notes
bass_notes = [62, 60, 59, 62, 64, 62, 60, 58, 59, 62, 64, 62, 60, 59, 62, 64]  # Dm walking line
for i, pitch in enumerate(bass_notes):
    start_time = 1.5 + i * BEAT_DURATION
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=start_time, end=start_time + 0.25))

## Diane: Piano comping on 2 and 4 with 7th chords
# Dm7 = D-F-A-C
# Comp on beats 2 and 4
chord_durations = [0.5, 0.5]  # 2 and 4 of each bar
chord_pitches = [62, 65, 67, 69]  # D-F-A-C
for bar in range(2, 5):  # Bars 2, 3, 4
    start = bar * BAR_DURATION
    for i, beat in enumerate([1, 3]):
        for pitch in chord_pitches:
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + chord_durations[i]))

## Little Ray: Drums continue as before
for bar in range(2, 5):
    start = bar * BAR_DURATION
    # Kick on 1 and 3
    for beat in [0, 2]:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1))
    # Snare on 2 and 4
    for beat in [1, 3]:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1))
    # Hi-hat on every eighth
    for eighth in range(8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start + eighth * BEAT_DURATION / 2, end=start + eighth * BEAT_DURATION / 2 + 0.05))

## Dante: Tenor Sax melody (Bars 2-4) - short motif, sings, leaves it hanging
# Dm sax motif: D - Bb - C - D (motif), then repeat and resolve
motif = [62, 60, 64, 62]  # D - Bb - C - D
for i, pitch in enumerate(motif):
    start = 1.5 + i * BEAT_DURATION
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Second pass of the motif, slightly delayed and resolved
for i, pitch in enumerate(motif):
    start = 1.5 + 4 * BEAT_DURATION + i * BEAT_DURATION
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Resolve the phrase with a gentle A (C# in Dm7)
sax.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 8 * BEAT_DURATION, end=1.5 + 8 * BEAT_DURATION + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("cellar_introduction.mid")
