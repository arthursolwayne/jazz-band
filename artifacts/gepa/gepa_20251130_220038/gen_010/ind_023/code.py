
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * 0.375
    if beat % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat % 2 == 1:
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 59),  # Fm root (F)
    (1.875, 60),  # b9 (Gb)
    (2.25, 58),  # 7 (E)
    (2.625, 62),  # 11 (A)
    # Bar 3 (3.0 - 4.5s)
    (3.0, 60),  # Gb
    (3.375, 58),  # E
    (3.75, 62),  # A
    (4.125, 63),  # Bb
    # Bar 4 (4.5 - 6.0s)
    (4.5, 63),  # Bb
    (4.875, 61),  # Ab
    (5.25, 60),  # Gb
    (5.625, 59)   # F
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (1.5, 64),  # F7 (F, A, C, Eb)
    (1.5, 69),  # A
    (1.5, 60),  # C
    (1.5, 62),  # Eb
    (1.875, 64),  # F
    (1.875, 69),  # A
    (1.875, 60),  # C
    (1.875, 62),  # Eb
    # Bar 3 (3.0 - 4.5s)
    (3.0, 64),  # F7
    (3.0, 69),  # A
    (3.0, 60),  # C
    (3.0, 62),  # Eb
    (3.375, 64),  # F
    (3.375, 69),  # A
    (3.375, 60),  # C
    (3.375, 62),  # Eb
    # Bar 4 (4.5 - 6.0s)
    (4.5, 64),  # F7
    (4.5, 69),  # A
    (4.5, 60),  # C
    (4.5, 62),  # Eb
    (4.875, 64),  # F
    (4.875, 69),  # A
    (4.875, 60),  # C
    (4.875, 62)   # Eb
]
for time, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C, Db
# Motif: F (1.5), Ab (1.875), B (2.25), F (2.625)
# Then leave it hanging on F (3.0), come back with Ab (3.375), B (3.75), F (4.125)
# Then resolve with a descending line: Eb (4.5), D (4.875), C (5.25), Bb (5.625)

sax_notes = [
    (1.5, 59),   # F
    (1.875, 62), # Ab
    (2.25, 64),  # B
    (2.625, 59), # F
    (3.0, 59),   # F (hanging)
    (3.375, 62), # Ab
    (3.75, 64),  # B
    (4.125, 59), # F
    (4.5, 62),   # Eb
    (4.875, 61), # D
    (5.25, 60),  # C
    (5.625, 62)  # Bb
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(8):
    time = 1.5 + beat * 0.375
    if beat % 2 == 0:
        # Kick on 1 and 3 (relative to bar 2)
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat % 2 == 1:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
