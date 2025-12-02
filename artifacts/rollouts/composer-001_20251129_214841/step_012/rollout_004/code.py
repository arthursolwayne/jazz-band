
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375),  # D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, D)
    (60, 1.5, 0.375),  # C
    (64, 1.5, 0.375),  # E
    (67, 1.5, 0.375),  # B
    (62, 1.5, 0.375),  # D
    # Bar 3: E7 (E, G#, B, D)
    (64, 2.25, 0.375),  # E
    (69, 2.25, 0.375),  # G#
    (67, 2.25, 0.375),  # B
    (62, 2.25, 0.375),  # D
    # Bar 4: Am7 (A, C, E, G)
    (65, 2.625, 0.375),  # A
    (60, 2.625, 0.375),  # C
    (67, 2.625, 0.375),  # E
    (67, 2.625, 0.375),  # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C - E♭ - D - rest
sax_notes = [
    (60, 1.5, 0.375),  # C
    (63, 1.875, 0.375),  # E♭
    (62, 2.25, 0.375),  # D
    (62, 2.625, 0.375),  # D (rest)
    (60, 3.0, 0.375),  # C
    (63, 3.375, 0.375),  # E♭
    (62, 3.75, 0.375),  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),  # Kick on 1
        (42, start, 0.375),  # Hihat on 1
        (38, start + 0.375, 0.375),  # Snare on 2
        (42, start + 0.375, 0.375),  # Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.375),  # Hihat on 3
        (38, start + 1.125, 0.375),  # Snare on 4
        (42, start + 1.125, 0.375),  # Hihat on 4
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
