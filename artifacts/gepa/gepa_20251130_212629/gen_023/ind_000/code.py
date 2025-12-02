
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
    (36, 0.0, 1.0),     # Kick on 1
    (38, 0.5, 0.5),     # Snare on 2
    (42, 0.0, 1.0),     # Hihat on every eighth
    (36, 1.0, 1.0),     # Kick on 3
    (38, 1.5, 0.5),     # Snare on 4
    (42, 1.5, 1.0)      # Hihat on every eighth
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),   # F
    (46, 1.875, 0.375), # F#
    (44, 2.25, 0.375),  # E
    (45, 2.625, 0.375), # F
    (46, 2.875, 0.375), # F#
    (47, 3.25, 0.375),  # G
    (45, 3.625, 0.375), # F
    (44, 3.875, 0.375)  # E
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (57, 1.5, 0.375),   # F7 (F, A, C, E)
    (57, 1.5, 0.375),
    (60, 1.5, 0.375),
    (64, 1.5, 0.375),
    (59, 1.875, 0.375), # D7 (D, F#, A, C)
    (59, 1.875, 0.375),
    (62, 1.875, 0.375),
    (66, 1.875, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),   # G
    (64, 2.25, 0.375),  # A
    (60, 2.625, 0.375)  # F
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (44, 3.0, 0.375),   # E
    (45, 3.375, 0.375), # F
    (43, 3.75, 0.375),  # D
    (44, 4.125, 0.375), # E
    (45, 4.5, 0.375),   # F
    (46, 4.875, 0.375), # F#
    (44, 5.25, 0.375),  # E
    (43, 5.625, 0.375)  # D
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (52, 3.0, 0.375),   # B7 (B, D#, F#, A)
    (52, 3.0, 0.375),
    (55, 3.0, 0.375),
    (58, 3.0, 0.375),
    (57, 3.5, 0.375),   # F7 (F, A, C, E)
    (57, 3.5, 0.375),
    (60, 3.5, 0.375),
    (64, 3.5, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif continuation
sax_notes = [
    (62, 3.0, 0.375),   # G
    (64, 3.375, 0.375), # A
    (60, 3.75, 0.375),  # F
    (62, 4.125, 0.375), # G
    (64, 4.5, 0.375)    # A
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),     # Kick on 1
    (38, 5.0, 0.5),     # Snare on 2
    (42, 4.5, 1.0),     # Hihat on every eighth
    (36, 5.5, 1.0),     # Kick on 3
    (38, 6.0, 0.5),     # Snare on 4
    (42, 5.5, 1.0)      # Hihat on every eighth
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (43, 4.5, 0.375),   # D
    (44, 4.875, 0.375), # E
    (42, 5.25, 0.375),  # C
    (43, 5.625, 0.375), # D
    (44, 6.0, 0.375),   # E
    (45, 6.375, 0.375), # F
    (43, 6.75, 0.375),  # D
    (42, 7.125, 0.375)  # C
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    (50, 4.5, 0.375),   # A7 (A, C#, E, G)
    (50, 4.5, 0.375),
    (53, 4.5, 0.375),
    (56, 4.5, 0.375),
    (52, 5.0, 0.375),   # B7 (B, D#, F#, A)
    (52, 5.0, 0.375),
    (55, 5.0, 0.375),
    (58, 5.0, 0.375)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif continuation, ends with a question
sax_notes = [
    (62, 4.5, 0.375),   # G
    (64, 4.875, 0.375), # A
    (60, 5.25, 0.375),  # F
    (62, 5.625, 0.375), # G
    (64, 6.0, 0.375)    # A
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
