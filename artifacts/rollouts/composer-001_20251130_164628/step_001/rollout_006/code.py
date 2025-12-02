
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
kick_kicks = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_kicks = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875]
hihat_kicks = [i * 0.375 for i in range(0, 8)]

for time in kick_kicks:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

for time in snare_kicks:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

for time in hihat_kicks:
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 46), (1.875, 47), (2.25, 48), (2.625, 47), 
    # Bar 3
    (3.0, 46), (3.375, 45), (3.75, 46), (4.125, 47), 
    # Bar 4
    (4.5, 48), (4.875, 47), (5.25, 46), (5.625, 45)
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Db
# Bar 2: 7th chord on 2 and 4
piano_notes = [
    (2.0, 65), (2.0, 69), (2.0, 72), (2.0, 71),
    (2.5, 65), (2.5, 69), (2.5, 72), (2.5, 71),
    # Bar 3: 7th chord on 2 and 4
    (3.5, 65), (3.5, 69), (3.5, 72), (3.5, 71),
    (4.0, 65), (4.0, 69), (4.0, 72), (4.0, 71),
    # Bar 4: 7th chord on 2 and 4
    (5.0, 65), (5.0, 69), (5.0, 72), (5.0, 71),
    (5.5, 65), (5.5, 69), (5.5, 72), (5.5, 71)
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Saxophone (Dante): One short motif, make it sing
# Motif: F Ab Bb (Fm triad), then leave it hanging on Ab
# Start on 1.5s, finish on 2.25s
sax_notes = [
    (1.5, 65),  # F
    (1.875, 69),  # Ab
    (2.25, 71)   # Bb
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
