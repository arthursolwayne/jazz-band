
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
    (36, 0.0, 0.375), (42, 0.0, 0.125), (42, 0.125, 0.125),
    (38, 0.375, 0.375), (42, 0.375, 0.125), (42, 0.499, 0.125),
    (36, 0.75, 0.375), (42, 0.75, 0.125), (42, 0.875, 0.125),
    (38, 1.125, 0.375), (42, 1.125, 0.125), (42, 1.25, 0.125),
    (42, 1.375, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (63, 2.25, 0.375), (65, 2.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, each bar a different chord
# Bar 2: Dmaj7 (D F# A C#)
piano_notes = [
    (62, 1.5, 0.125), (67, 1.5, 0.125), (71, 1.5, 0.125), (74, 1.5, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melodic motif - start with D, then F#, then C#, then leave it hanging
sax_notes = [
    (62, 1.5, 0.125), (67, 1.625, 0.125), (74, 1.75, 0.125)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (65, 3.0, 0.375), (67, 3.375, 0.375), (66, 3.75, 0.375), (68, 4.125, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: A7 (A C# E G)
piano_notes = [
    (69, 3.0, 0.125), (74, 3.0, 0.125), (76, 3.0, 0.125), (71, 3.0, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Continue the motif, resolve the tension
sax_notes = [
    (72, 3.0, 0.125), (74, 3.125, 0.125), (71, 3.25, 0.125), (67, 3.375, 0.125)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (68, 4.5, 0.375), (69, 4.875, 0.375), (68, 5.25, 0.375), (70, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: G7 (G B D F)
piano_notes = [
    (71, 4.5, 0.125), (76, 4.5, 0.125), (74, 4.5, 0.125), (71, 4.5, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Final resolution
sax_notes = [
    (74, 4.5, 0.125), (71, 4.625, 0.125), (67, 4.75, 0.125), (62, 4.875, 0.125)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375), (42, 4.5, 0.125), (42, 4.625, 0.125),
    (38, 4.875, 0.375), (42, 4.875, 0.125), (42, 5.0, 0.125),
    (36, 5.25, 0.375), (42, 5.25, 0.125), (42, 5.375, 0.125),
    (38, 5.625, 0.375), (42, 5.625, 0.125), (42, 5.75, 0.125),
    (42, 5.875, 0.125)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
