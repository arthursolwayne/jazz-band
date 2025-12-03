
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

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.75),  # Hihat on 1 & 2
    (42, 0.375, 0.75),  # Hihat on 1 & 2
    (42, 0.75, 1.125),  # Hihat on 3
    (42, 1.125, 1.5),  # Hihat on 4
    (36, 1.125, 1.5),  # Kick on 3
    (38, 1.5, 1.5),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (Bass) - walking line: D2, F2, G2, C2, with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (40, 1.875, 0.375),  # F2 on 2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 on 3
    (36, 2.625, 0.375),  # C2 on 4 (chromatic approach)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane (Piano) - Open voicings, resolve on the last chord
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (50, 1.5, 0.375),  # D
    (53, 1.5, 0.375),  # F
    (57, 1.5, 0.375),  # A
    (55, 1.5, 0.375),  # C
    # Bar 3: Gm7 (G, Bb, D, F)
    (55, 2.25, 0.375),  # G
    (58, 2.25, 0.375),  # Bb
    (59, 2.25, 0.375),  # D
    (53, 2.25, 0.375),  # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (52, 3.0, 0.375),  # C
    (55, 3.0, 0.375),  # Eb
    (59, 3.0, 0.375),  # G
    (58, 3.0, 0.375),  # Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar2 = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 0.75),  # Hihat on 1 & 2
    (42, 1.875, 0.75),  # Hihat on 1 & 2
    (42, 2.25, 2.625),  # Hihat on 3 and 4
    (36, 2.25, 0.375),  # Kick on 3
    (38, 2.625, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes_bar2:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus (Bass) - Walking line: C2, D2, F2, G2, with chromatic approaches
bass_notes_bar3 = [
    (36, 3.0, 0.375),  # C2 on 1
    (38, 3.375, 0.375),  # D2 on 2 (chromatic approach)
    (40, 3.75, 0.375),  # F2 on 3
    (43, 4.125, 0.375),  # G2 on 4 (chromatic approach)
]

for note, start, duration in bass_notes_bar3:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane (Piano) - Open voicings, resolve on the last chord
piano_notes_bar3 = [
    # Bar 3: Dm7 (D, F, A, C)
    (50, 3.0, 0.375),  # D
    (53, 3.0, 0.375),  # F
    (57, 3.0, 0.375),  # A
    (55, 3.0, 0.375),  # C
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (52, 3.75, 0.375),  # C
    (55, 3.75, 0.375),  # Eb
    (59, 3.75, 0.375),  # G
    (58, 3.75, 0.375),  # Bb
]

for note, start, duration in piano_notes_bar3:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar3 = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.75),  # Hihat on 1 & 2
    (42, 3.375, 0.75),  # Hihat on 1 & 2
    (42, 3.75, 4.125),  # Hihat on 3 and 4
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes_bar3:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus (Bass) - Walking line: G2, A2, B2, D2, with chromatic approaches
bass_notes_bar4 = [
    (43, 4.5, 0.375),  # G2 on 1
    (45, 4.875, 0.375),  # A2 on 2 (chromatic approach)
    (47, 5.25, 0.375),  # B2 on 3
    (50, 5.625, 0.375),  # D2 on 4 (chromatic approach)
]

for note, start, duration in bass_notes_bar4:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane (Piano) - Open voicings, resolve on the last chord
piano_notes_bar4 = [
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (52, 4.5, 0.375),  # C
    (55, 4.5, 0.375),  # Eb
    (59, 4.5, 0.375),  # G
    (58, 4.5, 0.375),  # Bb
]

for note, start, duration in piano_notes_bar4:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes_bar4 = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.75),  # Hihat on 1 & 2
    (42, 4.875, 0.75),  # Hihat on 1 & 2
    (42, 5.25, 5.625),  # Hihat on 3 and 4
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes_bar4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante (Sax) - Melodic motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (62, 1.5, 0.25),  # E4 on 1
    (65, 1.75, 0.25),  # G4 on 2
    (67, 2.0, 0.25),  # A4 on 3
    (65, 2.25, 0.25),  # G4 on 4
    (62, 3.0, 0.25),  # E4 on 1
    (67, 3.25, 0.25),  # A4 on 2
    (69, 3.5, 0.25),  # B4 on 3
    (65, 3.75, 0.25),  # G4 on 4
    (67, 4.5, 0.25),  # A4 on 1
    (69, 4.75, 0.25),  # B4 on 2
    (67, 5.0, 0.25),  # A4 on 3
    (65, 5.25, 0.25),  # G4 on 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
