
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> Eb2 (39) -> G2 (43) -> A2 (45)
    (1.5, 38), (1.75, 39), (2.0, 43), (2.25, 45),
    # Bar 3: C2 (36) -> Db2 (37) -> F2 (41) -> G2 (43)
    (2.5, 36), (2.75, 37), (3.0, 41), (3.25, 43),
    # Bar 4: Bb2 (35) -> Bb2 (35) -> D2 (38) -> Eb2 (39)
    (3.5, 35), (3.75, 35), (4.0, 38), (4.25, 39)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (1.5, 62), (1.5, 64), (1.5, 67), (1.5, 69),
    # Bar 3: G7 (G, B, D, F)
    (2.5, 67), (2.5, 71), (2.5, 69), (2.5, 64),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (3.5, 60), (3.5, 62), (3.5, 67), (3.5, 65)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    for i in [0, 2]:
        time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    # Snare on 2 and 4
    for i in [1, 3]:
        time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125))
    # Hihat on every eighth
    for i in range(0, 4):
        time = start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (64), G (67), D (62)
sax_notes = [
    (1.5, 62), (1.5, 64), (1.5, 67), (1.5, 62),
    (2.5, 62), (2.75, 64), (3.0, 67), (3.25, 62),
    (4.5, 62), (4.75, 64), (5.0, 67), (5.25, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
