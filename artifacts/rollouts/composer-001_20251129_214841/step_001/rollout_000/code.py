
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in C, chromatic approach to C7
bass_notes = [
    (1.5, 60),  # C
    (1.875, 61), # C#
    (2.25, 62),  # D
    (2.625, 60), # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 60),  # C
    (1.875, 64),  # E
    (1.875, 67),  # G
    (1.875, 71),  # B
    (2.625, 60),  # C
    (2.625, 64),  # E
    (2.625, 67),  # G
    (2.625, 71),  # B
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Motif - short, singing, leaves it hanging
sax_notes = [
    (1.5, 65),  # E
    (1.625, 67), # G
    (1.75, 69),  # A
    (1.875, 67), # G
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in C, chromatic approach to C7
bass_notes = [
    (3.0, 60),  # C
    (3.375, 61), # C#
    (3.75, 62),  # D
    (4.125, 60), # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (3.375, 60),  # C
    (3.375, 64),  # E
    (3.375, 67),  # G
    (3.375, 71),  # B
    (4.125, 60),  # C
    (4.125, 64),  # E
    (4.125, 67),  # G
    (4.125, 71),  # B
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Motif continued, resolves the tension
sax_notes = [
    (3.0, 65),  # E
    (3.125, 67), # G
    (3.25, 69),  # A
    (3.375, 71), # B
    (3.5, 69),  # A
    (3.625, 67), # G
    (3.75, 65),  # E
    (3.875, 60), # C
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in C, chromatic approach to C7
bass_notes = [
    (4.5, 60),  # C
    (4.875, 61), # C#
    (5.25, 62),  # D
    (5.625, 60), # C
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (4.875, 60),  # C
    (4.875, 64),  # E
    (4.875, 67),  # G
    (4.875, 71),  # B
    (5.625, 60),  # C
    (5.625, 64),  # E
    (5.625, 67),  # G
    (5.625, 71),  # B
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
    piano.notes.append(note)

# Dante: Motif resolution, leaves a hook
sax_notes = [
    (4.5, 65),  # E
    (4.625, 67), # G
    (4.75, 69),  # A
    (4.875, 67), # G
    (5.0, 65),  # E
    (5.125, 67), # G
    (5.25, 69),  # A
    (5.375, 67), # G
    (5.5, 65),  # E
    (5.625, 60), # C
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 4.5 + beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.125)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=hihat, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
