
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (1.5, 60),   # C3
    (1.875, 61), # C#3
    (2.25, 62),  # D3
    (2.625, 63), # D#3
    (3.0, 64),   # E3
    (3.375, 65), # F3
    (3.75, 66),  # F#3
    (4.125, 67), # G3
    (4.5, 68),   # G#3
    (4.875, 69), # A3
    (5.25, 70),  # A#3
    (5.625, 71), # B3
    (6.0, 72)    # C4
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 (C E G B)
note = pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
piano.notes.append(note)

# Bar 3: F7 (F A C E)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25)
piano.notes.append(note)

# Bar 4: G7 (G B D F)
note = pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.75)
piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
# Motif: C (60) -> D (62) -> C# (61) -> B (69)
# First note at 1.5s, second at 1.875s, third at 2.25s, fourth at 2.625s
note = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875)
sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
