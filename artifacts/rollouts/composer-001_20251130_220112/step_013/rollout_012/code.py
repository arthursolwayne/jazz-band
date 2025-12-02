
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.1875)  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches in D
bass_notes = [
    (62, 1.5, 0.375),    # D
    (63, 1.875, 0.375),  # Eb
    (60, 2.25, 0.375),   # C
    (59, 2.625, 0.375),  # B
    (62, 3.0, 0.375),    # D
    (64, 3.375, 0.375),  # F
    (62, 3.75, 0.375),   # D
    (61, 4.125, 0.375),  # Db
    (62, 4.5, 0.375),    # D
    (63, 4.875, 0.375),  # Eb
    (60, 5.25, 0.375),   # C
    (59, 5.625, 0.375)   # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 in D
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375),    # D
    (67, 1.5, 0.375),    # G
    (69, 1.5, 0.375),    # B
    (64, 1.5, 0.375),    # F
    # Bar 3
    (62, 3.0, 0.375),    # D
    (67, 3.0, 0.375),    # G
    (69, 3.0, 0.375),    # B
    (64, 3.0, 0.375),    # F
    # Bar 4
    (62, 4.5, 0.375),    # D
    (67, 4.5, 0.375),    # G
    (69, 4.5, 0.375),    # B
    (64, 4.5, 0.375)     # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, start it, leave it hanging, finish it
sax_notes = [
    (62, 1.5, 0.375),    # D (start of motif)
    (65, 1.875, 0.375),  # F
    (62, 2.25, 0.375),   # D (return)
    (67, 2.625, 0.375),  # G
    (65, 3.0, 0.375),    # F
    (62, 3.375, 0.375),  # D (finish)
    (64, 3.75, 0.375),   # F
    (62, 4.125, 0.375),  # D
    (65, 4.5, 0.375),    # F
    (67, 4.875, 0.375),  # G
    (65, 5.25, 0.375),   # F
    (62, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = 1.5 + (bar - 2) * 1.5
    drum_notes = [
        (36, start, 0.375),    # Kick on 1
        (42, start, 0.1875),   # Hihat on 1
        (38, start + 0.375, 0.375),  # Snare on 2
        (42, start + 0.375, 0.1875), # Hihat on 2
        (36, start + 0.75, 0.375),   # Kick on 3
        (42, start + 0.75, 0.1875),  # Hihat on 3
        (38, start + 1.125, 0.375),  # Snare on 4
        (42, start + 1.125, 0.1875)  # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
