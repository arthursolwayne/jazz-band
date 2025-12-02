
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Short motif (D - F# - G - A)
sax_notes = [
    (62, 1.5, 0.25),  # D (D4)
    (67, 1.75, 0.25), # F# (F#4)
    (69, 2.0, 0.25),  # G (G4)
    (71, 2.25, 0.25)  # A (A4)
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass: Walking line in D (D - C# - B - A, etc.)
bass_notes = [
    (62, 1.5, 0.25),  # D
    (61, 1.75, 0.25), # C#
    (60, 2.0, 0.25),  # B
    (59, 2.25, 0.25)  # A
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
# D7 on beat 2, A7 on beat 4
piano_notes = [
    # D7: D, F#, A, C
    (62, 1.75, 0.25), (67, 1.75, 0.25), (71, 1.75, 0.25), (64, 1.75, 0.25),
    # A7: A, C#, E, G
    (71, 2.25, 0.25), (74, 2.25, 0.25), (76, 2.25, 0.25), (78, 2.25, 0.25)
]
for note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue melody with a slight variation
sax_notes = [
    (67, 3.0, 0.25),  # F#
    (69, 3.25, 0.25), # G
    (71, 3.5, 0.25),  # A
    (72, 3.75, 0.25)  # Bb
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass: Walking line
bass_notes = [
    (62, 3.0, 0.25),  # D
    (61, 3.25, 0.25), # C#
    (60, 3.5, 0.25),  # B
    (59, 3.75, 0.25)  # A
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 again
    (62, 3.25, 0.25), (67, 3.25, 0.25), (71, 3.25, 0.25), (64, 3.25, 0.25),
    # A7 again
    (71, 3.75, 0.25), (74, 3.75, 0.25), (76, 3.75, 0.25), (78, 3.75, 0.25)
]
for note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a cry, resolving back to D
sax_notes = [
    (67, 4.5, 0.25),  # F#
    (69, 4.75, 0.25), # G
    (71, 5.0, 0.25),  # A
    (62, 5.25, 0.5)   # D (hold to end)
]
for note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2])
    sax.notes.append(n)

# Bass: Walking line
bass_notes = [
    (62, 4.5, 0.25),  # D
    (61, 4.75, 0.25), # C#
    (60, 5.0, 0.25),  # B
    (59, 5.25, 0.25)  # A
]
for note in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2])
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 again
    (62, 4.75, 0.25), (67, 4.75, 0.25), (71, 4.75, 0.25), (64, 4.75, 0.25),
    # A7 again
    (71, 5.25, 0.25), (74, 5.25, 0.25), (76, 5.25, 0.25), (78, 5.25, 0.25)
]
for note in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2])
    piano.notes.append(n)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375)
]
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
