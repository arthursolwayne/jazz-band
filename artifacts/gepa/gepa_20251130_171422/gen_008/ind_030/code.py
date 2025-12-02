
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
    (36, 0.0, 0.375), # Kick on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.125, 0.375), # Kick on 3
    (38, 1.5, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), # D
    (60, 1.875, 0.375), # Bb
    (62, 2.25, 0.375), # D
    (64, 2.625, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on 2, Gm7 on 4
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2
    (62, 2.25, 0.375), # D
    (64, 2.25, 0.375), # F
    (69, 2.25, 0.375), # A
    (67, 2.25, 0.375), # C

    # Gm7 (G, Bb, D, F) on beat 4
    (67, 2.625, 0.375), # G
    (60, 2.625, 0.375), # Bb
    (69, 2.625, 0.375), # D
    (64, 2.625, 0.375) # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Short motif, D, F#, C, G (Dm scale with tension)
sax_notes = [
    (62, 1.5, 0.375), # D
    (66, 1.875, 0.375), # F#
    (67, 2.25, 0.375), # G
    (60, 2.625, 0.375) # Bb (hanging note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 3.0, 0.375), # D
    (60, 3.375, 0.375), # Bb
    (62, 3.75, 0.375), # D
    (64, 4.125, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on 2, Gm7 on 4
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2
    (62, 3.75, 0.375), # D
    (64, 3.75, 0.375), # F
    (69, 3.75, 0.375), # A
    (67, 3.75, 0.375), # C

    # Gm7 (G, Bb, D, F) on beat 4
    (67, 4.125, 0.375), # G
    (60, 4.125, 0.375), # Bb
    (69, 4.125, 0.375), # D
    (64, 4.125, 0.375) # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375), # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.125, 0.375), # Kick on 3
    (38, 4.5, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif, restate the first phrase
sax_notes = [
    (62, 3.0, 0.375), # D
    (66, 3.375, 0.375), # F#
    (67, 3.75, 0.375), # G
    (60, 4.125, 0.375) # Bb (hanging note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 4.5, 0.375), # D
    (60, 4.875, 0.375), # Bb
    (62, 5.25, 0.375), # D
    (64, 5.625, 0.375) # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7 on 2, Gm7 on 4
piano_notes = [
    # Dm7 (D, F, A, C) on beat 2
    (62, 5.25, 0.375), # D
    (64, 5.25, 0.375), # F
    (69, 5.25, 0.375), # A
    (67, 5.25, 0.375), # C

    # Gm7 (G, Bb, D, F) on beat 4
    (67, 5.625, 0.375), # G
    (60, 5.625, 0.375), # Bb
    (69, 5.625, 0.375), # D
    (64, 5.625, 0.375) # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &
    (42, 5.625, 0.1875), # Hihat on 4
    (36, 5.625, 0.375), # Kick on 3
    (38, 6.0, 0.375)    # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif, resolve the tension
sax_notes = [
    (62, 4.5, 0.375), # D
    (66, 4.875, 0.375), # F#
    (67, 5.25, 0.375), # G
    (62, 5.625, 0.375) # D (resolve the tension)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
