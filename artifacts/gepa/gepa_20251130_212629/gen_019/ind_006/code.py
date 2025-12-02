
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
    (36, 1.0, 1.0),     # Kick on beat 1
    (38, 1.25, 0.25),   # Snare on beat 2
    (42, 1.0, 0.25),    # Hihat on 1& 
    (42, 1.25, 0.25),   # Hihat on 2& 
    (42, 1.5, 0.25),    # Hihat on 3& 
    (36, 1.5, 1.0),     # Kick on beat 3
    (38, 1.75, 0.25),   # Snare on beat 4
    (42, 1.5, 0.25),    # Hihat on 3& 
    (42, 1.75, 0.25),   # Hihat on 4& 
    (42, 2.0, 0.25)     # Hihat on 4& end
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (71, 3.75, 0.375),  # Bb
    (72, 4.125, 0.375), # B
    (69, 4.5, 0.375),   # A
    (67, 4.875, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.125),  # D7 (D, F#, A, C)
    (67, 1.5, 0.125),  # G
    (69, 1.5, 0.125),  # A
    (72, 1.5, 0.125),  # B
    (67, 1.875, 0.125), # G
    (69, 1.875, 0.125), # A
    (72, 1.875, 0.125), # B
    (74, 1.875, 0.125), # C
    (62, 2.25, 0.125),  # D
    (67, 2.25, 0.125),  # G
    (69, 2.25, 0.125),  # A
    (72, 2.25, 0.125),  # B
    (67, 2.625, 0.125), # G
    (69, 2.625, 0.125), # A
    (72, 2.625, 0.125), # B
    (74, 2.625, 0.125)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif - short, singable, leaves it hanging
sax_notes = [
    (69, 1.5, 0.5),    # A
    (67, 2.0, 0.5),    # G
    (69, 2.5, 0.5),    # A
    (67, 3.0, 0.5),    # G (rest)
    (62, 3.5, 0.5)     # D (end on a question)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (69, 3.0, 0.375),  # A
    (71, 3.375, 0.375), # Bb
    (72, 3.75, 0.375),  # B
    (69, 4.125, 0.375), # A
    (67, 4.5, 0.375),   # G
    (69, 4.875, 0.375), # A
    (71, 5.25, 0.375),  # Bb
    (72, 5.625, 0.375), # B
    (67, 6.0, 0.375),   # G
    (65, 6.375, 0.375)  # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.0, 0.125),  # D7 (D, F#, A, C)
    (67, 3.0, 0.125),  # G
    (69, 3.0, 0.125),  # A
    (72, 3.0, 0.125),  # B
    (67, 3.375, 0.125), # G
    (69, 3.375, 0.125), # A
    (72, 3.375, 0.125), # B
    (74, 3.375, 0.125), # C
    (62, 3.75, 0.125),  # D
    (67, 3.75, 0.125),  # G
    (69, 3.75, 0.125),  # A
    (72, 3.75, 0.125),  # B
    (67, 4.125, 0.125), # G
    (69, 4.125, 0.125), # A
    (72, 4.125, 0.125), # B
    (74, 4.125, 0.125)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue motif, develop it with space and tension
sax_notes = [
    (62, 3.0, 0.5),    # D
    (67, 3.5, 0.5),    # G
    (69, 4.0, 0.5),    # A
    (67, 4.5, 0.5),    # G (rest)
    (62, 5.0, 0.5)     # D (end on a question)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (67, 4.5, 0.375),  # G
    (69, 4.875, 0.375), # A
    (71, 5.25, 0.375),  # Bb
    (72, 5.625, 0.375), # B
    (69, 6.0, 0.375),   # A
    (67, 6.375, 0.375), # G
    (69, 6.75, 0.375),  # A
    (71, 7.125, 0.375), # Bb
    (72, 7.5, 0.375),   # B
    (67, 7.875, 0.375)  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.5, 0.125),  # D7 (D, F#, A, C)
    (67, 4.5, 0.125),  # G
    (69, 4.5, 0.125),  # A
    (72, 4.5, 0.125),  # B
    (67, 4.875, 0.125), # G
    (69, 4.875, 0.125), # A
    (72, 4.875, 0.125), # B
    (74, 4.875, 0.125), # C
    (62, 5.25, 0.125),  # D
    (67, 5.25, 0.125),  # G
    (69, 5.25, 0.125),  # A
    (72, 5.25, 0.125),  # B
    (67, 5.625, 0.125), # G
    (69, 5.625, 0.125), # A
    (72, 5.625, 0.125), # B
    (74, 5.625, 0.125)  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Resolve the question, leave it open
sax_notes = [
    (67, 4.5, 0.5),    # G
    (69, 5.0, 0.5),    # A
    (67, 5.5, 0.5),    # G
    (62, 6.0, 0.5)     # D (end on a question)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),     # Kick on beat 1
    (38, 4.75, 0.25),   # Snare on beat 2
    (42, 4.5, 0.25),    # Hihat on 1& 
    (42, 4.75, 0.25),   # Hihat on 2& 
    (42, 5.0, 0.25),    # Hihat on 3& 
    (36, 5.0, 1.0),     # Kick on beat 3
    (38, 5.25, 0.25),   # Snare on beat 4
    (42, 5.0, 0.25),    # Hihat on 3& 
    (42, 5.25, 0.25),   # Hihat on 4& 
    (42, 5.5, 0.25)     # Hihat on 4& end
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
