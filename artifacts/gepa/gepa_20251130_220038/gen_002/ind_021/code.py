
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line, chromatic approach on beat 3
bass_notes = [
    (37, 1.5, 0.375), (39, 1.875, 0.375), (40, 2.25, 0.375), (42, 2.625, 0.375),
    (44, 3.0, 0.375), (46, 3.375, 0.375), (47, 3.75, 0.375), (49, 4.125, 0.375),
    (51, 4.5, 0.375), (53, 4.875, 0.375), (55, 5.25, 0.375), (57, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano - 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 on beat 2
    (64, 1.875, 0.375), (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375),
    # Bar 3: Bb7 on beat 2
    (67, 3.375, 0.375), (70, 3.375, 0.375), (72, 3.375, 0.375), (74, 3.375, 0.375),
    # Bar 4: F7 on beat 2
    (64, 4.875, 0.375), (67, 4.875, 0.375), (69, 4.875, 0.375), (71, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums - continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875)
    ]
    for note, s, d in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d)
        drums.notes.append(dr)

# Saxophone - short motif: F - Bb - D - F
# Start on beat 2 of bar 2 (1.875), end on beat 3 of bar 2 (2.625)
sax_notes = [
    (64, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375), (64, 3.0, 0.375)
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
