
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante on tenor sax
bass = pretty_midi.Instrument(program=33)      # Marcus on bass
piano = pretty_midi.Instrument(program=0)      # Diane on piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray on drums

# Drum sounds
DRUM_KICK = 36
DRUM_SNARE = 38
DRUM_HI_HAT = 42

# Time in seconds per bar (160 BPM, 4/4 time)
BAR_LENGTH = 1.5  # 60 / 160 * 4 = 1.5 seconds per bar
TIME_PER_BEAT = 0.375  # 1.5 / 4

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Drums for Bar 1
drum_notes = [
    (0.0, DRUM_KICK), (0.375, DRUM_SNARE), (0.75, DRUM_HI_HAT),
    (1.125, DRUM_HI_HAT), (1.5, DRUM_KICK), (1.875, DRUM_SNARE),
    (2.25, DRUM_HI_HAT), (2.625, DRUM_HI_HAT)
]
for time, note_number in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Dm (D2 to G2, MIDI 38 to 43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.875, 40), (2.25, 41), (2.625, 38),
    (3.0, 40), (3.375, 41), (3.75, 38), (4.125, 40)
]
for time, note_number in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Diane: Open voicings, different chords each bar
# Bar 2: Dm7 (D F A C)
piano_notes = [
    # Dm7: D (D), F (F), A (A), C (C)
    (1.5, 62), (1.5, 65), (1.5, 69), (1.5, 72)
]
for time, note_number in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Dante: Tenor sax melody. One short motif, make it sing.
# Dm scale: D, E, F, G, A, Bb, C, D
# Start with D, then F, then A — leave it hanging
sax_notes = [
    (1.5, 62), (1.625, 65), (1.75, 69),  # D -> F -> A
]
for time, note_number in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line with a chromatic approach to Gm7
# Gm7 (G, Bb, D, F)
# Chromatic approach: F# -> G
bass_notes = [
    (3.0, 43), (3.375, 43), (3.75, 42), (4.125, 40)
]
for time, note_number in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Diane: Gm7 (G, Bb, D, F)
piano_notes = [
    (3.0, 67), (3.0, 70), (3.0, 74), (3.0, 76)
]
for time, note_number in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Dante: Tenor sax continues the motif, resolves and shifts
# D -> F -> A -> G
sax_notes = [
    (3.0, 69), (3.125, 67), (3.25, 69), (3.5, 67)
]
for time, note_number in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walks to C7 (C, E, G, B)
bass_notes = [
    (4.5, 60), (4.875, 64), (5.25, 67), (5.625, 71)
]
for time, note_number in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.1)
    bass.notes.append(bass_note)

# Diane: C7 (C, E, G, B)
piano_notes = [
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71)
]
for time, note_number in piano_notes:
    piano_note = pretty_midi.Note(velocity=95, pitch=note_number, start=time, end=time + 0.1)
    piano.notes.append(piano_note)

# Dante: Tenor sax resolves the motif. D -> F -> A -> D
sax_notes = [
    (4.5, 69), (4.625, 67), (4.75, 62), (5.0, 62)
]
for time, note_number in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    sax.notes.append(sax_note)

# Drums for Bar 3 and 4
drum_notes = [
    # Bar 3
    (3.0, DRUM_KICK), (3.375, DRUM_SNARE), (3.75, DRUM_HI_HAT),
    (4.125, DRUM_HI_HAT), (4.5, DRUM_KICK), (4.875, DRUM_SNARE),
    (5.25, DRUM_HI_HAT), (5.625, DRUM_HI_HAT),
    # Bar 4
    (6.0, DRUM_KICK), (6.375, DRUM_SNARE), (6.75, DRUM_HI_HAT),
    (7.125, DRUM_HI_HAT)
]
for time, note_number in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
