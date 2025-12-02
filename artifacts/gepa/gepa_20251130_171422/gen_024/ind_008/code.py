
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (0.0, 38, 100),     # Snare on 2
    (0.75, 42, 80),     # Hihat on 3
    (1.125, 36, 110),   # Kick on 3
    (1.5, 38, 100)      # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: D, F, G, Bb
sax_notes = [
    (1.5, 62, 100),     # D
    (1.75, 65, 105),    # F
    (2.0, 67, 95),      # G
    (2.25, 69, 110),    # Bb
    (2.5, 67, 90),      # G
    (2.75, 65, 100),    # F
    (3.0, 62, 95)       # D
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: walking with chromatic approach
bass_notes = [
    (1.5, 62, 90),      # D
    (1.75, 63, 95),     # Eb
    (2.0, 65, 90),      # F
    (2.25, 67, 95),     # G
    (2.5, 69, 90),      # A
    (2.75, 71, 95),     # Bb
    (3.0, 69, 90)       # A
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (1.75, 62, 80),     # D7: D, F, A, C
    (1.75, 64, 80),
    (1.75, 69, 80),
    (1.75, 67, 80),
    (2.25, 62, 80),
    (2.25, 64, 80),
    (2.25, 69, 80),
    (2.25, 67, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif: D, Bb, C, D
sax_notes = [
    (3.0, 62, 100),     # D
    (3.25, 69, 110),    # Bb
    (3.5, 60, 95),      # C
    (3.75, 62, 105),    # D
    (4.0, 60, 90),      # C
    (4.25, 62, 100),    # D
    (4.5, 60, 95)       # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: walking with chromatic approach
bass_notes = [
    (3.0, 60, 90),      # C
    (3.25, 62, 95),     # D
    (3.5, 64, 90),      # Eb
    (3.75, 67, 95),     # G
    (4.0, 69, 90),      # A
    (4.25, 71, 95),     # Bb
    (4.5, 69, 90)       # A
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (3.25, 60, 80),     # C7: C, E, G, Bb
    (3.25, 64, 80),
    (3.25, 67, 80),
    (3.25, 71, 80),
    (3.75, 60, 80),
    (3.75, 64, 80),
    (3.75, 67, 80),
    (3.75, 71, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif: D, Bb, C, D
sax_notes = [
    (4.5, 62, 100),     # D
    (4.75, 69, 110),    # Bb
    (5.0, 60, 95),      # C
    (5.25, 62, 105),    # D
    (5.5, 60, 90),      # C
    (5.75, 62, 100),    # D
    (6.0, 60, 95)       # C
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Bass line: walking with chromatic approach
bass_notes = [
    (4.5, 60, 90),      # C
    (4.75, 62, 95),     # D
    (5.0, 64, 90),      # Eb
    (5.25, 67, 95),     # G
    (5.5, 69, 90),      # A
    (5.75, 71, 95),     # Bb
    (6.0, 69, 90)       # A
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    (4.75, 60, 80),     # C7: C, E, G, Bb
    (4.75, 64, 80),
    (4.75, 67, 80),
    (4.75, 71, 80),
    (5.25, 60, 80),
    (5.25, 64, 80),
    (5.25, 67, 80),
    (5.25, 71, 80)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Drums: Bar 3-4 (3.0 - 6.0s)
drum_notes = [
    (3.0, 36, 100),     # Kick on 1
    (3.25, 42, 80),     # Hihat on 2
    (3.5, 38, 100),     # Snare on 3
    (3.75, 42, 80),     # Hihat on 4
    (4.0, 36, 100),     # Kick on 1
    (4.25, 42, 80),     # Hihat on 2
    (4.5, 38, 100),     # Snare on 3
    (4.75, 42, 80),     # Hihat on 4
    (5.0, 36, 100),     # Kick on 1
    (5.25, 42, 80),     # Hihat on 2
    (5.5, 38, 100),     # Snare on 3
    (5.75, 42, 80),     # Hihat on 4
    (6.0, 38, 100)      # Snare on 4
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
