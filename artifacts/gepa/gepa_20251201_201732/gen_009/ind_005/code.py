
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
    (36, 0.0, 0.375),    # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),   # Hihat on 1
    (42, 0.1875, 0.1875),# Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875),# Hihat on &
    (36, 0.75, 0.375),   # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),# Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875) # Hihat on &
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F2, Ab2, D2, G2), chromatic approaches
bass_notes = [
    (43, 1.5, 0.375),    # F2
    (41, 1.875, 0.375),  # Ab2
    (40, 2.25, 0.375),   # D2
    (43, 2.625, 0.375),  # G2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, resolve on last chord
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    (53, 1.5, 0.375),    # F
    (55, 1.5, 0.375),    # Ab
    (57, 1.5, 0.375),    # C
    (58, 1.5, 0.375),    # D
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (50, 2.25, 0.375),   # Bb
    (52, 2.25, 0.375),   # D
    (53, 2.25, 0.375),   # F
    (55, 2.25, 0.375),   # Ab
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (51, 3.0, 0.375),    # Eb
    (55, 3.0, 0.375),    # G
    (50, 3.0, 0.375),    # Bb
    (58, 3.0, 0.375),    # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, make it sing
# F, Ab, D, Eb
sax_notes = [
    (53, 1.5, 0.375),    # F
    (55, 1.875, 0.375),  # Ab
    (58, 2.25, 0.375),   # D
    (51, 2.625, 0.375),  # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    offset = 3.0 + i * 1.5
    drum_notes = [
        (36, offset + 0.0, 0.375),    # Kick on 1
        (38, offset + 0.375, 0.375),  # Snare on 2
        (42, offset + 0.0, 0.1875),   # Hihat on 1
        (42, offset + 0.1875, 0.1875),# Hihat on &
        (42, offset + 0.375, 0.1875), # Hihat on 2
        (42, offset + 0.5625, 0.1875),# Hihat on &
        (36, offset + 0.75, 0.375),   # Kick on 3
        (38, offset + 1.125, 0.375),  # Snare on 4
        (42, offset + 0.75, 0.1875),  # Hihat on 3
        (42, offset + 0.9375, 0.1875),# Hihat on &
        (42, offset + 1.125, 0.1875), # Hihat on 4
        (42, offset + 1.3125, 0.1875) # Hihat on &
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(2):
    offset = 4.5 + i * 1.5
    drum_notes = [
        (36, offset + 0.0, 0.375),    # Kick on 1
        (38, offset + 0.375, 0.375),  # Snare on 2
        (42, offset + 0.0, 0.1875),   # Hihat on 1
        (42, offset + 0.1875, 0.1875),# Hihat on &
        (42, offset + 0.375, 0.1875), # Hihat on 2
        (42, offset + 0.5625, 0.1875),# Hihat on &
        (36, offset + 0.75, 0.375),   # Kick on 3
        (38, offset + 1.125, 0.375),  # Snare on 4
        (42, offset + 0.75, 0.1875),  # Hihat on 3
        (42, offset + 0.9375, 0.1875),# Hihat on &
        (42, offset + 1.125, 0.1875), # Hihat on 4
        (42, offset + 1.3125, 0.1875) # Hihat on &
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
