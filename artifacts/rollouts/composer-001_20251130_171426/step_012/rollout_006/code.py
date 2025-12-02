
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
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    (36, bar1_start, 0.375),  # Kick on 1
    (38, bar1_start + 0.375, 0.375),  # Snare on 2
    (42, bar1_start, 0.75),  # Hihat on 1 & 2
    (42, bar1_start + 0.375, 0.75),
    (36, bar1_start + 0.75, 0.375),  # Kick on 3
    (38, bar1_start + 1.125, 0.375),  # Snare on 4
    (42, bar1_start + 0.75, 0.75),  # Hihat on 3 & 4
    (42, bar1_start + 1.125, 0.75)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet

# Bass: Marcus, walking line, chromatic approaches, Dm7 chord (D F A C)
# Bar 2: D, F, E, G
# Bar 3: A, Bb, B, C
# Bar 4: D, F, E, G (reprise)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

bass_notes = [
    (62, bar2_start, 0.375),  # D
    (65, bar2_start + 0.375, 0.375),  # F
    (64, bar2_start + 0.75, 0.375),  # E
    (67, bar2_start + 1.125, 0.375),  # G

    (67, bar3_start, 0.375),  # A
    (66, bar3_start + 0.375, 0.375),  # Bb
    (68, bar3_start + 0.75, 0.375),  # B
    (69, bar3_start + 1.125, 0.375),  # C

    (62, bar4_start, 0.375),  # D
    (65, bar4_start + 0.375, 0.375),  # F
    (64, bar4_start + 0.75, 0.375),  # E
    (67, bar4_start + 1.125, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Diane, 7th chords, comp on 2 and 4 (Dm7, G7, Cm7, F7)
# Bar 2: Dm7 (D F A C)
# Bar 3: G7 (G B D F)
# Bar 4: Cm7 (C Eb G Bb)
# Bar 2: comp on 2 and 4
# Bar 3: comp on 2 and 4
# Bar 4: comp on 2 and 4

# Bar 2
piano_notes = [
    (62, bar2_start + 0.375, 0.375),  # D
    (65, bar2_start + 0.375, 0.375),  # F
    (67, bar2_start + 0.375, 0.375),  # A
    (69, bar2_start + 0.375, 0.375),  # C
    (65, bar2_start + 1.125, 0.375),  # F
    (67, bar2_start + 1.125, 0.375),  # A
    (69, bar2_start + 1.125, 0.375),  # C
    (64, bar2_start + 1.125, 0.375),  # D

    # Bar 3
    (67, bar3_start + 0.375, 0.375),  # G
    (71, bar3_start + 0.375, 0.375),  # B
    (69, bar3_start + 0.375, 0.375),  # D
    (71, bar3_start + 0.375, 0.375),  # F
    (69, bar3_start + 1.125, 0.375),  # D
    (71, bar3_start + 1.125, 0.375),  # F
    (67, bar3_start + 1.125, 0.375),  # G
    (72, bar3_start + 1.125, 0.375),  # B

    # Bar 4
    (60, bar4_start + 0.375, 0.375),  # C
    (63, bar4_start + 0.375, 0.375),  # Eb
    (67, bar4_start + 0.375, 0.375),  # G
    (71, bar4_start + 0.375, 0.375),  # Bb
    (63, bar4_start + 1.125, 0.375),  # Eb
    (67, bar4_start + 1.125, 0.375),  # G
    (71, bar4_start + 1.125, 0.375),  # Bb
    (60, bar4_start + 1.125, 0.375)   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante, short motif in Dm, start it, leave it hanging, come back and finish it
# Motif: D (G) F (E) D (Bb) C (C)
# Bar 2: D, F, D, C (motif start)
# Bar 3: G, E, Bb, C (motif continuation)
# Bar 4: D, F, D, C (motif resolution)

sax_notes = [
    (62, bar2_start, 0.375),  # D
    (65, bar2_start + 0.375, 0.375),  # F
    (62, bar2_start + 0.75, 0.375),  # D
    (60, bar2_start + 1.125, 0.375),  # C

    (67, bar3_start, 0.375),  # G
    (64, bar3_start + 0.375, 0.375),  # E
    (60, bar3_start + 0.75, 0.375),  # Bb
    (60, bar3_start + 1.125, 0.375),  # C

    (62, bar4_start, 0.375),  # D
    (65, bar4_start + 0.375, 0.375),  # F
    (62, bar4_start + 0.75, 0.375),  # D
    (60, bar4_start + 1.125, 0.375)  # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
bar2_drum_notes = [
    (36, bar2_start, 0.375),  # Kick on 1
    (38, bar2_start + 0.375, 0.375),  # Snare on 2
    (42, bar2_start, 0.75),  # Hihat on 1 & 2
    (42, bar2_start + 0.375, 0.75),
    (36, bar2_start + 0.75, 0.375),  # Kick on 3
    (38, bar2_start + 1.125, 0.375),  # Snare on 4
    (42, bar2_start + 0.75, 0.75),  # Hihat on 3 & 4
    (42, bar2_start + 1.125, 0.75)
]
for note, start, duration in bar2_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
bar3_drum_notes = [
    (36, bar3_start, 0.375),  # Kick on 1
    (38, bar3_start + 0.375, 0.375),  # Snare on 2
    (42, bar3_start, 0.75),  # Hihat on 1 & 2
    (42, bar3_start + 0.375, 0.75),
    (36, bar3_start + 0.75, 0.375),  # Kick on 3
    (38, bar3_start + 1.125, 0.375),  # Snare on 4
    (42, bar3_start + 0.75, 0.75),  # Hihat on 3 & 4
    (42, bar3_start + 1.125, 0.75)
]
for note, start, duration in bar3_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
bar4_drum_notes = [
    (36, bar4_start, 0.375),  # Kick on 1
    (38, bar4_start + 0.375, 0.375),  # Snare on 2
    (42, bar4_start, 0.75),  # Hihat on 1 & 2
    (42, bar4_start + 0.375, 0.75),
    (36, bar4_start + 0.75, 0.375),  # Kick on 3
    (38, bar4_start + 1.125, 0.375),  # Snare on 4
    (42, bar4_start + 0.75, 0.75),  # Hihat on 3 & 4
    (42, bar4_start + 1.125, 0.75)
]
for note, start, duration in bar4_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
