
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
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (51, 2.625, 0.375), (50, 2.625, 0.375), (49, 2.625, 0.375), (48, 2.625, 0.375),
    (48, 3.0, 0.375), (49, 3.375, 0.375), (50, 3.75, 0.375), (51, 4.125, 0.375),
    (51, 4.5, 0.375), (50, 4.875, 0.375), (49, 5.25, 0.375), (48, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.5, 0.375), (69, 1.5, 0.375), (67, 1.5, 0.375), (71, 1.5, 0.375),
    (64, 2.25, 0.375), (69, 2.25, 0.375), (67, 2.25, 0.375), (71, 2.25, 0.375),
    (64, 3.0, 0.375), (69, 3.0, 0.375), (67, 3.0, 0.375), (71, 3.0, 0.375),
    (64, 3.75, 0.375), (69, 3.75, 0.375), (67, 3.75, 0.375), (71, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7 scale: F, G, A, Bb, B, C, D, F
sax_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (69, 2.25, 0.375), (65, 2.625, 0.375),
    (67, 3.0, 0.375), (69, 3.375, 0.375), (65, 3.75, 0.375), (67, 4.125, 0.375),
    (69, 4.5, 0.375), (65, 4.875, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 + (bar - 2) * 1.5
    kick_start = bar_start
    snare_start = bar_start + 0.375
    hihat_start = bar_start
    for i in range(4):
        kick_start += 0.75
        hihat_start += 0.375
        if i % 2 == 0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
        else:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
