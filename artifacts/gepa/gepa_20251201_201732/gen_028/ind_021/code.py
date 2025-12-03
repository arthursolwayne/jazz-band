
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
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375),  # F#2 (chromatic approach)
    (43, 2.25, 0.375),  # A2 (fifth)
    (41, 2.625, 0.375),  # G#2 (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    (38, 3.0, 0.375),  # D2
    (40, 3.375, 0.375),  # F#2
    (43, 3.75, 0.375),  # A2
    (41, 4.125, 0.375),  # G#2
    # Bar 4 (4.5 - 6.0s)
    (38, 4.5, 0.375),  # D2
    (40, 4.875, 0.375),  # F#2
    (43, 5.25, 0.375),  # A2
    (41, 5.625, 0.375),  # G#2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (50, 1.5, 0.375),  # D4
    (53, 1.5, 0.375),  # F4
    (57, 1.5, 0.375),  # A4
    (60, 1.5, 0.375),  # C5
    # Bar 3: Gm7 (G-Bb-D-F)
    (62, 3.0, 0.375),  # G4
    (65, 3.0, 0.375),  # Bb4
    (67, 3.0, 0.375),  # D5
    (69, 3.0, 0.375),  # F5
    # Bar 4: Cm7 (C-Eb-G-Bb)
    (60, 4.5, 0.375),  # C4
    (63, 4.5, 0.375),  # Eb4
    (67, 4.5, 0.375),  # G4
    (69, 4.5, 0.375),  # Bb4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - D5 (then resolve on G4)
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375),  # F4
    (67, 2.25, 0.375),  # A4
    (69, 2.625, 0.375),  # D5
    (67, 3.0, 0.375),  # A4
    (65, 3.375, 0.375),  # F4
    (62, 3.75, 0.375),  # D4
    (60, 4.125, 0.375),  # G4 (resolution)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
