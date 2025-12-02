
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
# Bass: Walking line, chromatic approaches
bass_notes = [
    (30, 1.5), (31, 1.875), (29, 2.25), (30, 2.625),  # Fm7
    (31, 3.0), (32, 3.375), (30, 3.75), (31, 4.125)   # Bb7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (36, 1.875), (39, 1.875), (43, 1.875), (46, 1.875),  # F7 on 2
    (45, 3.375), (48, 3.375), (50, 3.375), (53, 3.375)   # Bb7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif (start on 1.5s)
sax_notes = [
    (64, 1.5), (67, 1.75), (65, 2.0), (62, 2.25),  # Fm motif
    (64, 2.5), (67, 2.75), (65, 3.0), (62, 3.25)   # Repeat
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (32, 3.0), (33, 3.375), (31, 3.75), (32, 4.125),  # Bb7
    (33, 4.5), (34, 4.875), (32, 5.25), (33, 5.625)   # Eb7
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (45, 3.375), (48, 3.375), (50, 3.375), (53, 3.375),  # Bb7 on 2
    (52, 4.875), (55, 4.875), (57, 4.875), (60, 4.875)   # Eb7 on 4
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif (repeat)
sax_notes = [
    (64, 3.0), (67, 3.25), (65, 3.5), (62, 3.75),  # Fm motif
    (64, 4.0), (67, 4.25), (65, 4.5), (62, 4.75)   # Repeat
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (34, 4.5), (35, 4.875), (33, 5.25), (34, 5.625),  # Eb7
    (35, 6.0), (36, 6.375), (34, 6.75), (35, 7.125)   # Ab7 (end at 6.0)
]
for note, time in bass_notes:
    if time <= 6.0:
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (52, 4.875), (55, 4.875), (57, 4.875), (60, 4.875),  # Eb7 on 2
    (59, 6.375), (62, 6.375), (64, 6.375), (67, 6.375)   # Ab7 on 4 (end at 6.0)
]
for note, time in piano_notes:
    if time <= 6.0:
        piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif (repeat)
sax_notes = [
    (64, 4.5), (67, 4.75), (65, 5.0), (62, 5.25),  # Fm motif
    (64, 5.5), (67, 5.75), (65, 6.0), (62, 6.25)   # End on 6.0
]
for note, time in sax_notes:
    if time <= 6.0:
        sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    for i in range(4):
        time = start_time + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
