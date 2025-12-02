
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
    (36, 1.0, 0.5),    # Kick on beat 1
    (42, 1.0, 0.25),   # Hihat on 1 & 2
    (42, 1.25, 0.25),
    (38, 1.5, 0.5),    # Snare on beat 3
    (42, 1.5, 0.25),   # Hihat on 3 & 4
    (42, 1.75, 0.25)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (13, 1.5, 0.5),    # Fm7 - F (13) on beat 1
    (12, 2.0, 0.5),    # E (12) on beat 2
    (11, 2.5, 0.5),    # D (11) on beat 3
    (9, 3.0, 0.5),     # C (9) on beat 4
    (10, 3.5, 0.5),    # C# (10) on beat 1
    (12, 4.0, 0.5),    # E (12) on beat 2
    (13, 4.5, 0.5),    # F (13) on beat 3
    (15, 5.0, 0.5),    # G (15) on beat 4
    (14, 5.5, 0.5),    # G# (14) on beat 1
    (13, 6.0, 0.5)     # F (13) on beat 2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (15, 2.0, 0.25),  # G7 - G (15)
    (12, 2.0, 0.25),  # E (12)
    (10, 2.0, 0.25),  # C# (10)
    (9, 2.0, 0.25),   # C (9)
    (15, 3.0, 0.25),  # G7 - G (15)
    (12, 3.0, 0.25),  # E (12)
    (10, 3.0, 0.25),  # C# (10)
    (9, 3.0, 0.25),   # C (9)
    # Bar 3
    (10, 4.0, 0.25),  # C#7
    (7, 4.0, 0.25),   # A (7)
    (5, 4.0, 0.25),   # F# (5)
    (4, 4.0, 0.25),   # F (4)
    (10, 5.0, 0.25),  # C#7
    (7, 5.0, 0.25),   # A (7)
    (5, 5.0, 0.25),   # F# (5)
    (4, 5.0, 0.25),   # F (4)
    # Bar 4
    (15, 6.0, 0.25),  # G7
    (12, 6.0, 0.25),  # E
    (10, 6.0, 0.25),  # C#
    (9, 6.0, 0.25),   # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): Melody - sparse, expressive, with dynamic variation
sax_notes = [
    (13, 2.0, 0.5),    # F (13) - start of motif
    (10, 2.5, 0.5),    # C# (10)
    (13, 3.0, 0.5),    # F (13) - return
    (11, 3.5, 0.5),    # D (11)
    (9, 4.0, 0.5),     # C (9)
    (13, 4.5, 0.5),    # F (13)
    (11, 5.0, 0.5),    # D (11)
    (10, 5.5, 0.5),    # C# (10)
    (13, 6.0, 0.5)     # F (13) - end of motif
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110 if start >= 2.0 and start < 3.0 else 70, pitch=note, start=start, end=start + duration))

# Drums for Bars 2-4
drum_notes = [
    (36, 2.0, 0.5),    # Kick on beat 1
    (42, 2.0, 0.25),   # Hihat on 1 & 2
    (42, 2.25, 0.25),
    (38, 2.5, 0.5),    # Snare on beat 3
    (42, 2.5, 0.25),   # Hihat on 3 & 4
    (42, 2.75, 0.25),
    (36, 3.0, 0.5),    # Kick on beat 1
    (42, 3.0, 0.25),   # Hihat on 1 & 2
    (42, 3.25, 0.25),
    (38, 3.5, 0.5),    # Snare on beat 3
    (42, 3.5, 0.25),   # Hihat on 3 & 4
    (42, 3.75, 0.25),
    (36, 4.0, 0.5),    # Kick on beat 1
    (42, 4.0, 0.25),   # Hihat on 1 & 2
    (42, 4.25, 0.25),
    (38, 4.5, 0.5),    # Snare on beat 3
    (42, 4.5, 0.25),   # Hihat on 3 & 4
    (42, 4.75, 0.25),
    (36, 5.0, 0.5),    # Kick on beat 1
    (42, 5.0, 0.25),   # Hihat on 1 & 2
    (42, 5.25, 0.25),
    (38, 5.5, 0.5),    # Snare on beat 3
    (42, 5.5, 0.25),   # Hihat on 3 & 4
    (42, 5.75, 0.25),
    (36, 6.0, 0.5)     # Kick on beat 2
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
