
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
    (36, 0.0, 0.375), (42, 0.0, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm
bass_notes = [
    # Bar 2
    (36, 1.5, 0.375), (35, 1.875, 0.375), (37, 2.25, 0.375), (34, 2.625, 0.375),
    # Bar 3
    (36, 3.0, 0.375), (35, 3.375, 0.375), (37, 3.75, 0.375), (34, 4.125, 0.375),
    # Bar 4
    (36, 4.5, 0.375), (35, 4.875, 0.375), (37, 5.25, 0.375), (34, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords on 2 and 4 (comping)
piano_notes = [
    # Bar 2
    (40, 2.25, 0.375), (43, 2.25, 0.375), (45, 2.25, 0.375), (47, 2.25, 0.375),
    # Bar 3
    (39, 3.75, 0.375), (42, 3.75, 0.375), (44, 3.75, 0.375), (46, 3.75, 0.375),
    # Bar 4
    (40, 5.25, 0.375), (43, 5.25, 0.375), (45, 5.25, 0.375), (47, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375), (42, start, 0.125),
        (38, start + 0.375, 0.375), (42, start + 0.375, 0.125),
        (36, start + 0.75, 0.375), (42, start + 0.75, 0.125),
        (38, start + 1.125, 0.375), (42, start + 1.125, 0.125)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Saxophone (Dante): Short motif, make it sing
# Motif: Fm7 (F, Ab, Bb, Db) - start with F, then Ab, then Bb, leave it hanging
sax_notes = [
    (53, 1.5, 0.375), (56, 1.875, 0.375), (58, 2.25, 0.375),
    (53, 3.0, 0.375), (56, 3.375, 0.375), (58, 3.75, 0.375),
    (53, 4.5, 0.375), (56, 4.875, 0.375), (58, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
