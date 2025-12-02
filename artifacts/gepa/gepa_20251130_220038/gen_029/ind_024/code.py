
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (bass): Walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (61, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (60, 3.75, 0.375), (61, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (60, 5.25, 0.375), (61, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane (piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.5, 0.125), (71, 1.5, 0.125), (69, 1.5, 0.125), (72, 1.5, 0.125),
    # Bar 3
    (72, 2.625, 0.125), (76, 2.625, 0.125), (74, 2.625, 0.125), (77, 2.625, 0.125),
    # Bar 4
    (67, 3.75, 0.125), (71, 3.75, 0.125), (69, 3.75, 0.125), (72, 3.75, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (drums): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat_notes = [
        (bar_start, 0.375), (bar_start + 0.75, 0.375),
        (bar_start + 1.125, 0.375), (bar_start + 1.5, 0.375)
    ]
    for start, duration in hihat_notes:
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + duration)
        drums.notes.append(hihat)
    drums.notes.append(kick)
    drums.notes.append(snare)

# Dante (sax): One short motif, make it sing
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    (65, 2.625, 0.375), (62, 3.0, 0.375), (60, 3.375, 0.375),
    (62, 3.75, 0.375), (65, 4.125, 0.375), (67, 4.5, 0.375),
    (65, 4.875, 0.375), (62, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
