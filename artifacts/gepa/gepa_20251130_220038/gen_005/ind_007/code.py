
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line
bass_notes = [
    (44, 1.5, 0.375),  # D
    (46, 1.875, 0.375), # Eb
    (48, 2.25, 0.375),  # F
    (49, 2.625, 0.375), # F#
    (48, 3.0, 0.375),   # F
    (46, 3.375, 0.375), # Eb
    (44, 3.75, 0.375),  # D
    (42, 4.125, 0.375), # C
    (44, 4.5, 0.375),   # D
    (46, 4.875, 0.375), # Eb
    (48, 5.25, 0.375),  # F
    (49, 5.625, 0.375)  # F#
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: comping on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.875, 0.375), # E7
    (60, 1.875, 0.375),
    (62, 1.875, 0.375),
    (64, 1.875, 0.375),
    # Bar 3
    (57, 3.375, 0.375), # E7
    (60, 3.375, 0.375),
    (62, 3.375, 0.375),
    (64, 3.375, 0.375),
    # Bar 4
    (57, 4.875, 0.375), # E7
    (60, 4.875, 0.375),
    (62, 4.875, 0.375),
    (64, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Saxophone: your motif
sax_notes = [
    (62, 1.5, 0.5),    # F
    (65, 2.0, 0.5),    # A
    (64, 2.5, 0.5),    # G
    (62, 3.0, 0.5),    # F
    (65, 3.5, 0.5),    # A
    (64, 4.0, 0.5),    # G
    (62, 4.5, 0.5),    # F
    (65, 5.0, 0.5)     # A
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
