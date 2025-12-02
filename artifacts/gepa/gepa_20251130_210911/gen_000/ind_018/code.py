
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
for beat in [0, 2]:  # Beats 1 and 3
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:  # Beats 2 and 4
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):  # Every eighth note
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.1875, end=(beat + 1) * 0.1875)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    (2, 0.0, 0.375),  # D (2)
    (3, 0.375, 0.75), # Eb (3)
    (4, 0.75, 1.125), # E (4)
    (5, 1.125, 1.5),  # F (5)
    (7, 1.5, 1.875),  # G (7)
    (9, 1.875, 2.25), # A (9)
    (10, 2.25, 2.625),# Bb (10)
    (11, 2.625, 3.0), # B (11)
    (12, 3.0, 3.375), # C (12)
    (13, 3.375, 3.75),# C# (13)
    (14, 3.75, 4.125),# D (14)
    (15, 4.125, 4.5), # D# (15)
    (16, 4.5, 4.875), # E (16)
    (17, 4.875, 5.25),# F (17)
    (19, 5.25, 5.625),# G (19)
    (21, 5.625, 6.0)  # A (21)
]
for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start + 1.5, end=end + 1.5)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (2, 4, 6, 9)
    (2, 1.5, 1.75), (4, 1.5, 1.75), (6, 1.5, 1.75), (9, 1.5, 1.75),
    # Bar 3: G7 (7, 9, 11, 13)
    (7, 3.0, 3.25), (9, 3.0, 3.25), (11, 3.0, 3.25), (13, 3.0, 3.25),
    # Bar 4: C7 (0, 2, 4, 7)
    (0, 4.5, 4.75), (2, 4.5, 4.75), (4, 4.5, 4.75), (7, 4.5, 4.75)
]
for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Sax: Motif - short, singable, leaves it hanging
sax_notes = [
    (2, 1.5, 1.75),   # D
    (4, 1.75, 2.0),   # E
    (6, 2.0, 2.25),   # F
    (7, 2.25, 2.5),   # G
    (9, 2.5, 2.75),   # A
    (11, 2.75, 3.0),  # B
    (12, 3.0, 3.25),  # C
    (14, 3.25, 3.5),  # D
    (16, 3.5, 3.75),  # E
    (17, 3.75, 4.0),  # F
    (19, 4.0, 4.25),  # G
    (21, 4.25, 4.5),  # A
    (22, 4.5, 4.75),  # Bb
    (24, 4.75, 5.0),  # B
    (26, 5.0, 5.25),  # C
    (28, 5.25, 5.5),  # D
    (30, 5.5, 5.75),  # E
    (32, 5.75, 6.0)   # F
]
for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums continue for bars 2-4
for beat in [0, 2, 4, 6]:  # Beats 1 and 3 of each bar
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375 + 1.5, end=(beat + 1) * 0.375 + 1.5)
    drums.notes.append(note)
for beat in [1, 3, 5, 7]:  # Beats 2 and 4 of each bar
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375 + 1.5, end=(beat + 1) * 0.375 + 1.5)
    drums.notes.append(note)
for beat in range(8):  # Every eighth note for bars 2-4
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.1875 + 1.5, end=(beat + 1) * 0.1875 + 1.5)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
