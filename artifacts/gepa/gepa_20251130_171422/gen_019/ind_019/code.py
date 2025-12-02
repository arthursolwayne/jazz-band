
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat on 1
    (42, 0.125, 0.125),  # Hihat on &
    (42, 0.25, 0.125),  # Hihat on 2
    (38, 0.25, 0.375),  # Snare on 2
    (42, 0.375, 0.125),  # Hihat on &
    (42, 0.5, 0.125),  # Hihat on 3
    (36, 0.5, 0.375),  # Kick on 3
    (42, 0.625, 0.125),  # Hihat on &
    (42, 0.75, 0.125),  # Hihat on 4
    (38, 0.75, 0.375),  # Snare on 4
    (42, 0.875, 0.125),  # Hihat on &
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif in D, concise and memorable
sax_notes = [
    (62, 1.5, 0.375),  # D (melodic motif)
    (65, 1.875, 0.375),  # F#
    (67, 2.25, 0.375),  # A
    (62, 2.625, 0.375),  # D (repeat)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Chromatic walking line
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375),  # F#
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
# D7 on beat 2, G7 on beat 4
piano_notes = [
    # D7: D, F#, A, C
    (62, 1.875, 0.375),
    (65, 1.875, 0.375),
    (67, 1.875, 0.375),
    (60, 1.875, 0.375),
    # G7: G, B, D, F
    (67, 2.625, 0.375),
    (71, 2.625, 0.375),
    (62, 2.625, 0.375),
    (65, 2.625, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation
sax_notes = [
    (67, 3.0, 0.375),  # A (variation)
    (65, 3.375, 0.375),  # F#
    (62, 3.75, 0.375),  # D
    (67, 4.125, 0.375),  # A (repeat)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Chromatic walking line
bass_notes = [
    (65, 3.0, 0.375),  # F#
    (66, 3.375, 0.375),  # G
    (67, 3.75, 0.375),  # A
    (69, 4.125, 0.375),  # Bb
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
# G7 on beat 2, C7 on beat 4
piano_notes = [
    # G7: G, B, D, F
    (67, 3.375, 0.375),
    (71, 3.375, 0.375),
    (62, 3.375, 0.375),
    (65, 3.375, 0.375),
    # C7: C, E, G, Bb
    (60, 4.125, 0.375),
    (64, 4.125, 0.375),
    (67, 4.125, 0.375),
    (69, 4.125, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    (62, 4.5, 0.375),  # D
    (67, 4.875, 0.375),  # A
    (65, 5.25, 0.375),  # F#
    (62, 5.625, 0.375),  # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Chromatic walking line
bass_notes = [
    (69, 4.5, 0.375),  # Bb
    (71, 4.875, 0.375),  # B
    (72, 5.25, 0.375),  # C
    (74, 5.625, 0.375),  # D
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
# C7 on beat 2, F7 on beat 4
piano_notes = [
    # C7: C, E, G, Bb
    (60, 4.875, 0.375),
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (69, 4.875, 0.375),
    # F7: F, A, C, Eb
    (65, 5.625, 0.375),
    (69, 5.625, 0.375),
    (60, 5.625, 0.375),
    (62, 5.625, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on 1
    (42, 4.625, 0.125),  # Hihat on &
    (42, 4.75, 0.125),  # Hihat on 2
    (38, 4.75, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on &
    (42, 5.0, 0.125),  # Hihat on 3
    (36, 5.0, 0.375),  # Kick on 3
    (42, 5.125, 0.125),  # Hihat on &
    (42, 5.25, 0.125),  # Hihat on 4
    (38, 5.25, 0.375),  # Snare on 4
    (42, 5.375, 0.125),  # Hihat on &
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
