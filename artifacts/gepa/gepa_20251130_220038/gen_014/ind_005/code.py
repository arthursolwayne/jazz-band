
import pretty_midi

# Initialize the MIDI file with the specified tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
time = 0.0
bar_duration = 1.5
beat = 0.375

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 0.0, end=time + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 2*beat, end=time + 3*beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + beat, end=time + 2*beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + 3*beat, end=time + 4*beat))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + i*beat, end=time + (i+1)*beat))

# Bar 2: Full quartet (1.5 - 3.0s)
time = 1.5

## Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 0.0, end=time + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 2*beat, end=time + 3*beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + beat, end=time + 2*beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + 3*beat, end=time + 4*beat))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + i*beat, end=time + (i+1)*beat))

## Bass (Marcus): Walking line in Dm, chromatic approaches
# Dm: D - F - A - C
# We'll use Dm7 (D F A C) as the underlying harmony

# Walking bass line in Dm, playing D, F, A, C, Eb, D, F, A
bass_notes = [62, 65, 67, 69, 67, 62, 65, 67]  # D, F, A, C, Eb, D, F, A
for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time + i*beat, end=time + (i+1)*beat))

## Piano (Diane): 7th chords on 2 and 4
# Dm7: D - F - A - C
# Play Dm7 on 2 and 4
piano_notes = [62, 65, 67, 69]

# 2nd beat (time + beat)
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + beat, end=time + 1.5*beat))

# 4th beat (time + 3*beat)
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + 3*beat, end=time + 4*beat))

## Sax (Dante): Melody in Dm, short motif that lingers
# Dm: D - F - A - C, but with a chromatic twist
# Motif: D, Eb, F, A (1st bar), then repeat
# Start with D (62), then Eb (63), F (65), A (67)
melody_notes = [62, 63, 65, 67]
for i, note in enumerate(melody_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + i*beat, end=time + (i+1)*beat))

# Bar 3: (3.0 - 4.5s)
time = 3.0

## Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 0.0, end=time + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 2*beat, end=time + 3*beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + beat, end=time + 2*beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + 3*beat, end=time + 4*beat))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + i*beat, end=time + (i+1)*beat))

## Bass: Walk again, chromatic approach to C
bass_notes = [69, 67, 65, 62, 62, 69, 67, 65]  # C, Eb, F, D, D, C, Eb, F
for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time + i*beat, end=time + (i+1)*beat))

## Piano: 7th chords on 2 and 4 (Dm7 again)
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + beat, end=time + 1.5*beat))
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + 3*beat, end=time + 4*beat))

## Sax: Repeat the motif, but end on A (67), leaving it hanging
for i, note in enumerate(melody_notes):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time + i*beat, end=time + (i+1)*beat))

# Bar 4: (4.5 - 6.0s)
time = 4.5

## Drums
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 0.0, end=time + beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time + 2*beat, end=time + 3*beat))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + beat, end=time + 2*beat))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time + 3*beat, end=time + 4*beat))

# Hihat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + i*beat, end=time + (i+1)*beat))

## Bass: Chromatic approach to D, locking in the groove
bass_notes = [67, 65, 62, 62, 65, 67, 69, 67]  # F, D, D, D, F, G, A, G
for i, note in enumerate(bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time + i*beat, end=time + (i+1)*beat))

## Piano: 7th chords on 2 and 4 (Dm7 again)
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + beat, end=time + 1.5*beat))
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time + 3*beat, end=time + 4*beat))

## Sax: Final phrase — resolve the motif with a D, but with space
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=time + 3*beat, end=time + 4*beat))

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
