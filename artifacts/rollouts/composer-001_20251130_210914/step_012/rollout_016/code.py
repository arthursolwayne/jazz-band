
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
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    (44, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # G
    (45, 2.25, 0.375),  # Gb
    (44, 2.625, 0.375),  # F
    (47, 2.625, 0.375),  # Ab
    (46, 2.625, 0.375),  # G
    (45, 2.625, 0.375),  # Gb
    (44, 2.625, 0.375),  # F
    (48, 3.0, 0.375),  # Bb
    (47, 3.375, 0.375),  # Ab
    (46, 3.75, 0.375),  # G
    (45, 4.125, 0.375),  # Gb
    (44, 4.5, 0.375),  # F
    (46, 4.875, 0.375),  # G
    (45, 5.25, 0.375),  # Gb
    (44, 5.625, 0.375)   # F
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (44, 1.5, 0.375),  # F7 (F, A, C, Eb)
    (46, 1.5, 0.375),
    (48, 1.5, 0.375),
    (49, 1.5, 0.375),
    # Bar 3
    (44, 2.25, 0.375),  # F7
    (46, 2.25, 0.375),
    (48, 2.25, 0.375),
    (49, 2.25, 0.375),
    # Bar 4
    (44, 3.0, 0.375),  # F7
    (46, 3.0, 0.375),
    (48, 3.0, 0.375),
    (49, 3.0, 0.375)
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick 1
    (42, 1.5, 0.375),  # Hihat 1
    (38, 1.875, 0.375),  # Snare 2
    (42, 1.875, 0.375),  # Hihat 2
    (36, 2.25, 0.375),  # Kick 3
    (42, 2.25, 0.375),  # Hihat 3
    (38, 2.625, 0.375),  # Snare 4
    (42, 2.625, 0.375),  # Hihat 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick 1
    (42, 3.0, 0.375),  # Hihat 1
    (38, 3.375, 0.375),  # Snare 2
    (42, 3.375, 0.375),  # Hihat 2
    (36, 3.75, 0.375),  # Kick 3
    (42, 3.75, 0.375),  # Hihat 3
    (38, 4.125, 0.375),  # Snare 4
    (42, 4.125, 0.375),  # Hihat 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick 1
    (42, 4.5, 0.375),  # Hihat 1
    (38, 4.875, 0.375),  # Snare 2
    (42, 4.875, 0.375),  # Hihat 2
    (36, 5.25, 0.375),  # Kick 3
    (42, 5.25, 0.375),  # Hihat 3
    (38, 5.625, 0.375),  # Snare 4
    (42, 5.625, 0.375)   # Hihat 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Sax (Dante): Motif in Fm
sax_notes = [
    (44, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # G
    (45, 2.25, 0.375),  # Gb
    (44, 2.625, 0.375),  # F
    (44, 3.0, 0.375),  # F
    (46, 3.375, 0.375),  # G
    (45, 3.75, 0.375),  # Gb
    (44, 4.125, 0.375),  # F
    (44, 4.5, 0.375),  # F
    (46, 4.875, 0.375),  # G
    (45, 5.25, 0.375),  # Gb
    (44, 5.625, 0.375)   # F
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
