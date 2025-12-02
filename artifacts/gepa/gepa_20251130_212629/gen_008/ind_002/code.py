
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

# Bass: Walking line, chromatic approaches, D minor scale
bass_notes = [
    (50, 1.5, 0.375), (51, 1.875, 0.375), (49, 2.25, 0.375), (50, 2.625, 0.375),
    (52, 3.0, 0.375), (53, 3.375, 0.375), (51, 3.75, 0.375), (52, 4.125, 0.375),
    (54, 4.5, 0.375), (55, 4.875, 0.375), (53, 5.25, 0.375), (54, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.375), (67, 1.875, 0.375), (64, 1.875, 0.375), (69, 1.875, 0.375),
    # Bar 3
    (62, 3.375, 0.375), (67, 3.375, 0.375), (64, 3.375, 0.375), (69, 3.375, 0.375),
    # Bar 4
    (62, 4.875, 0.375), (67, 4.875, 0.375), (64, 4.875, 0.375), (69, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375), (38, start + 0.375, 0.375), (42, start + 0.0, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875)
    ]
    for note, start_time, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D minor scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G -> D, F, Eb, G
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (67, 2.625, 0.375),
    (62, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (67, 4.125, 0.375),
    (62, 4.5, 0.375), (64, 4.875, 0.375), (63, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
