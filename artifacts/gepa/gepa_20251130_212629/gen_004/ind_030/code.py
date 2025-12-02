
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
    (36, 0.0, 0.375),
    (38, 0.375, 0.375),
    (42, 0.0, 0.125),
    (42, 0.125, 0.125),
    (42, 0.25, 0.125),
    (42, 0.375, 0.125),
    (36, 1.125, 0.375),
    (38, 1.5, 0.375),
    (42, 1.125, 0.375),
    (42, 1.25, 0.125),
    (42, 1.375, 0.125),
    (42, 1.5, 0.125)
]
for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F, chromatic approaches, no repeated notes
bass_notes = [
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375), # Gb
    (47, 2.25, 0.375),  # G
    (48, 2.625, 0.375), # Ab
    (49, 3.0, 0.375),   # A
    (50, 3.375, 0.375), # Bb
    (51, 3.75, 0.375),  # B
    (53, 4.125, 0.375), # C
    (52, 4.5, 0.375),   # Bb
    (51, 4.875, 0.375), # B
    (50, 5.25, 0.375),  # A
    (49, 5.625, 0.375)  # G
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (53, 1.875, 0.125), # C
    (50, 1.875, 0.125), # Bb
    (48, 1.875, 0.125), # Ab
    (45, 1.875, 0.125), # F
    (53, 2.25, 0.125),  # C
    (50, 2.25, 0.125),  # Bb
    (48, 2.25, 0.125),  # Ab
    (45, 2.25, 0.125),  # F
    # Bar 3: Bb7 on 2 and 4
    (50, 3.375, 0.125), # F
    (48, 3.375, 0.125), # Eb
    (45, 3.375, 0.125), # Bb
    (43, 3.375, 0.125), # G
    (50, 3.75, 0.125),  # F
    (48, 3.75, 0.125),  # Eb
    (45, 3.75, 0.125),  # Bb
    (43, 3.75, 0.125),  # G
    # Bar 4: E7 on 2 and 4
    (55, 4.875, 0.125), # B
    (52, 4.875, 0.125), # G
    (49, 4.875, 0.125), # D
    (47, 4.875, 0.125), # F
    (55, 5.25, 0.125),  # B
    (52, 5.25, 0.125),  # G
    (49, 5.25, 0.125),  # D
    (47, 5.25, 0.125)   # F
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing
sax_notes = [
    (62, 1.5, 0.5),    # E (F7 chord tone)
    (64, 2.0, 0.5),    # G (F7 chord tone)
    (66, 2.5, 0.5),    # A (F7 chord tone)
    (62, 3.0, 0.5),    # E (F7 chord tone)
    (64, 3.5, 0.5),    # G (Bb7 chord tone)
    (67, 4.0, 0.5),    # B (Bb7 chord tone)
    (69, 4.5, 0.5),    # D (E7 chord tone)
    (66, 5.0, 0.5)     # A (E7 chord tone)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
