
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
bar1 = 1.5
drum_notes = [
    (0.0, 36, 100), (0.375, 42, 100),
    (0.75, 36, 100), (1.125, 42, 100),
    (1.5, 38, 100), (1.875, 42, 100),
    (2.25, 38, 100), (2.625, 42, 100)
]
for time, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    (1.5, 65, 100), (1.75, 66, 100), (2.0, 67, 100), (2.25, 68, 100),
    (2.5, 69, 100), (2.75, 70, 100), (3.0, 71, 100), (3.25, 72, 100)
]
for time, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity, note, time, time + 0.25))

# Piano: 7th chords on 2 and 4, F7, Bb7, F7, Bb7
piano_notes = [
    # Bar 2: F7 = F, A, C, E
    (2.0, 77, 100), (2.0, 82, 100), (2.0, 87, 100), (2.0, 90, 100),
    # Bar 3: Bb7 = Bb, D, F, Ab
    (3.0, 71, 100), (3.0, 76, 100), (3.0, 87, 100), (3.0, 84, 100),
    # Bar 4: F7 again
    (4.0, 77, 100), (4.0, 82, 100), (4.0, 87, 100), (4.0, 90, 100)
]
for time, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Sax: motif - short, melodic, starts at 1.5s
# F, G#, B, D (F7 arpeggio with a twist)
sax_notes = [
    (1.5, 77, 100), (1.75, 81, 100), (2.0, 87, 100), (2.25, 82, 100),
    (2.5, 77, 100), (2.75, 81, 100), (3.0, 87, 100), (3.25, 82, 100),
    (3.5, 77, 100), (3.75, 81, 100), (4.0, 87, 100), (4.25, 82, 100)
]
for time, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity, note, time, time + 0.1875))

# Drums for bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

def add_drums(start):
    for i in range(4):
        kick_time = start + i * 0.75
        snare_time = start + i * 0.75 + 0.375
        hihat_time = start + i * 0.75 + 0.1875
        drums.notes.append(pretty_midi.Note(100, 36, kick_time, kick_time + 0.1875))
        drums.notes.append(pretty_midi.Note(100, 38, snare_time, snare_time + 0.1875))
        for j in range(4):
            hihat_time = start + i * 0.75 + j * 0.375
            drums.notes.append(pretty_midi.Note(100, 42, hihat_time, hihat_time + 0.1875))

add_drums(bar2_start)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
