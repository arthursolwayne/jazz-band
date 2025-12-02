
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in C
# C Eb F G (chromatic approach to F)
bass_notes = [
    (60, 1.5), (61, 1.75), (62, 2.0), (63, 2.25),
    (64, 2.5), (65, 2.75), (66, 3.0), (67, 3.25)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
# C7 on beat 2, F7 on beat 4
piano_notes = [
    # C7 (C E G Bb) on beat 2 (2.0s)
    (60, 2.0), (64, 2.0), (67, 2.0), (70, 2.0),
    # F7 (F A C Eb) on beat 4 (3.0s)
    (65, 3.0), (69, 3.0), (72, 3.0), (74, 3.0)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Dante: saxophone motif - C Eb F G (start on beat 1)
sax_notes = [
    (60, 1.5), (62, 1.75), (64, 2.0), (65, 2.25)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: walking bass line in C
# C Eb F G (chromatic approach to F)
bass_notes = [
    (60, 3.0), (61, 3.25), (62, 3.5), (63, 3.75),
    (64, 4.0), (65, 4.25), (66, 4.5), (67, 4.75)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
# C7 on beat 2 (3.5s), F7 on beat 4 (4.5s)
piano_notes = [
    # C7 (C E G Bb) on beat 2 (3.5s)
    (60, 3.5), (64, 3.5), (67, 3.5), (70, 3.5),
    # F7 (F A C Eb) on beat 4 (4.5s)
    (65, 4.5), (69, 4.5), (72, 4.5), (74, 4.5)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Dante: Saxophone motif - repeat and resolve
# C Eb F G -> F G C (resolution)
sax_notes = [
    (60, 3.0), (62, 3.25), (64, 3.5), (65, 3.75),
    (64, 4.0), (65, 4.25), (60, 4.5)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: walking bass line in C
# C Eb F G (chromatic approach to F)
bass_notes = [
    (60, 4.5), (61, 4.75), (62, 5.0), (63, 5.25),
    (64, 5.5), (65, 5.75), (66, 6.0), (67, 6.25)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4
# C7 on beat 2 (5.0s), F7 on beat 4 (6.0s)
piano_notes = [
    # C7 (C E G Bb) on beat 2 (5.0s)
    (60, 5.0), (64, 5.0), (67, 5.0), (70, 5.0),
    # F7 (F A C Eb) on beat 4 (6.0s)
    (65, 6.0), (69, 6.0), (72, 6.0), (74, 6.0)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Dante: Saxophone motif - resolution and leave it hanging
# F G C (resolution) -> leave it on C
sax_notes = [
    (64, 4.5), (65, 4.75), (60, 5.0),
    (60, 5.25)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
