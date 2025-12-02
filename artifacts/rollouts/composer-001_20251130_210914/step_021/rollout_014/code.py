
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
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# D minor (D F G A C) with chromatic passing tones
bass_notes = [
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    (64, 3.0, 0.375), (65, 3.375, 0.375), (62, 3.75, 0.375), (64, 4.125, 0.375),
    (67, 4.5, 0.375), (65, 4.875, 0.375), (64, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
# D7 (D F# A C) with some chromatic passing
piano_notes = [
    # Bar 2
    (62, 1.5, 0.375), (67, 1.5, 0.375), (69, 1.5, 0.375), (64, 1.5, 0.375),  # D7
    (63, 2.25, 0.375), (67, 2.25, 0.375), (69, 2.25, 0.375), (64, 2.25, 0.375),  # D7
    # Bar 3
    (62, 3.0, 0.375), (67, 3.0, 0.375), (69, 3.0, 0.375), (65, 3.0, 0.375),  # D7
    (63, 3.75, 0.375), (67, 3.75, 0.375), (70, 3.75, 0.375), (65, 3.75, 0.375),  # D7
    # Bar 4
    (62, 4.5, 0.375), (67, 4.5, 0.375), (69, 4.5, 0.375), (64, 4.5, 0.375),  # D7
    (63, 5.25, 0.375), (67, 5.25, 0.375), (69, 5.25, 0.375), (64, 5.25, 0.375)   # D7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.5 + 0.375)
    # Hihat on every eighth
    for i in range(0, 4):
        hihat = pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    # Add kick and snare
    drums.notes.append(kick1)
    drums.notes.append(kick2)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (67), A (69), C (64) - motif: D -> F# -> A -> C
# Bar 2: Start the motif
sax_notes = [
    (62, 1.5, 0.375), (67, 1.875, 0.375), (69, 2.25, 0.375), (64, 2.625, 0.375),
    # Bar 3: Leave it hanging
    (62, 3.0, 0.375), (67, 3.375, 0.375), (69, 3.75, 0.375),
    # Bar 4: Come back and finish it
    (64, 4.125, 0.375), (62, 4.5, 0.375), (67, 4.875, 0.375), (69, 5.25, 0.375), (64, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
