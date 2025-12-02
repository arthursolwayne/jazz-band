
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.375), (36, 1.125, 0.375),
    # Snare on 2 and 4
    (38, 0.75, 0.375), (38, 1.875, 0.375),
    # Hihat on every eighth
    (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875),
    (42, 1.125, 0.1875), (42, 1.3125, 0.1875),
    (42, 1.5, 0.1875),
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (60, 2.25, 0.375), (64, 2.25, 0.375), (67, 2.25, 0.375),
    # Bar 3: C7 on beat 4
    (60, 3.75, 0.375), (64, 3.75, 0.375), (67, 3.75, 0.375),
    # Bar 4: C7 on beat 2 and 4
    (60, 5.25, 0.375), (64, 5.25, 0.375), (67, 5.25, 0.375),
    (60, 5.625, 0.375), (64, 5.625, 0.375), (67, 5.625, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375), # E
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    # Bar 3: Let it hang
    (60, 3.0, 0.375),  # C
    (60, 3.375, 0.375), # C
    # Bar 4: Come back and finish it
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375), # E
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375), # C
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: Full bar 2-4
drum_notes_2_4 = [
    # Kick on 1 and 3 for each bar
    (36, 1.5, 0.375), (36, 2.625, 0.375), (36, 3.75, 0.375), (36, 4.875, 0.375),
    # Snare on 2 and 4 for each bar
    (38, 1.875, 0.375), (38, 3.0, 0.375), (38, 4.125, 0.375), (38, 5.25, 0.375),
    # Hihat on every eighth
    (42, 1.5, 0.1875), (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875), (42, 2.8125, 0.1875),
    (42, 3.0, 0.1875), (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    (42, 4.5, 0.1875), (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875),
    (42, 6.0, 0.1875),
]
for note in drum_notes_2_4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
