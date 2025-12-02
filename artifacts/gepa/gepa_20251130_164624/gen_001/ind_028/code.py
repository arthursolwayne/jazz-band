
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (61, 2.625, 0.375),
    (63, 3.0, 0.375), (64, 3.375, 0.375), (62, 3.75, 0.375), (63, 4.125, 0.375),
    (64, 4.5, 0.375), (65, 4.875, 0.375), (63, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    (62, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875), (72, 1.875, 0.1875),
    # Bar 3: Dm7
    (62, 3.375, 0.1875), (67, 3.375, 0.1875), (69, 3.375, 0.1875), (72, 3.375, 0.1875),
    # Bar 4: Dm7
    (62, 4.875, 0.1875), (67, 4.875, 0.1875), (69, 4.875, 0.1875), (72, 4.875, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick=36, snare=38, hihat=42
# Bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    drum_notes = [
        (36, bar_start + 0.0, 0.375), (38, bar_start + 0.375, 0.375), (42, bar_start + 0.0, 0.1875),
        (36, bar_start + 0.75, 0.375), (38, bar_start + 1.125, 0.375), (42, bar_start + 0.75, 0.1875)
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), G (67), D (62)
sax_notes = [
    (62, 1.5, 0.5), (65, 2.0, 0.5), (67, 2.5, 0.5), (62, 3.0, 0.5)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
