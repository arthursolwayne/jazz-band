
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

# Marcus: Walking bass line in Dm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375),  # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (38, 2.625, 0.375),  # D2 (root)
    (40, 2.625, 0.375),  # D2 (root)
    (41, 3.0, 0.375),  # E2 (chromatic approach)
    (43, 3.375, 0.375),  # G2 (fifth)
    (38, 3.75, 0.375),  # D2 (root)
    (40, 4.125, 0.375),  # Eb2 (chromatic approach)
    (43, 4.5, 0.375),  # G2 (fifth)
    (38, 4.875, 0.375),  # D2 (root)
    (40, 5.25, 0.375),  # Eb2 (chromatic approach)
    (43, 5.625, 0.375),  # G2 (fifth)
    (38, 6.0, 0.375),  # D2 (root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.5, 0.375),  # F4
    (67, 1.5, 0.375),  # A4
    (69, 1.5, 0.375),  # C5
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    (67, 2.25, 0.375),  # G4
    (71, 2.25, 0.375),  # B4
    (69, 2.25, 0.375),  # D5
    (71, 2.25, 0.375),  # F5
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (60, 3.0, 0.375),  # C4
    (63, 3.0, 0.375),  # Eb4
    (67, 3.0, 0.375),  # G4
    (67, 3.0, 0.375),  # Bb4 (Bb is 67, but you can use Ab for a different color)
])
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5-2.25s
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

# Bar 3: 2.25-3.0s
drum_notes = [
    (36, 2.25, 0.375),  # Kick on 1
    (42, 2.25, 0.375),  # Hihat on 1
    (38, 2.625, 0.375),  # Snare on 2
    (42, 2.625, 0.375),  # Hihat on 2
    (36, 3.0, 0.375),  # Kick on 3
    (42, 3.0, 0.375),  # Hihat on 3
    (38, 3.375, 0.375),  # Snare on 4
    (42, 3.375, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: 3.0-3.75s
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

# You: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bars 2-4: Dm melody (D, F, G, Bb)
# Bar 2: Start motif
sax_notes = [
    (62, 1.5, 0.375),  # D4
    (65, 1.875, 0.375),  # F4
    (67, 2.25, 0.375),  # G4
    (67, 2.625, 0.375),  # Bb4
]
# Bar 3: Leave it hanging
sax_notes.extend([
    (67, 3.0, 0.375),  # G4
])
# Bar 4: Return and finish
sax_notes.extend([
    (62, 3.375, 0.375),  # D4
    (65, 3.75, 0.375),  # F4
    (67, 4.125, 0.375),  # G4
    (67, 4.5, 0.375),  # Bb4
])
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
