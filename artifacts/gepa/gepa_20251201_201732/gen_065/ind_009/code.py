
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375),  # E2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (42, 2.625, 0.375),  # F#2 (chromatic approach)
    (38, 3.0, 0.375),  # D2 (root)
    (40, 3.375, 0.375),  # E2 (chromatic approach)
    (43, 3.75, 0.375),  # G2 (fifth)
    (42, 4.125, 0.375),  # F#2 (chromatic approach)
    (38, 4.5, 0.375),  # D2 (root)
    (40, 4.875, 0.375),  # E2 (chromatic approach)
    (43, 5.25, 0.375),  # G2 (fifth)
    (42, 5.625, 0.375)   # F#2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    (62, 1.5, 0.375), (67, 1.5, 0.375), (71, 1.5, 0.375), (65, 1.5, 0.375),
    # Bar 3: Bm7 (B, D, F#, A)
    (69, 2.25, 0.375), (71, 2.25, 0.375), (67, 2.25, 0.375), (72, 2.25, 0.375),
    # Bar 4: G7 (G, B, D, F)
    (71, 3.0, 0.375), (76, 3.0, 0.375), (74, 3.0, 0.375), (71, 3.0, 0.375),
    # Bar 4 resolution: Cmaj7 (C, E, G, B)
    (60, 3.75, 0.375), (64, 3.75, 0.375), (67, 3.75, 0.375), (71, 3.75, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.375 + 0.375))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.375 + 0.375))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.75 + 0.375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.125 + 0.375))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif
    (62, 1.5, 0.375),  # D4
    (66, 1.875, 0.375),  # F#4
    (69, 2.25, 0.375),  # A4
    # Bar 3: Leave it hanging
    (72, 2.625, 0.375),  # C#5 (suspense)
    # Bar 4: Come back and finish it
    (69, 3.0, 0.375),  # A4
    (66, 3.375, 0.375),  # F#4
    (62, 3.75, 0.375)   # D4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
