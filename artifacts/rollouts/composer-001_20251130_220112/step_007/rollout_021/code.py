
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
# Sax motif: F (75) - G# (77) - A (79) - Bb (76)
sax_notes = [
    (75, 1.5), (77, 1.75), (79, 2.0), (76, 2.25)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass line: F (75) - G (76) - Ab (77) - A (79) - Bb (76) - C (80) - Db (78) - D (81)
bass_notes = [
    (75, 1.5), (76, 1.75), (77, 2.0), (79, 2.25),
    (76, 2.5), (80, 2.75), (78, 3.0), (81, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2 (1.75), Bb7 on beat 4 (2.5)
piano_notes = [
    # F7 (F, A, C, Eb)
    (75, 1.75), (79, 1.75), (82, 1.75), (77, 1.75),
    # Bb7 (Bb, D, F, Ab)
    (76, 2.5), (80, 2.5), (75, 2.5), (77, 2.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif: Repeat the original motif starting at 3.0
sax_notes = [
    (75, 3.0), (77, 3.25), (79, 3.5), (76, 3.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass line: F (75) - G (76) - Ab (77) - A (79) - Bb (76) - C (80) - Db (78) - D (81)
bass_notes = [
    (75, 3.0), (76, 3.25), (77, 3.5), (79, 3.75),
    (76, 4.0), (80, 4.25), (78, 4.5), (81, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 3: F7 on beat 2 (3.25), Bb7 on beat 4 (4.0)
piano_notes = [
    # F7 (F, A, C, Eb)
    (75, 3.25), (79, 3.25), (82, 3.25), (77, 3.25),
    # Bb7 (Bb, D, F, Ab)
    (76, 4.0), (80, 4.0), (75, 4.0), (77, 4.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: F (75) - G# (77) - A (79) - Bb (76) - F (75) to close the phrase
sax_notes = [
    (75, 4.5), (77, 4.75), (79, 5.0), (76, 5.25), (75, 5.5)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bass line: F (75) - G (76) - Ab (77) - A (79) - Bb (76) - C (80) - Db (78) - D (81)
bass_notes = [
    (75, 4.5), (76, 4.75), (77, 5.0), (79, 5.25),
    (76, 5.5), (80, 5.75), (78, 6.0), (81, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
# Bar 4: F7 on beat 2 (4.75), Bb7 on beat 4 (5.5)
piano_notes = [
    # F7 (F, A, C, Eb)
    (75, 4.75), (79, 4.75), (82, 4.75), (77, 4.75),
    # Bb7 (Bb, D, F, Ab)
    (76, 5.5), (80, 5.5), (75, 5.5), (77, 5.5)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
