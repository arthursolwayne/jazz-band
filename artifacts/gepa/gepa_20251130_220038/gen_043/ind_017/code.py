
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.5, 38, 100),  # Snare on 3
    (1.75, 42, 100), # Hihat on 4
    (1.75, 38, 100)  # Snare on 4 (ghost note)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in D minor (D, Eb, F, G)
bass_notes = [
    (1.5, 65, 100),  # D
    (1.75, 64, 100), # Eb
    (2.25, 67, 100), # F
    (2.5, 69, 100),  # G
    (3.0, 65, 100),  # D (end of bar)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 65, 100),  # D7 (D, F#, A, C)
    (1.75, 70, 100),  # A
    (1.75, 76, 100),  # C
    (2.5, 65, 100),   # D7 (D, F#, A, C)
    (2.5, 70, 100),   # A
    (2.5, 76, 100),   # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Whisper at first, then a cry (D, F#, Bb, C)
sax_notes = [
    (1.5, 62, 70),    # D
    (1.75, 67, 80),   # F#
    (2.0, 70, 90),    # Bb
    (2.25, 64, 100),  # C
    (2.5, 62, 70),    # D (repeat)
    (2.75, 67, 80),   # F#
    (3.0, 70, 90),    # Bb
    (3.25, 64, 100)   # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line in D minor (D, Eb, F, G)
bass_notes = [
    (3.0, 65, 100),  # D
    (3.25, 64, 100), # Eb
    (3.75, 67, 100), # F
    (4.0, 69, 100),  # G
    (4.5, 65, 100),  # D (end of bar)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 65, 100),  # D7 (D, F#, A, C)
    (3.25, 70, 100),  # A
    (3.25, 76, 100),  # C
    (4.0, 65, 100),   # D7 (D, F#, A, C)
    (4.0, 70, 100),   # A
    (4.0, 76, 100),   # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Continue motif with variation
sax_notes = [
    (3.0, 62, 70),    # D
    (3.25, 67, 80),   # F#
    (3.5, 70, 90),    # Bb
    (3.75, 64, 100),  # C
    (4.0, 62, 70),    # D (repeat)
    (4.25, 67, 80),   # F#
    (4.5, 70, 90),    # Bb
    (4.75, 64, 100)   # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line in D minor (D, Eb, F, G)
bass_notes = [
    (4.5, 65, 100),  # D
    (4.75, 64, 100), # Eb
    (5.25, 67, 100), # F
    (5.5, 69, 100),  # G
    (6.0, 65, 100),  # D (end of bar)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 65, 100),  # D7 (D, F#, A, C)
    (4.75, 70, 100),  # A
    (4.75, 76, 100),  # C
    (5.5, 65, 100),   # D7 (D, F#, A, C)
    (5.5, 70, 100),   # A
    (5.5, 76, 100),   # C
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Final variation, leave it hanging
sax_notes = [
    (4.5, 62, 70),    # D
    (4.75, 67, 80),   # F#
    (5.0, 70, 90),    # Bb
    (5.25, 64, 100),  # C
    (5.5, 62, 70),    # D
    (5.75, 67, 80),   # F#
    (6.0, 70, 90),    # Bb
    (6.25, 64, 100)   # C (outside bar, fade)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 3 and 4 (3.0 - 6.0s)
drum_notes = [
    (3.0, 36, 100),   # Kick on 1
    (3.75, 42, 100),  # Hihat on 2
    (4.5, 38, 100),   # Snare on 3
    (4.75, 42, 100),  # Hihat on 4
    (4.75, 38, 100),  # Snare on 4 (ghost note)
    (5.0, 36, 100),   # Kick on 1
    (5.75, 42, 100),  # Hihat on 2
    (6.5, 38, 100),   # Snare on 3 (outside bar)
    (6.75, 42, 100),  # Hihat on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
