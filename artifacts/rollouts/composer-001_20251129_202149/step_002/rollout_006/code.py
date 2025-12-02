
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # in seconds
beat = bar_length / 4  # 0.375 seconds per beat

# Drums - Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))  # Snare on 4

# Bass - Bar 2 (Marcus)
# Walking line in C, chromatic approaches
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
bass_beats = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for i in range(len(bass_notes)):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_beats[i], end=bass_beats[i] + 0.375))

# Piano - Bar 2 (Diane)
# 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (64, 67, 71, 72), # C7 on beat 2 (1.875)
    (64, 67, 71, 72), # C7 on beat 4 (3.375)
]
piano_beats = [1.875, 3.375]
for i in range(len(piano_notes)):
    for note in piano_notes[i]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=piano_beats[i], end=piano_beats[i] + 0.375))

# Drums - Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))  # Snare on 4

# Sax - Bar 2 (Dante)
# Motif: C (60) -> E (64) -> B (67) -> G (67) -> G (67) -> F (65)
sax_notes = [60, 64, 67, 67, 67, 65]
sax_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375]
for i in range(len(sax_notes)):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.125))

# Drums - Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))  # Snare on 4

# Piano - Bar 3
# 7th chords on 2 and 4
piano_notes = [
    # Bar 3
    (64, 67, 71, 72), # C7 on beat 2 (3.375)
    (64, 67, 71, 72), # C7 on beat 4 (4.875)
]
piano_beats = [3.375, 4.875]
for i in range(len(piano_notes)):
    for note in piano_notes[i]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=piano_beats[i], end=piano_beats[i] + 0.375))

# Bass - Bar 3
# Walking line in C
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
bass_beats = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125]
for i in range(len(bass_notes)):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_beats[i], end=bass_beats[i] + 0.375))

# Drums - Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4

# Sax - Bar 4
# Motif: C (60) -> E (64) -> B (67) -> G (67) -> G (67) -> F (65)
sax_notes = [60, 64, 67, 67, 67, 65]
sax_times = [4.5, 4.875, 5.25, 5.625, 6.0, 6.375]
for i in range(len(sax_notes)):
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=sax_notes[i], start=sax_times[i], end=sax_times[i] + 0.125))

# Piano - Bar 4
# 7th chords on 2 and 4
piano_notes = [
    # Bar 4
    (64, 67, 71, 72), # C7 on beat 2 (4.875)
    (64, 67, 71, 72), # C7 on beat 4 (6.375)
]
piano_beats = [4.875, 6.375]
for i in range(len(piano_notes)):
    for note in piano_notes[i]:
        piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=piano_beats[i], end=piano_beats[i] + 0.375))

# Bass - Bar 4
# Walking line in C
bass_notes = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
bass_beats = [4.5, 4.875, 5.25, 5.625, 6.0, 6.375, 6.75, 7.125, 7.5, 7.875, 8.25, 8.625]
for i in range(len(bass_notes)):
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=bass_notes[i], start=bass_beats[i], end=bass_beats[i] + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
