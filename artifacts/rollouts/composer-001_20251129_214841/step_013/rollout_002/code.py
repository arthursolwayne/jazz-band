
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.5),     # Kick on 1
    (42, 0.0, 0.5),     # Hihat on 1
    (38, 0.5, 0.5),     # Snare on 2
    (42, 0.5, 0.5),     # Hihat on 2
    (36, 1.0, 0.5),     # Kick on 3
    (42, 1.0, 0.5),     # Hihat on 3
    (38, 1.5, 0.5),     # Snare on 4
    (42, 1.5, 0.5)      # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bassline: Walking line in C, chromatic approaches
bass_notes = [
    (60, 1.5, 0.5),     # C
    (61, 2.0, 0.5),     # C#
    (62, 2.5, 0.5),     # D
    (63, 3.0, 0.5),     # D#
    (64, 3.5, 0.5),     # E
    (65, 4.0, 0.5),     # F
    (66, 4.5, 0.5),     # F#
    (67, 5.0, 0.5),     # G
    (68, 5.5, 0.5),     # G#
    (69, 6.0, 0.5)      # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (60, 2.0, 0.5),     # C7: C, E, B
    (64, 2.0, 0.5),
    (69, 2.0, 0.5),
    # Bar 3
    (60, 3.0, 0.5),
    (64, 3.0, 0.5),
    (69, 3.0, 0.5),
    # Bar 4
    (60, 4.0, 0.5),
    (64, 4.0, 0.5),
    (69, 4.0, 0.5)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Motif (C, E, B, D) - short, singable, leave it hanging
sax_notes = [
    (60, 1.5, 0.5),     # C
    (64, 2.0, 0.5),     # E
    (69, 2.5, 0.5),     # B
    (67, 3.0, 0.5),     # D
    (60, 4.5, 0.5),     # C (return)
    (64, 5.0, 0.5),     # E
    (69, 5.5, 0.5),     # B
    (67, 6.0, 0.5)      # D (end on D)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue for full 4 bars
drum_notes = [
    (36, 1.5, 0.5),     # Kick on 1
    (42, 1.5, 0.5),     # Hihat on 1
    (38, 2.0, 0.5),     # Snare on 2
    (42, 2.0, 0.5),     # Hihat on 2
    (36, 2.5, 0.5),     # Kick on 3
    (42, 2.5, 0.5),     # Hihat on 3
    (38, 3.0, 0.5),     # Snare on 4
    (42, 3.0, 0.5),     # Hihat on 4
    (36, 3.5, 0.5),     # Kick on 1
    (42, 3.5, 0.5),     # Hihat on 1
    (38, 4.0, 0.5),     # Snare on 2
    (42, 4.0, 0.5),     # Hihat on 2
    (36, 4.5, 0.5),     # Kick on 3
    (42, 4.5, 0.5),     # Hihat on 3
    (38, 5.0, 0.5),     # Snare on 4
    (42, 5.0, 0.5),     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
