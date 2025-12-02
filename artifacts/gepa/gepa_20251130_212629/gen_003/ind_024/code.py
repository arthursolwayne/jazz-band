
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F minor, chromatic approaches
bass_notes = [
    (48, 1.5), (49, 1.875), (47, 2.25), (46, 2.625),
    (50, 3.0), (51, 3.375), (49, 3.75), (48, 4.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 1.875), (57, 1.875), (50, 1.875), (58, 1.875),  # F7 on beat 2
    (53, 3.375), (57, 3.375), (50, 3.375), (58, 3.375)   # F7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: Motif - F, G#, Bb, A
sax_notes = [
    (65, 1.5), (68, 1.875), (62, 2.25), (60, 2.625),
    (65, 3.0), (68, 3.375), (62, 3.75), (60, 4.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in F minor
bass_notes = [
    (50, 3.0), (51, 3.375), (49, 3.75), (48, 4.125),
    (52, 4.5), (53, 4.875), (51, 5.25), (50, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 3.375), (57, 3.375), (50, 3.375), (58, 3.375),  # F7 on beat 2
    (53, 4.875), (57, 4.875), (50, 4.875), (58, 4.875)   # F7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif variation - F, G#, A, Bb
sax_notes = [
    (65, 3.0), (68, 3.375), (60, 3.75), (62, 4.125),
    (65, 4.5), (68, 4.875), (60, 5.25), (62, 5.625)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in F minor
bass_notes = [
    (52, 4.5), (53, 4.875), (51, 5.25), (50, 5.625),
    (54, 6.0), (55, 6.375), (53, 6.75), (52, 7.125)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (53, 4.875), (57, 4.875), (50, 4.875), (58, 4.875),  # F7 on beat 2
    (53, 6.375), (57, 6.375), (50, 6.375), (58, 6.375)   # F7 on beat 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif resolution - F, Bb, A, G#
sax_notes = [
    (65, 4.5), (62, 4.875), (60, 5.25), (68, 5.625),
    (65, 6.0), (62, 6.375), (60, 6.75), (68, 7.125)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
