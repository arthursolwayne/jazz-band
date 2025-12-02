
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 1.0, 0.375),  # Kick on beat 1
    (42, 1.0, 0.125),  # Hi-hat on 1& (beat 1 + 0.125)
    (42, 1.0, 0.375),  # Hi-hat on &2
    (38, 1.0, 0.5),    # Snare on beat 2
    (42, 1.0, 0.625),  # Hi-hat on 2&
    (42, 1.0, 0.875),  # Hi-hat on &3
    (36, 1.0, 1.0),    # Kick on beat 3
    (42, 1.0, 1.125),  # Hi-hat on 3&
    (42, 1.0, 1.375),  # Hi-hat on &4
    (38, 1.0, 1.5),    # Snare on beat 4
]

for note, velocity, time in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start and leave it hanging

# Sax - F (F4), G (G4), Bb (Bb4), F (F4) - 8th notes
sax_notes = [
    (78, 100, 1.5),    # F4
    (81, 100, 1.75),   # G4
    (82, 100, 2.0),    # Bb4
    (78, 100, 2.25),   # F4
]

for note, velocity, time in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass: walking line in F
# F (F3), G (G3), A (A3), Bb (Bb3), F (F3), G (G3), A (A3), Bb (Bb3)
bass_notes = [
    (53, 80, 1.5),     # F3
    (55, 80, 1.75),    # G3
    (57, 80, 2.0),     # A3
    (58, 80, 2.25),    # Bb3
    (53, 80, 2.5),     # F3
    (55, 80, 2.75),    # G3
    (57, 80, 3.0),     # A3
    (58, 80, 3.25),    # Bb3
]

for note, velocity, time in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 (F, A, C, E) on beat 2 (1.75s)
piano_notes = [
    (53, 90, 1.75),    # F3
    (60, 90, 1.75),    # A4
    (55, 90, 1.75),    # C4
    (58, 90, 1.75),    # E4
]

for note, velocity, time in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif with variation in rhythm

# Sax - F (F4), G (G4), Bb (Bb4), F (F4) - 8th notes, but with a rest on the last note
sax_notes = [
    (78, 100, 3.0),    # F4
    (81, 100, 3.25),   # G4
    (82, 100, 3.5),    # Bb4
    # (78, 100, 3.75),  # F4 (rested)
]

for note, velocity, time in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(n)

# Bass: walking line in F
# F (F3), G (G3), A (A3), Bb (Bb3), F (F3), G (G3), A (A3), Bb (Bb3)
bass_notes = [
    (53, 80, 3.0),     # F3
    (55, 80, 3.25),    # G3
    (57, 80, 3.5),     # A3
    (58, 80, 3.75),    # Bb3
    (53, 80, 4.0),     # F3
    (55, 80, 4.25),    # G3
    (57, 80, 4.5),     # A3
    (58, 80, 4.75),    # Bb3
]

for note, velocity, time in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# Bar 3: F7 (F, A, C, E) on beat 2 (3.25s)
piano_notes = [
    (53, 90, 3.25),    # F3
    (60, 90, 3.25),    # A4
    (55, 90, 3.25),    # C4
    (58, 90, 3.25),    # E4
]

for note, velocity, time in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: end of motif with a prolonged note

# Sax - F (F4) on beat 3 (4.5s) with a duration of 0.75s
sax_notes = [
    (78, 100, 4.5),    # F4
]

for note, velocity, time in sax_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.75)
    sax.notes.append(n)

# Bass: walking line in F
# F (F3), G (G3), A (A3), Bb (Bb3), F (F3), G (G3), A (A3), Bb (Bb3)
bass_notes = [
    (53, 80, 4.5),     # F3
    (55, 80, 4.75),    # G3
    (57, 80, 5.0),     # A3
    (58, 80, 5.25),    # Bb3
    (53, 80, 5.5),     # F3
    (55, 80, 5.75),    # G3
    (57, 80, 6.0),     # A3
    (58, 80, 6.25),    # Bb3
]

for note, velocity, time in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# Bar 4: F7 (F, A, C, E) on beat 2 (4.75s)
piano_notes = [
    (53, 90, 4.75),    # F3
    (60, 90, 4.75),    # A4
    (55, 90, 4.75),    # C4
    (58, 90, 4.75),    # E4
]

for note, velocity, time in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Drums: Bar 4
drum_notes = [
    (36, 1.0, 4.5),    # Kick on beat 1
    (42, 1.0, 4.625),  # Hi-hat on 1&
    (42, 1.0, 4.875),  # Hi-hat on &2
    (38, 1.0, 5.0),    # Snare on beat 2
    (42, 1.0, 5.125),  # Hi-hat on 2&
    (42, 1.0, 5.375),  # Hi-hat on &3
    (36, 1.0, 5.5),    # Kick on beat 3
    (42, 1.0, 5.625),  # Hi-hat on 3&
    (42, 1.0, 5.875),  # Hi-hat on &4
    (38, 1.0, 6.0),    # Snare on beat 4
]

for note, velocity, time in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
