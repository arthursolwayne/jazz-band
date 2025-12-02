
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
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (36, 1.125, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on &
    (42, 1.5, 0.1875),  # Hihat on 4
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7: D F A C
# Walking line in Dm: D F Ab Bb C Eb F A
bass_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (60, 2.25, 0.375),  # Ab
    (61, 2.625, 0.375),  # Bb
    (65, 3.0, 0.375),  # C
    (63, 3.375, 0.375),  # Eb
    (64, 3.75, 0.375),  # F
    (67, 4.125, 0.375),  # A
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375),  # F
    (60, 5.25, 0.375),  # Ab
    (61, 5.625, 0.375),  # Bb
]
for note, start, duration in bass_notes:
    nb = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(nb)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.1875),  # D
    (64, 1.5, 0.1875),  # F
    (69, 1.5, 0.1875),  # A
    (67, 1.5, 0.1875),  # C
    # Bar 3 (3.0 - 4.5s)
    (71, 3.0, 0.1875),  # G
    (76, 3.0, 0.1875),  # B
    (71, 3.0, 0.1875),  # D
    (72, 3.0, 0.1875),  # F
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.1875),  # C
    (63, 4.5, 0.1875),  # Eb
    (67, 4.5, 0.1875),  # G
    (66, 4.5, 0.1875),  # Bb
    (67, 4.5, 0.1875),  # F
    (72, 4.5, 0.1875),  # A
    (67, 4.5, 0.1875),  # C
    (69, 4.5, 0.1875),  # Eb
]
for note, start, duration in piano_notes:
    np = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(np)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm: D, F, Ab, Bb, C, Eb
# Motif: D - F - Ab - D (hanging on Ab)
# Then return with Bb - C - Eb - D
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (60, 2.25, 0.375),  # Ab
    (62, 2.625, 0.375),  # D
    (61, 3.0, 0.375),  # Bb
    (65, 3.375, 0.375),  # C
    (63, 3.75, 0.375),  # Eb
    (62, 4.125, 0.375),  # D
]
for note, start, duration in sax_notes:
    ns = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(ns)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (38, start + 0.375, 0.375),  # Snare on 2
        (42, start, 0.1875),  # Hihat on 1
        (42, start + 0.1875, 0.1875),  # Hihat on &
        (42, start + 0.375, 0.1875),  # Hihat on 2
        (42, start + 0.5625, 0.1875),  # Hihat on &
        (42, start + 0.75, 0.1875),  # Hihat on 3
        (42, start + 0.9375, 0.1875),  # Hihat on &
        (36, start + 1.125, 0.375),  # Kick on 3
        (38, start + 1.5, 0.375),  # Snare on 4
        (42, start + 1.125, 0.1875),  # Hihat on 3
        (42, start + 1.3125, 0.1875),  # Hihat on &
        (42, start + 1.5, 0.1875),  # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
