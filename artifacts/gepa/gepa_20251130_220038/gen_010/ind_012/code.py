
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
    (42, 0.0, 0.1875), # Hihat on 1 & 2
    (42, 0.375, 0.1875), # Hihat on 2
    (38, 0.75, 0.375),  # Snare on 3
    (42, 0.75, 0.1875), # Hihat on 3 & 4
    (42, 1.125, 0.1875),# Hihat on 4
    (36, 1.5, 0.375)    # Kick on 1 of next bar
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (63, 1.875, 0.375), # Eb (chromatic up)
    (60, 2.25, 0.375),  # B (7th)
    (62, 2.625, 0.375), # D (root)
    (65, 2.875, 0.375), # F# (chromatic up)
    (64, 3.25, 0.375),  # F (chromatic down)
    (62, 3.625, 0.375), # D (root)
    (63, 3.875, 0.375), # Eb (chromatic up)
    (60, 4.25, 0.375),  # B (7th)
    (62, 4.625, 0.375), # D (root)
    (65, 5.0, 0.375),   # F# (chromatic up)
    (64, 5.375, 0.375), # F (chromatic down)
    (62, 5.75, 0.375)   # D (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (67, 1.875, 0.375), # F7 (F, A, C, Eb)
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (64, 1.875, 0.375),
    # Bar 3
    (67, 3.25, 0.375),
    (69, 3.25, 0.375),
    (71, 3.25, 0.375),
    (64, 3.25, 0.375),
    # Bar 4
    (67, 4.625, 0.375),
    (69, 4.625, 0.375),
    (71, 4.625, 0.375),
    (64, 4.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875))

# Saxophone (Dante): short motif, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # B
    (62, 3.5, 0.375),   # D (return)
    (64, 3.875, 0.375), # E
    (62, 4.25, 0.375),  # D
    (60, 4.625, 0.375)  # B
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
