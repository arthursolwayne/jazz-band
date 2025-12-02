
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (45, 1.5, 0.375), (46, 1.875, 0.375), (45, 2.25, 0.375), (44, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (46, 3.0, 0.375), (47, 3.375, 0.375), (46, 3.75, 0.375), (45, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (45, 4.5, 0.375), (46, 4.875, 0.375), (45, 5.25, 0.375), (44, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (59, 1.5, 0.375), (60, 1.5, 0.375), (62, 1.5, 0.375), (64, 1.5, 0.375),  # F7 (59, 60, 62, 64)
    (63, 2.25, 0.375), (61, 2.25, 0.375), (60, 2.25, 0.375), (59, 2.25, 0.375),  # F7
    # Bar 3 (3.0 - 4.5s)
    (59, 3.0, 0.375), (60, 3.0, 0.375), (62, 3.0, 0.375), (64, 3.0, 0.375),  # F7
    (63, 3.75, 0.375), (61, 3.75, 0.375), (60, 3.75, 0.375), (59, 3.75, 0.375),  # F7
    # Bar 4 (4.5 - 6.0s)
    (59, 4.5, 0.375), (60, 4.5, 0.375), (62, 4.5, 0.375), (64, 4.5, 0.375),  # F7
    (63, 5.25, 0.375), (61, 5.25, 0.375), (60, 5.25, 0.375), (59, 5.25, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, start it, leave it hanging, finish it
# Melody in F: F - A - Bb - F (bar 2) then F - Bb - A - F (bar 3), ascending again bar 4
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (59, 1.5, 0.375), (62, 1.875, 0.375), (62, 2.25, 0.375), (59, 2.625, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (59, 3.0, 0.375), (60, 3.375, 0.375), (62, 3.75, 0.375), (59, 4.125, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (59, 4.5, 0.375), (62, 4.875, 0.375), (62, 5.25, 0.375), (59, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
