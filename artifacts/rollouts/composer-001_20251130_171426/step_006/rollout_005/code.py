
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
    # Bar 1
    (36, 0.0), (38, 0.375), (42, 0.0), (42, 0.125), (42, 0.25), (42, 0.375),
    (42, 0.5), (42, 0.625), (42, 0.75), (42, 0.875),
    (36, 1.125), (38, 1.5)
]

for note, time in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    (32, 1.5), (33, 1.875), (31, 2.25), (34, 2.625),
    # Bar 3
    (35, 3.0), (33, 3.375), (32, 3.75), (36, 4.125),
    # Bar 4
    (34, 4.5), (32, 4.875), (33, 5.25), (31, 5.625)
]

for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on beat 2 and 4)
    (45, 2.0), (47, 2.0), (49, 2.0), (50, 2.0),
    (45, 2.5), (47, 2.5), (49, 2.5), (50, 2.5),
    # Bar 3 (comp on beat 2 and 4)
    (45, 3.0), (47, 3.0), (49, 3.0), (50, 3.0),
    (45, 3.5), (47, 3.5), (49, 3.5), (50, 3.5),
    # Bar 4 (comp on beat 2 and 4)
    (45, 4.0), (47, 4.0), (49, 4.0), (50, 4.0),
    (45, 4.5), (47, 4.5), (49, 4.5), (50, 4.5)
]

for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.125)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.875)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.5)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.25)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    # Add kick and snare
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Ab - Bb - F (hanging on Bb)
sax_notes = [
    # Bar 2 (melody starts here)
    (53, 1.5), (51, 1.875), (50, 2.25),
    # Bar 3 (leave it hanging on Bb)
    (50, 2.625),
    # Bar 4 (resolve back to F)
    (53, 3.0), (51, 3.375), (50, 3.75)
]

for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
