
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (44, 1.5, 0.375),  # F
    (43, 1.875, 0.375), # Eb
    (42, 2.25, 0.375),  # D
    (41, 2.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (1.875)
    (52, 1.875, 0.1875), # F
    (56, 1.875, 0.1875), # A
    (50, 1.875, 0.1875), # Eb
    (57, 1.875, 0.1875), # Bb
    # Bb7 on beat 4 (2.625)
    (50, 2.625, 0.1875), # Bb
    (53, 2.625, 0.1875), # D
    (48, 2.625, 0.1875), # F
    (55, 2.625, 0.1875), # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody - 4-note motif starting on F (52)
sax_notes = [
    (52, 1.5, 0.375), # F
    (54, 1.875, 0.375), # G
    (50, 2.25, 0.375), # Eb
    (52, 2.625, 0.375), # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (44, 3.0, 0.375),  # F
    (43, 3.375, 0.375), # Eb
    (42, 3.75, 0.375),  # D
    (41, 4.125, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (3.375)
    (52, 3.375, 0.1875), # F
    (56, 3.375, 0.1875), # A
    (50, 3.375, 0.1875), # Eb
    (57, 3.375, 0.1875), # Bb
    # Bb7 on beat 4 (4.125)
    (50, 4.125, 0.1875), # Bb
    (53, 4.125, 0.1875), # D
    (48, 4.125, 0.1875), # F
    (55, 4.125, 0.1875), # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody - mirror of the opening motif
sax_notes = [
    (52, 3.0, 0.375), # F
    (54, 3.375, 0.375), # G
    (50, 3.75, 0.375), # Eb
    (52, 4.125, 0.375), # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    (44, 4.5, 0.375),  # F
    (43, 4.875, 0.375), # Eb
    (42, 5.25, 0.375),  # D
    (41, 5.625, 0.375)  # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (4.875)
    (52, 4.875, 0.1875), # F
    (56, 4.875, 0.1875), # A
    (50, 4.875, 0.1875), # Eb
    (57, 4.875, 0.1875), # Bb
    # Bb7 on beat 4 (5.625)
    (50, 5.625, 0.1875), # Bb
    (53, 5.625, 0.1875), # D
    (48, 5.625, 0.1875), # F
    (55, 5.625, 0.1875), # Ab
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody - variation of the motif
sax_notes = [
    (52, 4.5, 0.375), # F
    (54, 4.875, 0.375), # G
    (50, 5.25, 0.375), # Eb
    (52, 5.625, 0.375), # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 5.625, 0.1875), (42, 5.8125, 0.1875), (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
