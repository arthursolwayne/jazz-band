
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 walking line, chromatic approaches, no repeating notes
bass_notes = [
    (37, 1.5),   # Bb (Fm7 rootless)
    (35, 1.75),  # Eb (chromatic approach)
    (34, 2.0),   # D (chromatic approach)
    (36, 2.25),  # F (root)
    (38, 2.5),   # G (3rd)
    (37, 2.75),  # F (chromatic approach)
    (35, 3.0),   # Eb (chromatic approach)
    (33, 3.25),  # D (chromatic approach)
    (36, 3.5),   # F (root)
    (38, 3.75),  # G (3rd)
    (37, 4.0),   # F (chromatic approach)
    (35, 4.25),  # Eb (chromatic approach)
    (34, 4.5),   # D (chromatic approach)
    (36, 4.75),  # F (root)
    (38, 5.0),   # G (3rd)
    (37, 5.25),  # F (chromatic approach)
    (35, 5.5),   # Eb (chromatic approach)
    (33, 5.75)   # D (chromatic approach)
]
for note, time in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
# Fm7, Bbm7, Ebm7, Abm7
piano_notes = [
    # Bar 2
    (34, 1.75), (31, 1.75), (30, 1.75), (28, 1.75),  # Fm7
    # Bar 3
    (30, 2.75), (27, 2.75), (26, 2.75), (24, 2.75),  # Bbm7
    # Bar 4
    (26, 3.75), (23, 3.75), (22, 3.75), (20, 3.75),  # Ebm7
    # Bar 5
    (22, 4.75), (19, 4.75), (18, 4.75), (16, 4.75)   # Abm7
]
for note, time in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Sax: One short motif, make it sing
# F, Ab, Bb, D, F
sax_notes = [
    (36, 1.5), (34, 1.625), (33, 1.75), (38, 1.875), (36, 2.0)
]
for note, time in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(n)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start), (38, start + 0.375), (42, start + 0.375),
        (36, start + 0.75), (38, start + 1.125), (42, start + 1.125),
        (36, start + 1.5), (38, start + 1.875), (42, start + 1.875)
    ]
    for note, time in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
