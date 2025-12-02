
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
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5, 0.375),    # F (beat 1)
    (46, 1.875, 0.375),  # Gb (beat 2)
    (47, 2.25, 0.375),   # G (beat 3)
    (44, 2.625, 0.375),  # E (beat 4)
    (45, 3.0, 0.375),    # F (beat 1)
    (47, 3.375, 0.375),  # G (beat 2)
    (48, 3.75, 0.375),   # Ab (beat 3)
    (46, 4.125, 0.375),  # Gb (beat 4)
    (47, 4.5, 0.375),    # G (beat 1)
    (48, 4.875, 0.375),  # Ab (beat 2)
    (49, 5.25, 0.375),   # A (beat 3)
    (47, 5.625, 0.375)   # G (beat 4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (53, 1.875, 0.375),  # C7 (C E G Bb)
    (50, 1.875, 0.375),
    (55, 1.875, 0.375),
    (57, 1.875, 0.375),
    # Bar 3
    (53, 3.375, 0.375),  # C7 (C E G Bb)
    (50, 3.375, 0.375),
    (55, 3.375, 0.375),
    (57, 3.375, 0.375),
    # Bar 4
    (53, 4.875, 0.375),  # C7 (C E G Bb)
    (50, 4.875, 0.375),
    (55, 4.875, 0.375),
    (57, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# F (G) Bb (A) C (Bb) D (C) - then back to F
sax_notes = [
    (61, 1.5, 0.375),    # G
    (60, 1.875, 0.375),  # A
    (62, 2.25, 0.375),   # Bb
    (63, 2.625, 0.375),  # C
    (62, 3.0, 0.375),    # Bb
    (61, 3.375, 0.375),  # A
    (60, 3.75, 0.375),   # G
    (59, 4.125, 0.375),  # F
    (60, 4.5, 0.375),    # G
    (61, 4.875, 0.375),  # A
    (62, 5.25, 0.375),   # Bb
    (63, 5.625, 0.375)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
