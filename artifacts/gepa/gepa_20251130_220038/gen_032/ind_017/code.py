
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    (62, 3.0, 0.375), (63, 3.375, 0.375), (61, 3.75, 0.375), (60, 4.125, 0.375),
    (62, 4.5, 0.375), (63, 4.875, 0.375), (61, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
# Dm7 = D F A C
piano_notes = [
    (50, 2.0, 0.375), (52, 2.0, 0.375), (55, 2.0, 0.375), (57, 2.0, 0.375),
    (50, 3.0, 0.375), (52, 3.0, 0.375), (55, 3.0, 0.375), (57, 3.0, 0.375),
    (50, 4.0, 0.375), (52, 4.0, 0.375), (55, 4.0, 0.375), (57, 4.0, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Saxophone (Dante): short motif, make it sing
# Start on D (62), then Bb (60), then F (57), then D (62) again
sax_notes = [
    (62, 1.5, 0.375), (60, 1.875, 0.375), (57, 2.25, 0.375), (62, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375), (38, start + 0.375, 0.375), (42, start + 0.0, 0.1875),
        (36, start + 0.75, 0.375), (38, start + 1.125, 0.375), (42, start + 0.75, 0.1875)
    ]
    for note, start_time, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
