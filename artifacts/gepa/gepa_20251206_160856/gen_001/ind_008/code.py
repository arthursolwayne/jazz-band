
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.75),  # Hihat on 1 & 2
    (36, 0.75, 0.375),  # Kick on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 0.75, 1.5),  # Hihat on 3 & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375),  # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (41, 2.625, 0.375),  # Ab2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 0.375),  # F (root)
    (60, 1.5, 0.375),  # C (major 7)
    (64, 1.5, 0.375),  # G (octave)
    (65, 1.5, 0.375),  # Ab (minor 7)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Dm7 (D, F, A, C)
piano_notes = [
    (62, 3.0, 0.375),  # D
    (65, 3.0, 0.375),  # F
    (67, 3.0, 0.375),  # A
    (69, 3.0, 0.375),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Gm7 (G, Bb, D, F)
piano_notes = [
    (67, 4.5, 0.375),  # G
    (71, 4.5, 0.375),  # Bb
    (69, 4.5, 0.375),  # D
    (64, 4.5, 0.375),  # F
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
sax_notes = [
    (53, 1.5, 0.375),  # F
    (55, 1.875, 0.375),  # G
    (58, 2.25, 0.375),  # A
    (60, 2.625, 0.375),  # Bb
    (53, 3.0, 0.375),  # F (return)
    (58, 3.375, 0.375),  # A
    (60, 3.75, 0.375),  # Bb
    (62, 4.125, 0.375),  # C
    (53, 4.5, 0.375),  # F (resolve)
    (55, 4.875, 0.375),  # G
    (58, 5.25, 0.375),  # A
    (60, 5.625, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums continue for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 2.25),  # Hihat on 1 & 2
    (36, 2.25, 0.375),  # Kick on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.25, 3.0),  # Hihat on 3 & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 3.75),  # Hihat on 1 & 2
    (36, 3.75, 0.375),  # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.75, 4.5),  # Hihat on 3 & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 5.25),  # Hihat on 1 & 2
    (36, 5.25, 0.375),  # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.25, 6.0),  # Hihat on 3 & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
