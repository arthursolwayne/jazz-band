
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # kick on 1
    (38, 0.75, 0.375), # snare on 2
    (42, 0.0, 0.125),  # hihat on 1
    (42, 0.125, 0.125),# hihat on 2
    (42, 0.25, 0.125), # hihat on 3
    (42, 0.375, 0.125),# hihat on 4
    (36, 1.125, 0.375),# kick on 3
    (38, 1.5, 0.375),  # snare on 4
    (42, 1.125, 0.125),# hihat on 3
    (42, 1.25, 0.125), # hihat on 4
    (42, 1.375, 0.125),# hihat on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Piano: C7 - E7 - G7 - Ab7
piano_notes = [
    (72, 1.5, 0.375), # C7
    (74, 2.25, 0.375), # E7
    (76, 3.0, 0.375),  # G7
    (78, 3.75, 0.375), # Ab7
]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(piano_note)

# Bass: F2 - G2 - C2 - Bb2 (with chromatic approaches)
bass_notes = [
    (38, 1.5, 0.375),  # F2
    (40, 1.875, 0.375), # G2
    (35, 2.25, 0.375),  # C2
    (41, 2.625, 0.375), # Bb2
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bass_note)

# Sax: F - Bb - D - Eb
sax_notes = [
    (84, 1.5, 0.375),  # F
    (78, 2.25, 0.375), # Bb
    (82, 3.0, 0.375),  # D
    (80, 3.75, 0.375), # Eb
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Piano: Ab7 - G7 - F7 - E7
piano_notes = [
    (78, 3.0, 0.375),  # Ab7
    (76, 3.75, 0.375), # G7
    (72, 4.5, 0.375),  # F7
    (74, 5.25, 0.375), # E7
]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(piano_note)

# Bass: Bb2 - A2 - G2 - F2 (with chromatic approaches)
bass_notes = [
    (41, 3.0, 0.375),  # Bb2
    (40, 3.375, 0.375), # A2
    (38, 3.75, 0.375),  # G2
    (38, 4.125, 0.375), # F2
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bass_note)

# Sax: D - F - Bb - D (with a rest on the second note)
sax_notes = [
    (82, 3.0, 0.375),  # D
    (0, 3.75, 0.375),  # rest
    (78, 4.5, 0.375),  # Bb
    (82, 5.25, 0.375), # D
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Piano: D7 - C7 - Bb7 - Ab7
piano_notes = [
    (76, 4.5, 0.375),  # D7
    (72, 5.25, 0.375), # C7
    (78, 6.0, 0.375),  # Bb7
    (78, 6.0, 0.375),  # Ab7 (sustained)
]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(piano_note)

# Bass: F2 - G2 - D2 - F2 (with chromatic approaches)
bass_notes = [
    (38, 4.5, 0.375),  # F2
    (40, 4.875, 0.375), # G2
    (36, 5.25, 0.375),  # D2
    (38, 5.625, 0.375), # F2
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(bass_note)

# Sax: F - Bb - D - F (ending with a sustained note)
sax_notes = [
    (84, 4.5, 0.375),  # F
    (78, 5.25, 0.375), # Bb
    (82, 6.0, 0.375),  # D
    (84, 6.0, 0.375),  # F (sustained)
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(sax_note)

# Drums for bars 2-4:
# Bar 2: kick on 1, snare on 2, kick on 3, snare on 4
# Bar 3: kick on 1, snare on 2, kick on 3, snare on 4
# Bar 4: kick on 1, snare on 2, kick on 3, snare on 4
# Hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.append(kick1)
    drums.notes.append(kick3)
    drums.notes.append(snare2)
    drums.notes.append(snare4)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
