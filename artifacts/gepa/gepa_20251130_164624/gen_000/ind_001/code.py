
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
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=90, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (2, 1.5, 1.5 + 0.375),  # D
    (4, 1.5 + 0.375, 1.5 + 0.75),  # F
    (6, 1.5 + 0.75, 1.5 + 1.125),  # Ab
    (5, 1.5 + 1.125, 1.5 + 1.5),  # G
    (2, 1.5 + 1.5, 1.5 + 1.875),  # D
    (4, 1.5 + 1.875, 1.5 + 2.25),  # F
    (6, 1.5 + 2.25, 1.5 + 2.625),  # Ab
    (5, 1.5 + 2.625, 1.5 + 3.0),  # G
    (2, 1.5 + 3.0, 1.5 + 3.375),  # D
    (4, 1.5 + 3.375, 1.5 + 3.75),  # F
    (6, 1.5 + 3.75, 1.5 + 4.125),  # Ab
    (5, 1.5 + 4.125, 1.5 + 4.5),  # G
    (2, 1.5 + 4.5, 1.5 + 4.875),  # D
    (4, 1.5 + 4.875, 1.5 + 5.25),  # F
    (6, 1.5 + 5.25, 1.5 + 5.625),  # Ab
    (5, 1.5 + 5.625, 1.5 + 6.0),  # G
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 1 and 3
    (2, 1.5, 1.5 + 0.375),  # D
    (4, 1.5, 1.5 + 0.375),  # F
    (6, 1.5, 1.5 + 0.375),  # Ab
    (7, 1.5, 1.5 + 0.375),  # C
    (2, 1.5 + 1.125, 1.5 + 1.5),  # D
    (4, 1.5 + 1.125, 1.5 + 1.5),  # F
    (6, 1.5 + 1.125, 1.5 + 1.5),  # Ab
    (7, 1.5 + 1.125, 1.5 + 1.5),  # C
    # Bar 3: Dm7 on 2 and 4
    (2, 1.5 + 1.5, 1.5 + 1.875),  # D
    (4, 1.5 + 1.5, 1.5 + 1.875),  # F
    (6, 1.5 + 1.5, 1.5 + 1.875),  # Ab
    (7, 1.5 + 1.5, 1.5 + 1.875),  # C
    (2, 1.5 + 2.25, 1.5 + 2.625),  # D
    (4, 1.5 + 2.25, 1.5 + 2.625),  # F
    (6, 1.5 + 2.25, 1.5 + 2.625),  # Ab
    (7, 1.5 + 2.25, 1.5 + 2.625),  # C
    # Bar 4: Dm7 on 2 and 4
    (2, 1.5 + 3.0, 1.5 + 3.375),  # D
    (4, 1.5 + 3.0, 1.5 + 3.375),  # F
    (6, 1.5 + 3.0, 1.5 + 3.375),  # Ab
    (7, 1.5 + 3.0, 1.5 + 3.375),  # C
    (2, 1.5 + 3.75, 1.5 + 4.125),  # D
    (4, 1.5 + 3.75, 1.5 + 4.125),  # F
    (6, 1.5 + 3.75, 1.5 + 4.125),  # Ab
    (7, 1.5 + 3.75, 1.5 + 4.125),  # C
]
for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Drums: continued
for bar in range(2, 4):
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.1)
        drums.notes.append(note)
    for beat in range(4):
        note = pretty_midi.Note(velocity=90, pitch=42, start=bar*1.5 + beat*0.375, end=bar*1.5 + beat*0.375 + 0.05)
        drums.notes.append(note)

# Sax: short motif, make it sing
# Bar 2: Start the motif
sax_notes = [
    (2, 1.5, 1.5 + 0.375),  # D
    (4, 1.5 + 0.375, 1.5 + 0.75),  # F
    (6, 1.5 + 0.75, 1.5 + 1.125),  # Ab
    (2, 1.5 + 1.5, 1.5 + 1.875),  # D
    (4, 1.5 + 1.875, 1.5 + 2.25),  # F
    (6, 1.5 + 2.25, 1.5 + 2.625),  # Ab
    (2, 1.5 + 3.0, 1.5 + 3.375),  # D
    (4, 1.5 + 3.375, 1.5 + 3.75),  # F
    (6, 1.5 + 3.75, 1.5 + 4.125),  # Ab
    (7, 1.5 + 4.125, 1.5 + 4.5),  # C
    (6, 1.5 + 4.5, 1.5 + 4.875),  # Ab
    (4, 1.5 + 4.875, 1.5 + 5.25),  # F
    (2, 1.5 + 5.25, 1.5 + 5.625),  # D
    (7, 1.5 + 5.625, 1.5 + 6.0),  # C
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
