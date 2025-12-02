
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm, Fm7 (F, Ab, Bb, D)
bass_notes = [
    (64, 1.5, 0.375),    # F (1)
    (61, 1.875, 0.375),  # Eb (2)
    (62, 2.25, 0.375),   # F (3)
    (60, 2.625, 0.375),  # D (4)
    (64, 3.0, 0.375),    # F (1)
    (61, 3.375, 0.375),  # Eb (2)
    (62, 3.75, 0.375),   # F (3)
    (59, 4.125, 0.375),  # C (4)
    (64, 4.5, 0.375),    # F (1)
    (61, 4.875, 0.375),  # Eb (2)
    (62, 5.25, 0.375),   # F (3)
    (60, 5.625, 0.375)   # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Piano, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, 1.875, 0.25),  # F7 (F, A, C, Eb) on 2
    (64, 1.875, 0.25),
    (60, 1.875, 0.25),
    (58, 1.875, 0.25),
    # Bar 3
    (62, 3.375, 0.25),  # F7 on 2
    (64, 3.375, 0.25),
    (60, 3.375, 0.25),
    (58, 3.375, 0.25),
    # Bar 4
    (62, 4.875, 0.25),  # F7 on 2
    (64, 4.875, 0.25),
    (60, 4.875, 0.25),
    (58, 4.875, 0.25)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.5, end=start + 1.5 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 2.25, end=start + 2.25 + 0.375))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F - Ab - Bb (half note) - leave it hanging
# Come back with Ab - B - C (half note) - end with a whisper

# Bar 2: Start the motif
sax_notes = [
    (64, 1.5, 1.0),    # F (half note)
    (61, 2.5, 1.0),    # Ab (half note)
    (60, 3.5, 1.0),    # Bb (half note)
    (61, 4.5, 1.0),    # Ab (half note)
    (63, 5.5, 0.5)     # B (quarter note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Leave it hanging
sax_notes = [
    (61, 4.5, 0.5),    # Ab (quarter note)
    (63, 5.0, 0.5),    # B (quarter note)
    (64, 5.5, 0.5)     # C (quarter note)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
