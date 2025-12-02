
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.25, 38, 100), # Snare on 3
    (1.5, 42, 100)   # Hihat on 4
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 59, 100), # D (root)
    (1.875, 58, 100), # C# (chromatic)
    (2.25, 60, 100), # E (3rd)
    (2.625, 57, 100), # C (b7)
    # Bar 3
    (3.0, 62, 100), # F (5th)
    (3.375, 61, 100), # E (4th)
    (3.75, 63, 100), # G (6th)
    (4.125, 60, 100), # E (3rd)
    # Bar 4
    (4.5, 59, 100), # D (root)
    (4.875, 58, 100), # C# (chromatic)
    (5.25, 60, 100), # E (3rd)
    (5.625, 57, 100), # C (b7)
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    (1.875, 62, 100), # F (7th chord: Dm7 = D, F, A, C)
    (1.875, 64, 100), # A
    (1.875, 60, 100), # D
    (1.875, 58, 100), # C
    (2.625, 62, 100),
    (2.625, 64, 100),
    (2.625, 60, 100),
    (2.625, 58, 100),
    # Bar 3 (comp on 2 and 4)
    (3.375, 62, 100),
    (3.375, 64, 100),
    (3.375, 60, 100),
    (3.375, 58, 100),
    (4.125, 62, 100),
    (4.125, 64, 100),
    (4.125, 60, 100),
    (4.125, 58, 100),
    # Bar 4 (comp on 2 and 4)
    (4.875, 62, 100),
    (4.875, 64, 100),
    (4.875, 60, 100),
    (4.875, 58, 100),
    (5.625, 62, 100),
    (5.625, 64, 100),
    (5.625, 60, 100),
    (5.625, 58, 100),
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Drums: Bar 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on 1
    (1.875, 42, 100), # Hihat on 2
    (2.25, 38, 100), # Snare on 3
    (2.625, 42, 100), # Hihat on 4
    (3.0, 36, 100),  # Kick on 1
    (3.375, 42, 100), # Hihat on 2
    (3.75, 38, 100), # Snare on 3
    (4.125, 42, 100), # Hihat on 4
    (4.5, 36, 100),  # Kick on 1
    (4.875, 42, 100), # Hihat on 2
    (5.25, 38, 100), # Snare on 3
    (5.625, 42, 100)  # Hihat on 4
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, start, start + 0.375))

# Sax: Motif in Dm, short and singable
sax_notes = [
    # Bar 2 (start on 1)
    (1.5, 62, 100), # F (Dm7)
    (1.75, 64, 100), # A
    (2.0, 60, 100), # D
    (2.25, 62, 100), # F
    (2.5, 64, 100), # A
    (2.75, 60, 100), # D
    # Bar 3 (rest)
    (3.0, 0, 0), # rest
    (3.25, 0, 0),
    (3.5, 0, 0),
    (3.75, 0, 0),
    # Bar 4 (return to motif)
    (4.5, 62, 100), # F
    (4.75, 64, 100), # A
    (5.0, 60, 100), # D
    (5.25, 62, 100), # F
    (5.5, 64, 100), # A
    (5.75, 60, 100)  # D
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, start, start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_shorter_intro.mid')
