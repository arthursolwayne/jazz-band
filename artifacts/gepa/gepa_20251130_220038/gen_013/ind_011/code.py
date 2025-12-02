
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Marcus - Bass: Walking line, chromatic approaches
# Dm7: D F A C
# Walking line in D Dorian
bass_notes = [
    # Bar 2
    (62, bar2_start, 0.375),  # D
    (64, bar2_start + 0.375, 0.375),  # Eb
    (62, bar2_start + 0.75, 0.375),  # D
    (60, bar2_start + 1.125, 0.375),  # C
    # Bar 3
    (59, bar3_start, 0.375),  # B
    (62, bar3_start + 0.375, 0.375),  # D
    (64, bar3_start + 0.75, 0.375),  # Eb
    (62, bar3_start + 1.125, 0.375),  # D
    # Bar 4
    (60, bar4_start, 0.375),  # C
    (59, bar4_start + 0.375, 0.375),  # B
    (62, bar4_start + 0.75, 0.375),  # D
    (64, bar4_start + 1.125, 0.375)  # Eb
]
for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Diane - Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Comp on 2 and 4
piano_notes = [
    # Bar 2
    (62, bar2_start + 0.375, 0.375),  # D
    (64, bar2_start + 0.375, 0.375),  # F
    (67, bar2_start + 0.375, 0.375),  # A
    (69, bar2_start + 0.375, 0.375),  # C
    # Bar 3
    (62, bar3_start + 0.375, 0.375),  # D
    (64, bar3_start + 0.375, 0.375),  # F
    (67, bar3_start + 0.375, 0.375),  # A
    (69, bar3_start + 0.375, 0.375),  # C
    # Bar 4
    (62, bar4_start + 0.375, 0.375),  # D
    (64, bar4_start + 0.375, 0.375),  # F
    (67, bar4_start + 0.375, 0.375),  # A
    (69, bar4_start + 0.375, 0.375)   # C
]
for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Little Ray - Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Already handled in Bar 1, now repeat in bars 2-4 with same pattern
for bar in [bar2_start, bar3_start, bar4_start]:
    for note, start, duration in drum_notes:
        new_start = start + bar
        dr = pretty_midi.Note(velocity=100, pitch=note, start=new_start, end=new_start + duration)
        drums.notes.append(dr)

# Dante - Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7: D F A C
# Motif: D - F - A - C, then leave it hanging on A
sax_notes = [
    (62, bar2_start, 0.375),   # D
    (64, bar2_start + 0.375, 0.375),  # F
    (67, bar2_start + 0.75, 0.375),   # A
    (69, bar2_start + 1.125, 0.375),  # C
    (67, bar2_start + 1.5, 0.375),    # A (hanging)
    (62, bar2_start + 3.0, 0.375),    # D (come back)
    (64, bar2_start + 3.375, 0.375),  # F
    (67, bar2_start + 3.75, 0.375),   # A
    (69, bar2_start + 4.125, 0.375)   # C
]
for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
