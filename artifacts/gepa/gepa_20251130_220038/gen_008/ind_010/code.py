
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
    (36, 0.0, 0.375),   # kick on 1
    (42, 0.0, 0.1875),  # hihat on 1 & 2
    (42, 0.375, 0.1875), # hihat on 2
    (38, 0.75, 0.375),  # snare on 3
    (42, 0.75, 0.1875), # hihat on 3 & 4
    (42, 1.125, 0.1875),# hihat on 4
    (36, 1.5, 0.375)    # kick on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5, 0.375),   # F3
    (46, 1.875, 0.375), # G3
    (47, 2.25, 0.375),  # A3
    (45, 2.625, 0.375), # F3
    (44, 2.999, 0.375), # E3 (chromatic approach)
    (45, 3.375, 0.375), # F3
    (47, 3.75, 0.375),  # A3
    (48, 4.125, 0.375), # Bb3
    (49, 4.5, 0.375),   # B3
    (48, 4.875, 0.375), # Bb3
    (47, 5.25, 0.375),  # A3
    (45, 5.625, 0.375)  # F3
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    (57, 1.5, 0.1875), # F7: F (57), A (60), C (61), E (64)
    (60, 1.5, 0.1875),
    (61, 1.5, 0.1875),
    (64, 1.5, 0.1875),
    (57, 1.875, 0.1875),
    (60, 1.875, 0.1875),
    (61, 1.875, 0.1875),
    (64, 1.875, 0.1875),
    # Bar 3
    (57, 2.25, 0.1875),
    (60, 2.25, 0.1875),
    (61, 2.25, 0.1875),
    (64, 2.25, 0.1875),
    (57, 2.625, 0.1875),
    (60, 2.625, 0.1875),
    (61, 2.625, 0.1875),
    (64, 2.625, 0.1875),
    # Bar 4
    (57, 3.0, 0.1875),
    (60, 3.0, 0.1875),
    (61, 3.0, 0.1875),
    (64, 3.0, 0.1875),
    (57, 3.375, 0.1875),
    (60, 3.375, 0.1875),
    (61, 3.375, 0.1875),
    (64, 3.375, 0.1875)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: motif that sings, starts and ends with a question
sax_notes = [
    (66, 1.5, 0.375),   # F4
    (67, 1.875, 0.375), # G4
    (64, 2.25, 0.375),  # E4 (leave it hanging)
    (66, 2.625, 0.375), # F4
    (67, 2.999, 0.375), # G4
    (69, 3.375, 0.375), # A4
    (67, 3.75, 0.375),  # G4
    (66, 4.125, 0.375), # F4
    (64, 4.5, 0.375),   # E4
    (66, 4.875, 0.375), # F4
    (67, 5.25, 0.375),  # G4
    (69, 5.625, 0.375)  # A4
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # kick on 1
    (42, 1.5, 0.1875),  # hihat on 1 & 2
    (42, 1.875, 0.1875),
    (38, 2.25, 0.375),  # snare on 3
    (42, 2.25, 0.1875), # hihat on 3 & 4
    (42, 2.625, 0.1875),
    (36, 3.0, 0.375),   # kick on 1
    (42, 3.0, 0.1875),  # hihat on 1 & 2
    (42, 3.375, 0.1875),
    (38, 3.75, 0.375),  # snare on 3
    (42, 3.75, 0.1875), # hihat on 3 & 4
    (42, 4.125, 0.1875),
    (36, 4.5, 0.375),   # kick on 1
    (42, 4.5, 0.1875),  # hihat on 1 & 2
    (42, 4.875, 0.1875),
    (38, 5.25, 0.375),  # snare on 3
    (42, 5.25, 0.1875), # hihat on 3 & 4
    (42, 5.625, 0.1875)
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
