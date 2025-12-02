
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
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, dur in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - Fm7 (F, Ab, Bb, D) - start with Ab, then F, then Bb
sax_notes = [
    (90, 1.5, 0.375),  # Ab
    (84, 1.875, 0.375),  # F
    (96, 2.25, 0.375),  # Bb
    (89, 2.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    sax.notes.append(n)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (84, 1.5, 0.375),  # F
    (83, 1.875, 0.375),  # Gb
    (90, 2.25, 0.375),  # Ab
    (88, 2.625, 0.375)  # A
]
for note, start, dur in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    (84, 1.875, 0.375),  # F
    (83, 1.875, 0.375),  # Gb
    (96, 1.875, 0.375),  # Bb
    (89, 1.875, 0.375),  # D
    # Bar 3: Fm7 on beat 2
    (84, 3.375, 0.375),  # F
    (83, 3.375, 0.375),  # Gb
    (96, 3.375, 0.375),  # Bb
    (89, 3.375, 0.375),  # D
    # Bar 4: Fm7 on beat 2
    (84, 4.875, 0.375),  # F
    (83, 4.875, 0.375),  # Gb
    (96, 4.875, 0.375),  # Bb
    (89, 4.875, 0.375)   # D
]
for note, start, dur in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif again, but this time with a chromatic twist
sax_notes = [
    (89, 3.0, 0.375),  # D
    (90, 3.375, 0.375),  # Eb
    (84, 3.75, 0.375),  # F
    (83, 4.125, 0.375)  # Gb
]
for note, start, dur in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    sax.notes.append(n)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (84, 3.0, 0.375),  # F
    (83, 3.375, 0.375),  # Gb
    (90, 3.75, 0.375),  # Ab
    (88, 4.125, 0.375)  # A
]
for note, start, dur in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 2
    (84, 3.375, 0.375),  # F
    (83, 3.375, 0.375),  # Gb
    (96, 3.375, 0.375),  # Bb
    (89, 3.375, 0.375),  # D
    # Bar 4: Fm7 on beat 2
    (84, 4.875, 0.375),  # F
    (83, 4.875, 0.375),  # Gb
    (96, 4.875, 0.375),  # Bb
    (89, 4.875, 0.375)   # D
]
for note, start, dur in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif again, but this time with a resolution
sax_notes = [
    (90, 4.5, 0.375),  # Ab
    (84, 4.875, 0.375),  # F
    (96, 5.25, 0.375),  # Bb
    (89, 5.625, 0.375)  # D
]
for note, start, dur in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    sax.notes.append(n)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    (84, 4.5, 0.375),  # F
    (83, 4.875, 0.375),  # Gb
    (90, 5.25, 0.375),  # Ab
    (88, 5.625, 0.375)  # A
]
for note, start, dur in bass_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    (84, 4.875, 0.375),  # F
    (83, 4.875, 0.375),  # Gb
    (96, 4.875, 0.375),  # Bb
    (89, 4.875, 0.375)   # D
]
for note, start, dur in piano_notes:
    n = pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, dur in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
