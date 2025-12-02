
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.1875, 0.1875),  # Hihat on &1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.5625, 0.1875),  # Hihat on &2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.9375, 0.1875),  # Hihat on &3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.3125, 0.1875)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    (36, 1.5, 0.375),  # F
    (37, 1.875, 0.375),  # F#
    (35, 2.25, 0.375),  # E
    (34, 2.625, 0.375),  # D
    (33, 3.0, 0.375),  # C
    (34, 3.375, 0.375),  # D
    (35, 3.75, 0.375),  # E
    (36, 4.125, 0.375),  # F
    (37, 4.5, 0.375),  # F#
    (38, 4.875, 0.375),  # G
    (37, 5.25, 0.375),  # F#
    (36, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (42, 1.5, 0.1875),  # Bb7 - Bb
    (46, 1.5, 0.1875),  # D
    (48, 1.5, 0.1875),  # F
    (50, 1.5, 0.1875),  # Ab
    (46, 1.875, 0.1875),  # D
    (50, 1.875, 0.1875),  # Ab
    (52, 1.875, 0.1875),  # B
    # Bar 3
    (42, 2.25, 0.1875),  # Bb7 - Bb
    (46, 2.25, 0.1875),  # D
    (48, 2.25, 0.1875),  # F
    (50, 2.25, 0.1875),  # Ab
    (46, 2.625, 0.1875),  # D
    (50, 2.625, 0.1875),  # Ab
    (52, 2.625, 0.1875),  # B
    # Bar 4
    (42, 3.0, 0.1875),  # Bb7 - Bb
    (46, 3.0, 0.1875),  # D
    (48, 3.0, 0.1875),  # F
    (50, 3.0, 0.1875),  # Ab
    (46, 3.375, 0.1875),  # D
    (50, 3.375, 0.1875),  # Ab
    (52, 3.375, 0.1875),  # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Bar 2
    if bar == 2:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start + 0.1875, 0.1875),  # Hihat on &1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.5625, 0.1875),  # Hihat on &2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.9375, 0.1875),  # Hihat on &3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.3125, 0.1875)  # Hihat on &4
        ]
    # Bar 3
    elif bar == 3:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start + 0.1875, 0.1875),  # Hihat on &1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.5625, 0.1875),  # Hihat on &2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.9375, 0.1875),  # Hihat on &3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.3125, 0.1875)  # Hihat on &4
        ]
    # Bar 4
    elif bar == 4:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start + 0.1875, 0.1875),  # Hihat on &1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.5625, 0.1875),  # Hihat on &2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.9375, 0.1875),  # Hihat on &3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.3125, 0.1875)  # Hihat on &4
        ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    (62, 1.5, 0.25),  # G
    (60, 1.75, 0.25),  # E
    # Bar 3: Leave it hanging
    (62, 2.25, 0.25),  # G
    # Bar 4: Come back and finish
    (60, 3.0, 0.25),  # E
    (62, 3.25, 0.25),  # G
    (64, 3.5, 0.25),  # A
    (60, 3.75, 0.25)  # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
