
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line: Fm7 -> Bb7 -> Eb7 -> Am7
# Fm7: F, Ab, D, C
# Bb7: Bb, D, F, Ab
# Eb7: Eb, G, Bb, Db
# Am7: A, C, E, G

# Marcus (bass) - walking line with chromatic approaches
bass_notes = [
    (53, 1.5, 1.5),  # F2
    (51, 1.875, 1.875),  # Eb2
    (55, 2.25, 2.25),  # G2
    (53, 2.625, 2.625),  # F2
    (58, 2.625, 3.0),  # Bb2
    (56, 3.0, 3.0),  # Ab2
    (58, 3.375, 3.375),  # Bb2
    (60, 3.75, 3.75),  # C2
    (58, 4.125, 4.125),  # Bb2
    (62, 4.5, 4.5),  # D2
    (60, 4.875, 4.875),  # C2
    (62, 5.25, 5.25),  # D2
    (64, 5.625, 5.625),  # Eb2
    (62, 6.0, 6.0)  # D2
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Diane (piano) - open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, D) -> resolve on D
piano_notes = [
    (62, 1.5, 1.5),  # F4
    (64, 1.5, 1.5),  # Ab4
    (67, 1.5, 1.5),  # C5
    (69, 1.5, 1.5),  # D5

    # Bar 3: Bb7 (Bb, D, F, Ab) -> resolve on F
    (66, 2.25, 2.25),  # Bb4
    (69, 2.25, 2.25),  # D5
    (67, 2.25, 2.25),  # F5
    (64, 2.25, 2.25),  # Ab4

    # Bar 4: Eb7 (Eb, G, Bb, Db) -> resolve on G
    (60, 3.0, 3.0),  # Eb4
    (62, 3.0, 3.0),  # G4
    (66, 3.0, 3.0),  # Bb4
    (61, 3.0, 3.0),  # Db4
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Little Ray (drums) - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 1.5),  # Kick on 1
    (42, 1.5, 1.5),  # Hihat on 1
    (38, 1.875, 1.875),  # Snare on 2
    (42, 1.875, 1.875),  # Hihat on 2
    (36, 2.25, 2.25),  # Kick on 3
    (42, 2.25, 2.25),  # Hihat on 3
    (38, 2.625, 2.625),  # Snare on 4
    (42, 2.625, 2.625),  # Hihat on 4

    (36, 3.0, 3.0),  # Kick on 1
    (42, 3.0, 3.0),  # Hihat on 1
    (38, 3.375, 3.375),  # Snare on 2
    (42, 3.375, 3.375),  # Hihat on 2
    (36, 3.75, 3.75),  # Kick on 3
    (42, 3.75, 3.75),  # Hihat on 3
    (38, 4.125, 4.125),  # Snare on 4
    (42, 4.125, 4.125),  # Hihat on 4

    (36, 4.5, 4.5),  # Kick on 1
    (42, 4.5, 4.5),  # Hihat on 1
    (38, 4.875, 4.875),  # Snare on 2
    (42, 4.875, 4.875),  # Hihat on 2
    (36, 5.25, 5.25),  # Kick on 3
    (42, 5.25, 5.25),  # Hihat on 3
    (38, 5.625, 5.625),  # Snare on 4
    (42, 5.625, 5.625)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Dante (sax) - one short motif that sings, starts, leaves it hanging, returns to finish it
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F -> Gb -> Ab -> A -> F (half note, quarter note, eighth note, eighth note, half note)
sax_notes = [
    (62, 1.5, 3.0),  # F4 - half note
    (61, 3.0, 3.375),  # Gb4 - quarter note
    (64, 3.375, 3.75),  # Ab4 - eighth note
    (65, 3.75, 4.125),  # A4 - eighth note
    (62, 4.125, 6.0)  # F4 - half note
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
