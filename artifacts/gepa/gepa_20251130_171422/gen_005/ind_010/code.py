
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (30, 1.5), (31, 1.875), (29, 2.25), (30, 2.625),
    (31, 3.0), (32, 3.375), (31, 3.75), (30, 4.125),
    (29, 4.5), (30, 4.875), (31, 5.25), (32, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F A C E)
    (53, 1.875), (58, 1.875), (55, 1.875), (57, 1.875),
    # Bar 3: Bb7 (Bb D F Ab)
    (50, 3.375), (55, 3.375), (53, 3.375), (52, 3.375),
    # Bar 4: Eb7 (Eb G Bb D)
    (56, 4.875), (59, 4.875), (55, 4.875), (58, 4.875)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging, come back and finish it
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F - Ab - A - Db
sax_notes = [
    (53, 1.5), (55, 1.5), (56, 1.5), (58, 1.5),
    (53, 1.875), (56, 1.875), (58, 1.875),
    (56, 2.25), (58, 2.25), (60, 2.25),
    (55, 2.625), (58, 2.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    for i in [0, 2]:
        time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    # Snare on 2 and 4
    for i in [1, 3]:
        time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    # Hihat on every eighth
    for i in range(4):
        time = bar_start + i * 0.375
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
