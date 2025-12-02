
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante - Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Marcus - Bass
piano = pretty_midi.Instrument(program=0)      # Diane - Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray - Drums

# Drum note numbers
kick = 36
snare = 38
hihat = 42

# Time signatures and durations
bar_length = 1.5  # 60 / 160 * 4 = 1.5 seconds per bar
beat_length = bar_length / 4  # 0.375s per beat

# -------------------
# Bar 1: Little Ray alone (0.0 - 1.5s)
# -------------------

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth note
for i in range(0, 8):
    start = i * beat_length
    end = start + beat_length / 2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=start, end=end))

# -------------------
# Bar 2: Full band in (1.5 - 3.0s)
# -------------------

# Bass line (Marcus): Walking line, chromatic approaches
# Fm7 (F, Ab, C, Eb)
# Walking bass line: F, Gb, G, Ab, A, Bb, B, C
bass_notes = [76, 75, 76, 77, 78, 77, 78, 79]
for i, pitch in enumerate(bass_notes):
    start = 1.5 + i * beat_length
    end = start + beat_length
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano (Diane): 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Comp on 2 and 4
# Fm7 on 2, Bbm7 on 4
piano_notes = [
    # Bar 2: Fm7 on 2
    (76, 1.5 + 0.75, 1.5 + 1.125),  # F
    (88, 1.5 + 0.75, 1.5 + 1.125),  # Ab
    (79, 1.5 + 0.75, 1.5 + 1.125),  # C
    (82, 1.5 + 0.75, 1.5 + 1.125),  # Eb

    # Bar 2: Bbm7 on 4
    (77, 1.5 + 1.125, 1.5 + 1.5),  # Bb
    (89, 1.5 + 1.125, 1.5 + 1.5),  # Db
    (80, 1.5 + 1.125, 1.5 + 1.5),  # D
    (83, 1.5 + 1.125, 1.5 + 1.5),  # F
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax (Dante): Motif - F, Ab, Eb, F (with a slight chromatic bend on the Eb)
sax_notes = [
    (76, 1.5, 1.5 + 0.375),  # F
    (88, 1.5 + 0.375, 1.5 + 0.75),  # Ab
    (82, 1.5 + 0.75, 1.5 + 1.125),  # Eb
    (76, 1.5 + 1.125, 1.5 + 1.5),  # F
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# -------------------
# Bar 3: Full band in (3.0 - 4.5s)
# -------------------

# Bass line: Fm7 -> Bbm7 -> Ebm7 -> Abm7
bass_notes = [76, 75, 76, 77, 78, 77, 78, 79]
for i, pitch in enumerate(bass_notes):
    start = 3.0 + i * beat_length
    end = start + beat_length
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Bbm7 on 2, Ebm7 on 4
piano_notes = [
    # Bar 3: Bbm7 on 2
    (77, 3.0 + 0.75, 3.0 + 1.125),  # Bb
    (89, 3.0 + 0.75, 3.0 + 1.125),  # Db
    (80, 3.0 + 0.75, 3.0 + 1.125),  # D
    (83, 3.0 + 0.75, 3.0 + 1.125),  # F

    # Bar 3: Ebm7 on 4
    (82, 3.0 + 1.125, 3.0 + 1.5),  # Eb
    (91, 3.0 + 1.125, 3.0 + 1.5),  # G
    (84, 3.0 + 1.125, 3.0 + 1.5),  # Ab
    (87, 3.0 + 1.125, 3.0 + 1.5),  # Bb
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Motif variation - F, Ab, Eb, F (with a slight chromatic bend on the Eb)
sax_notes = [
    (76, 3.0, 3.0 + 0.375),  # F
    (88, 3.0 + 0.375, 3.0 + 0.75),  # Ab
    (82, 3.0 + 0.75, 3.0 + 1.125),  # Eb
    (76, 3.0 + 1.125, 3.0 + 1.5),  # F
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# -------------------
# Bar 4: Full band in (4.5 - 6.0s)
# -------------------

# Bass line: Ebm7 -> Abm7 -> Dbm7 -> Gbm7
bass_notes = [82, 81, 82, 83, 84, 83, 84, 85]
for i, pitch in enumerate(bass_notes):
    start = 4.5 + i * beat_length
    end = start + beat_length
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Ebm7 on 2, Abm7 on 4
piano_notes = [
    # Bar 4: Ebm7 on 2
    (82, 4.5 + 0.75, 4.5 + 1.125),  # Eb
    (91, 4.5 + 0.75, 4.5 + 1.125),  # G
    (84, 4.5 + 0.75, 4.5 + 1.125),  # Ab
    (87, 4.5 + 0.75, 4.5 + 1.125),  # Bb

    # Bar 4: Abm7 on 4
    (83, 4.5 + 1.125, 4.5 + 1.5),  # Ab
    (92, 4.5 + 1.125, 4.5 + 1.5),  # C
    (86, 4.5 + 1.125, 4.5 + 1.5),  # B
    (89, 4.5 + 1.125, 4.5 + 1.5),  # Db
]

for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Motif variation - F, Ab, Eb, F (with a slight chromatic bend on the Eb)
sax_notes = [
    (76, 4.5, 4.5 + 0.375),  # F
    (88, 4.5 + 0.375, 4.5 + 0.75),  # Ab
    (82, 4.5 + 0.75, 4.5 + 1.125),  # Eb
    (76, 4.5 + 1.125, 4.5 + 1.5),  # F
]

for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# -------------------
# Finalize
# -------------------

midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_russo_intro.mid")
