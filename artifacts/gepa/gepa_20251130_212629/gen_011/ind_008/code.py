
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (36, 0.75, 0.375), # Kick on 3
    (42, 0.75, 0.375), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 2
    (42, 1.125, 0.375), # Hihat on 2
    (38, 1.5, 0.375),   # Snare on 4
    (42, 1.5, 0.375)    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches, no repeated notes)
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (61, 2.625, 0.375), # C
    (62, 2.625, 0.375), # D
    (63, 2.625, 0.375), # Eb
    (64, 2.625, 0.375), # E
    (65, 2.625, 0.375), # F
    (64, 3.0, 0.375),   # E
    (63, 3.375, 0.375), # Eb
    (62, 3.75, 0.375),  # D
    (61, 4.125, 0.375), # C
    (62, 4.5, 0.375),   # D
    (63, 4.875, 0.375), # Eb
    (64, 5.25, 0.375),  # E
    (65, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    (62, 1.875, 0.375),  # D7 on 2
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (69, 1.875, 0.375),
    (62, 3.375, 0.375),  # D7 on 4
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (69, 3.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums (full kit)
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (36, 2.25, 0.375), # Kick on 3
    (42, 2.25, 0.375), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 2
    (42, 2.625, 0.375), # Hihat on 2
    (38, 3.0, 0.375),   # Snare on 4
    (42, 3.0, 0.375),   # Hihat on 4
    (36, 3.75, 0.375),  # Kick on 1
    (42, 3.75, 0.375),  # Hihat on 1
    (36, 4.5, 0.375),   # Kick on 3
    (42, 4.5, 0.375),   # Hihat on 3
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.375), # Hihat on 2
    (38, 5.25, 0.375),  # Snare on 4
    (42, 5.25, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax (short motif, melodic, not scale runs)
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    (62, 3.0, 0.375),   # D
    (64, 3.375, 0.375), # E
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # C
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
