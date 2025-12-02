
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line in Fm, chromatic approaches
bass_notes = [
    (44, 1.5, 0.375), (45, 1.875, 0.375), (43, 2.25, 0.375), (42, 2.625, 0.375),
    (44, 3.0, 0.375), (45, 3.375, 0.375), (43, 3.75, 0.375), (42, 4.125, 0.375),
    (44, 4.5, 0.375), (45, 4.875, 0.375), (43, 5.25, 0.375), (42, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 and 4, Fm7, Bb7, Eb7, Ab7
piano_notes = [
    # Bar 2
    (53, 1.875, 0.375), (57, 1.875, 0.375), (58, 1.875, 0.375), (60, 1.875, 0.375),
    # Bar 3
    (56, 3.375, 0.375), (60, 3.375, 0.375), (61, 3.375, 0.375), (63, 3.375, 0.375),
    # Bar 4
    (55, 4.875, 0.375), (59, 4.875, 0.375), (60, 4.875, 0.375), (62, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Saxophone - short motif, make it sing
# Fm7: F, Ab, Bb, Db
# Melody: F -> Ab -> Bb -> Db -> F (descending)
# Start at 1.5s (bar 2), each note 0.375s
sax_notes = [
    (53, 1.5, 0.375),  # F
    (51, 1.875, 0.375), # Ab
    (50, 2.25, 0.375),  # Bb
    (48, 2.625, 0.375), # Db
    (53, 3.0, 0.375)    # F (return)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
