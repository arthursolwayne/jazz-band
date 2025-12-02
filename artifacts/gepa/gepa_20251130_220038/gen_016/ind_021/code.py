
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum samples (MIDI note numbers)
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
for beat in range(4):
    time = beat * 0.375
    # Kick on beats 0 and 2 (1 and 3 in bar)
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Snare on beats 1 and 3 (2 and 4 in bar)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hi-hat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

## Drums
for beat in range(4):
    time = 1.5 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

## Bass: Walking line in F (F, G#, A, Bb) - chromatic approach to A
bass_notes = [78, 81, 82, 80]  # F, G#, A, Bb
for i, note in enumerate(bass_notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

## Piano: 7th chords on 2 and 4 (comping)
# F7 (F, A, C, E)
# Bb7 (Bb, D, F, Ab)
chord_f7 = [78, 82, 72, 76]
chord_bb7 = [76, 79, 78, 74]

# Bar 2, beat 1: rest
# Bar 2, beat 2: F7
for note in chord_f7:
    time = 1.5 + 1.0  # beat 2
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Bar 2, beat 4: Bb7
for note in chord_bb7:
    time = 1.5 + 3.0  # beat 4
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

## Sax: Melody - short motif
# F (78), G# (81), A (82), D (76) -> F, G#, A, D
# Start on beat 2 (1.5 + 1.0)
sax_notes = [81, 82, 76, 78]  # G#, A, D, F
for i, note in enumerate(sax_notes):
    time = 1.5 + 1.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

## Drums
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

## Bass: Walking line in F (F, G#, A, Bb)
bass_notes = [78, 81, 82, 80]
for i, note in enumerate(bass_notes):
    time = 3.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

## Piano: 7th chords on 2 and 4
# Bar 3, beat 2: F7
for note in chord_f7:
    time = 3.0 + 1.0  # beat 2
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Bar 3, beat 4: Bb7
for note in chord_bb7:
    time = 3.0 + 3.0  # beat 4
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

## Sax: Melody - repeat the motif with variation
# F (78), G# (81), A (82), C (72) -> F, G#, A, C
# Start on beat 2 (3.0 + 1.0)
sax_notes = [81, 82, 72, 78]  # G#, A, C, F
for i, note in enumerate(sax_notes):
    time = 3.0 + 1.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

## Drums
for beat in range(4):
    time = 4.5 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=SNARE, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=HIHAT, start=time, end=time + 0.125)
    drums.notes.append(note)

## Bass: Walking line in F (F, G#, A, Bb)
bass_notes = [78, 81, 82, 80]
for i, note in enumerate(bass_notes):
    time = 4.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note_obj)

## Piano: 7th chords on 2 and 4
# Bar 4, beat 2: F7
for note in chord_f7:
    time = 4.5 + 1.0  # beat 2
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

# Bar 4, beat 4: Bb7
for note in chord_bb7:
    time = 4.5 + 3.0  # beat 4
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note_obj)

## Sax: Melody - resolution
# F (78), G# (81), A (82), F (78)
# Start on beat 2 (4.5 + 1.0)
sax_notes = [81, 82, 78, 78]  # G#, A, F, F
for i, note in enumerate(sax_notes):
    time = 4.5 + 1.0 + i * 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25)
    sax.notes.append(note_obj)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
