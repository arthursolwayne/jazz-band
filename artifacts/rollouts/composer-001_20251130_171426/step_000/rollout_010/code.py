
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &1
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &2
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &3
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on &3
    (42, 1.5, 0.1875)  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Sax melody
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F - Ab - Bb - Ab (Fm6/9)

sax_notes = [
    (84, 1.5, 0.375),  # F
    (81, 1.875, 0.375),  # Ab
    (80, 2.25, 0.375),  # Bb
    (81, 2.625, 0.375),  # Ab
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm with chromatic approaches
# F - Gb - Ab - A - Bb - B - Db - Eb - F
bass_notes = [
    (53, 1.5, 0.375),  # F
    (52, 1.875, 0.375),  # Gb
    (50, 2.25, 0.375),  # Ab
    (51, 2.625, 0.375),  # A
    (50, 2.625, 0.375),  # Bb
    (51, 2.625, 0.375),  # B
    (49, 2.625, 0.375),  # Db
    (50, 2.625, 0.375),  # Eb
    (53, 3.0, 0.375),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Ab7 on 4
piano_notes = [
    (53, 1.875, 0.375),  # F
    (51, 1.875, 0.375),  # Bb
    (50, 1.875, 0.375),  # Ab
    (48, 1.875, 0.375),  # D
    (53, 2.625, 0.375),  # F
    (51, 2.625, 0.375),  # Bb
    (50, 2.625, 0.375),  # Ab
    (47, 2.625, 0.375),  # G
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Sax melody repeats, but shifts up a third
# Ab - Bb - Db - Bb (Abm6/9)
sax_notes = [
    (81, 3.0, 0.375),  # Ab
    (80, 3.375, 0.375),  # Bb
    (78, 3.75, 0.375),  # Db
    (80, 4.125, 0.375),  # Bb
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Abm
# Ab - Bb - C - Db - Eb - F - Gb - Ab
bass_notes = [
    (50, 3.0, 0.375),  # Ab
    (51, 3.375, 0.375),  # Bb
    (52, 3.75, 0.375),  # C
    (50, 4.125, 0.375),  # Db
    (51, 4.125, 0.375),  # Eb
    (52, 4.125, 0.375),  # F
    (51, 4.125, 0.375),  # Gb
    (50, 4.125, 0.375),  # Ab
    (50, 4.5, 0.375),  # Ab
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
# Abm7 on 2, Bbm7 on 4
piano_notes = [
    (50, 3.375, 0.375),  # Ab
    (48, 3.375, 0.375),  # Db
    (51, 3.375, 0.375),  # Bb
    (47, 3.375, 0.375),  # G
    (51, 4.125, 0.375),  # Bb
    (50, 4.125, 0.375),  # Ab
    (48, 4.125, 0.375),  # Db
    (47, 4.125, 0.375),  # G
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Sax melody ends with a resolution
# F - F - Ab - F (Fm6)
sax_notes = [
    (84, 4.5, 0.375),  # F
    (84, 4.875, 0.375),  # F
    (81, 5.25, 0.375),  # Ab
    (84, 5.625, 0.375),  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bass: Walking line in Fm
# F - Gb - Ab - A - Bb - B - Db - Eb - F
bass_notes = [
    (53, 4.5, 0.375),  # F
    (52, 4.875, 0.375),  # Gb
    (50, 5.25, 0.375),  # Ab
    (51, 5.625, 0.375),  # A
    (50, 5.625, 0.375),  # Bb
    (51, 5.625, 0.375),  # B
    (49, 5.625, 0.375),  # Db
    (50, 5.625, 0.375),  # Eb
    (53, 6.0, 0.375),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Am7 on 4
piano_notes = [
    (53, 4.875, 0.375),  # F
    (51, 4.875, 0.375),  # Bb
    (50, 4.875, 0.375),  # Ab
    (48, 4.875, 0.375),  # D
    (57, 5.625, 0.375),  # A
    (55, 5.625, 0.375),  # C
    (53, 5.625, 0.375),  # E
    (51, 5.625, 0.375),  # G
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes = [
        (36, start + 0.0, 0.375),  # Kick on 1
        (38, start + 0.375, 0.375),  # Snare on 2
        (42, start + 0.0, 0.1875),
        (42, start + 0.1875, 0.1875),
        (42, start + 0.375, 0.1875),
        (42, start + 0.5625, 0.1875),
        (42, start + 0.75, 0.1875),
        (42, start + 0.9375, 0.1875),
        (36, start + 1.125, 0.375),  # Kick on 3
        (38, start + 1.5, 0.375),  # Snare on 4
        (42, start + 1.125, 0.1875),
        (42, start + 1.3125, 0.1875),
        (42, start + 1.5, 0.1875)
    ]
    for note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

# Write to MIDI file
midi.write("jazz_intro.mid")
