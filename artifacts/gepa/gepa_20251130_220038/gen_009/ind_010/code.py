
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
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62),    # D4
    (1.875, 63),  # Eb4
    (2.25, 64),   # E4
    (2.625, 65),  # F4
    (3.0, 67),    # G4
    (3.375, 69),  # A4
    (3.75, 71),   # Bb4
    (4.125, 72),  # B4
    (4.5, 74),    # C5
    (4.875, 76),  # Db5
    (5.25, 77),   # D5
    (5.625, 79),  # Eb5
    (6.0, 62)     # D4
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2 (1.875)
    (1.875, 67), (1.875, 71), (1.875, 72), (1.875, 76),
    # Bar 3: D7 on beat 2 (3.375)
    (3.375, 67), (3.375, 71), (3.375, 72), (3.375, 76),
    # Bar 4: D7 on beat 2 (4.875)
    (4.875, 67), (4.875, 71), (4.875, 72), (4.875, 76),
    # Bar 4: D7 on beat 4 (5.625)
    (5.625, 67), (5.625, 71), (5.625, 72), (5.625, 76)
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Drums: continue pattern
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

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65),     # E4
    (1.625, 67),   # G4
    (1.75, 69),    # A4
    (2.0, 67),     # G4
    (2.25, 69),    # A4
    (2.5, 67),     # G4
    (2.625, 69),   # A4
    (2.75, 65),    # E4
    (3.0, 62),     # D4
    (3.25, 65),    # E4
    (3.5, 67),     # G4
    (3.625, 69),   # A4
    (3.75, 67),    # G4
    (4.0, 69),     # A4
    (4.25, 67),    # G4
    (4.5, 65),     # E4
    (4.75, 62),    # D4
    (5.0, 65),     # E4
    (5.25, 67),    # G4
    (5.5, 69),     # A4
    (5.625, 67),   # G4
    (5.75, 69),    # A4
    (6.0, 67)      # G4
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.125)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
