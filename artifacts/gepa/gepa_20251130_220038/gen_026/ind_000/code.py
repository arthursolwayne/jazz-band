
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.375),     # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.375),   # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.375),    # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (36, 1.5, 0.375),     # F (root)
    (37, 1.875, 0.375),   # Gb (chromatic approach)
    (38, 2.25, 0.375),    # G (3rd)
    (39, 2.625, 0.375),   # Ab (chromatic)
    (40, 3.0, 0.375),     # A (5th)
    (41, 3.375, 0.375),   # Bb (chromatic)
    (42, 3.75, 0.375),    # B (7th)
    (43, 4.125, 0.375),   # C (chromatic)
    (44, 4.5, 0.375),     # C# (9th)
    (45, 4.875, 0.375),   # D (chromatic)
    (46, 5.25, 0.375),    # D# (11th)
    (47, 5.625, 0.375),   # E (chromatic)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (43, 2.25, 0.375),    # B7 (2nd beat)
    (46, 2.25, 0.375),
    (48, 2.25, 0.375),
    (50, 2.25, 0.375),
    (43, 3.75, 0.375),    # B7 (4th beat)
    (46, 3.75, 0.375),
    (48, 3.75, 0.375),
    (50, 3.75, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.375),     # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.375),   # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.375),    # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.375),   # Hihat on 4
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.375),     # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.375),   # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.375),    # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.375),   # Hihat on 4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.375),     # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.375),   # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.375),    # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.375),   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Whisper -> cry. One short motif, start it, leave it hanging, come back and finish
sax_notes = [
    (46, 1.5, 0.375),     # D
    (48, 1.875, 0.375),   # E (rest on 2)
    (43, 2.25, 0.375),    # B on 3
    (48, 2.625, 0.375),   # E on 4
    (43, 3.0, 0.375),     # B on 1
    (46, 3.375, 0.375),   # D on 2
    (48, 3.75, 0.375),    # E on 3
    (50, 4.125, 0.375),   # F on 4
    (48, 4.5, 0.375),     # E on 1
    (43, 4.875, 0.375),   # B on 2
    (46, 5.25, 0.375),    # D on 3
    (50, 5.625, 0.375),   # F on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
