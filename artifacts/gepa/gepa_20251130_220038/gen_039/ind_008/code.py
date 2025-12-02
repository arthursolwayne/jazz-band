
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375), (42, 1.125, 0.375),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.375), (42, 2.625, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
# Dm scale: D F G A C (Dorian mode)
# Walking bass line: D → F → Eb → G → A → Bb → C → D
bass_notes = [
    (50, 1.5, 0.375), (53, 1.875, 0.375), (51, 2.25, 0.375), (55, 2.625, 0.375),
    (57, 3.0, 0.375), (58, 3.375, 0.375), (59, 3.75, 0.375), (62, 4.125, 0.375),
    (50, 4.5, 0.375), (53, 4.875, 0.375), (51, 5.25, 0.375), (55, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = [
    # Bar 2 - Dm7
    (50, 1.5, 0.375), (53, 1.5, 0.375), (57, 1.5, 0.375), (60, 1.5, 0.375),
    # Bar 3 - G7
    (67, 3.0, 0.375), (71, 3.0, 0.375), (67, 3.0, 0.375), (74, 3.0, 0.375),
    # Bar 4 - Cm7
    (60, 4.5, 0.375), (63, 4.5, 0.375), (67, 4.5, 0.375), (71, 4.5, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.375), (42, 2.625, 0.375),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.75, 0.375), (42, 4.125, 0.375),
    # Bar 3
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 5.25, 0.375), (42, 5.625, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish
# Motif: D (62) → F (65) → Eb (64) → G (67) 
# Start on bar 2, let it hang, then resolve on bar 4
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (64, 2.25, 0.375), (67, 2.625, 0.375),
    (62, 4.5, 0.375), (65, 4.875, 0.375), (64, 5.25, 0.375), (67, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
