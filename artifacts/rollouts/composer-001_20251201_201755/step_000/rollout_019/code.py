
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.75), # Hihat on 2
    (36, 0.75, 1.125), # Kick on 3
    (42, 1.125, 1.5)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root) on 1
    (42, 1.875, 0.375), # F2 (fifth of Dm) on 2
    (40, 2.25, 0.375),  # Eb2 (chromatic approach to D) on 3
    (38, 2.625, 0.375), # D2 (root) on 4
    (43, 2.625, 0.375), # G2 (fifth) on 4
    (40, 3.0, 0.375),   # Eb2 on 1
    (38, 3.375, 0.375), # D2 on 2
    (42, 3.75, 0.375),  # F2 on 3
    (40, 4.125, 0.375), # Eb2 on 4
    (38, 4.5, 0.375),   # D2 on 1
    (42, 4.875, 0.375), # F2 on 2
    (40, 5.25, 0.375),  # Eb2 on 3
    (38, 5.625, 0.375)  # D2 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (50, 1.5, 0.375),  # D
    (53, 1.5, 0.375),  # F
    (57, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C
    # Bar 3: G7 (G, B, D, F)
    (55, 2.25, 0.375), # G
    (58, 2.25, 0.375), # B
    (62, 2.25, 0.375), # D
    (60, 2.25, 0.375), # F
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0, 0.375),  # C
    (63, 3.0, 0.375),  # Eb
    (67, 3.0, 0.375),  # G
    (67, 3.0, 0.375),  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (42, 1.875, 0.375), # Hihat on 2
    (38, 1.875, 0.375), # Snare on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (42, 2.625, 0.375), # Hihat on 4
    (38, 2.625, 0.375), # Snare on 4
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.375),   # Hihat on 1
    (42, 3.375, 0.375), # Hihat on 2
    (38, 3.375, 0.375), # Snare on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (42, 4.125, 0.375), # Hihat on 4
    (38, 4.125, 0.375), # Snare on 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.375),   # Hihat on 1
    (42, 4.875, 0.375), # Hihat on 2
    (38, 4.875, 0.375), # Snare on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (42, 5.625, 0.375), # Hihat on 4
    (38, 5.625, 0.375)  # Snare on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    (62, 1.5, 0.375),  # E4 on 1
    (64, 1.875, 0.375), # F#4 on 2
    (62, 2.25, 0.375),  # E4 on 3
    (60, 2.625, 0.375), # D4 on 4
    (62, 3.0, 0.375),   # E4 on 1
    (64, 3.375, 0.375), # F#4 on 2
    (62, 3.75, 0.375),  # E4 on 3
    (60, 4.125, 0.375), # D4 on 4
    (62, 4.5, 0.375),   # E4 on 1
    (64, 4.875, 0.375), # F#4 on 2
    (62, 5.25, 0.375),  # E4 on 3
    (60, 5.625, 0.375)  # D4 on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
