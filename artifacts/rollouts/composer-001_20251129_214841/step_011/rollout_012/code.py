
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
# Saxophone: Tenor sax motif
sax_notes = [
    # Bar 2
    (62, 1.5, 0.25),  # C5
    (65, 1.75, 0.25),  # E5
    (64, 2.0, 0.25),  # D5
    (62, 2.25, 0.25),  # C5
    # Bar 3
    (62, 2.5, 0.25),  # C5
    (67, 2.75, 0.25),  # G5
    (64, 3.0, 0.25),  # D5
    (62, 3.25, 0.25),  # C5
    # Bar 4
    (62, 3.5, 0.25),  # C5
    (67, 3.75, 0.25),  # G5
    (69, 4.0, 0.25),  # B5
    (67, 4.25, 0.25),  # G5
    (64, 4.5, 0.25),  # D5
    (62, 4.75, 0.25),  # C5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in C
bass_notes = [
    # Bar 2
    (49, 1.5, 0.25),  # C3
    (50, 1.75, 0.25),  # D3
    (48, 2.0, 0.25),  # B2
    (49, 2.25, 0.25),  # C3
    # Bar 3
    (50, 2.5, 0.25),  # D3
    (51, 2.75, 0.25),  # E3
    (50, 3.0, 0.25),  # D3
    (49, 3.25, 0.25),  # C3
    # Bar 4
    (49, 3.5, 0.25),  # C3
    (50, 3.75, 0.25),  # D3
    (52, 4.0, 0.25),  # F3
    (51, 4.25, 0.25),  # E3
    (50, 4.5, 0.25),  # D3
    (49, 4.75, 0.25),  # C3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.75, 0.25),  # C7 (C-E-G-B)
    (64, 1.75, 0.25),
    (67, 1.75, 0.25),
    (71, 1.75, 0.25),
    # Bar 3
    (60, 2.75, 0.25),
    (64, 2.75, 0.25),
    (67, 2.75, 0.25),
    (71, 2.75, 0.25),
    # Bar 4
    (60, 3.75, 0.25),
    (64, 3.75, 0.25),
    (67, 3.75, 0.25),
    (71, 3.75, 0.25),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
    # Bar 3
    (36, 2.875, 0.375),  # Kick on 1
    (42, 2.875, 0.375),  # Hihat on 1
    (38, 3.25, 0.375),  # Snare on 2
    (42, 3.25, 0.375),  # Hihat on 2
    (36, 3.625, 0.375),  # Kick on 3
    (42, 3.625, 0.375),  # Hihat on 3
    (38, 4.0, 0.375),  # Snare on 4
    (42, 4.0, 0.375),  # Hihat on 4
    # Bar 4
    (36, 4.25, 0.375),  # Kick on 1
    (42, 4.25, 0.375),  # Hihat on 1
    (38, 4.625, 0.375),  # Snare on 2
    (42, 4.625, 0.375),  # Hihat on 2
    (36, 5.0, 0.375),  # Kick on 3
    (42, 5.0, 0.375),  # Hihat on 3
    (38, 5.375, 0.375),  # Snare on 4
    (42, 5.375, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
