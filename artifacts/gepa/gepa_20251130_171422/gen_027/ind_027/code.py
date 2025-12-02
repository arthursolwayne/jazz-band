
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (36, 0.0, 1.0),     # Kick on beat 1
    (42, 0.125, 0.25),  # Hihat on 1&
    (38, 0.5, 1.0),     # Snare on beat 2
    (42, 0.625, 0.75),  # Hihat on 2&
    (36, 1.0, 1.5),     # Kick on beat 3
    (42, 1.125, 1.25),  # Hihat on 3&
    (38, 1.5, 1.5),     # Snare on beat 4
    (42, 1.625, 1.75)
]
for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line with chromatic approach
bass_notes = [
    (37, 1.5, 1.75),    # D
    (38, 1.75, 2.0),    # D#
    (39, 2.0, 2.25),    # E
    (37, 2.25, 2.5),    # D
    (36, 2.5, 2.75),    # C
    (37, 2.75, 3.0),    # D
]
for note, start, end in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(n)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 1.75),    # F7 (F, A, C, E)
    (64, 1.5, 1.75),
    (65, 1.5, 1.75),
    (67, 1.5, 1.75),
    (64, 2.0, 2.25),    # F7 on beat 2
    (66, 2.0, 2.25),
    (67, 2.0, 2.25),
    (69, 2.0, 2.25)
]
for note, start, end in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(n)

# Dante on sax: sparse, expressive motif
sax_notes = [
    (66, 1.5, 1.75),    # G
    (68, 2.0, 2.25),    # A
    (69, 2.5, 2.75),    # Bb
    (66, 3.0, 3.25),    # G
]
for note, start, end in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line with chromatic approach
bass_notes = [
    (39, 3.0, 3.25),    # E
    (40, 3.25, 3.5),    # F
    (41, 3.5, 3.75),    # F#
    (39, 3.75, 4.0),    # E
    (38, 4.0, 4.25),    # D#
    (39, 4.25, 4.5),    # E
]
for note, start, end in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(n)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.0, 3.25),    # F7 (F, A, C, E)
    (64, 3.0, 3.25),
    (65, 3.0, 3.25),
    (67, 3.0, 3.25),
    (64, 3.5, 3.75),    # F7 on beat 2
    (66, 3.5, 3.75),
    (67, 3.5, 3.75),
    (69, 3.5, 3.75)
]
for note, start, end in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(n)

# Dante on sax: sparse, expressive motif
sax_notes = [
    (68, 3.0, 3.25),    # A
    (69, 3.5, 3.75),    # Bb
    (67, 4.0, 4.25),    # G
    (65, 4.5, 4.75),    # E
]
for note, start, end in sax_notes:
    n = pretty_midi.Note(velocity=105, pitch=note, start=start, end=end)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line with chromatic approach
bass_notes = [
    (41, 4.5, 4.75),    # F#
    (42, 4.75, 5.0),    # G
    (43, 5.0, 5.25),    # G#
    (41, 5.25, 5.5),    # F#
    (40, 5.5, 5.75),    # F
    (41, 5.75, 6.0),    # F#
]
for note, start, end in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    bass.notes.append(n)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.5, 4.75),    # F7 (F, A, C, E)
    (64, 4.5, 4.75),
    (65, 4.5, 4.75),
    (67, 4.5, 4.75),
    (64, 5.0, 5.25),    # F7 on beat 2
    (66, 5.0, 5.25),
    (67, 5.0, 5.25),
    (69, 5.0, 5.25)
]
for note, start, end in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=end)
    piano.notes.append(n)

# Dante on sax: sparse, expressive motif
sax_notes = [
    (65, 4.5, 4.75),    # E
    (67, 5.0, 5.25),    # G
    (64, 5.5, 5.75),    # F
    (62, 6.0, 6.25),    # E
]
for note, start, end in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=end)
    sax.notes.append(n)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    (36, 4.5, 4.75),    # Kick on beat 1
    (42, 4.625, 4.75),  # Hihat on 1&
    (38, 5.0, 5.25),    # Snare on beat 2
    (42, 5.125, 5.25),  # Hihat on 2&
    (36, 5.5, 5.75),    # Kick on beat 3
    (42, 5.625, 5.75),  # Hihat on 3&
    (38, 6.0, 6.0),     # Snare on beat 4
    (42, 6.125, 6.25)
]
for note, start, end in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=end)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
