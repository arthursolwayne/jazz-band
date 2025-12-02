
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
    (36, 0.0, 1.0),      # Kick on 1
    (38, 0.5, 0.5),      # Snare on 2
    (42, 0.0, 1.0),      # Hihat on every eighth
    (36, 1.0, 1.0),      # Kick on 3
    (38, 1.5, 0.5),      # Snare on 4
    (42, 1.5, 1.0)       # Hihat on every eighth
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (37, 1.5, 0.375),    # D (root)
    (39, 1.875, 0.375),  # F (chromatic up)
    (38, 2.25, 0.375),   # E (bass approach)
    (36, 2.625, 0.375),  # D (root)
    (38, 2.625, 0.375),  # E (up beat)
    (39, 3.0, 0.375),    # F
    (41, 3.375, 0.375),  # A (chromatic up)
    (40, 3.75, 0.375),   # G (bass approach)
    (39, 4.125, 0.375),  # F
    (40, 4.125, 0.375),  # G (up beat)
    (41, 4.5, 0.375),    # A
    (43, 4.875, 0.375),  # C (chromatic up)
    (42, 5.25, 0.375),   # B (bass approach)
    (41, 5.625, 0.375),  # A
    (42, 5.625, 0.375),  # B (up beat)
    (43, 6.0, 0.375)     # C
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.5),      # F7: F, A, C, E (root)
    (64, 1.5, 0.5),      # A
    (67, 1.5, 0.5),      # C
    (69, 1.5, 0.5),      # E
    (64, 2.5, 0.5),      # A (comp on 2)
    (67, 2.5, 0.5),      # C
    (69, 2.5, 0.5),      # E
    (62, 2.5, 0.5),      # F
    (67, 3.5, 0.5),      # C (comp on 4)
    (69, 3.5, 0.5),      # E
    (62, 3.5, 0.5),      # F
    (64, 3.5, 0.5),      # A
    (67, 4.5, 0.5),      # C (comp on 2)
    (69, 4.5, 0.5),      # E
    (62, 4.5, 0.5),      # F
    (64, 4.5, 0.5),      # A
    (67, 5.5, 0.5),      # C (comp on 4)
    (69, 5.5, 0.5),      # E
    (62, 5.5, 0.5),      # F
    (64, 5.5, 0.5)       # A
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Sax: Motif, one short phrase, with space, ends on a question

# F, G, A, rest
sax_notes = [
    (65, 1.5, 0.375),    # F
    (66, 1.875, 0.375),  # G
    (67, 2.25, 0.375),   # A
    (67, 2.625, 0.375),  # A (tie)
    (65, 2.625, 0.375),  # F (rest)
    (65, 3.0, 0.375),    # F
    (66, 3.375, 0.375),  # G
    (67, 3.75, 0.375),   # A
    (67, 4.125, 0.375),  # A (tie)
    (65, 4.125, 0.375),  # F (rest)
    (65, 4.5, 0.375),    # F
    (66, 4.875, 0.375),  # G
    (67, 5.25, 0.375),   # A
    (67, 5.625, 0.375),  # A (tie)
    (65, 5.625, 0.375),  # F (rest)
    (64, 6.0, 0.375)     # E (ends on a question)
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
