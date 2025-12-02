
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.75, 0.375),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.875, 0.375)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C4 (60) -> E4 (64) -> G4 (67) -> B4 (71) -> C5 (72) -> G4 (67) -> E4 (64) -> C4 (60)
sax_notes = [
    (60, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375), (71, 2.625, 0.375),
    (72, 2.625, 0.375), (67, 3.0, 0.375), (64, 3.375, 0.375), (60, 3.75, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in C (C3 -> D3 -> E3 -> F3 -> G3 -> A3 -> B3 -> C4)
bass_notes = [
    (48, 1.5, 0.375), (50, 1.875, 0.375), (52, 2.25, 0.375), (53, 2.625, 0.375),
    (55, 2.625, 0.375), (57, 3.0, 0.375), (59, 3.375, 0.375), (60, 3.75, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4 (C7 on 2, F7 on 4)
piano_notes = [
    # C7: C4 (60) + E4 (64) + B4 (71) + D5 (72)
    (60, 1.875, 0.375), (64, 1.875, 0.375), (71, 1.875, 0.375), (72, 1.875, 0.375),
    # F7: F4 (65) + A4 (69) + D5 (72) + E5 (74)
    (65, 3.0, 0.375), (69, 3.0, 0.375), (72, 3.0, 0.375), (74, 3.0, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: Bar 2
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 2.25, 0.375),
    (36, 2.625, 0.375), (38, 3.0, 0.375), (42, 3.375, 0.375)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif but with a slight variation
sax_notes = [
    (60, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375), (71, 4.125, 0.375),
    (72, 4.125, 0.375), (67, 4.5, 0.375), (64, 4.875, 0.375), (60, 5.25, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in C (C3 -> D3 -> E3 -> F3 -> G3 -> A3 -> B3 -> C4)
bass_notes = [
    (48, 3.0, 0.375), (50, 3.375, 0.375), (52, 3.75, 0.375), (53, 4.125, 0.375),
    (55, 4.125, 0.375), (57, 4.5, 0.375), (59, 4.875, 0.375), (60, 5.25, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4 (C7 on 2, F7 on 4)
piano_notes = [
    # C7: C4 (60) + E4 (64) + B4 (71) + D5 (72)
    (60, 3.375, 0.375), (64, 3.375, 0.375), (71, 3.375, 0.375), (72, 3.375, 0.375),
    # F7: F4 (65) + A4 (69) + D5 (72) + E5 (74)
    (65, 4.5, 0.375), (69, 4.5, 0.375), (72, 4.5, 0.375), (74, 4.5, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: Bar 3
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.75, 0.375),
    (36, 4.125, 0.375), (38, 4.5, 0.375), (42, 4.875, 0.375)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a phrase that echoes the first
sax_notes = [
    (60, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375), (71, 5.625, 0.375),
    (72, 5.625, 0.375), (67, 6.0, 0.375), (64, 6.375, 0.375), (60, 6.75, 0.375)
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bass: Walking line in C (C3 -> D3 -> E3 -> F3 -> G3 -> A3 -> B3 -> C4)
bass_notes = [
    (48, 4.5, 0.375), (50, 4.875, 0.375), (52, 5.25, 0.375), (53, 5.625, 0.375),
    (55, 5.625, 0.375), (57, 6.0, 0.375), (59, 6.375, 0.375), (60, 6.75, 0.375)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano: 7th chords on 2 and 4 (C7 on 2, F7 on 4)
piano_notes = [
    # C7: C4 (60) + E4 (64) + B4 (71) + D5 (72)
    (60, 4.875, 0.375), (64, 4.875, 0.375), (71, 4.875, 0.375), (72, 4.875, 0.375),
    # F7: F4 (65) + A4 (69) + D5 (72) + E5 (74)
    (65, 6.0, 0.375), (69, 6.0, 0.375), (72, 6.0, 0.375), (74, 6.0, 0.375)
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 5.25, 0.375),
    (36, 5.625, 0.375), (38, 6.0, 0.375), (42, 6.375, 0.375)
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
