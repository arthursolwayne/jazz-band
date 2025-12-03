
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
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38), C (43), chromatic approach to Bb (41)
    (38, 1.5, 0.375),  # F
    (43, 1.875, 0.375), # C
    (41, 2.25, 0.375),  # chromatic approach
    (40, 2.625, 0.375), # bB
    # Bar 3: Bb (41), F (38), chromatic approach to Eb (37)
    (41, 3.0, 0.375),  # Bb
    (38, 3.375, 0.375), # F
    (39, 3.75, 0.375),  # chromatic approach
    (37, 4.125, 0.375), # Eb
    # Bar 4: Eb (37), Bb (41), chromatic approach to Ab (40)
    (37, 4.5, 0.375),  # Eb
    (41, 4.875, 0.375), # Bb
    (40, 5.25, 0.375),  # chromatic approach
    (39, 5.625, 0.375)  # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    (65, 1.5, 0.375),  # F
    (69, 1.5, 0.375),  # A
    (67, 1.5, 0.375),  # C
    (70, 1.5, 0.375),  # E
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    (62, 3.0, 0.375),  # Bb
    (67, 3.0, 0.375),  # D
    (65, 3.0, 0.375),  # F
    (69, 3.0, 0.375),  # Ab
    # Bar 4: Ebmaj7 (Eb, G, Bb, D)
    (64, 4.5, 0.375),  # Eb
    (69, 4.5, 0.375),  # G
    (62, 4.5, 0.375),  # Bb
    (67, 4.5, 0.375)   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
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
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> Eb (64) -> F (65) -> G (67), then space before returning
sax_notes = [
    (65, 1.5, 0.375),  # F
    (64, 1.875, 0.375), # Eb
    (65, 2.25, 0.375),  # F
    (67, 2.625, 0.375), # G
    (65, 4.5, 0.375),  # F (return)
    (64, 4.875, 0.375), # Eb
    (65, 5.25, 0.375),  # F
    (67, 5.625, 0.375)  # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
