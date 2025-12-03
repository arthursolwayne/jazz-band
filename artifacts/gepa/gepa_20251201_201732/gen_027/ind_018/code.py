
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
    (36, 0.0, 0.375),     # Kick on 1
    (38, 0.375, 0.375),   # Snare on 2
    (36, 0.75, 0.375),    # Kick on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 0.0, 1.5),       # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),    # D2 - root
    (40, 1.875, 0.375),  # Eb2 - chromatic approach
    (43, 2.25, 0.375),   # G2 - fifth
    (38, 2.625, 0.375),  # D2 - root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (50, 1.5, 0.375),    # D
    (53, 1.5, 0.375),    # F
    (57, 1.5, 0.375),    # A
    (60, 1.5, 0.375),    # C
    (58, 1.875, 0.375),  # Bb - chromatic passing
    (62, 2.25, 0.375),   # D (root) resolution
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (36, 2.25, 0.375),   # Kick on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 1.5, 1.5),      # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),    # E (Dm7) - start of motif
    (65, 1.875, 0.375),  # G - second note
    (62, 2.25, 0.375),   # E - return to first note
    (67, 2.625, 0.375),  # Bb - resolution
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 3.0, 0.375),    # D2 - root
    (40, 3.375, 0.375),  # Eb2 - chromatic approach
    (43, 3.75, 0.375),   # G2 - fifth
    (38, 4.125, 0.375),  # D2 - root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (57, 3.0, 0.375),    # Bb
    (62, 3.0, 0.375),    # D
    (60, 3.0, 0.375),    # F
    (55, 3.0, 0.375),    # Ab
    (58, 3.375, 0.375),  # Bb (root) resolution
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),    # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (36, 3.75, 0.375),   # Kick on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 3.0, 1.5),      # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - motif variation, leave it hanging
sax_notes = [
    (67, 3.0, 0.375),    # Bb - motif continuation
    (65, 3.375, 0.375),  # G - second note
    (62, 3.75, 0.375),   # E - return to first note
    (65, 4.125, 0.375),  # G - leave it hanging
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5, 0.375),    # D2 - root
    (40, 4.875, 0.375),  # Eb2 - chromatic approach
    (43, 5.25, 0.375),   # G2 - fifth
    (38, 5.625, 0.375),  # D2 - root
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    (62, 4.5, 0.375),    # G
    (67, 4.5, 0.375),    # B
    (65, 4.5, 0.375),    # D
    (60, 4.5, 0.375),    # F
    (62, 4.875, 0.375),  # G (root) resolution
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),    # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (36, 5.25, 0.375),   # Kick on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 4.5, 1.5),      # Hihat on every eighth
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax - finish the motif
sax_notes = [
    (62, 4.5, 0.375),    # G - motif continuation
    (65, 4.875, 0.375),  # B - second note
    (62, 5.25, 0.375),   # G - return to first note
    (65, 5.625, 0.375),  # B - resolution
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
