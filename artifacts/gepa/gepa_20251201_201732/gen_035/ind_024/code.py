
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # F (root)
    (40, 1.875, 0.375), # G (fifth)
    (39, 2.25, 0.375),  # Gb (chromatic approach)
    (41, 2.625, 0.375), # A (fifth of Bb)
    (43, 3.0, 0.375),   # Bb (root)
    (45, 3.375, 0.375), # C (fifth)
    (44, 3.75, 0.375),  # C# (chromatic approach)
    (46, 4.125, 0.375), # D (fifth of Eb)
    (48, 4.5, 0.375),   # Eb (root)
    (50, 4.875, 0.375), # F (fifth)
    (49, 5.25, 0.375),  # F# (chromatic approach)
    (51, 5.625, 0.375)  # G (fifth of A)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane) - Open voicings, different chords each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (53, 1.5, 0.1875), # F
    (58, 1.5, 0.1875), # A
    (57, 1.5, 0.1875), # C
    (60, 1.5, 0.1875), # E

    # Bar 3: Bb7 (Bb, D, F, Ab)
    (50, 2.25, 0.1875), # Bb
    (55, 2.25, 0.1875), # D
    (53, 2.25, 0.1875), # F
    (57, 2.25, 0.1875), # Ab

    # Bar 4: Ebmaj7 (Eb, G, Bb, D)
    (48, 3.0, 0.1875), # Eb
    (53, 3.0, 0.1875), # G
    (50, 3.0, 0.1875), # Bb
    (58, 3.0, 0.1875), # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums (Little Ray) - 16th note hihat pattern, kick on 1 and 3, snare on 2 and 4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Saxophone (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F -> G -> Eb -> F (sax part)
sax_notes = [
    (62, 1.5, 0.1875), # F
    (65, 1.875, 0.1875), # G
    (59, 2.25, 0.1875), # Eb
    (62, 2.625, 0.1875), # F
    (62, 4.5, 0.1875), # F (return)
    (65, 4.875, 0.1875), # G
    (59, 5.25, 0.1875), # Eb
    (62, 5.625, 0.1875) # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
