
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 50), (1.875, 51), (2.25, 48), (2.625, 47),  # Dm walk
    (3.0, 50), (3.375, 51), (3.75, 48), (4.125, 47),
    (4.5, 50), (4.875, 51), (5.25, 48), (5.625, 47)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords on 2 and 4, Dm7, F7, Bb7, C7
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (2.25, 62), (2.25, 65), (2.25, 67), (2.25, 69),
    # Bar 3: F7 (F, A, C, E)
    (3.75, 65), (3.75, 67), (3.75, 69), (3.75, 71),
    # Bar 4: Bb7 (Bb, D, F, A)
    (5.25, 61), (5.25, 64), (5.25, 66), (5.25, 68)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Sax: Whisper -> cry, one motif, no repetition
# Motif: D (62), E (64), F (65), Bb (61)
sax_notes = [
    (1.5, 62), (1.5 + 0.375, 64), (1.5 + 0.75, 65), (1.5 + 1.125, 61),
    (1.5 + 1.5, 62), (1.5 + 1.875, 64), (1.5 + 2.25, 65), (1.5 + 2.625, 61),
    (1.5 + 3.0, 62), (1.5 + 3.375, 64), (1.5 + 3.75, 65), (1.5 + 4.125, 61),
    (1.5 + 4.5, 62), (1.5 + 4.875, 64), (1.5 + 5.25, 65), (1.5 + 5.625, 61)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
