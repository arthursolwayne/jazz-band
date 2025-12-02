
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
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (1.5, 50, 100),  # D
    (1.875, 49, 100), # C#
    (2.25, 52, 100),  # E
    (2.625, 51, 100), # D#
    (3.0, 53, 100),   # F
    (3.375, 52, 100), # E
    (3.75, 50, 100),  # D
    (4.125, 49, 100), # C#
    (4.5, 53, 100),   # F
    (4.875, 52, 100), # E
    (5.25, 50, 100),  # D
    (5.625, 49, 100), # C#
]
for time, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (Dm7, G7, Cm7, F7)
piano_notes = [
    # Bar 2
    (1.875, 62, 100),  # D
    (1.875, 67, 100),  # G
    (1.875, 71, 100),  # Bb
    (1.875, 74, 100),  # D
    # Bar 3
    (3.375, 62, 100),  # D
    (3.375, 67, 100),  # G
    (3.375, 71, 100),  # Bb
    (3.375, 74, 100),  # D
    # Bar 4
    (4.875, 60, 100),  # C
    (4.875, 65, 100),  # F
    (4.875, 69, 100),  # A
    (4.875, 72, 100),  # C
]
for time, pitch, vel in piano_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + 0.125)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat % 2 == 0:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        else:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: Tenor sax, short motif, make it sing
# Melody: D (62), F (65), Bb (67), D (62) - then leave it hanging
sax_notes = [
    (1.5, 62, 110, 0.25),  # D
    (1.75, 65, 110, 0.25), # F
    (2.0, 67, 110, 0.25),  # Bb
    (2.25, 62, 110, 0.25), # D
    (2.5, 67, 110, 0.25),  # Bb (rest)
    (2.75, 65, 110, 0.25), # F (rest)
    (3.0, 62, 110, 0.25),  # D (rest)
    (3.25, 62, 110, 0.25), # D (rest)
    (3.5, 65, 110, 0.25),  # F
    (3.75, 67, 110, 0.25), # Bb
    (4.0, 62, 110, 0.25),  # D
    (4.25, 62, 110, 0.25), # D (rest)
    (4.5, 65, 110, 0.25),  # F (rest)
    (4.75, 67, 110, 0.25), # Bb (rest)
    (5.0, 62, 110, 0.25),  # D (rest)
    (5.25, 62, 110, 0.25), # D (rest)
    (5.5, 65, 110, 0.25),  # F
    (5.75, 67, 110, 0.25), # Bb
    (6.0, 62, 110, 0.25),  # D
]
for time, pitch, vel, duration in sax_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
