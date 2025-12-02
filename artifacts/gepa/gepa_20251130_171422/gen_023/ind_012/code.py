
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
    (36, 0.0, 1.0),     # Kick on beat 1
    (38, 0.5, 1.0),     # Snare on beat 2
    (42, 0.0, 1.0),     # Hihat on beat 1
    (42, 0.25, 1.0),    # Hihat on beat 1 &
    (42, 0.5, 1.0),     # Hihat on beat 2
    (42, 0.75, 1.0),    # Hihat on beat 2 &
    (36, 1.0, 1.0),     # Kick on beat 3
    (38, 1.5, 1.0),     # Snare on beat 4
    (42, 1.0, 1.0),     # Hihat on beat 3
    (42, 1.25, 1.0),    # Hihat on beat 3 &
    (42, 1.5, 1.0),     # Hihat on beat 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (Marcus) - chromatic walking line with melodic intent
bass_notes = [
    (62, 1.5, 0.375),   # D (root)
    (63, 1.875, 0.375), # Eb (chromatic)
    (64, 2.25, 0.375),  # E (3rd)
    (65, 2.625, 0.375), # F (4th)
    (67, 3.0, 0.375),   # G (5th)
    (69, 3.375, 0.375), # A (6th)
    (71, 3.75, 0.375),  # Bb (7th)
    (72, 4.125, 0.375), # B (octave)
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano comp (Diane) - 7th chords on 2 and 4, with emotion and space
piano_notes = [
    (62, 1.875, 0.375), # D7 (D, F#, A, C)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    (70, 1.875, 0.375),
    (62, 3.0, 0.375),
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    (70, 3.0, 0.375),
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Saxophone motif (Dante) - concise, emotional, and haunting
sax_notes = [
    (62, 1.5, 0.375),   # D
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # G
    (62, 2.625, 0.375), # D
    (65, 3.0, 0.375),   # F
    (67, 3.375, 0.375), # G
    (62, 3.75, 0.375),  # D
    (65, 4.125, 0.375), # F
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line (Marcus) - chromatic walking line with melodic intent
bass_notes = [
    (62, 3.0, 0.375),   # D (root)
    (63, 3.375, 0.375), # Eb (chromatic)
    (64, 3.75, 0.375),  # E (3rd)
    (65, 4.125, 0.375), # F (4th)
    (67, 4.5, 0.375),   # G (5th)
    (69, 4.875, 0.375), # A (6th)
    (71, 5.25, 0.375),  # Bb (7th)
    (72, 5.625, 0.375), # B (octave)
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano comp (Diane) - 7th chords on 2 and 4, with emotion and space
piano_notes = [
    (62, 3.375, 0.375), # D7 (D, F#, A, C)
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    (70, 3.375, 0.375),
    (62, 4.5, 0.375),
    (64, 4.5, 0.375),
    (67, 4.5, 0.375),
    (70, 4.5, 0.375),
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Saxophone motif (Dante) - variation of the opening motif
sax_notes = [
    (62, 3.0, 0.375),   # D
    (67, 3.375, 0.375), # G
    (65, 3.75, 0.375),  # F
    (62, 4.125, 0.375), # D
    (67, 4.5, 0.375),   # G
    (65, 4.875, 0.375), # F
    (62, 5.25, 0.375),  # D
    (67, 5.625, 0.375), # G
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),     # Kick on beat 1
    (38, 5.0, 1.0),     # Snare on beat 2
    (42, 4.5, 1.0),     # Hihat on beat 1
    (42, 4.75, 1.0),    # Hihat on beat 1 &
    (42, 5.0, 1.0),     # Hihat on beat 2
    (42, 5.25, 1.0),    # Hihat on beat 2 &
    (36, 5.5, 1.0),     # Kick on beat 3
    (38, 6.0, 1.0),     # Snare on beat 4
    (42, 5.5, 1.0),     # Hihat on beat 3
    (42, 5.75, 1.0),    # Hihat on beat 3 &
    (42, 6.0, 1.0),     # Hihat on beat 4
]

for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bass line (Marcus) - chromatic walking line with melodic intent
bass_notes = [
    (62, 4.5, 0.375),   # D (root)
    (63, 4.875, 0.375), # Eb (chromatic)
    (64, 5.25, 0.375),  # E (3rd)
    (65, 5.625, 0.375), # F (4th)
    (67, 6.0, 0.375),   # G (5th)
    (69, 6.375, 0.375), # A (6th)
    (71, 6.75, 0.375),  # Bb (7th)
    (72, 7.125, 0.375), # B (octave)
]

for note, start, duration in bass_notes:
    bn = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    bass.notes.append(bn)

# Piano comp (Diane) - 7th chords on 2 and 4, with emotion and space
piano_notes = [
    (62, 4.875, 0.375), # D7 (D, F#, A, C)
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
    (70, 4.875, 0.375),
    (62, 6.0, 0.375),
    (64, 6.0, 0.375),
    (67, 6.0, 0.375),
    (70, 6.0, 0.375),
]

for note, start, duration in piano_notes:
    pn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(pn)

# Saxophone motif (Dante) - resolution of the opening motif
sax_notes = [
    (62, 4.5, 0.375),   # D
    (67, 4.875, 0.375), # G
    (65, 5.25, 0.375),  # F
    (62, 5.625, 0.375), # D
    (67, 6.0, 0.375),   # G
    (65, 6.375, 0.375), # F
    (62, 6.75, 0.375),  # D
    (67, 7.125, 0.375), # G
]

for note, start, duration in sax_notes:
    sn = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sn)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
