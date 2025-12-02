
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on 2
    (42, 0.375, 0.1875), # Hihat on 3
    (42, 0.5625, 0.1875), # Hihat on 4
    (36, 1.125, 0.375), # Kick on 3
    (38, 1.5, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 3
    (42, 1.3125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: A - C - D - Bb (Dorian mode, D Dorian)
sax_notes = [
    (62, 1.5, 0.375),   # A
    (64, 2.0, 0.375),   # C
    (65, 2.5, 0.375),   # D
    (60, 3.0, 0.375)    # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line (D - C - B - A - D)
bass_notes = [
    (62, 1.5, 0.375),   # D
    (60, 2.0, 0.375),   # C
    (59, 2.5, 0.375),   # B
    (60, 3.0, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 2: C7 on 2 (chord on beat 2)
piano_notes = [
    (60, 2.0, 0.375),   # C
    (64, 2.0, 0.375),   # E
    (67, 2.0, 0.375),   # G
    (62, 2.0, 0.375)    # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Bb - A - D - C# (half-step resolution)
sax_notes = [
    (60, 3.0, 0.375),   # Bb
    (60, 3.5, 0.375),   # A
    (65, 4.0, 0.375),   # D
    (66, 4.5, 0.375)    # C#
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line (A - Bb - C - D)
bass_notes = [
    (60, 3.0, 0.375),   # A
    (62, 3.5, 0.375),   # Bb
    (64, 4.0, 0.375),   # C
    (65, 4.5, 0.375)    # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 3: D7 on 2 (chord on beat 2)
piano_notes = [
    (65, 3.5, 0.375),   # D
    (67, 3.5, 0.375),   # F
    (72, 3.5, 0.375),   # A
    (67, 3.5, 0.375)    # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: C# - D - C - Bb (ending on a question)
sax_notes = [
    (66, 4.5, 0.375),   # C#
    (65, 5.0, 0.375),   # D
    (64, 5.5, 0.375),   # C
    (60, 6.0, 0.375)    # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line (D - C - B - A)
bass_notes = [
    (65, 4.5, 0.375),   # D
    (64, 5.0, 0.375),   # C
    (59, 5.5, 0.375),   # B
    (60, 6.0, 0.375)    # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
# Bar 4: Bb7 on 2 (chord on beat 2)
piano_notes = [
    (60, 5.0, 0.375),   # Bb
    (63, 5.0, 0.375),   # D
    (67, 5.0, 0.375),   # F
    (62, 5.0, 0.375)    # A
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums: Bar 4
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (38, 5.0, 0.375),  # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on 2
    (42, 4.875, 0.1875), # Hihat on 3
    (42, 5.0625, 0.1875), # Hihat on 4
    (36, 5.25, 0.375), # Kick on 3
    (38, 5.5, 0.375),  # Snare on 4
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
