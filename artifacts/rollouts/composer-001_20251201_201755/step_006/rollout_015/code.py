
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
    (42, 1.5, 0.0)  # Hihat off
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375),  # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (41, 2.625, 0.375)  # F2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
piano_notes = [
    (65, 1.5, 0.375),  # F4
    (69, 1.5, 0.375),  # A4
    (67, 1.5, 0.375),  # C5
    (70, 1.5, 0.375),  # E5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Start motif (F Bb D)
sax_notes = [
    (65, 1.5, 0.25),  # F4
    (67, 1.75, 0.25),  # Bb4
    (69, 2.0, 0.25),  # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (Bb2-D2), roots and fifths with chromatic approaches
bass_notes = [
    (42, 3.0, 0.375),  # Bb2 (root)
    (43, 3.375, 0.375),  # C2 (chromatic approach)
    (46, 3.75, 0.375),  # D2 (fifth)
    (44, 4.125, 0.375)  # C2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Bb7 (Bb D F A)
piano_notes = [
    (62, 3.0, 0.375),  # Bb4
    (67, 3.0, 0.375),  # D5
    (65, 3.0, 0.375),  # F5
    (69, 3.0, 0.375),  # A5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif
sax_notes = [
    (62, 3.0, 0.25),  # Bb4
    (65, 3.25, 0.25),  # D5
    (67, 3.5, 0.25),  # F5
    (69, 3.75, 0.25),  # A5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-A2), roots and fifths with chromatic approaches
bass_notes = [
    (38, 4.5, 0.375),  # F2 (root)
    (40, 4.875, 0.375),  # G2 (chromatic approach)
    (43, 5.25, 0.375),  # A2 (fifth)
    (41, 5.625, 0.375)  # G2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: F7 (F A C E)
piano_notes = [
    (65, 4.5, 0.375),  # F4
    (69, 4.5, 0.375),  # A4
    (67, 4.5, 0.375),  # C5
    (70, 4.5, 0.375),  # E5
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Finish motif (F Bb D)
sax_notes = [
    (65, 4.5, 0.25),  # F4
    (67, 4.75, 0.25),  # Bb4
    (69, 5.0, 0.25),  # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
    (42, 6.0, 0.0)  # Hihat off
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
