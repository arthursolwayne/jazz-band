
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2 (1.5 - 3.0s): Everyone in
# Bass: Walking line with chromatic approaches and roots/fifths
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 43), (2.25, 42),
    (2.5, 45), (2.75, 47), (3.0, 43), (3.25, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [(1.5, 62), (1.5, 67), (1.5, 72), (1.5, 74)]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Bar 3: Gm7 (G Bb D F)
piano_notes = [(2.5, 67), (2.5, 71), (2.5, 74), (2.5, 76)]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Bar 4: Cmaj7 (C E G B)
piano_notes = [(3.5, 60), (3.5, 64), (3.5, 67), (3.5, 71)]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.5))

# Drums: continue with kick, snare, hihat
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Melody - concise, melodic, memorable, starts on beat 2
sax_notes = [
    (1.75, 65), (2.0, 67), (2.25, 65), (2.5, 62),
    (2.75, 64), (3.0, 65), (3.25, 62), (3.5, 65),
    (3.75, 67), (4.0, 65), (4.25, 62), (4.5, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
