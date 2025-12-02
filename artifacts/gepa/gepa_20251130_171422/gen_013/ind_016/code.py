
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
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.125, 0.1875), # Hihat on 3
    (38, 1.5, 0.375),   # Snare on 4
    (42, 1.5, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (64, 1.5, 0.375),   # F
    (65, 1.875, 0.375), # Gb
    (62, 2.25, 0.375),  # Eb
    (60, 2.625, 0.375), # D
    (61, 2.625, 0.375), # Eb
    (62, 2.625, 0.375), # Eb
    (64, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # Ab
    (65, 3.375, 0.375), # Gb
    (63, 3.75, 0.375),  # E
    (62, 4.125, 0.375), # Eb
    (61, 4.5, 0.375),   # E
    (60, 4.875, 0.375), # D
    (62, 5.25, 0.375),  # Eb
    (63, 5.625, 0.375), # E
    (64, 6.0, 0.375)    # F
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano (Diane)
piano_notes = [
    (64, 1.5, 0.375),   # F7 (F, Ab, C)
    (64, 1.5, 0.375),
    (70, 1.5, 0.375),
    (64, 1.875, 0.375), # F7
    (64, 1.875, 0.375),
    (70, 1.875, 0.375),
    (64, 2.25, 0.375),  # F7
    (64, 2.25, 0.375),
    (70, 2.25, 0.375),
    (64, 2.625, 0.375), # F7
    (64, 2.625, 0.375),
    (70, 2.625, 0.375),
    (64, 3.0, 0.375),   # F7
    (64, 3.0, 0.375),
    (70, 3.0, 0.375),
    (64, 3.375, 0.375), # F7
    (64, 3.375, 0.375),
    (70, 3.375, 0.375),
    (64, 3.75, 0.375),  # F7
    (64, 3.75, 0.375),
    (70, 3.75, 0.375),
    (64, 4.125, 0.375), # F7
    (64, 4.125, 0.375),
    (70, 4.125, 0.375),
    (64, 4.5, 0.375),   # F7
    (64, 4.5, 0.375),
    (70, 4.5, 0.375),
    (64, 4.875, 0.375), # F7
    (64, 4.875, 0.375),
    (70, 4.875, 0.375),
    (64, 5.25, 0.375),  # F7
    (64, 5.25, 0.375),
    (70, 5.25, 0.375),
    (64, 5.625, 0.375), # F7
    (64, 5.625, 0.375),
    (70, 5.625, 0.375),
    (64, 6.0, 0.375)    # F7
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - motif: F, Ab, Eb, D
sax_notes = [
    (64, 1.5, 0.375),   # F
    (70, 1.875, 0.375), # Ab
    (62, 2.25, 0.375),  # Eb
    (60, 2.625, 0.375), # D
    (64, 3.0, 0.375),   # F
    (70, 3.375, 0.375), # Ab
    (62, 3.75, 0.375),  # Eb
    (60, 4.125, 0.375), # D
    (64, 4.5, 0.375),   # F
    (70, 4.875, 0.375), # Ab
    (62, 5.25, 0.375),  # Eb
    (60, 5.625, 0.375)  # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875),# Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875),# Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875),# Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
