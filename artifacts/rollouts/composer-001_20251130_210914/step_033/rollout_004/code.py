
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Drums in Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 1, 2, 3]:
    time = beat * 0.375
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (1.5, 48),  # F
    (1.75, 49), # F#
    (2.0, 50),  # G
    (2.25, 51), # G#
    (2.5, 53),  # A#
    (2.75, 52), # A
    (3.0, 51),  # G#
    (3.25, 50), # G
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 on beat 2
piano_notes = [
    (2.0, 53), # F
    (2.0, 57), # Bb
    (2.0, 60), # E
    (2.0, 62), # G
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Melody - Start with a motif
# F (60), A (65), Bb (62), F (60)
sax_notes = [
    (1.5, 60), # F
    (1.75, 65), # A
    (2.0, 62), # Bb
    (2.25, 60), # F
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (3.0, 53),  # A#
    (3.25, 52), # A
    (3.5, 51),  # G#
    (3.75, 50), # G
    (4.0, 49),  # F#
    (4.25, 48), # F
    (4.5, 49),  # F#
    (4.75, 50), # G
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3: Bb7 on beat 2
piano_notes = [
    (3.5, 57), # Bb
    (3.5, 62), # D
    (3.5, 64), # F
    (3.5, 67), # A
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Melody - Continue with a variation
# F (60), D (62), E (64), F (60)
sax_notes = [
    (3.0, 60), # F
    (3.25, 62), # D
    (3.5, 64), # E
    (3.75, 60), # F
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (4.5, 50),  # G
    (4.75, 51), # G#
    (5.0, 53),  # A#
    (5.25, 52), # A
    (5.5, 51),  # G#
    (5.75, 50), # G
    (6.0, 51),  # G#
    (6.25, 50), # G
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4: F7 on beat 2
piano_notes = [
    (4.5, 53), # F
    (4.5, 57), # Bb
    (4.5, 60), # E
    (4.5, 62), # G
]

for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Melody - Finish the motif
# F (60), A (65), Bb (62), F (60)
sax_notes = [
    (4.5, 60), # F
    (4.75, 65), # A
    (5.0, 62), # Bb
    (5.25, 60), # F
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums in Bar 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    for beat in [0, 1, 2, 3]:
        time = (bar - 1) * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
