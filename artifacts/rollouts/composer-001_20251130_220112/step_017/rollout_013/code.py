
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), (63, 1.875, 0.375), (64, 2.25, 0.375), (65, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (65, 3.0, 0.375), (64, 3.375, 0.375), (63, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375), (63, 4.875, 0.375), (64, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (67, 1.875, 0.375), (69, 1.875, 0.375), (71, 1.875, 0.375), (74, 1.875, 0.375),  # D7
    (67, 2.625, 0.375), (69, 2.625, 0.375), (71, 2.625, 0.375), (74, 2.625, 0.375),  # D7
    # Bar 3 (3.0 - 4.5s)
    (67, 3.875, 0.375), (69, 3.875, 0.375), (71, 3.875, 0.375), (74, 3.875, 0.375),  # D7
    (67, 4.625, 0.375), (69, 4.625, 0.375), (71, 4.625, 0.375), (74, 4.625, 0.375),  # D7
    # Bar 4 (4.5 - 6.0s)
    (67, 5.875, 0.375), (69, 5.875, 0.375), (71, 5.875, 0.375), (74, 5.875, 0.375)   # D7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick_start = bar_start + 0.0
    kick_start_2 = bar_start + 1.125
    # Snare on 2 and 4
    snare_start = bar_start + 0.375
    snare_start_2 = bar_start + 1.5
    # Hihat on every eighth
    hihat_notes = [
        (bar_start + 0.0, 0.1875), (bar_start + 0.1875, 0.1875),
        (bar_start + 0.375, 0.1875), (bar_start + 0.5625, 0.1875),
        (bar_start + 0.75, 0.1875), (bar_start + 0.9375, 0.1875),
        (bar_start + 1.125, 0.1875), (bar_start + 1.3125, 0.1875),
        (bar_start + 1.5, 0.1875)
    ]
    for start, duration in hihat_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + duration))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start_2, end=kick_start_2 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start_2, end=snare_start_2 + 0.375))

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Bar 2 (1.5 - 3.0s): Start motif
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375), (66, 1.875, 0.375), (67, 2.25, 0.375), (65, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s): Leave it hanging
    (67, 3.75, 0.375),
    # Bar 4 (4.5 - 6.0s): Come back and finish it
    (62, 4.5, 0.375), (66, 4.875, 0.375), (67, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
