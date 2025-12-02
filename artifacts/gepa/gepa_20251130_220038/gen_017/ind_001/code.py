
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.375), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 1.5, 0.375), # F (root)
    (40, 1.875, 0.375), # Gb (chromatic)
    (37, 2.25, 0.375), # Eb (3rd)
    (36, 2.625, 0.375) # D (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (44, 1.875, 0.375), # Bb7 (2)
    (41, 1.875, 0.375),
    (47, 1.875, 0.375),
    (50, 1.875, 0.375),
    (44, 2.625, 0.375), # Bb7 (4)
    (41, 2.625, 0.375),
    (47, 2.625, 0.375),
    (50, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Melody - One short motif, make it sing
sax_notes = [
    (41, 1.5, 0.75),   # Gm (start)
    (43, 2.25, 0.75),  # A (leave it hanging)
    (41, 3.0, 0.75)    # Gm (come back and finish)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (36, 3.0, 0.375), # D (root)
    (37, 3.375, 0.375), # Eb (chromatic)
    (39, 3.75, 0.375), # F (3rd)
    (40, 4.125, 0.375) # Gb (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (44, 3.375, 0.375), # Bb7 (2)
    (41, 3.375, 0.375),
    (47, 3.375, 0.375),
    (50, 3.375, 0.375),
    (44, 4.125, 0.375), # Bb7 (4)
    (41, 4.125, 0.375),
    (47, 4.125, 0.375),
    (50, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.375), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (39, 4.5, 0.375), # F (root)
    (40, 4.875, 0.375), # Gb (chromatic)
    (37, 5.25, 0.375), # Eb (3rd)
    (36, 5.625, 0.375) # D (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (44, 4.875, 0.375), # Bb7 (2)
    (41, 4.875, 0.375),
    (47, 4.875, 0.375),
    (50, 4.875, 0.375),
    (44, 5.625, 0.375), # Bb7 (4)
    (41, 5.625, 0.375),
    (47, 5.625, 0.375),
    (50, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.375)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: End on a sustained note, leave a pause
sax_notes = [
    (41, 5.625, 0.375), # Gm
    (41, 6.0, 0.375)    # Gm
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
