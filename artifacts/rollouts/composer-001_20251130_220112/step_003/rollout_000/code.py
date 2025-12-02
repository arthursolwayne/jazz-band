
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
    (36, 1.5), (38, 1.875), (42, 1.875),
    (36, 2.25), (38, 2.625), (42, 2.625)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Fm (F, Eb, D, C#, F)
bass_notes = [
    (53, 1.5), (51, 1.875), (50, 2.25), (49, 2.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 on beat 2 (1.875s)
    (53, 1.875), (50, 1.875), (48, 1.875), (55, 1.875),
    # Bb7 on beat 4 (2.625s)
    (51, 2.625), (48, 2.625), (46, 2.625), (53, 2.625)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Dante: Motif in Fm (F, Ab, G, Eb) on beat 1
sax_notes = [
    (53, 1.5), (50, 1.875), (51, 2.25), (48, 2.625)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line (F, Eb, D, C#, F)
bass_notes = [
    (53, 3.0), (51, 3.375), (50, 3.75), (49, 4.125)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (53, 3.375), (50, 3.375), (48, 3.375), (55, 3.375),
    (51, 4.125), (48, 4.125), (46, 4.125), (53, 4.125)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0), (38, 3.375), (42, 3.375),
    (36, 3.75), (38, 4.125), (42, 4.125),
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Dante: Motif variation (F, Ab, G, Eb) on beat 1
sax_notes = [
    (53, 3.0), (50, 3.375), (51, 3.75), (48, 4.125)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line (F, Eb, D, C#, F)
bass_notes = [
    (53, 4.5), (51, 4.875), (50, 5.25), (49, 5.625)
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(note_obj)

# Diane: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    (53, 4.875), (50, 4.875), (48, 4.875), (55, 4.875),
    (51, 5.625), (48, 5.625), (46, 5.625), (53, 5.625)
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(note_obj)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
    (36, 6.75), (38, 7.125), (42, 7.125)
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note_obj)

# Dante: Finish the motif (F, Ab, G, Eb) on beat 1, with a lift
sax_notes = [
    (53, 4.5), (50, 4.875), (51, 5.25), (48, 5.625)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
