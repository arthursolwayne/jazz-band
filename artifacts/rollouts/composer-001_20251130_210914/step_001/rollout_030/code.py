
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
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4
# Bar 2 and 3: sax melody, piano comp, bass walking
# Bar 4: sax finishes the motif, piano resolves, bass walks to the end

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (64, 1.5, 0.375), (65, 1.875, 0.375), (63, 2.25, 0.375),
    (62, 2.625, 0.375),
    # Bar 3
    (64, 3.0, 0.375), (65, 3.375, 0.375), (63, 3.75, 0.375),
    (62, 4.125, 0.375),
    # Bar 4
    (64, 4.5, 0.375), (65, 4.875, 0.375), (63, 5.25, 0.375),
    (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (59, 2.25, 0.1875), (60, 2.25, 0.1875), (62, 2.25, 0.1875), (64, 2.25, 0.1875),
    # Bar 3: Fm7 on beat 2
    (59, 3.75, 0.1875), (60, 3.75, 0.1875), (62, 3.75, 0.1875), (64, 3.75, 0.1875),
    # Bar 4: Fm7 on beat 2
    (59, 5.25, 0.1875), (60, 5.25, 0.1875), (62, 5.25, 0.1875), (64, 5.25, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: melody in Fm
# Motif: F - Ab - Bb - D - F
sax_notes = [
    # Bar 2: start the motif
    (65, 1.5, 0.375), (63, 1.875, 0.375), (62, 2.25, 0.375),
    (67, 2.625, 0.375),
    # Bar 3: continue the motif
    (63, 3.0, 0.375), (62, 3.375, 0.375), (65, 3.75, 0.375),
    (67, 4.125, 0.375),
    # Bar 4: finish the motif
    (65, 4.5, 0.375), (63, 4.875, 0.375), (62, 5.25, 0.375),
    (67, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
