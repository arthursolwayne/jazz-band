
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2: Everybody in
# Sax melody: F7 -> A7 -> Bb7 -> C7 -> F7 (with a slight chromatic approach on A)
for bar in range(1, 3):
    time = bar * 1.5
    # Sax
    note = pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.375)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=90, start=time + 0.375, end=time + 0.75)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=89, start=time + 0.75, end=time + 1.125)
    sax.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=92, start=time + 1.125, end=time + 1.5)
    sax.notes.append(note)
    
    # Bass: Walking line
    note = pretty_midi.Note(velocity=80, pitch=46, start=time, end=time + 0.375)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=48, start=time + 0.375, end=time + 0.75)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=47, start=time + 0.75, end=time + 1.125)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=50, start=time + 1.125, end=time + 1.5)
    bass.notes.append(note)
    
    # Piano: 7th chords, comp on 2 and 4
    if bar == 1:
        note = pretty_midi.Note(velocity=90, pitch=65, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=68, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=70, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=90, pitch=65, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=68, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=69, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)
        note = pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125)
        piano.notes.append(note)

    # Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 3: Sax continues, same pattern
time = 3 * 1.5
note = pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=90, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=89, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=92, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

# Bass: Walking line
note = pretty_midi.Note(velocity=80, pitch=46, start=time, end=time + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=48, start=time + 0.375, end=time + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=47, start=time + 0.75, end=time + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=50, start=time + 1.125, end=time + 1.5)
bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=65, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)

# Drums
for beat in range(4):
    time = 3 * 1.5 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 4: Sax ends the motif
time = 4 * 1.5
note = pretty_midi.Note(velocity=100, pitch=87, start=time, end=time + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=90, start=time + 0.375, end=time + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=89, start=time + 0.75, end=time + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=92, start=time + 1.125, end=time + 1.5)
sax.notes.append(note)

# Bass: Walking line
note = pretty_midi.Note(velocity=80, pitch=46, start=time, end=time + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=48, start=time + 0.375, end=time + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=47, start=time + 0.75, end=time + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=50, start=time + 1.125, end=time + 1.5)
bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=65, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=time + 0.75, end=time + 1.125)
piano.notes.append(note)

# Drums
for beat in range(4):
    time = 4 * 1.5 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
