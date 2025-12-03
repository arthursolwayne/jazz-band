
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),  # Bar 1
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),  # Bar 3
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]

for time, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Bass starts (1.5 - 3.0s)
# Walking line with chromatic approaches, roots and fifths
bass_notes = [
    (1.5, 62), # D2
    (1.875, 65), # F#2 (chromatic approach to G2)
    (2.25, 67), # G2
    (2.625, 65), # F#2
    (3.0, 62), # D2
    (3.375, 65), # F#2
    (3.75, 67), # G2
    (4.125, 65)  # F#2
]

for time, note in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Bar 2: Piano starts (1.5 - 3.0s)
# Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: G7 (G, B, D, F)
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 60),
    # Bar 3: G7 (G, B, D, F)
    (3.0, 67), (3.0, 71), (3.0, 62), (3.0, 65),
    # Bar 4: Cmaj7 (C, E, G, B)
    (4.5, 60), (4.5, 64), (4.5, 67), (4.5, 71)
]

for time, note in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.75)
    piano.notes.append(note_obj)

# Bar 2: Tenor sax starts (1.5 - 3.0s)
# One short motif, haunting, incomplete
# Start it, leave it hanging
sax_notes = [
    (1.5, 65), # F#4
    (1.75, 64), # E4
    (2.0, 65), # F#4
    (2.25, 62), # D4
    (2.5, 64), # E4
    (2.75, 62), # D4
    (3.0, 60)  # C4
]

for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Tenor sax continues (3.0 - 4.5s)
# Continue the motif but leave it unresolved
sax_notes = [
    (3.0, 62), # D4
    (3.25, 64), # E4
    (3.5, 62), # D4
    (3.75, 60), # C4
    (4.0, 62), # D4
    (4.25, 64), # E4
    (4.5, 62)  # D4 (end on D, unresolved)
]

for time, note in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Tenor sax ends on D4, incomplete
# No resolution, leaves the question

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
