
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(100, 36, time, time + 0.125))  # Kick
    drums.notes.append(pretty_midi.Note(100, 38, time + 0.375, time + 0.5))  # Snare
    drums.notes.append(pretty_midi.Note(100, 42, time, time + 0.125))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.125, time + 0.25))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.25, time + 0.375))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.375, time + 0.5))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.5, time + 0.625))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.625, time + 0.75))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.75, time + 0.875))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.875, time + 1.0))  # Hihat

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches
# Start on D (62) and walk up chromatically in 16th notes
bass_notes = [
    (1.5, 62), (1.625, 63), (1.75, 64), (1.875, 65),
    (2.0, 67), (2.125, 68), (2.25, 69), (2.375, 70),
    (2.5, 72), (2.625, 73), (2.75, 74), (2.875, 75),
    (3.0, 76), (3.125, 77), (3.25, 78), (3.375, 79),
    (3.5, 81), (3.625, 82), (3.75, 83), (3.875, 84),
    (4.0, 86), (4.125, 87), (4.25, 88), (4.375, 89),
    (4.5, 90), (4.625, 91), (4.75, 92), (4.875, 93),
    (5.0, 94), (5.125, 95), (5.25, 96), (5.375, 97),
    (5.5, 98), (5.625, 99), (5.75, 100), (5.875, 101)
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.125))

# Piano: 7th chords on 2 and 4
# D7 on 2, G7 on 4, B7 on 6, F7 on 8
piano_notes = [
    # Bar 2 - D7 (D, F#, A, C)
    (2.0, 62), (2.0, 66), (2.0, 69), (2.0, 72),
    # Bar 3 - G7 (G, B, D, F)
    (3.0, 67), (3.0, 71), (3.0, 74), (3.0, 76),
    # Bar 4 - B7 (B, D#, F#, A)
    (4.0, 71), (4.0, 76), (4.0, 78), (4.0, 81),
    # Bar 5 - F7 (F, A, C, E)
    (5.0, 65), (5.0, 69), (5.0, 72), (5.0, 76)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.5))

# Drums: continue with the same pattern
for i in range(8):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(100, 36, time, time + 0.125))  # Kick
    drums.notes.append(pretty_midi.Note(100, 38, time + 0.375, time + 0.5))  # Snare
    drums.notes.append(pretty_midi.Note(100, 42, time, time + 0.125))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.125, time + 0.25))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.25, time + 0.375))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.375, time + 0.5))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.5, time + 0.625))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.625, time + 0.75))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.75, time + 0.875))  # Hihat
    drums.notes.append(pretty_midi.Note(100, 42, time + 0.875, time + 1.0))  # Hihat

# Sax: your moment - one short motif, make it sing
# Start on D, chromatic up to F#, then resolution to G
sax_notes = [
    (1.5, 62), (1.5 + 0.125, 63), (1.5 + 0.25, 64), (1.5 + 0.375, 66),
    (1.5 + 0.5, 67), (1.5 + 0.625, 69), (1.5 + 0.75, 71), (1.5 + 0.875, 72)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note, time, time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
