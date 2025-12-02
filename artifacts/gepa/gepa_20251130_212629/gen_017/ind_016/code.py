
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
    (0.0, 36, 100),     # Kick on 1
    (0.375, 42, 60),    # Hihat
    (0.75, 38, 100),    # Snare on 2
    (1.125, 42, 60),    # Hihat
    (1.5, 36, 100),     # Kick on 3
    (1.875, 42, 60),    # Hihat
    (2.25, 38, 100),    # Snare on 4
    (2.625, 42, 60)     # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches
# F - Gb - G - Ab - A - Bb - B - C - C# - D - Eb - E - F
bass_notes = [
    (1.5, 77, 100),     # F
    (1.75, 76, 100),    # Gb
    (2.0, 78, 100),     # G
    (2.25, 77, 100),    # Ab
    (2.5, 79, 100),     # A
    (2.75, 77, 100),    # Bb
    (3.0, 81, 100),     # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 on 2 (2.0s)
    (2.0, 77, 100),     # F
    (2.0, 82, 100),     # B
    (2.0, 81, 100),     # Bb
    (2.0, 79, 100),     # A

    # Bb7 on 4 (3.0s)
    (3.0, 77, 100),     # Bb
    (3.0, 82, 100),     # D
    (3.0, 80, 100),     # C
    (3.0, 78, 100),     # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: Motif - F, A, Bb, rest
# Start with F on beat 1, A on beat 2, Bb on beat 3, rest on beat 4
sax_notes = [
    (1.5, 77, 100),     # F
    (1.875, 80, 100),   # A
    (2.25, 81, 100),    # Bb
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
# F - Gb - G - Ab - A - Bb - B - C
bass_notes = [
    (3.0, 77, 100),     # F
    (3.25, 76, 100),    # Gb
    (3.5, 78, 100),     # G
    (3.75, 77, 100),    # Ab
    (4.0, 79, 100),     # A
    (4.25, 77, 100),    # Bb
    (4.5, 81, 100),     # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 on 2 (3.5s)
    (3.5, 77, 100),     # F
    (3.5, 82, 100),     # B
    (3.5, 81, 100),     # Bb
    (3.5, 79, 100),     # A

    # Bb7 on 4 (4.5s)
    (4.5, 77, 100),     # Bb
    (4.5, 82, 100),     # D
    (4.5, 80, 100),     # C
    (4.5, 78, 100),     # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: motif variation - F, Ab, A, rest
# Start with F on beat 1, Ab on beat 2, A on beat 3, rest on beat 4
sax_notes = [
    (3.0, 77, 100),     # F
    (3.375, 77, 100),   # Ab
    (3.75, 79, 100),    # A
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36, 100),     # Kick on 1
    (3.375, 42, 60),    # Hihat
    (3.75, 38, 100),    # Snare on 2
    (4.125, 42, 60),    # Hihat
    (4.5, 36, 100),     # Kick on 3
    (4.875, 42, 60),    # Hihat
    (5.25, 38, 100),    # Snare on 4
    (5.625, 42, 60)     # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
# F - Gb - G - Ab - A - Bb - B - C
bass_notes = [
    (4.5, 77, 100),     # F
    (4.75, 76, 100),    # Gb
    (5.0, 78, 100),     # G
    (5.25, 77, 100),    # Ab
    (5.5, 79, 100),     # A
    (5.75, 77, 100),    # Bb
    (6.0, 81, 100),     # B
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4
# F7 on 2, Bb7 on 4
piano_notes = [
    # F7 on 2 (5.0s)
    (5.0, 77, 100),     # F
    (5.0, 82, 100),     # B
    (5.0, 81, 100),     # Bb
    (5.0, 79, 100),     # A

    # Bb7 on 4 (6.0s)
    (6.0, 77, 100),     # Bb
    (6.0, 82, 100),     # D
    (6.0, 80, 100),     # C
    (6.0, 78, 100),     # B
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Sax: motif variation - F, Bb, C, rest
# Start with F on beat 1, Bb on beat 2, C on beat 3, rest on beat 4
sax_notes = [
    (4.5, 77, 100),     # F
    (4.875, 81, 100),   # Bb
    (5.25, 79, 100),    # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36, 100),     # Kick on 1
    (4.875, 42, 60),    # Hihat
    (5.25, 38, 100),    # Snare on 2
    (5.625, 42, 60),    # Hihat
    (6.0, 36, 100),     # Kick on 3
    (6.375, 42, 60),    # Hihat
    (6.75, 38, 100),    # Snare on 4
    (7.125, 42, 60)     # Hihat
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
