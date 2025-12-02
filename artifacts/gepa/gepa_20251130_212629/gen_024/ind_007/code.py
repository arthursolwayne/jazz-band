
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.25),  # Kick on 1
    (38, 0.5, 0.25),  # Snare on 2
    (42, 0.0, 0.25),  # Hihat on 1
    (42, 0.25, 0.25), # Hihat on &
    (42, 0.5, 0.25),  # Hihat on 2
    (42, 0.75, 0.25), # Hihat on &
    (36, 1.0, 0.25),  # Kick on 3
    (38, 1.5, 0.25),  # Snare on 4
    (42, 1.0, 0.25),  # Hihat on 3
    (42, 1.25, 0.25), # Hihat on &
    (42, 1.5, 0.25),  # Hihat on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: D - F# - A - B
sax_notes = [
    (62, 1.5, 0.4),   # D
    (67, 1.9, 0.3),   # F#
    (69, 2.2, 0.4),   # A
    (71, 2.6, 0.4),   # B
    (69, 2.6, 0.2),   # A (rest)
    (67, 2.8, 0.2),   # F#
    (62, 3.0, 0.2),   # D (rest)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line in D minor
bass_notes = [
    (62, 1.5, 0.25),  # D
    (64, 1.75, 0.25), # Eb
    (67, 2.0, 0.25),  # F#
    (69, 2.25, 0.25), # A
    (71, 2.5, 0.25),  # B
    (67, 2.75, 0.25), # F#
    (64, 3.0, 0.25),  # Eb
    (62, 3.25, 0.25), # D
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    # D7 on 2 (F#, A, C#, D)
    (67, 1.9, 0.25),  # F#
    (69, 1.9, 0.25),  # A
    (72, 1.9, 0.25),  # C#
    (62, 1.9, 0.25),  # D
    # Bar 3
    # Bm7 on 2 (D, F#, A, B)
    (62, 2.9, 0.25),  # D
    (67, 2.9, 0.25),  # F#
    (69, 2.9, 0.25),  # A
    (71, 2.9, 0.25),  # B
    # Bar 4
    # D7 on 4 (F#, A, C#, D)
    (67, 3.5, 0.25),  # F#
    (69, 3.5, 0.25),  # A
    (72, 3.5, 0.25),  # C#
    (62, 3.5, 0.25),  # D
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax melody: leave it hanging
sax_notes = [
    (69, 3.0, 0.2),   # A
    (67, 3.2, 0.2),   # F#
    (62, 3.4, 0.2),   # D
    (67, 3.6, 0.2),   # F#
    (69, 3.8, 0.2),   # A
    (71, 4.0, 0.2),   # B
    (69, 4.2, 0.2),   # A
    (67, 4.4, 0.2),   # F#
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line in D minor
bass_notes = [
    (67, 3.0, 0.25),  # F#
    (69, 3.25, 0.25), # A
    (71, 3.5, 0.25),  # B
    (67, 3.75, 0.25), # F#
    (69, 4.0, 0.25),  # A
    (71, 4.25, 0.25), # B
    (67, 4.5, 0.25),  # F#
    (71, 4.75, 0.25), # B
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3
    # Bm7 on 2 (D, F#, A, B)
    (62, 3.9, 0.25),  # D
    (67, 3.9, 0.25),  # F#
    (69, 3.9, 0.25),  # A
    (71, 3.9, 0.25),  # B
    # Bar 4
    # D7 on 4 (F#, A, C#, D)
    (67, 4.5, 0.25),  # F#
    (69, 4.5, 0.25),  # A
    (72, 4.5, 0.25),  # C#
    (62, 4.5, 0.25),  # D
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.25),  # Kick on 1
    (38, 5.0, 0.25),  # Snare on 2
    (42, 4.5, 0.25),  # Hihat on 1
    (42, 4.75, 0.25), # Hihat on &
    (42, 5.0, 0.25),  # Hihat on 2
    (42, 5.25, 0.25), # Hihat on &
    (36, 5.5, 0.25),  # Kick on 3
    (38, 6.0, 0.25),  # Snare on 4
    (42, 5.5, 0.25),  # Hihat on 3
    (42, 5.75, 0.25), # Hihat on &
    (42, 6.0, 0.25),  # Hihat on 4
]

for note_number, start, duration in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    drums.notes.append(note)

# Sax: complete the motif
sax_notes = [
    (71, 4.5, 0.2),   # B
    (69, 4.7, 0.2),   # A
    (67, 4.9, 0.2),   # F#
    (62, 5.1, 0.2),   # D
    (67, 5.3, 0.2),   # F#
    (69, 5.5, 0.2),   # A
    (71, 5.7, 0.2),   # B
    (71, 5.9, 0.1),   # B (rest)
]
for note_number, start, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + duration)
    sax.notes.append(note)

# Bass: walking line in D minor
bass_notes = [
    (62, 4.5, 0.25),  # D
    (64, 4.75, 0.25), # Eb
    (67, 5.0, 0.25),  # F#
    (69, 5.25, 0.25), # A
    (71, 5.5, 0.25),  # B
    (67, 5.75, 0.25), # F#
    (64, 6.0, 0.25),  # Eb
    (62, 6.25, 0.25), # D
]
for note_number, start, duration in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4
    # D7 on 2 (F#, A, C#, D)
    (67, 5.9, 0.25),  # F#
    (69, 5.9, 0.25),  # A
    (72, 5.9, 0.25),  # C#
    (62, 5.9, 0.25),  # D
]
for note_number, start, duration in piano_notes:
    note = pretty_midi.Note(velocity=95, pitch=note_number, start=start, end=start + duration)
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro.mid")
