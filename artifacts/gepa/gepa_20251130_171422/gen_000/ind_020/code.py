
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875), (42, 1.5, 0.1875)
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Dm7 chord (D, F, A, C)
    (62, 1.5, 0.375), (60, 1.875, 0.375), (63, 2.25, 0.375), (61, 2.625, 0.375),
    # Bar 3: Chromatic approach to G
    (64, 3.0, 0.375), (63, 3.375, 0.375), (62, 3.75, 0.375), (61, 4.125, 0.375),
    # Bar 4: Dm7 again
    (62, 4.5, 0.375), (60, 4.875, 0.375), (63, 5.25, 0.375), (61, 5.625, 0.375)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    (62, 1.5, 0.375), (60, 1.5, 0.375), (63, 1.5, 0.375), (61, 1.5, 0.375),
    (62, 1.875, 0.375), (60, 1.875, 0.375), (63, 1.875, 0.375), (61, 1.875, 0.375),
    # Bar 3: F7 (F, A, C, E)
    (60, 3.0, 0.375), (63, 3.0, 0.375), (61, 3.0, 0.375), (64, 3.0, 0.375),
    (60, 3.375, 0.375), (63, 3.375, 0.375), (61, 3.375, 0.375), (64, 3.375, 0.375),
    # Bar 4: Dm7 again
    (62, 4.5, 0.375), (60, 4.5, 0.375), (63, 4.5, 0.375), (61, 4.5, 0.375),
    (62, 4.875, 0.375), (60, 4.875, 0.375), (63, 4.875, 0.375), (61, 4.875, 0.375)
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note[0], start=note[1], end=note[2]))

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> F7 -> Dm7
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # F
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375),  # C
    (62, 3.0, 0.375),  # D
    (64, 3.375, 0.375),  # F
    (66, 3.75, 0.375),  # G
    (65, 4.125, 0.375),  # G#
    (62, 4.5, 0.375),  # D
    (64, 4.875, 0.375),  # F
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375)   # C
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick_start = start + 0.0
    snare_start = start + 0.375
    hihat_start1 = start + 0.1875
    hihat_start2 = start + 0.375
    hihat_start3 = start + 0.5625
    hihat_start4 = start + 0.75
    hihat_start5 = start + 0.9375
    hihat_start6 = start + 1.125
    hihat_start7 = start + 1.3125
    hihat_start8 = start + 1.5

    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start1, end=hihat_start1 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start2, end=hihat_start2 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start3, end=hihat_start3 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start4, end=hihat_start4 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start5, end=hihat_start5 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start6, end=hihat_start6 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start7, end=hihat_start7 + 0.1875))
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=hihat_start8, end=hihat_start8 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
