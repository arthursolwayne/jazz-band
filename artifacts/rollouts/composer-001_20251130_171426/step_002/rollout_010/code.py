
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
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375), (39, 1.875, 0.375), (38, 2.25, 0.375), (36, 2.625, 0.375),  # Bar 2
    (35, 3.0, 0.375), (37, 3.375, 0.375), (38, 3.75, 0.375), (40, 4.125, 0.375),  # Bar 3
    (39, 4.5, 0.375), (37, 4.875, 0.375), (36, 5.25, 0.375), (34, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (42, 2.25, 0.375), (44, 2.25, 0.375), (46, 2.25, 0.375), (48, 2.25, 0.375),  # F7 on beat 3
    (43, 3.0, 0.375), (45, 3.0, 0.375), (47, 3.0, 0.375), (49, 3.0, 0.375),      # Bb7 on beat 2
    (42, 4.5, 0.375), (44, 4.5, 0.375), (46, 4.5, 0.375), (48, 4.5, 0.375),      # F7 on beat 3
    (43, 5.625, 0.375), (45, 5.625, 0.375), (47, 5.625, 0.375), (49, 5.625, 0.375) # Bb7 on beat 2
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif - start with a short phrase, leave it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F, Ab, Bb, F
sax_notes = [
    (53, 1.5, 0.375), (51, 1.875, 0.375), (50, 2.25, 0.375), (53, 2.625, 0.375)  # Bar 2
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
