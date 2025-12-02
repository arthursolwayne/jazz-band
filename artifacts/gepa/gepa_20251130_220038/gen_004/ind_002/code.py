
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.375),   # Hihat on 1
    (38, 0.375, 0.75),  # Snare on 2
    (42, 0.375, 0.75),  # Hihat on 2
    (36, 0.75, 1.125),  # Kick on 3
    (42, 0.75, 1.125),  # Hihat on 3
    (38, 1.125, 1.5),   # Snare on 4
    (42, 1.125, 1.5)    # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm
bass_notes = [
    (45, 1.5, 0.375),  # F
    (47, 1.875, 0.375), # Ab
    (48, 2.25, 0.375),  # Bb
    (45, 2.625, 0.375), # F
    (47, 2.625, 0.375), # Ab
    (49, 2.625, 0.375), # C
    (48, 2.625, 0.375), # Bb
    (45, 2.625, 0.375), # F
    (46, 3.0, 0.375),   # G
    (48, 3.375, 0.375), # Bb
    (49, 3.75, 0.375),  # C
    (47, 4.125, 0.375), # Ab
    (46, 4.5, 0.375),   # G
    (45, 4.875, 0.375), # F
    (44, 5.25, 0.375),  # Eb
    (45, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.375),  # F7 (Bb)
    (53, 1.875, 0.375),  # F7 (D)
    (55, 1.875, 0.375),  # F7 (F)
    (57, 1.875, 0.375),  # F7 (Ab)
    # Bar 3
    (50, 3.375, 0.375),  # F7 (Bb)
    (53, 3.375, 0.375),  # F7 (D)
    (55, 3.375, 0.375),  # F7 (F)
    (57, 3.375, 0.375),  # F7 (Ab)
    # Bar 4
    (50, 4.875, 0.375),  # F7 (Bb)
    (53, 4.875, 0.375),  # F7 (D)
    (55, 4.875, 0.375),  # F7 (F)
    (57, 4.875, 0.375),  # F7 (Ab)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums (Little Ray) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.375),   # Hihat on 1
    (38, 1.875, 0.75),  # Snare on 2
    (42, 1.875, 0.75),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.75),  # Snare on 4
    (42, 2.625, 0.75),  # Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (38, 3.375, 0.75),  # Snare on 2
    (42, 3.375, 0.75),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.75),  # Snare on 4
    (42, 4.125, 0.75),  # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (38, 4.875, 0.75),  # Snare on 2
    (42, 4.875, 0.75),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.75),  # Snare on 4
    (42, 5.625, 0.75)   # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Saxophone (Dante)
sax_notes = [
    (62, 1.875, 0.375),  # D
    (64, 2.25, 0.375),   # E
    (62, 2.625, 0.375),  # D
    (60, 3.0, 0.375),    # C
    (62, 3.375, 0.375),  # D
    (64, 3.75, 0.375),   # E
    (62, 4.125, 0.375),  # D
    (60, 4.5, 0.375),    # C
    (62, 4.875, 0.375),  # D
    (64, 5.25, 0.375),   # E
    (62, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
