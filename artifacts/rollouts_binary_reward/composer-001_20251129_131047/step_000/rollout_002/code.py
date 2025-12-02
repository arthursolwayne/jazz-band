
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
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Sax - motif: C4 (60), E4 (64), Bb4 (62), D5 (67)
# Start at bar 2 (1.5s)
# First note: C4 on beat 0 of bar 2 (1.5s)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875)
sax.notes.append(note)
# Second note: E4 on beat 2 of bar 2 (2.25s)
note = pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625)
sax.notes.append(note)
# Third note: Bb4 on beat 3 of bar 3 (3.75s)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125)
sax.notes.append(note)
# Fourth note: D5 on beat 0 of bar 4 (4.5s)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875)
sax.notes.append(note)

# Bass - walking line in C, chromatic approaches
# Bar 2: C3 (48), D#3 (50), E3 (52), F3 (53)
note = pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)
bass.notes.append(note)

# Bar 3: G3 (47), A3 (49), Bb3 (50), B3 (51)
note = pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5)
bass.notes.append(note)

# Bar 4: C3 (48), D#3 (50), E3 (52), F3 (53)
note = pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0)
bass.notes.append(note)

# Piano - comp on 2 and 4, 7th chords
# Bar 2: C7 (C4, E4, Bb4, D5)
note = pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25)
piano.notes.append(note)

# Bar 3: C7 again
note = pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75)
piano.notes.append(note)

# Bar 4: C7 again
note = pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25)
piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=80, pitch=42, start=(bar * 1.5) + (beat * 0.375), end=(bar * 1.5) + (beat + 1) * 0.375)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
