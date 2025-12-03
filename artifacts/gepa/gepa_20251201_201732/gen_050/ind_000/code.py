
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
    (36, 0.0, 0.375),   # Kick on beat 1
    (42, 0.375, 0.75),  # Hihat on &1
    (36, 0.75, 1.125),  # Kick on beat 2
    (42, 1.125, 1.5),   # Hihat on &2
    (38, 1.5, 1.875),   # Snare on beat 3
    (42, 1.875, 2.25),  # Hihat on &3
    (36, 2.25, 2.625),  # Kick on beat 4
    (42, 2.625, 3.0),   # Hihat on &4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) on beat 1, Ab2 (MIDI 55) on beat 2, Bb2 (MIDI 57) on beat 3, D2 (MIDI 50) on beat 4
bass_notes = [
    (53, 1.5, 1.875),   # F2 on beat 1
    (55, 2.25, 2.625),  # Ab2 on beat 2
    (57, 2.625, 3.0),   # Bb2 on beat 3
    (50, 3.0, 3.375),   # D2 on beat 4
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 1.5, 3.0),     # F
    (60, 1.5, 3.0),     # C
    (64, 1.5, 3.0),     # Eb
    (55, 1.5, 3.0),     # Ab
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: Melody - short motif, haunting and incomplete
# Start on G (MIDI 67) on beat 1, move to Ab (MIDI 68) on beat 2, rest on beat 3, and end on Bb (MIDI 62) on beat 4
sax_notes = [
    (67, 1.5, 1.875),   # G on beat 1
    (68, 2.25, 2.625),  # Ab on beat 2
    (62, 3.0, 3.375),   # Bb on beat 4
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F2 (MIDI 53) on beat 1, Bb2 (MIDI 57) on beat 2, C2 (MIDI 52) on beat 3, Eb2 (MIDI 59) on beat 4
bass_notes = [
    (53, 3.0, 3.375),   # F2 on beat 1
    (57, 3.75, 4.125),  # Bb2 on beat 2
    (52, 4.125, 4.5),   # C2 on beat 3
    (59, 4.5, 4.875),   # Eb2 on beat 4
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    (50, 3.0, 4.5),     # D
    (55, 3.0, 4.5),     # F
    (57, 3.0, 4.5),     # A
    (60, 3.0, 4.5),     # C
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: Melody - continue the motif, leave it hanging
# Start on C (MIDI 60) on beat 1, move to D (MIDI 62) on beat 2, rest on beat 3, and end on Eb (MIDI 63) on beat 4
sax_notes = [
    (60, 3.0, 3.375),   # C on beat 1
    (62, 3.75, 4.125),  # D on beat 2
    (63, 4.5, 4.875),   # Eb on beat 4
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F2 (MIDI 53) on beat 1, Ab2 (MIDI 55) on beat 2, Bb2 (MIDI 57) on beat 3, D2 (MIDI 50) on beat 4
bass_notes = [
    (53, 4.5, 4.875),   # F2 on beat 1
    (55, 5.25, 5.625),  # Ab2 on beat 2
    (57, 5.625, 6.0),   # Bb2 on beat 3
    (50, 6.0, 6.375),   # D2 on beat 4
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, 4.5, 6.0),     # F
    (60, 4.5, 6.0),     # C
    (64, 4.5, 6.0),     # Eb
    (55, 4.5, 6.0),     # Ab
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Sax: Melody - return to the original motif, end it
# Start on G (MIDI 67) on beat 1, move to Ab (MIDI 68) on beat 2, rest on beat 3, and end on Bb (MIDI 62) on beat 4
sax_notes = [
    (67, 4.5, 4.875),   # G on beat 1
    (68, 5.25, 5.625),  # Ab on beat 2
    (62, 6.0, 6.375),   # Bb on beat 4
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    (36, 4.5, 4.875),   # Kick on beat 1
    (42, 4.875, 5.25),  # Hihat on &1
    (36, 5.25, 5.625),  # Kick on beat 2
    (42, 5.625, 6.0),   # Hihat on &2
    (38, 6.0, 6.375),   # Snare on beat 3
    (42, 6.375, 6.75),  # Hihat on &3
    (36, 6.75, 7.125),  # Kick on beat 4
    (42, 7.125, 7.5),   # Hihat on &4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
