
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
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.375),
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
bass_notes = [
    (43, 1.5, 0.375), (44, 1.875, 0.375), (42, 2.25, 0.375), (45, 2.625, 0.375),  # Bar 2
    (43, 3.0, 0.375), (44, 3.375, 0.375), (42, 3.75, 0.375), (45, 4.125, 0.375),   # Bar 3
    (43, 4.5, 0.375), (44, 4.875, 0.375), (42, 5.25, 0.375), (45, 5.625, 0.375)    # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.875, 0.1875), (50, 1.875, 0.1875), (53, 1.875, 0.1875), (55, 1.875, 0.1875),  # F7
    # Bar 3
    (48, 3.375, 0.1875), (50, 3.375, 0.1875), (53, 3.375, 0.1875), (55, 3.375, 0.1875),  # F7
    # Bar 4
    (48, 4.875, 0.1875), (50, 4.875, 0.1875), (53, 4.875, 0.1875), (55, 4.875, 0.1875)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.4375, 0.1875), (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante): short motif, make it sing, start it, leave it hanging, finish it
# Motif: F -> Ab -> Bb -> C
# Bar 2: start the motif
sax_notes = [
    (53, 1.5, 0.375), (51, 1.875, 0.375), (50, 2.25, 0.375), (55, 2.625, 0.375),  # Bar 2
    (50, 3.0, 0.375), (51, 3.375, 0.375), (53, 3.75, 0.375), (55, 4.125, 0.375),   # Bar 3
    (53, 4.5, 0.375), (51, 4.875, 0.375), (50, 5.25, 0.375), (55, 5.625, 0.375)    # Bar 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('waynes_intro.mid')
