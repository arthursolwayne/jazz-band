
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on beat 1, snare on beat 2, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.125),  # Hihat
    (42, 0.125, 0.125),  # Hihat
    (42, 0.25, 0.125),  # Hihat
    (42, 0.375, 0.125),  # Hihat
    (38, 0.5, 0.375),  # Snare on 2
    (42, 0.5, 0.125),  # Hihat
    (42, 0.625, 0.125),  # Hihat
    (42, 0.75, 0.125),  # Hihat
    (42, 0.875, 0.125),  # Hihat
    (36, 1.0, 0.375),  # Kick on 3
    (42, 1.0, 0.125),  # Hihat
    (42, 1.125, 0.125),  # Hihat
    (42, 1.25, 0.125),  # Hihat
    (42, 1.375, 0.125),  # Hihat
    (38, 1.5, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Everyone in (1.5 - 3.0s)

# Bass (Marcus): Walking line in Fm, chromatic approach to Bb
bass_notes = [
    (64, 1.5, 0.375),  # F (root)
    (63, 1.875, 0.375),  # Eb (chromatic approach to Bb)
    (62, 2.25, 0.375),  # D (approach to C)
    (60, 2.625, 0.375),  # Bb (target)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.5, 0.375),  # F7 (F, A, C, Eb)
    (66, 1.5, 0.375),
    (69, 1.5, 0.375),
    (62, 1.5, 0.375),
    (66, 2.25, 0.375),  # F7 again on beat 4
    (69, 2.25, 0.375),
    (64, 2.25, 0.375),
    (62, 2.25, 0.375),
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax (Dante): Motif starts on beat 2, sparse, expressive, haunted
sax_notes = [
    (60, 1.875, 0.25),  # G (melodic note)
    (62, 2.125, 0.25),  # A (melodic note)
    (60, 2.625, 0.25),  # G (return, unresolved)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Everyone in (3.0 - 4.5s)

# Bass (Marcus): Walking line in Fm, chromatic approach to Ab
bass_notes = [
    (64, 3.0, 0.375),  # F (root)
    (62, 3.375, 0.375),  # D (approach to Eb)
    (63, 3.75, 0.375),  # Eb (target)
    (60, 4.125, 0.375),  # Bb (target)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.0, 0.375),  # F7
    (66, 3.0, 0.375),
    (69, 3.0, 0.375),
    (62, 3.0, 0.375),
    (66, 3.75, 0.375),  # F7 again on beat 4
    (69, 3.75, 0.375),
    (64, 3.75, 0.375),
    (62, 3.75, 0.375),
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Drums: Kick on 1, snare on 2, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat
    (42, 3.125, 0.125),  # Hihat
    (42, 3.25, 0.125),  # Hihat
    (42, 3.375, 0.125),  # Hihat
    (38, 3.5, 0.375),  # Snare on 2
    (42, 3.5, 0.125),  # Hihat
    (42, 3.625, 0.125),  # Hihat
    (42, 3.75, 0.125),  # Hihat
    (42, 3.875, 0.125),  # Hihat
    (36, 4.0, 0.375),  # Kick on 3
    (42, 4.0, 0.125),  # Hihat
    (42, 4.125, 0.125),  # Hihat
    (42, 4.25, 0.125),  # Hihat
    (42, 4.375, 0.125),  # Hihat
    (38, 4.5, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Sax (Dante): Motif continues, sparse, expressive
sax_notes = [
    (62, 3.375, 0.25),  # A
    (60, 3.625, 0.25),  # G
    (62, 4.125, 0.25),  # A (return)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 4: Everyone in (4.5 - 6.0s)

# Bass (Marcus): Walking line in Fm, chromatic approach to Ab
bass_notes = [
    (64, 4.5, 0.375),  # F (root)
    (62, 4.875, 0.375),  # D (approach to Eb)
    (63, 5.25, 0.375),  # Eb (target)
    (60, 5.625, 0.375),  # Bb (target)
]
for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.5, 0.375),  # F7
    (66, 4.5, 0.375),
    (69, 4.5, 0.375),
    (62, 4.5, 0.375),
    (66, 5.25, 0.375),  # F7 again on beat 4
    (69, 5.25, 0.375),
    (64, 5.25, 0.375),
    (62, 5.25, 0.375),
]
for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Drums: Kick on 1, snare on 2, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat
    (42, 4.625, 0.125),  # Hihat
    (42, 4.75, 0.125),  # Hihat
    (42, 4.875, 0.125),  # Hihat
    (38, 5.0, 0.375),  # Snare on 2
    (42, 5.0, 0.125),  # Hihat
    (42, 5.125, 0.125),  # Hihat
    (42, 5.25, 0.125),  # Hihat
    (42, 5.375, 0.125),  # Hihat
    (36, 5.5, 0.375),  # Kick on 3
    (42, 5.5, 0.125),  # Hihat
    (42, 5.625, 0.125),  # Hihat
    (42, 5.75, 0.125),  # Hihat
    (42, 5.875, 0.125),  # Hihat
    (38, 6.0, 0.375),  # Snare on 4
]
for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Sax (Dante): Motif resolves, sparse, expressive
sax_notes = [
    (60, 5.0, 0.25),  # G
    (62, 5.25, 0.25),  # A
    (60, 5.5, 0.25),  # G (resolution)
]
for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
