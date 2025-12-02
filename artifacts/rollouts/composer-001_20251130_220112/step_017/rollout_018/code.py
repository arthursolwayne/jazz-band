
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
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Sax melody - motif in F: F, G#, Bb, A (F7sus4)
sax_notes = [
    (84, 1.5, 0.375), (87, 1.875, 0.375), (82, 2.25, 0.375), (81, 2.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in F, chromatic approach to Bb on beat 3
bass_notes = [
    (53, 1.5, 0.375), (54, 1.875, 0.375), (55, 2.25, 0.375), (51, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    (76, 1.875, 0.375), (79, 1.875, 0.375), (78, 1.875, 0.375), # F7 on beat 2
    (76, 2.625, 0.375), (79, 2.625, 0.375), (78, 2.625, 0.375)  # F7 on beat 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif, but transposes up a third to A
sax_notes = [
    (93, 3.0, 0.375), (96, 3.375, 0.375), (91, 3.75, 0.375), (90, 4.125, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in A, chromatic approach to D on beat 3
bass_notes = [
    (64, 3.0, 0.375), (65, 3.375, 0.375), (66, 3.75, 0.375), (62, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Comp on 2 and 4 with 7th chords in A
piano_notes = [
    (81, 3.375, 0.375), (84, 3.375, 0.375), (83, 3.375, 0.375), # A7 on beat 2
    (81, 4.125, 0.375), (84, 4.125, 0.375), (83, 4.125, 0.375)  # A7 on beat 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Continue pattern
drum_notes = [
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (42, 4.125, 0.1875), (42, 4.3125, 0.1875), (42, 4.5, 0.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax resolves motif back to F, ending on A
sax_notes = [
    (84, 4.5, 0.375), (87, 4.875, 0.375), (81, 5.25, 0.375), (81, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in F, resolves on beat 4
bass_notes = [
    (53, 4.5, 0.375), (54, 4.875, 0.375), (55, 5.25, 0.375), (53, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Comp on 2 and 4 with 7th chords in F
piano_notes = [
    (76, 4.875, 0.375), (79, 4.875, 0.375), (78, 4.875, 0.375), # F7 on beat 2
    (76, 5.625, 0.375), (79, 5.625, 0.375), (78, 5.625, 0.375)  # F7 on beat 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Final bar
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875), (42, 6.0, 0.0)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
